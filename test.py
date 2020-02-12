import os

print('Running test script...')

access_key = os.getenv('aws-access-key-id', None)
if access_key is not None:
  print(f'Found credential of length {len(access_key)}')
else:
  raise KeyError('Access key not found!')
