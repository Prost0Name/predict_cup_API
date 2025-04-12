import asyncio
import database
import api

async def main():
    await database.setup()
    await api.setup()

if __name__ == "__main__":
    asyncio.run(main())