curl \
  -X PUT \
  -H "Content-Type: application/json" \
  --data @$2 \
  http://0.0.0.0:8080/user-info/$1
