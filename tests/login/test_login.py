def test_user_login(user_login_fixture):
    login_page = user_login_fixture
    login_page.sign_in("qa.ajax.app.automation@gmail.com", "qa_automation_password")

    print(login_page.driver.page_source)
    assert True
