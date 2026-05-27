import os 
import sys
import logging


log_dir = "logs"
log_filepath=os.path.join(log_dir, "logging.log")

if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    logging.info("Created log directory: %s", log_dir)

if not os.path.exists(log_filepath):
    with open(log_filepath, 'w') as f:
        pass
    logging.info("Created log file: %s", log_filepath)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
                    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)])


logger = logging.getLogger(__name__)