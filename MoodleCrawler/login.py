from playwright.sync_api import Playwright
import re


HOME_URL = re.compile(r"https://courses\.ctda\.hcmus\.edu\.vn/my/?(?:[?#].*)?$")
HOME_SELECTOR = (
    "body#page-my-index, "
    "[data-region='myoverview'], "
    "[data-region='course-content'], "
    ".block_myoverview"
)

def login(p: Playwright):
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://courses.ctda.hcmus.edu.vn/my/")
    
    page.wait_for_url(HOME_URL, timeout=0)
    page.wait_for_load_state("networkidle")
    page.wait_for_selector(HOME_SELECTOR, timeout=0)
    
    context.storage_state(path="state.json")
    browser.close()
