from playwright.sync_api import sync_playwright, Playwright
from dotenv import load_dotenv
import os


def login(p: Playwright):
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://portal.ctdb.hcmus.edu.vn/sinh-vien")
    
    page.locator('xpath=//*[@id="dnn_ctr_Login_Login_DNN_txtUsername"]').fill("your_username")
    page.locator('xpath=//*[@id="dnn_ctr_Login_Login_DNN_txtPassword"]').fill("your_password")
    page.locator('xpath=//*[@id="dnn_ctr_Login_DNN"]/div/div[3]/span[2]/span/span').click()
    page.locator('xpath=//*[@id="dnn_ctr_Login_Login_DNN_cmdLogin"]').click()
    
    input()


if __name__ == "__main__":
    with sync_playwright() as p: login(p)
