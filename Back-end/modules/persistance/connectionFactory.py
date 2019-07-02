import asyncio
import asyncpg
from asyncpg.connection import Connection
from modules.utils import config

async def getDBDriverConnection():
    try:
        conn = await asyncpg.connect('postgresql://' + config.getDBUser() + "@database:5432/" + config.getDBName(), password=config.getDBPwd())
        return conn
    except Exception as exceptMsg:
        print(str(exceptMsg))
        raise Exception