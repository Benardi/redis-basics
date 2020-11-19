from redis import Redis

from utils import put_config

if __name__ == "__main__":
  
  key = "consumer_conf"
  cnsmr_conf = {
     "auto_offset_reset": "earliest",
     "consumer_timeout_ms": 1000,
     "bootstrap_servers": '["10.11.19.164"]' 
   }
  
  put_config(key, cnsmr_conf)
