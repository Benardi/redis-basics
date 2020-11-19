from redis import Redis

from utils import put_config

if __name__ == "__main__":
  
  key = "consumer_conf"
  cnsmr_conf = {
     "auto_offset_reset": "latest",
     "consumer_timeout_ms": 5555,
     "bootstrap_servers": '["0.0.0.0"]' 
   }
  
  put_config(key, cnsmr_conf, {"seconds": 10})
