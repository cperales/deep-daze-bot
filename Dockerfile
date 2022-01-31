FROM nvidia/cuda:11.3.1-base-ubuntu20.04

# Environments
ARG DEBIAN_FRONTEND=noninteractive
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
CMD nvidia-smi

RUN apt-get -y update && apt-get -y install \
    python3.9 \
    python3-pip

RUN python3.9 -m pip install --no-cache-dir -U pip && python3.9 -m pip \
    install --no-cache-dir \
    torch==1.10.2+cu113 torchvision==0.11.3+cu113 \
    torchaudio==0.10.2+cu113 -f \
    https://download.pytorch.org/whl/cu113/torch_stable.html
RUN python3.9 -m pip install --no-cache-dir deep-daze tweepy deep_translator

ADD twitter_bot.py .
ADD config.ini .
ADD bearer_token.txt .
RUN python3.9 -c "import torch; x = (torch.cuda.get_device_name(0) if torch.cuda.is_available() else None); print(x)"
