import asyncio

async def pobierz_dane():
    print("Początek pobierania danych...")
    await asyncio.sleep(2)  # Symulacja opóźnienia
    print("Dane pobrane!")

async def main():
    await pobierz_dane()

asyncio.run(main())