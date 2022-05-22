'''
Tested with curl command for sign up

curl --location --request POST 'http://127.0.0.1:9000/create_user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"ABC",
    "email":"abc@xyz.com,
    "mobile":"123"
}'

Tested with curl command for login

curl --location --request GET 'http://127.0.0.1:9000/login_user?mobile=123'

'''

