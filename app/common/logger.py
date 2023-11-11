import logging
from datetime import datetime

color = {
    logging.DEBUG: "\033[94m",
    logging.INFO: "\033[0m",
    logging.WARNING: "\033[33m",
    logging.ERROR: "\033[31m",
    logging.CRITICAL: "\033[95m"
}

class loggingHandler(logging.StreamHandler):
	def emit(self, record):
		try:
			self.stream.write(color[record.levelno])
			super().emit(record)
		finally:
			self.stream.write("\033[0m")

class sysLog:
    
    def __init__(self, level="WARNING") -> None:
        self.logger = logging.getLogger(__file__)
        if not self.logger.hasHandlers(): # 二重にハンドラーが作成されると同じログが複数流れるため
            self.logger.setLevel(level)
            ntime = '{:%Y-%m-%d}.log'.format(datetime.now())
            latestfile = ntime
            fhandler = logging.FileHandler(ntime, "w", encoding="utf-8")
            fhandler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y/%m/%d %H:%M:%S'))
            self.logger.addHandler(fhandler)
            handler = loggingHandler()
            handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y/%m/%d %H:%M:%S'))
            self.logger.addHandler(handler)
        else:
            self.logger.debug("Logging handler was not created because it already exists.")