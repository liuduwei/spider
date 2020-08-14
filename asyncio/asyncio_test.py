import asyncio
import time

import aiohttp

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response

url = 'https://www.baidu.com'
""" coruntine = get(url) """


async def my_request():
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'response', response)


""" coruntine = my_request() """
tasks = [asyncio.ensure_future(my_request()) for _ in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('Cost:', end - start)
