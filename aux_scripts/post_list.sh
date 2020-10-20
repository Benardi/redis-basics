curl \
  -X POST \
  -H "Content-Type: application/json" \
  --data '{"key": "userinfo", "values": [0,1,2,3,4,5,6,7,8,9,10], "strat": "right"}' \
  http://0.0.0.0:8080/list
