from platform_utils.config import (
    API_BASE_URL,
    HEALTH_ENDPOINT,
    REQUEST_TIMEOUT,
)
import requests

def check_health():
    url = API_BASE_URL + HEALTH_ENDPOINT
    print(f"Checking: {url}")
    response = requests.get(
        url,
        timeout=REQUEST_TIMEOUT
    )

    print(response.status_code)
    print(response.json()["status"])

    if response.status_code == 200:

        print("PASS")

    else:
        
        print("FAIL")

check_health()

