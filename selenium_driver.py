from selenium import webdriver
from selenium.webdriver.ie.options import Options


class SeleniumDriver:
    def __init__(self):
        opts = Options()
        # opts.ignore_protected_mode_settings = True
        opts.require_window_focus = True
        opts.ignore_zoom_level = True
        self.browser = webdriver.Ie("drivers\\32bit_IEDriverServer.exe", options=opts)
