import sys
import requests

print(sys.version)
print(sys.executable)

r = requests.get("http://www.cnn.com")
print(r.status_code)

print ("hello world")