
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Get the absolute path to the HTML file
        file_path = os.path.abspath('docs/index.html')

        # Go to the local HTML file
        await page.goto(f'file://{file_path}')

        # Wait for the images to be loaded
        await page.wait_for_selector('img[alt="スタジオ図面"]')
        await page.wait_for_selector('img[alt="スタジオ内観"]')

        # Take a screenshot of the entire page
        await page.screenshot(path='jules-scratch/verification/verification.png', full_page=True)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
