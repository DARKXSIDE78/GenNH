# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Bot Information
API_ID = int(environ.get("API_ID", "29478593"))
API_HASH = environ.get("API_HASH", "24c3a9ded4ac74bab73cbe6dafbc8b3e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8108195011:AAHr_JhDOxmHDPJcC-Z8epJQ82t1GfHfap4")

PICS = (environ.get('PICS', 'https://img.freepik.com/premium-photo/cute-anime-girl-character-sexy-body-bikini-summer-vibe-swimming-pool_483949-9736.jpg https://img.freepik.com/premium-photo/sexy-anime-style-girl-with-costume-gothic-dark-black-style-background-wallpaper-ai-generated-image_1087980-6703.jpg https://image.cdn2.seaart.me/2023-12-19/cm0p3g5e878c73fn099g/3460a918c2e79304bbe77d8839e522e6be2be1a2_high.webp https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d2c5c087-28c0-45d2-a01c-5e8a6f5c3663/dh8qy2r-0c22fb27-2cb5-43fa-85f0-8a6b6c06d34d.png/v1/fill/w_1280,h_720,q_80,strp/ai_anime_art__wallpaper__by_aianimeart9_dh8qy2r-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzIwIiwicGF0aCI6IlwvZlwvZDJjNWMwODctMjhjMC00NWQyLWEwMWMtNWU4YTZmNWMzNjYzXC9kaDhxeTJyLTBjMjJmYjI3LTJjYjUtNDNmYS04NWYwLThhNmI2YzA2ZDM0ZC5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.qLWa7NZozb-5UJl7IXk8RIj_z1OOow-8_-3VhzANGXE https://w0.peakpx.com/wallpaper/150/288/HD-wallpaper-anime-bikini-model-anime-ai-art-model-abstract-redhead-bikini.jpg')).split() # Bot Start Picture
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6302971969 7086472788').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "GenHRoBot") # without @
PORT = environ.get("PORT", "8000")

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False

# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "")

# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://nitinkumardhundhara:DARKXSIDE78@cluster0.wdive.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "GenHRoBot")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002476753332"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', True)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "shrinkme.io") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "d7173d21335001918a3ebec8c8f2d1a9e3b42f43") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', False)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "https://t.me/GenAnimeOfc") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://testofvjfilter-1fa60b1b8498.herokuapp.com/")


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
    
