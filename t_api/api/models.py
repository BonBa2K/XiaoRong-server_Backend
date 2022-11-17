from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import JSON
from sqlalchemy.sql.sqltypes import Boolean
from .database import Base

class Connectwifi(Base):
    __tablename__ = "connectwifi"
    id = Column(Integer, primary_key=True, index=True)
    SSID = Column(String)
    password = Column(String)
    isConnected = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_connectwifi = relationship("User", back_populates="connectwifi")
class Turnoffwifi(Base):
    __tablename__ = "turnoffwifi"
    id = Column(Integer, primary_key=True, index=True)
    isSuccess = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_offwifi = relationship("User", back_populates="offwifi")
class Turnonwifi(Base):
    __tablename__ = "turnonwifi"
    id = Column(Integer, primary_key=True, index=True)
    isSuccess = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_onwifi = relationship("User", back_populates="onwifi")
class Log(Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_log = relationship("User", back_populates="log")
class Nickname(Base):
    __tablename__ = "speakernickname"

    id = Column(Integer, primary_key=True, index=True)
    speakerNickname = Column(String)
    isSuccess = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_nickname = relationship("User", back_populates="nickname")
class Lineaccount(Base):
    __tablename__ = "lineaccountsr"

    id = Column(Integer, primary_key=True, index=True)
    searchResultURL = Column(String)
    userLINEID = Column(String)
    searchKeyWord = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_lineaccountsr = relationship("User", back_populates="lineaccountsr")
class Searchresult(Base):
    __tablename__ = "serachresult"

    id = Column(Integer, primary_key=True, index=True)
    searchResultURL = Column(String)
    searchKeyWord = Column(String)
    time = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_searchresult = relationship("User", back_populates="searchresult")
class Playingcondition(Base):
    __tablename__ = "playing"
    
    id = Column(Integer, primary_key=True, index=True)
    isPlaying = Column(Boolean)
    isPause = Column(Boolean)
    isStop = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_playing = relationship("User", back_populates="playing")
class Location(Base):
    __tablename__ = "location"
    
    id = Column(Integer, primary_key=True, index=True)
    userArea = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_location = relationship("User", back_populates="location")
class Googletokenc(Base):
    __tablename__ = "Googletokent"

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String)
    api_key = Column(String)
    client_secret = Column(String) # 注意為 json file 先改成 string
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_googletoken = relationship("User", back_populates="Googletokenu")
class Googlecalendar(Base):
    __tablename__ = "Googlecalendar"

    id = Column(Integer, primary_key=True, index=True)
    ACCESS_TOKEN = Column(String)
    API_KEY = Column(String)
    CLIENT_SECRET = Column(String) # 注意為 json file 先改成 string
    user_id = Column(Integer, ForeignKey('users.id'))

    creator_googlecalendar = relationship("User", back_populates="googlecalendar")
class Bluetooth(Base):
    __tablename__ = "Bluetooth"

    id = Column(Integer, primary_key=True, index=True)
    bluetoothDeviceName = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    creator_bluetooth = relationship("User", back_populates="Bluetooth") #device not user 之後建好要改
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    # location = Column(String)

    blogs = relationship("Blog", back_populates="creator")
    Bluetooth = relationship("Bluetooth", back_populates="creator_bluetooth")
    Googletokenu = relationship("Googletokenc", back_populates="creator_googletoken")
    location = relationship("Location", back_populates="creator_location")
    playing = relationship("Playingcondition", back_populates="creator_playing")
    searchresult = relationship("Searchresult", back_populates="creator_searchresult")
    lineaccountsr = relationship("Lineaccount", back_populates="creator_lineaccountsr")
    googlecalendar = relationship("Googlecalendar", back_populates="creator_googlecalendar")
    nickname = relationship("Nickname", back_populates="creator_nickname")
    log = relationship("Log", back_populates="creator_log")
    onwifi = relationship("Turnonwifi", back_populates="creator_onwifi")
    offwifi = relationship("Turnoffwifi", back_populates="creator_offwifi")
    connectwifi = relationship("Connectwifi", back_populates="creator_connectwifi")
class Blog(Base):
    __tablename__ = "Blogs"

    id = Column(Integer, primary_key=True, index=True)
    #bluetoothDeviceName = Column(String)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))
    
    creator = relationship("User",back_populates="blogs") 
#以下為穎恆
class Userdata(Base):
    __tablename__ = 'userdatas'

    id = Column(Integer, primary_key = True, index = True)
    status = Column(String)
    music_account = Column(String)
    device = Column(String)#List
    user_name = Column(String)
    user_email = Column(String)

    devicedatas = relationship("Devicedata", back_populates="creator2")
class Devicedata(Base):
    __tablename__ = 'devicedatas'

    id = Column(Integer, primary_key = True, index = True)
    user_token = Column(String)
    status = Column(String)
    dev_id = Column(String)
    dev_name = Column(String)
    language = Column(String)
    system_volume = Column(Integer)
    media_volume = Column(Integer)
    region = Column(String)
    time_zone = Column(String)
    user_account = Column(Integer, ForeignKey('userdatas.user_email'))

    creator2 = relationship("Userdata", back_populates="devicedatas")