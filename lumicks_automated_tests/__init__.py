import logging
import os
import sys

logging.basicConfig(
    format="[%(levelname)s %(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)

BASE_URL = os.environ.get("BASE_URL")

if not BASE_URL:
    raise ValueError(
        "You must provide BASE_URL environment variable to point the system under testing "
        "e.g. `export BASE_URL=http://localhost:8000/`"
    )

BASE_URL = BASE_URL if BASE_URL.endswith("/") else "f{BASE_URL}/"
