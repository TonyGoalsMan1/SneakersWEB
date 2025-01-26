from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.sql import text
from .models import User, Sneaker
from .auth import get_password_hash, verify_password, create_access_token
from .schemas import UserCreate, SneakerCreate

DATABASE_URL = "postgresql+asyncpg://postgres:Push1234@localhost:5432/mydatabase"

# DATABASE_URL = "postgresql+asyncpg://postgres:Push1234@localhost:5435/postgres"


Base = declarative_base()
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)



app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with async_session() as session:
        yield session


@app.get("/test_db/")
async def test_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        return {"status": "Database is connected"}
    except Exception as e:
        return {"status": "Failed to connect", "error": str(e)}


@app.post("/register/")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        print("Register function started")  # Отладка 1
        hashed_password = get_password_hash(user.password)
        print(f"Password hashed: {hashed_password}")  # Отладка 2

        # Проверяем перед вставкой
        print(f"User data to insert: username={user.username}, password={hashed_password}")

        query = text(
            "INSERT INTO users (username, hashed_password, created_at) VALUES (:username, :hashed_password, NOW()) RETURNING id"
        )
        result = await db.execute(query, {"username": user.username, "hashed_password": hashed_password})
        user_id = result.scalar()  # Получаем ID добавленного пользователя
        await db.commit()

        # Логирование после вставки
        print(f"User added successfully: username={user.username}, ID={user_id}")
        return {"message": "User registered successfully", "user_id": user_id}
    except Exception as e:
        await db.rollback()
        print(f"Error during registration: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to register user: {str(e)}")



@app.get("/users/")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


@app.get("/add_test_user/")
async def add_test_user(db: AsyncSession = Depends(get_db)):
    try:
        db_user = User(username="testuser", hashed_password="testpassword")
        db.add(db_user)
        await db.commit()
        return {"status": "User added"}
    except Exception as e:
        return {"status": "Failed", "error": str(e)}


@app.post("/login/")
async def login(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user.username))
    db_user = result.scalars().first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/sneakers/")
async def create_sneaker(sneaker: SneakerCreate, db: AsyncSession = Depends(get_db)):
    db_sneaker = Sneaker(
        name=sneaker.name,
        size=sneaker.size,
        price=sneaker.price,
        description=sneaker.description,
        owner_id=sneaker.owner_id,
    )
    db.add(db_sneaker)
    await db.commit()
    await db.refresh(db_sneaker)
    return db_sneaker


@app.get("/sneakers/")
async def get_sneakers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Sneaker))
    sneakers = result.scalars().all()
    return sneakers


@app.get("/sneakers/{id}")
async def get_sneaker(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Sneaker).where(Sneaker.id == id))
    sneaker = result.scalars().first()
    if not sneaker:
        raise HTTPException(status_code=404, detail="Sneaker not found")
    return sneaker


@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with PostgreSQL!"}


from sqlalchemy.sql import text

@app.get("/test_db_connection/")
async def test_db_connection(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        return {"status": "Database is connected"}
    except Exception as e:
        return {"status": "Failed to connect", "error": str(e)}


@app.delete("/sneakers/{id}")
async def delete_sneaker(id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Sneaker).where(Sneaker.id == id))
        sneaker = result.scalars().first()
        if not sneaker:
            raise HTTPException(status_code=404, detail="Sneaker not found")

        await db.delete(sneaker)
        await db.commit()
        return {"message": f"Sneaker with id {id} has been deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete sneaker: {str(e)}")



@app.delete("/users/{id}")
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(User).where(User.id == id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        await db.delete(user)
        await db.commit()
        return {"message": f"User with id {id} has been deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete user: {str(e)}")


@app.put("/sneakers/{id}")
async def update_sneaker(
        id: int, updated_sneaker: SneakerCreate, db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(select(Sneaker).where(Sneaker.id == id))
        sneaker = result.scalars().first()
        if not sneaker:
            raise HTTPException(status_code=404, detail="Sneaker not found")

        # Обновление полей
        sneaker.name = updated_sneaker.name
        sneaker.size = updated_sneaker.size
        sneaker.price = updated_sneaker.price
        sneaker.description = updated_sneaker.description
        sneaker.owner_id = updated_sneaker.owner_id

        await db.commit()
        await db.refresh(sneaker)
        return {"message": "Sneaker updated successfully", "sneaker": sneaker}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update sneaker: {str(e)}")


# uvicorn backend.server:app --reload

# from fastapi.middleware.cors import CORSMiddleware
#
# app = FastAPI()
#
# # Разрешённые источники
# origins = [
#     "http://localhost:8080",  # Адрес вашего фронтенда
#     "http://127.0.0.1:8080",  # Альтернативный адрес
# ]
#
# # Настройка CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
