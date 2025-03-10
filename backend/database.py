from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL = "postgresql+asyncpg://postgres:Push1234@localhost:5435/postgres"
DATABASE_URL = "postgresql+asyncpg://postgres:Push1234@localhost:5432/mydatabase"


engine = create_async_engine(DATABASE_URL, echo=True)


SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()


async def get_db():
    async with SessionLocal() as session:
        yield session
