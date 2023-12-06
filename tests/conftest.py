import subprocess
import time
import pytest
import socket
from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils.logger import logger
from utils.android_utils import android_get_desired_capabilities


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
        logger.info("Ожидание доступности порта Appium server 4723")
        time.sleep(1)

    yield

    close_appium_server(4723)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    capabilities_options = UiAutomator2Options().load_capabilities(android_get_desired_capabilities())
    driver = webdriver.Remote('http://localhost:4723', options=capabilities_options)

    logger.info("Appium driver cоздан")

    yield driver

    driver.quit()
    logger.info("Завершен процесс Appium driver")


def is_port_open(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0


def close_appium_server(port: int) -> None:
    appium_pid = get_pid_by_port(port)
    if appium_pid:
        msg = terminate_process_by_pid(appium_pid)
        logger.info(f"Завершение Appium server. Сообщение: {msg}.")
    else:
        logger.info(f"Завершение Appium server невозможно. Сообщение: PID прцоесса не найден.")


def get_pid_by_port(port: int) -> int | None:
    command = f'netstat -ano | find "{port}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        lines = result.stdout.splitlines()
        if lines:
            lines = [line.split() for line in lines if line.split()[-1] != '0']
            pid = lines[-1][-1]
            return int(pid)

    return None


def terminate_process_by_pid(pid: int) -> str:
    try:
        subprocess.run(['taskkill', '/F', '/PID', str(pid)], check=True)
        return f"Process with PID {pid} killed successfully"
    except subprocess.CalledProcessError as e:
        return f"Failed to kill process with PID {pid}. Error: {e}"
