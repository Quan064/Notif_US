from playwright.sync_api import sync_playwright
import shutil
import sqlite3
import subprocess
import os

HISTORY_PATH = "history_path.txt"
HISTORY_VISITED = "history_visited.txt"
OMISSION = "omission.txt"

def check_link(web, xpath, last_link):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36"
        )

        page = context.new_page()
        page.goto(web)

        index = 1
        while True:
            try:
                link = page.locator(f'xpath={xpath.replace("<i>", str(index))}').get_attribute("href")
                if link:
                    if link == last_link: break
                    else:
                        if index == 1: new_last_link = link
                        full_name = page.locator(f'xpath={xpath.replace("<i>", str(index))}').inner_text().strip()

                        message = fr'''
                        $BlogButton = New-BTButton -Content "Mở trang" -Arguments "{link}"
                        New-BurntToastNotification -Text "{page.title()}", "{full_name}" -Button $BlogButton -AppLogo "{os.path.join(os.path.dirname(__file__), "noti.ico")}"
                        '''

                        subprocess.run(["powershell", "-Command", message])
                        index += 1

                        with open(OMISSION, mode="a", encoding="utf-8") as f:
                            f.write(f"{link} $ {page.title()} $ {full_name}\n")
                else: break
            except: break

        browser.close()
        return new_last_link

def check_history():
    with open(HISTORY_PATH, mode="r", encoding="utf-8") as f:
        history_path = f.read().strip()
    temp_copy = "history_copy.db"
    shutil.copy2(history_path, temp_copy)

    conn = sqlite3.connect(temp_copy)
    cursor = conn.cursor()

    with open(OMISSION, mode="r", encoding="utf-8") as f:
        omission = [i.split(" $ ", maxsplit=2) for i in f.read().strip().split("\n")]
        new_omission = []
        if omission != [[""]]:
            for link, title, full_name in omission:

                cursor.execute("SELECT url, title FROM urls WHERE url = ?", (link,))
                if cursor.fetchone(): continue
                else:
                    message = fr'''
                    $BlogButton = New-BTButton -Content "Mở trang" -Arguments "{link}"
                    New-BurntToastNotification -Text "{title}", "{full_name}" -Button $BlogButton -AppLogo "{os.path.join(os.path.dirname(__file__), "noti.ico")}"
                    '''
                    subprocess.run(["powershell", "-Command", message])
                    new_omission.append([link, title, full_name])

    with open(OMISSION, mode="w", encoding="utf-8") as f:
        f.write("\n".join(" $ ".join(i) for i in new_omission))

    conn.close()

def main():
    try:
        check_history()

        new_noti = []
        with open(HISTORY_VISITED, mode="r", encoding="utf-8") as f:
            his = [i.split(maxsplit=2) for i in f.read().strip().split("\n")]
            for web, xpath, last_link in his:
                new_last_link = check_link(web, xpath, last_link)
                new_noti.append([web, xpath, new_last_link])
                
        with open(HISTORY_VISITED, mode="w", encoding="utf-8") as f:
            f.write("\n".join(" ".join(i) for i in new_noti))
    except: pass

if __name__ == "__main__":
    main()