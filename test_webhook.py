import requests

def send_webhook(message: str):
    url = "http://localhost:5678/webhook-test/90cd0c90-2601-4064-a7ad-2166848f37b1"

    payload = {
        "message": message
    }

    try:
        response = requests.post(url, json=payload)

        print("Status Code:", response.status_code)
        print("Raw Response:", response.text)

        # Try parsing JSON safely
        try:
            data = response.json()
            print("JSON Response:", data)
            return data
        except ValueError:
            print("Response is not valid JSON.")
            return response.text

    except requests.exceptions.RequestException as e:
        print("Request failed:", str(e))
        return None


if __name__ == "__main__":
    user_message = "Create a meeting called Test tomorrow at 10am"
    send_webhook(user_message)