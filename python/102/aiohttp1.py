import aiohttp
import asyncio

async def pobierz_dane_z_apis(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3'
    ]
    zadania = [pobierz_dane_z_apis(url) for url in urls]
    wyniki = await asyncio.gather(*zadania)
    for wynik in wyniki:
        print(wynik)

if __name__ == '__main__':
    asyncio.run(main())  # Użycie asyncio.run() zapewnia właściwe zarządzanie pętlą zdarzeń
