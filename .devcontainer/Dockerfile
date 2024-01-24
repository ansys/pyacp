FROM mcr.microsoft.com/devcontainers/universal:2

RUN apt update && apt install -y \
    xvfb \
    pandoc \
    && apt clean -y && rm -rf /var/lib/apt/lists/*

RUN echo 'poetry shell' >> /home/codespace/.profile
