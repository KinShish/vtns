from playwright.sync_api import sync_playwright
from browserforge.fingerprints import FingerprintGenerator
from browserforge.injectors.playwright import NewContext
import json
import time
import os
array=[
       ['https://www.google.com/maps?output=search&q=','google-chrome.png'],
       ['https://ya.ru/maps?text=','ya-chrome.png'],
       ['https://www.list-org.com/search?type=name&val=','list-org-chrome.png'],
       ['https://www.rusprofile.ru/search?query=','rusprofile-chrome.png']]#['https://www.avito.ru/?q=','avito-chrome.png'],
def send_parser(id,adress):
    with sync_playwright() as p:
        fingerprints = FingerprintGenerator()
        fingerprint = fingerprints.generate()
        browser = p.chromium.launch()
        for i in range(len(array)):
            print(array[i])
            try:
                if not os.path.isfile(f"../upload/{account['accountId']}/{array[i][1]}"):
                    context = NewContext(browser, fingerprint=fingerprint)
                    page = context.new_page()
                    time.sleep(20)
                    page.goto(array[i][0]+adress, wait_until="domcontentloaded")
                    page.screenshot(path=f"../upload/{account['accountId']}/{array[i][1]}")
            except ZeroDivisionError:
                print("error parser "+array[i])
                browser.close()
        browser.close()
with open('../dataset/dataset_test.json', 'r', encoding='utf-8') as f:
  dataset_train = json.load(f)
for account in dataset_train:
    if not os.path.exists(f"../upload/{account['accountId']}"):
        os.makedirs(f"../upload/{account['accountId']}", exist_ok=True)
        send_parser(account['accountId'],account['address'])