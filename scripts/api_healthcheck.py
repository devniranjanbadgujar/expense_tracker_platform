from platform_utils.config import (
    API_BASE_URL,
    HEALTH_ENDPOINT,
    REQUEST_TIMEOUT,
)

import requests
from platform_utils.logger import logger

def check_health():
    url = API_BASE_URL + HEALTH_ENDPOINT
    logger.info(f"Calling URL: {url}")
    response = requests.get(
        url,
        timeout=REQUEST_TIMEOUT
    )

    print(response.status_code)
    logger.debug(response.json()["status"])

    if response.status_code == 200:

        logger.info("Health Check Passed")

    else:
        
        logger.error("FAIL")

check_health()

