# Deep Daze Bot for Twitter
## Requirements

```bash
pip install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio==0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
pip install deep-daze tweepy deep_translator
```

## Docker container
### Create container

```bash
docker build -t deepdaze:latest -f Dockerfile .
```

### Run interactive mode and activate GPU

```bash
docker run -it --rm --gpus all --privileged -v $(pwd):/test deepdaze:latest python3.9 twitter_bot.py
```
