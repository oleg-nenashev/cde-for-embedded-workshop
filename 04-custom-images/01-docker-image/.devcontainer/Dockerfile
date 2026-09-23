FROM debian:bookworm-20250317
# TODO: Replace by another image to reduce traffic

# NOTE: There is a Dev Container feature for apt packages, this is just for an example


RUN apt-get update
RUN apt-get install -y \
    build-essential git checkinstall libssl-dev openssl software-properties-common \
    golang-go \
    sudo \
    libpq-dev

## vscode user
RUN useradd -ms /bin/bash vscode \
    && apt-get update \
    && apt-get install -y sudo \
    && echo vscode ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/vscode \
    && chmod 0440 /etc/sudoers.d/vscode

USER vscode
WORKDIR /home/vscode

## Python will run in venv
RUN python3 -m venv /home/vscode/venv
ENV PATH="/home/vscode/venv/bin:$PATH"
