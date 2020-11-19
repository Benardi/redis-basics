
# DELETE ALL USERS
bash delete_userinfo.sh | jq

# GET INFO ON ALL USERS
bash get_all_userinfo.sh | jq

# POST 3 USERS TO DB
bash post_userinfo.sh ./data.json | jq

# GET 3RD USER
bash get_userinfo_at_idx.sh 2 | jq

# GET 2ND USER
bash get_userinfo_at_idx.sh 1 | jq

# GET 1RSt USER
bash get_userinfo_at_idx.sh 0 | jq

bash put_userinfo.sh 0 ./newuser.json | jq

# GET INFO ON ALL USERS
bash get_all_userinfo.sh | jq

# DELETE ALL USERS
bash delete_userinfo.sh | jq

# GET INFO ON ALL USERS
bash get_all_userinfo.sh | jq
