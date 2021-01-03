from os import getenv

from dotenv import load_dotenv

load_dotenv()

ip_address = getenv("IP")
assert ip_address, "IP not configured"
