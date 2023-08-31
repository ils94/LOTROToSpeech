import threading
import asyncio


def start_monitoring(function):
    monitor_thread = threading.Thread(target=function)
    monitor_thread.setDaemon(True)
    monitor_thread.start()


def monitor_loop(function):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(function)
