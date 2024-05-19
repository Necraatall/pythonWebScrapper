# dagger.py

import dagger

with dagger.Connection(dagger.Config.defaults()) as client:
    async def lint():
        await client.container().from_("python:3.12").with_exec([
            "pip install poetry", 
            "poetry install", 
            "poetry run ruff src tests"
        ]).run()

    async def test():
        await client.container().from_("python:3.12").with_exec([
            "pip install poetry", 
            "poetry install", 
            "poetry run pytest --cov=src tests/"
        ]).run()

    async def trivy_scan():
        await client.container().from_("aquasec/trivy:latest").with_exec([
            "trivy image --severity HIGH,CRITICAL --ignore-unfixed your-image-name"
        ]).run()

    if __name__ == "__main__":
        lint()
        test()
        trivy_scan()
