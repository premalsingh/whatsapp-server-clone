'''
Tested with curl command

curl --location --request POST 'http://127.0.0.1:9000/create_user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"ABC",
    "email":"abc@xyz.com,
    "mobile":"123"
}'

'''