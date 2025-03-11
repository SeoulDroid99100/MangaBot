# MangaBot-master/config.py
env_vars = {
  # Get From my.telegram.org
  "API_HASH": "",
  # Get From my.telegram.org
  "API_ID": "",
  #Get For @BotFather
  "BOT_TOKEN": "",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "sqlite:///mydatabase.db",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "drunkCache0",
  # Force Subs Channel username without @
  "CHANNEL": "drunkCache0",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "",
  # Put Thumb Link
  "THUMB": ""
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///:memory:' # This line is changed.

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
