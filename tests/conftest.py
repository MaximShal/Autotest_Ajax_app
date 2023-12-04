import logging
import subprocess
import time
import pytest
import socket
from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils.android_utils import android_get_desired_capabilities

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )

    while not is_port_open('localhost', 4723):
        logger.info("Ожидание доступности порта 4723")
        time.sleep(1)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    logger.info("Создание драйвера Appium")

    capabilities_options = UiAutomator2Options().load_capabilities(android_get_desired_capabilities())
    driver = webdriver.Remote('http://localhost:4723', options=capabilities_options)

    yield driver


def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0
