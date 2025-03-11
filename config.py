# MangaBot-master/config.py
env_vars = {
  # Get From my.telegram.org
  "API_HASH": "",
  # Get From my.telegram.org
  "API_ID": "",
  #Get For @BotFather
  "BOT_TOKEN": "",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "WizardBotHelper",
  # Force Subs Channel username without @
  "CHANNEL": "WizardBotHelper",
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
