import os
import requests

# Get API address and port from environment variables or use defaults
api_address = os.environ.get('API_ADDRESS', 'api')
api_port = os.environ.get('API_PORT', '8000')


user_data = [
    {'username': 'alice',
    'password': 'wonderland'},
    {'username': 'bob',
    'password': 'builder'}
    ]

# Make the request to the API

for user in user_data:
#v1
    r = requests.get(  
    url=f'http://{api_address}:{api_port}/v1/sentiment',
        params = user
    )
    status_code = r.status_code
    # Determine test status based on the HTTP status code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    # Output results
    output_v1 = f'''
    ============================
        Authentication test
    ============================
    request done at "/v1/sentiment"
    {user}
    expected result = 200
    actual result = {status_code}
    ==>  {test_status}
    '''

    print(output_v1)

# Print to a file if LOG environment variable is set to '1'
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output_v1)

#v2
   r = requests.get(  
    url=f'http://{api_address}:{api_port}/v2/sentiment',
        params = user
    )
    status_code = r.status_code
    # Determine test status based on the HTTP status code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    # Output results
    output_v2 = f'''
    ============================
        Authentication test
    ============================
    request done at "/v2/sentiment"
    {user}
    expected result = 200
    actual result = {status_code}
    ==>  {test_status}
    '''

    print(output_v2)


# Print to a file if LOG environment variable is set to '1'
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output_v2)
