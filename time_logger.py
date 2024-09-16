# time_logger.py
import time
from datetime import datetime

# Path to the log file
log_file_path = '/var/log/mydata.log'

# Function to log current date and time
def log_time():
    with open(log_file_path, 'a') as file:
        while True:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f'{current_time}\n')
            file.flush()  # Make sure data is written to file immediately
            time.sleep(3)

if __name__ == "__main__":
    log_time()
