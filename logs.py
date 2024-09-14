import sys
import os
import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler

if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")

def create_log_file(file_path: Path):
    if not file_path.exists():
        file_path.mkdir()
    file_path.open().close()

def check_debug():
    get_trace = getattr(sys, 'gettrace', None)
    if get_trace is None or 'PYDEVD_LOAD_VALUES_ASYNC' not in os.environ:
        return False
    else:
        if 'PYDEVD_LOAD_VALUES_ASYNC' in os.environ:
            return True
        elif get_trace() is None:
            return False
        else:
            return True

log_file_name = './files/logs/bot.log'
file_handlers = (RotatingFileHandler(log_file_name, backupCount=20, maxBytes=2000000, encoding='utf-8'),)

if not check_debug():
    create_log_file(Path(log_file_name))
else:
    log_file_name = ''
    file_handlers = None

# TODO: https://betterstack.com/community/guides/logging/how-to-start-logging-with-python/
# def keep_log_size():
#     f = open('logs/bot.log')
#     _l = len(f.readlines())
#     f.close()
#     if _l >= 10000:
#         os.rename('logs/bot.log', newName)


logging.basicConfig(level=logging.DEBUG,
                    # filename=log_file_name,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format="%(name)s %(asctime)s %(levelname)s %(message)s",
                    # encoding='utf-8',
                    handlers=file_handlers)


logging.info(f'{"-" * 47}program started{"-" * 47}')