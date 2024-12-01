import datetime
import os
def log_message(message, visited_nodes):
    '''Log a message to a file'''
    if not visited_nodes:
        raise ValueError("No nodes has been visited")
    file_path = os.path.join(os.path.dirname(__file__), 'message_log.txt') # Variable to store the path of message_log.txt
    with open(file_path, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")
