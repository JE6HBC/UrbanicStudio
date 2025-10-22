from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the local HTML file
        file_path = os.path.abspath('docs/index.html')
        page.goto(f'file://{file_path}')

        # Take a screenshot of the initial page state
        page.screenshot(path='jules-scratch/verification/verification.png')

        browser.close()

if __name__ == "__main__":
    run()
