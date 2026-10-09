from playwright.sync_api import sync_playwright
from login import login


LOGIN_URL_FRAGMENT = "/Login"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://portal.ctdb.hcmus.edu.vn/sinh-vien")
    
    # If the login session has expired
    if LOGIN_URL_FRAGMENT in page.url:
        login(p)
        page.goto("https://portal.ctdb.hcmus.edu.vn/sinh-vien") # Reload
    
    input("Press Enter to close the browser...")
