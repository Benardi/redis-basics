curl \
  -X POST \
  -H "Content-Type: application/json" \
  --data @$1 \
  http://0.0.0.0:8080/user-info
