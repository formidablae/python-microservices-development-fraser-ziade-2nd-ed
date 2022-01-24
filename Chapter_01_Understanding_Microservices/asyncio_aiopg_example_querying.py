import asyncio
import aiopg


# Start and example postgres instance with:
# docker run -p5432:5432 name some-postgres \
# -e POSTGRES_PASSWORD=mysecretpassword -d postgres

dsn = "dbname=postgres user=postgres password=mysecretpassword host=127.0.0.1"

async def go():
    pool = await aiopg.create_pool(dsn)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 1")
            ret = []
            async for row in cur:
                ret.append(row)
            assert ret == [(1,)]
    await pool.clear()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(go())
