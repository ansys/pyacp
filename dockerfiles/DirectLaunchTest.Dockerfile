# syntax=docker/dockerfile:1

ARG BASE_IMAGE=ghcr.io/ansys/acp:latest

FROM $BASE_IMAGE

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    libxrender1 \
    pipx \
    python3-pip \
    python3.11 \
    python3.11-venv \
    && \
    rm -rf /var/lib/apt/lists/*


USER container

RUN pipx install poetry

ENV PATH="$PATH:/home/container/.local/bin"

# COPY --chown=container:container . /home/container/pyacp

WORKDIR /home/container/pyacp

# Make /home/container writable to any user
RUN chmod -R 777 /home/container/

COPY --chmod=755 <<EOF /home/container/install_and_run_tests.sh
#!/usr/bin/bash
poetry env use python3.11
poetry install --all-groups --all-extras
poetry run pytest --cov=ansys.acp.core --cov-report=term --cov-report=xml --cov-report=html --server-bin=/usr/ansys_inc/acp/acp_grpcserver "\$@"
EOF

ENTRYPOINT ["/home/container/install_and_run_tests.sh"]
CMD ["tests/unittests"]
