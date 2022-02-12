# url_for.py
import asyncio

from quart import url_for

from quart_converter import app


async def run_url_for():
    async with app.test_request_context("/", method="GET"):
        print(url_for("person", name="Tarek"))


loop = asyncio.get_event_loop()
loop.run_until_complete(run_url_for())
