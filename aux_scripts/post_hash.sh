curl \
  -X POST \
  -H "Content-Type: application/json" \
  --data '{"key": "userinfo", "pairs": {"Name":"Pradeep", "Company":"SCTL", "Address":"Mumbai", "Location":"RCP"}}' \
  http://0.0.0.0:8080/hash
