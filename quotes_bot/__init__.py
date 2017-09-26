from .bot_manager import start

if python_version_manager.is_python_2():
    # In python 3.x, the default encoding is already utf8.
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

start()
