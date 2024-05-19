# src/dagger_io.py

import dagger

async def main():
    async with dagger.Connection() as client:
        # Define your tasks
        task_init = client.task(name="init")
        task_lint = client.task(name="lint")
        task_test = client.task(name="test")
        task_fetch_data = client.task(name="fetch_data")
        task_analyze = client.task(name="analyze")

        # Run tasks
        await task_init.run()
        await task_lint.run()
        await task_test.run()
        await task_fetch_data.run()
        await task_analyze.run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
