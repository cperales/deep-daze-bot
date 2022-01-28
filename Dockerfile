FROM nvidia/cuda:11.0-base-ubuntu20.04

# Environments
ARG DEBIAN_FRONTEND=noninteractive
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
CMD nvidia-smi

RUN apt-get -y update && apt-get -y install \
    python3.9 \
    python3-pip

RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir \
    torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 \
    -f https://download.pytorch.org/whl/torch_stable.html
RUN  pip install --no-cache-dir deep-daze

VOLUME /test
WORKDIR /test
RUN python3 -c "import torch; x = (torch.cuda.get_device_name(0) if torch.cuda.is_available() else None); print(x)"
