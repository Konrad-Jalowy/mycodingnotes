import asyncio

async def zadanie_1():
    await asyncio.sleep(1)
    print("Zadanie 1 zakończone")

async def zadanie_2():
    await asyncio.sleep(2)
    print("Zadanie 2 zakończone")

async def main():
    task1 = asyncio.create_task(zadanie_1())
    task2 = asyncio.create_task(zadanie_2())
    await task1
    await task2

asyncio.run(main())