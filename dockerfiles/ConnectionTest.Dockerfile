# syntax=docker/dockerfile:1

ARG BASE_IMAGE=ghcr.io/ansys/pyacp:latest

FROM $BASE_IMAGE

USER root

RUN apt-get update && apt-get install -y \
    iproute2 \
    sudo \
    && \
    rm -rf /var/lib/apt/lists/*

#escape=`
COPY --chmod=755 <<EOF /usr/ansys_inc/acp/acp_grpcserver_wrapper.sh
#!/usr/bin/bash

set -ex

DELAY=\$1
RATE=\$2

shift 2

# Create an Intermediate Functional Block (IFB) through which ingress traffic
# is routed. This is necessary because the 'tc ... netem' command only affects
# egress packets.
# NOTE: if this fails, you may have to run 'modprobe ifb' on the host machine.
ip link add ifb0 type ifb
ip link set dev ifb0 up
tc qdisc add dev eth0 ingress
tc filter add dev eth0 parent ffff: protocol ip u32 match u32 0 0 flowid 1:1 action mirred egress redirect dev ifb0

tc qdisc add dev eth0 root netem delay \$DELAY rate \$RATE
tc qdisc add dev ifb0 root netem delay \$DELAY rate \$RATE
sudo -u container --preserve-env /usr/ansys_inc/acp/acp_grpcserver "\$@"
EOF
#escape=\

ENTRYPOINT ["/usr/ansys_inc/acp/acp_grpcserver_wrapper.sh"]
CMD ["100ms", "1mbit", "--server-address=0.0.0.0:50051"]
