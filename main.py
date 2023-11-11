import sys

import orjson
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from app.common.logger import sysLog
from app.view.mw import LuminaUI

level = "WARNING"
with open("config.json", "r") as f:
    cfg = orjson.loads(f.read())
    if cfg["debug"]:
        level = "DEBUG"

logger = sysLog(level).logger

QApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

app = QApplication(cfg["args"])
LUI = LuminaUI()
LUI.setWindowTitle("Lumina - Fluent Misskey Client")
LUI.show()
app.exec_()
