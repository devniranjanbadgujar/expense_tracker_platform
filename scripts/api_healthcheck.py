import requests
import sys, time, requests

from platform_utils.config import (
    API_BASE_URL,
    HEALTH_ENDPOINT,
    REQUEST_TIMEOUT,
    MAX_RETRIES,
    RETRY_DELAY,
)

from requests.exceptions import RequestException
from platform_utils.logger import logger

def check_health():

    url = API_BASE_URL + HEALTH_ENDPOINT
    logger.info(f"Calling URL: {url}")

    for attempt in range(1, MAX_RETRIES + 1):
        logger.info(f"Attempt {attempt}/{MAX_RETRIES}")

        try:
            start_time = time.perf_counter()
        
            response = requests.get(
                url,
                timeout=REQUEST_TIMEOUT
            )

            end_time = time.perf_counter()

            response_time = round(
                (end_time - start_time) * 1000,
                2
            )

            logger.info(f"Response Time: {response_time} ms")

            print(response.status_code)
            logger.debug(response.json()["status"])

            if response.status_code == 200:

                logger.info("Health Check Passed")

                sys.exit(0)
        
            logger.error(
                f"Unexpected Status Code : {response.status_code}"
            )
        
        except RequestException as e:

            logger.error(e)

        if attempt < MAX_RETRIES:

            logger.warning(
                f"Retrying in {RETRY_DELAY} seconds......"
            )

            time.sleep(RETRY_DELAY)

    logger.critical("Health Check failed")
    sys.exit(1)

check_health()

