# syntax=docker/dockerfile:1

ARG BASE_IMAGE=ghcr.io/pyansys/pyacp-private:latest

FROM $BASE_IMAGE

USER root

RUN yum install -y \
    iproute \
    sudo \
    && \
    yum autoremove -y \
    && \
    yum clean all -y

#escape=`
COPY --chmod=755 <<EOF /usr/ansys_inc/acp/acp_grpcserver_wrapper.sh
#!/usr/bin/bash

set -e

DELAY=\$1
RATE=\$2

shift 2
tc qdisc add dev eth0 root netem delay \$DELAY rate \$RATE
/usr/ansys_inc/acp/acp_grpcserver "\$@"
EOF
#escape=\

RUN chmod u+s /usr/sbin/tc

USER container

ENTRYPOINT ["/usr/ansys_inc/acp/acp_grpcserver_wrapper.sh"]
CMD ["100ms", "1mbit", "--server-address=0.0.0.0:50051"]
