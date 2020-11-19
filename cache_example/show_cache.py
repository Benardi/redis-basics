from redis import Redis

from utils import show_config

if __name__ == "__main__":
  key = "consumer_conf"
  show_config(key)  
