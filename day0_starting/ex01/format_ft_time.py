import time
from datetime import datetime

# Get the current time in seconds since the epoch
seconds_since_epoch = time.time()
human_readable = datetime.now().strftime("%b %d %Y")

# Print the formatted output
print(f"Seconds since January 1, 1970: {seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} in scientific notation")
print(human_readable)