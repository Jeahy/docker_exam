import os
import requests

# Get API address and port from environment variables or use defaults
api_address = os.environ.get('API_ADDRESS', 'api')
api_port = os.environ.get('API_PORT', '8000')


user_data = [
    {'username': 'alice',
    'password': 'wonderland'},
    {'username': 'bob',
    'password': 'builder'},
    {'username': 'clementine',
    'password': 'manarine'}
    ]

# Make the request to the API


for user in user_data:
    r = requests.get(  
    url=f'http://{api_address}:{api_port}/permissions',
        params = user
    )
    status_code = r.status_code
    # Determine test status based on the HTTP status code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    # Output results
    output = f'''
    ============================
        Authentication test
    ============================
    request done at "/permissions"
    {user}
    expected result = 200
    actual result = {status_code}
    ==>  {test_status}
    '''

    print(output)


# Print to a file if LOG environment variable is set to '1'
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output)
