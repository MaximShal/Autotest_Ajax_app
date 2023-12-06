import pytest

from utils.logger import logger


@pytest.mark.parametrize("input_data, expected_output", [
    (("example@example.com", "ex_password"), False),
    (("qa.ajax.app.automation@gmail.com", "qa_automation_password"), True),
])
def test_user_login(user_login_fixture, input_data, expected_output):
    logger.info(f'Using {input_data} credentials, expected output: {expected_output}')
    login_page = user_login_fixture
    result = login_page.sign_in(username=input_data[0], password=input_data[1])
    assert result == expected_output
