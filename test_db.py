from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.sql import text
import asyncio

DATABASE_URL = "postgresql+asyncpg://postgres:Push1234@localhost:5435/postgres"

async def test_connection():
    engine = create_async_engine(DATABASE_URL, echo=True)
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            print(f"Database connection successful! Result: {result.scalar()}")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(test_connection())
