import logging
import os
from datetime import datetime

# Create logs directory
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create a logger object you can use everywhere
logger = logging.getLogger("customLogger")

if __name__ == "__main__":
    logger.info("Logging has started")
