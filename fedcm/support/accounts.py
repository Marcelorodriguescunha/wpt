import importlib
error_checker = importlib.import_module("fedcm.support.request-params-check")

def main(request, response):
  request_error = error_checker.accountsCheck(request)
  if (request_error):
    return request_error

  response.headers.set(b"Content-Type", b"application/json")

  return """
{
 "accounts": [{
   "id": "1234",
   "given_name": "John",
   "name": "John Doe",
   "email": "john_doe@idp.example",
   "picture": "https://idp.example/profile/123",
   "approved_clients": ["123", "456", "789"],
   "login_hints": ["john_doe"],
   "domain_hints": ["idp.example", "example"]
  }]
}
"""
