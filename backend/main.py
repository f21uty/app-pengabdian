from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import auth, kegiatan
from api.internal import admin
from api.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(auth.router)
app.include_router(kegiatan.router)
app.include_router(admin.router)
