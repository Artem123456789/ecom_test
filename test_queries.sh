#!/bin/bash

curl --location --request POST 'http://localhost:8000/get_form?user_email=neznajkinartem357%40gmail.com&user_phone=%2b77051596157&date_register=09.10.2023&date_interests=my_text'
curl --location --request POST 'http://localhost:8000/get_form?user_email=neznajkinartem357%40gmail.com&date_interests=my_text'
curl --location --request POST 'http://localhost:8000/get_form?check_email=neznajkinartem357%40gmail.com&check_phone=%2b77051596157'
curl --location --request POST 'http://localhost:8000/get_form?place=test_place&gender=test_gender'