from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, kegiatan, users, pamong
from app.internal import admin
from app.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(kegiatan.router)
app.include_router(admin.router)
app.include_router(pamong.router)
