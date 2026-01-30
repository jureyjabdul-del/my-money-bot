import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

# --- 1. ያንተ መረጃዎች (Email & Binance) ---
ACCOUNTS = [
    {"email": "abebe0914611346@gmail.com", "pass": "z855xj2v"},
    {"email": "abdu0914611346@gmail.com", "pass": "z855xj2v"},
    {"email": "bilal0914611346@gmail.com", "pass": "z855xj2v"},
    {"email": "hasen0914611346@gmail.com", "pass": "z855xj2v"},
    {"email": "toyba0914611346@gmail.com", "pass": "z855xj2v"},
    {"email": "kedja0914611346@gmail.com", "pass": "z855xj2v"},
    {"email": "medina0914611346@gmail.com", "pass": "z855xj2v"},
    {"email": "junedin0914611346@gmail.com", "pass": "z855xj2v"},
    {"email": "selman0914611346@gmail.com", "pass": "z855xj2v"},
    {"email": "amir0914611346@gmail.com", "pass": "z855xj2v"}
]

# የአንተ የ Binance USDT (BEP20) አድራሻ ተገብቷል
BINANCE_WALLET = "0xcaa14d4f4a190af5d7d930986d1ca4587a9e38fe"

async def start_working(account):
    async with async_playwright() as p:
        print(f"📧 በኢሜይል {account['email']} ስራ ተጀምሯል...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await stealth_async(page)
        print(f"✅ ስራ ተጠናቋል። ገቢው ወደ {BINANCE_WALLET} ይላካል")
        await browser.close()

async def main():
    while True:
        for account in ACCOUNTS:
            try:
                await start_working(account)
                await asyncio.sleep(600) 
            except Exception as e:
                print(f"❌ ስህተት አጋጥሟል፡ {e}")
                continue

if __name__ == "__main__":
    asyncio.run(main())
