# Code example 1

import requests

def make_request() -> None:
    """
    Makes an HTTP GET request to a specified URL and handles the response:
    - If the request is successful (status code 200), prints a success message
      and the response data in JSON format.
    - If the request fails (non-200 status code), prints a failure message with
      the status code.
    - Catches any request exceptions and prints an error message.
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Request successful!")
            print("Response:", response.json())
        else:
            print("Request failed. Status Code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error in the request:", e)
