# Redis Basics
Basic Redis functionalities offered via REST API

## Requirements

### Redis 

A Redis server must be already running in a given address and port

> In the example below we use the address 0.0.0.0 (running on same machine ) and the port 7777 

### Python 3 programming environment

The following commands will give you a programming environment for Python 3 on Ubuntu 18.04, this environment is a requirement for the application:

```bash
# Update and upgrade system
sudo apt update
sudo apt -y upgrade

# Install pip
sudo apt install -y python3-pip

# Install Additional Tools
sudo apt install build-essential libssl-dev libffi-dev python3-dev

#  Install venv
sudo apt install -y python3-venv
```

* If you wish to use `venv` check [Python official documentation](https://docs.python.org/3/tutorial/venv.html) on it.
* If you choose to not use venv you Python binaries will most likely be `python3` and `pip3` instead of `python` and `pip`. We'll use the notation `python` and `pip` throughout this document. 

## Execute application

### Set up environment

```bash
# Create virtual environment 
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

pip install -r ./requirements.txt
```

### Raise API

For help run `python ./api.py --help` 

```bash
python ./api.py -a 0.0.0.0 -p 8080 -rp 7777
```
