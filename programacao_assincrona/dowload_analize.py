import asyncio

async def download(url):
    print(f"Baixando : {url}")
    await asyncio.sleep(4)
    print(f"Download concluído para: {url}")

async def analize(url):
    print(f"Analisando : {url}")
    await asyncio.sleep(5)
    print(f"Análise concluída para: {url}")

async def main():
    url = "http://example.com"
    async with asyncio.TaskGroup() as tg:
        tg.create_task(download(url))
        tg.create_task(analize(url))

asyncio.run(main())