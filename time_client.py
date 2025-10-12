import socket
import time

NIST_BYTES = 4
NIST_PORT = 37
NIST_URL = "time.nist.gov"

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

s = socket.socket()
server = (NIST_URL, NIST_PORT)
s.connect(server)
data = s.recv(NIST_BYTES)
decoded_data = int.from_bytes(data, byteorder='big')

print(f"NIST time: {decoded_data}")
print(f"System Time: {system_seconds_since_1900()}")





