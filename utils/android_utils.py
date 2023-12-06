import subprocess
from utils.logger import logger


def android_get_desired_capabilities() -> dict[str, bool | str | int]:
    uuid_list = get_connected_devices()
    logger.info(f'Found these uuid: {uuid_list}. Took {uuid_list[0]}')
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        "commandTimeout": 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': uuid_list[0],
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }


def get_connected_devices() -> list[str]:
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)
        output = result.stdout

        lines = output.split('\n')[1:-2]
        devices = [line.split('\t')[0] for line in lines if 'device' in line]
        return devices
    except subprocess.CalledProcessError as e:
        logger.info(f"Error executing 'adb devices': {e}")
        return []
