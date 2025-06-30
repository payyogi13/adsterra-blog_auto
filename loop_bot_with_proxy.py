import requests
import random
import time

TARGET_URL = "https://payyogi13.github.io/adsterra-blog_auto/"
SMARTLINK_URL = "https://www.profitableratecpm.com/my1dmgzw5?key=410c20d30ba8e00b7968ec87d50ff1d2"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

# Sample public proxies (rotate or update regularly)
PROXIES = [
    "http://51.158.68.68:8811",
    "http://103.111.55.58:8080",
    "http://190.104.1.21:80",
    "http://188.166.56.246:80",
    "http://45.77.24.239:3128",
]

def simulate_visit():
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Referer": "https://google.com",
    }
    proxy = {"http": random.choice(PROXIES), "https": random.choice(PROXIES)}
    try:
        r = requests.get(TARGET_URL, headers=headers, proxies=proxy, timeout=10)
        print(f"🌍 Visited BLOG - Status: {r.status_code}")
        time.sleep(random.randint(3, 6))
        click = requests.get(SMARTLINK_URL, headers=headers, proxies=proxy, timeout=10)
        print(f"🖱️ Clicked SMARTLINK - Status: {click.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    for _ in range(5):  # Run 5 visit + click cycles
        simulate_visit()
        time.sleep(random.randint(10, 20))
