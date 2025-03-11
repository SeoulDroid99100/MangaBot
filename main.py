import asyncio as aio
from bot import *
from flask import Flask
import threading
import uvloop  # Import uvloop

# --- Flask App ---
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

def run_flask():
    """Run the Flask app in a separate thread."""
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

# --- Async Main & Bot ---
async def async_main():
    db = DB()
    await db.connect()

if __name__ == '__main__':
    # Set uvloop as the event loop policy
    uvloop.install()  # This line is the key addition for uvloop

    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Run the asyncio event loop (now using uvloop)
    loop = aio.get_event_loop_policy().get_event_loop()  #or aio.get_event_loop() will also work.
    loop.run_until_complete(async_main())
    loop.create_task(manga_updater())
    for i in range(10):
        loop.create_task(chapter_creation(i + 1))
    bot.run()
