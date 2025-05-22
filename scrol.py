import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--start-maximized'])
    page = await browser.newPage()
    await page.goto('https://faucets.chain.link/', {'waitUntil': 'networkidle2'})

    # Wait for the wallet address input field to appear
    await page.waitForSelector('input[type="text"]', timeout=20000)

    # Enter your Scroll Sepolia wallet address
    wallet_address = '0xYourScrollSepoliaWalletAddress'  # <-- Replace with your address
    await page.type('input[type="text"]', wallet_address)

    # Select Scroll Sepolia faucet (update selector if needed)
    # The label's "for" attribute might be like "scrollSepolia"
    await page.click('label[for="scrollSepolia"]')

    # Click the "Send Request" button (update selector if needed)
    await page.click('button[type="submit"]')

    # Wait to observe the result
    await page.waitFor(5000)

    print("Faucet request sent (if all went well).")
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
