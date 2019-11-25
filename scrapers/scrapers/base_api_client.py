import json

class ApiClient(object):
	def __init__(self, api_uri, api_key):
		self.api_uri	= api_uri
		self.api_key	= api_key

	def set_headers(self, nonce = None):
		from base64 import b64encode
		from hashlib import sha256
		from hmac import new

		if not nonce:
			from time import time
			nonce = int(time())

		return {
			'X-Authentication-Key': self.api_key,
			'X-Authentication-Nonce': str(nonce)
		}

	@staticmethod
	def merge_dicts(*dict_args):
		result = {}
		for dictionary in dict_args:
			result.update(dictionary)

		return result

	def request(self, method, path, data = {}, headers = {}, params = {}):
		from requests import request

		url = '{0}{1}'.format(self.api_uri, path)
		headers = self.merge_dicts(self.set_headers(), headers)

		if method == "GET":
			params.update(data)
			return request(method, url, headers=headers, params=params)
		else:
			return request(method, url, headers=headers, params=params, data=json.dumps(data))

	def post(self, path, data = {}, params = {}):
		return Response(self.request("POST", path, data, {'Content-Type': 'application/json'}, params))

	def get(self, path, data = {}):
		return Response(self.request("GET", path, data, params = {}))

	def put(self, path, data = {}):
		return Response(self.request("PUT", path, data, {'Content-Type': 'application/json'}))

	def delete(self, path, data = {}):
		return Response(self.request("DELETE", path, data))

class Response(object):
	def __init__(self, response):
		self.response = response

		try:
			self.content = self.response.json()
		except ValueError:
			self.content = self.response.text
			print(f"Error while getting the response: {str(ValueError)}")

	def ok(self):
		import requests
		return self.response.status_code == requests.codes.ok

	def errors(self):
		if self.ok():
			return {}

		errors = self.content

		if(not isinstance(errors, dict)):
			errors = {"error": errors} # convert to dict for consistency
		elif('errors' in errors):
			errors = errors['errors']

		return errors

	def __getitem__(self, key):
		return self.content[key]
