from enum import Enum

from qfluentwidgets import getIconColor, Theme, FluentIconBase


class MyFluentIcon(FluentIconBase, Enum):
    """ Custom icons """

    HOME = "Home"
    SEARCH = "Search"
    CHAT = "Chat"
    CLOUD = "Cloud"
    SETTING = "Setting"
    
    COPY = "Copy"

    def path(self, theme=Theme.AUTO):
        # getIconColor() return "white" or "black" according to current theme
        return f'./resource/icons/{self.value}_{getIconColor(theme)}.svg'