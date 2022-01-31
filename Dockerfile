FROM nvidia/cuda:11.3.1-base-ubuntu20.04

# Environments
ARG DEBIAN_FRONTEND=noninteractive
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
CMD nvidia-smi

RUN apt-get -y update && apt-get -y install \
    python3.9 \
    python3-pip

RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir \
    torch==1.10.2+cu113 torchvision==0.11.3+cu113 \
    torchaudio==0.10.2+cu113 -f \
    https://download.pytorch.org/whl/cu113/torch_stable.html
RUN  pip install --no-cache-dir deep-daze tweepy deep_translator

VOLUME /test
WORKDIR /test
RUN python3 -c "import torch; x = (torch.cuda.get_device_name(0) if torch.cuda.is_available() else None); print(x)"
