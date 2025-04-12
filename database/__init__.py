from tortoise import Tortoise

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "87.242.100.33",
                "port": "5433",
                "user": "root",
                "password": "reg2025",
                "database": "fullstack_man",
            }
        }
    },
    "apps": {
        "models": {
            "models": ["database.models"],
            "default_connection": "default",
        },
    },
}


async def setup():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()