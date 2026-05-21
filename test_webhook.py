import requests


user_message = "Create a meeting called Test tomorrow at 10am"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/90cd0c90-2601-4064-a7ad-2166848f37b1"

response = requests.post(url, json=request_message)

print(response.status_code)
print(response.json())
# print(response.json()[0]["output"])