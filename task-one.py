import queue
import time
import random

def generate_request(q, request_id):
    request_data = f"Request ID: {request_id}"
    q.put(request_data)
    print(f"Generated and added to queue: {request_data}")

def process_request(q):
    if not q.empty():
        request = q.get()
        print(f"Processing request: {request}")
    else: 
        print("No requests to process")


def main():
    q = queue.Queue()
    request_id = 0
    
    try:
        while True:
            request_id += 1
            generate_request(q, request_id)
            process_request(q)
            time.sleep(random.randint(1, 3))
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()
