import asyncio


async def execute(x):
    print('Number:', x)
print('Afger calling execute')
loop = asyncio.get_event_loop()  # 进行了对coroutine的封装成task
task = asyncio.ensure_future(execute(2))
loop.run_until_complete(task)
# 进行了对coroutine的封装成task
# loop.run_until_complete(coroutine)
print('After calling loop')
