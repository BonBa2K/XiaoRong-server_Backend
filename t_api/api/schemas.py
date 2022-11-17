from typing import List, Optional
from pydantic import BaseModel
# from sqlalchemy import JSON

class BlogBase(BaseModel):
    user_id: int
    class Config():
        orm_mode = True 
class Blog(BlogBase):
    title:str
    body:str
    user_id:int
    class Config():
        orm_mode = True 
class User(BaseModel):
    name: str
    email: str
    password:str
class ShowUser(BaseModel):
    name: str
    email: str
    password:str
    location:str #如何只輸出 loation
    blogs :List[Blog]= []
    id:int
    class Config():
        orm_mode = True 
class ShowBlog(BaseModel):
    title: str
    body: str
    id: int
    creator: ShowUser

    class Config():
        orm_mode = True
class Connectwifi(BaseModel):
    # 連接 Wi-Fi
    SSID:str
    password:str
    isConnected:bool
    user_id:int
    class Config():
        orm_mode = True 
class Turnoffwifi(BaseModel):
    # 開啟 Wi-Fi AP
    isSuccess:bool
    user_id:int
    class Config():
        orm_mode = True 
class Turnonwifi(BaseModel):
    # 開啟 Wi-Fi AP
    isSuccess:bool
    user_id:int
    class Config():
        orm_mode = True 
class Log(BaseModel):
    # LOG接收
    status:str
    user_id:int
    class Config():
        orm_mode = True 
class Nickname(BaseModel):
    # 請求刪除音箱資料
    speakerNickname:str
    isSuccess:bool
    user_id:int
    class Config():
        orm_mode = True 
class Googlecalendar(BaseModel):
    # Google Calendar
    ACCESS_TOKEN:str
    API_KEY:str
    CLIENT_SECRET:str #JSON
    user_id:int
    class Config():
        orm_mode = True 
class Lineaccount(BaseModel):
    # 傳送搜尋結果給使用者的 LINE 帳號
    searchResultURL:str
    userLINEID:str
    searchKeyWord:str
    user_id:int
    class Config():
        orm_mode = True 
class Searchresult(BaseModel):
    # 傳送搜尋結果給前端網頁
    searchResultURL:str
    searchKeyWord:str
    time:str    
    user_id:int
    class Config():
        orm_mode = True 
class Playingcondition(BaseModel):
    # 系統 playing 狀態偵測
    isPlaying:bool
    isPause:bool
    isStop:bool
    user_id:int
    class Config():
        orm_mode = True 
class Location(BaseModel):
    # 系統 playing 狀態偵測
    isPlaying:bool
    isPause:bool
    isStop:bool
    user_id: int
class Googletokens(BaseModel):
    # Google 使用者 Access_Token
    user_id:int
    access_token:str  #ACCESS_TOKEN
    api_key:str
    client_secret:str # 注意正確為 json file 先改成 string
    class Config():
        orm_mode = True 
class ShowGoogletoken(BaseModel):
    # Google 使用者 Access_Token
    user_id:int
    access_token:str  #ACCESS_TOKEN
    api_key:str
    client_secret:str # 注意正確為 json file 先改成 string
    id:int
    class Config():
        orm_mode = True 
class Bluetooth(BaseModel):
    # 藍牙音箱更改名稱
    bluetoothDeviceName: str
    user_id: int
class Login(BaseModel):
    username:str
    password:str
class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    email: Optional[str] = None

#以下為穎恆的
class UserdataBase(BaseModel):
    status: str
    music_account: str
    device: str
    user_name: str
    user_email: str
class Userdata(UserdataBase):
    class Config():
        orm_mode = True

class UpdateEmailBase(BaseModel):
    user_email: str
    new_email: str
class UpdateEmail(UpdateEmailBase):
    class Config():
        orm_mode = True

class UpdateNameBase(BaseModel):
    user_email: str
    user_name: str
class UpdateName(UpdateNameBase):
    class Config():
        orm_mode = True

class DevicedataBase(BaseModel):
    user_token: str
    status: str
    dev_id: str
    dev_name: str
    language: str
    system_volume: int
    media_volume: int
    region: str
    time_zone: str
    user_account: str
class Devicedata(DevicedataBase):
    class Config():
        orm_mode = True

class CreateDevicedataBase(BaseModel):
    user_token: str
    dev_id: str
    dev_name: str
    language: str
    system_volume: int
    media_volume: int
    region: str
    time_zone: str
    user_account: str
class CreateDevicedata(CreateDevicedataBase):
    class Config():
        orm_mode = True

class UpdateRegionBase(BaseModel):
    dev_id: str
    region: str
class UpdateRegion(UpdateRegionBase):
    class Config():
        orm_mode = True

class UpdateTimezoneBase(BaseModel):
    dev_id: str
    time_zone: str
class UpdateTimezone(UpdateTimezoneBase):
    class Config():
        orm_mode = True