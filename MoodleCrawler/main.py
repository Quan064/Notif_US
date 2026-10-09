from playwright.sync_api import sync_playwright
import os
from login import login


with sync_playwright() as p:
    # Check if the login state file exists
    if not os.path.exists("state.json"): login(p)
    
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    
    page.goto("https://courses.ctda.hcmus.edu.vn/my/")
    
    # If the login session has expired
    if page.locator('xpath=//*[@id="loginerrormessage"]').count() > 0:
        page.locator('xpath=//*[@id="region-main"]/div/div/div/div/div[4]/a[1]').click()
    
    # Crawling the assignment list
    container = page.locator('//div[@data-region="event-list-container"]')
    container.scroll_into_view_if_needed()
    page.wait_for_selector('//div[@data-region="event-list-container"]//a', timeout=10000)
    print(container.inner_text())
    input("Press Enter to close the browser...")
