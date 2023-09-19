from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service  
import time
import random
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Get proxy list and Discord webhook URL from .env file
proxies = os.getenv('PROXIES').split(',')
discord_webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

def create_proxy_driver(proxy_address):
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = proxy_address
    prox.socks_proxy = proxy_address
    prox.ssl_proxy = proxy_address

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    webdriver_service = Service(executable_path="")  
    return webdriver.Chrome(desired_capabilities=capabilities, service=webdriver_service)

def send_discord_notification(message):
    payload = {
        "content": message
    }
    r = requests.post(discord_webhook_url, json=payload)
    if r.status_code == 204:
        print("Sent notification to Discord.")
    else:
        print("Failed to send notification to Discord.")

prev_content = None

while True:
    selected_proxy = random.choice(proxies)
    driver = create_proxy_driver(selected_proxy)

    driver.get('https://www.brownsshoes.com/en/women/accessories-and-outerwear/slippers/product/ugg/tazz/266618.html?dwvar_266618_color=015&position=2')

    try:
        element = driver.find_element(By.CLASS_NAME, 'bs-select-size')
        curr_content = element.text

        if prev_content is not None and curr_content != prev_content:
            print("Change detected!")
            send_discord_notification("Change detected in bs-select-size: " + curr_content)
        
        prev_content = curr_content
        print("Current content:", curr_content)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

    time.sleep(5)  