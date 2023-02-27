from modules.ui.page_object.sign_in_page import SignInPage
import pytest

@pytest.mark.ui 
def test_incorrect_username_page_object():
    sing_in_page = SignInPage()

    sing_in_page.go_to()

    sing_in_page.try_login("gkfmgdf@gmail.com", "mgkfqewrkmfk")

    assert sing_in_page.check_title("Sign in to GitHub · GitHub")

    sing_in_page.driver.close()