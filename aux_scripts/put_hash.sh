curl \
  -X PUT \
  -H "Content-Type: application/json" \
  --data '{"key": "userinfo", "newkey": "newuser-info", "expire": {"minutes": 1, "seconds": 31},  "pairs": {"Name":"TioBen", "Company":"SCTL", "Address":"Mumbai", "Location":"RCP"}}' \
  http://0.0.0.0:8080/hash
