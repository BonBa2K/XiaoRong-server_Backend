from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication,userdata, devicedata, bluetooth, googletoken, location
from .routers import location, playingcondition, searchresult, googlecalendar, nickname, log
from .routers import turnonwifi, turnoffwifi, connectwifi
# from .routers import lineaccount
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

#app.include_router(authentication.router)
#app.include_router(blog.router)
#app.include_router(user.router)
app.include_router(bluetooth.router)
app.include_router(googletoken.router)
#app.include_router(location.router)
app.include_router(playingcondition.router)
app.include_router(searchresult.router)
app.include_router(googlecalendar.router)
#app.include_router(lineaccount.router)
app.include_router(nickname.router)
app.include_router(log.router)
app.include_router(turnonwifi.router)
app.include_router(turnoffwifi.router)
app.include_router(connectwifi.router)
#以下為穎恆
app.include_router(userdata.router)
app.include_router(devicedata.router)