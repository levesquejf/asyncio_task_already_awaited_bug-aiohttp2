import aiohttp
import asyncio


async def http_call(url):
    timeout = aiohttp.ClientTimeout(total=2)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                print(f"Status code is {resp.status}")
    except asyncio.TimeoutError:
        print("TimeoutError")


async def run():
    await http_call("http://10.10.10.10")
    await http_call("http://10.10.10.10")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


if __name__ == "__main__":
    main()
