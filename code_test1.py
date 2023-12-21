import os
import requests

# Get API address and port from environment variables or use defaults
api_address = os.environ.get('API_ADDRESS', 'api')
api_port = os.environ.get('API_PORT', '8000')


# Make the request to the API
r = requests.get(  
url=f'http://{api_address}:{api_port}/permissions',
    params= {
        'username': 'alice',
        'password': 'wonderland'
    }
)

# Determine test status based on the HTTP status code
if r.status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

# Output results
output = '''
============================
    Authentication test
============================
request done at "/permissions"
| username="alice"
| password="wonderland"
expected result = 200
actual restult = {status_code}
==>  {test_status}
'''
print(output.format(status_code=r.status_code, 
test_status=test_status))


# Print to a file if LOG environment variable is set to '1'
if os.environ.get('LOG') == '1':
    with open('api_test.log', 'a') as file:
        file.write(output)
