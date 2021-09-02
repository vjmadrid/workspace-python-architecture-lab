# -*- coding: utf-8 -*-

import logging

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from webdriver_manager.firefox import GeckoDriverManager


logger = logging.getLogger(__name__)


# ********************
#    Setup Firefox
# ********************

DEFAULT_FIREFOX_DRIVER_PATH = "/usr/local/bin/geckodriver"
DEFAULT_FIREFOX_DOWNLOAD_FOLDER = "/Users/vjmadrid/Downloads/"


def setup_driver_firefox():
    logger.debug("[SETUP] [setup_driver_firefox] Setup Driver Firefox ...")

    caps = DesiredCapabilities().FIREFOX

    profile = webdriver.FirefoxProfile()
    profile.set_preference("webdriver_assume_untrusted_issuer", False)
    profile.update_preferences()

    return webdriver.Firefox(capabilities=caps, firefox_profile=profile)


def setup_driver_firefox_install():
    logger.debug("[SETUP] [setup_driver_chrome_install] Setup Driver Chrome with Install ...")

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver


def default_firefox_options():
    options = Options()
    options.headless = True

    # Notifications
    options.set_preference("dom.webnotifications.enabled", False)

    # Download
    options.set_preference("browser.download.dir", DEFAULT_FIREFOX_DOWNLOAD_FOLDER)
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/mp3")

    # options.add_argument("--window-size=1920,1200")

    # options.add_argument('--ignore-ssl-errors=yes')
    # options.add_argument('--ignore-certificate-errors')
    return options


def setup_driver_firefox_default():
    logger.debug("[SETUP] [setup_driver_firefox_default] Setup Driver Firefox Default ...")

    return webdriver.Firefox(
        executable_path=DEFAULT_FIREFOX_DRIVER_PATH, options=default_firefox_options()
    )


def setup_driver_firefox_with_options(custom_options):
    logger.debug("[SETUP] [setup_driver_firefox_headless] Setup Driver Firefox with Options ...")

    return webdriver.Firefox(
        executable_path=DEFAULT_FIREFOX_DRIVER_PATH, options=custom_options
    )