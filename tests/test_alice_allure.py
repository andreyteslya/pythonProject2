from pytest import mark
import allure

data = [('hello', 'world'),
         ('hello', ''),
        ('123', 'world')]
ddt = {
    'argnames':'name,description',
    'argvalues':[('hello', 'world'),
         ('hello', ''),
        ('123', 'world')],
    'ids': ['general test', 'no description test', 'test with digits in name']
}
@allure.title('test allure')
@mark.parametrize(**ddt)
def test_new_testcases( desktop_app_auth, name, description):
    test_name = 'hello'
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_test_exists(name)
    desktop_app_auth.test_cases.delete_test_by_name(name)

def test_wait_more_30_sec(desktop_app_auth):
    desktop_app_auth.navigate_to('Demo pages')
    desktop_app_auth.demo.pages.open_page_after_wait(32)
    assert desktop_app_auth.demo_pages.check_wait_page()