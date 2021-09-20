class TestMyClass:
    def setup(self):
        print('hello')

    def test_new_testcases(self, desktop_app_auth):
        test_name = 'hello'
        desktop_app_auth.navigate_to('Create new test')
        desktop_app_auth.create_test(test_name, 'world')
        desktop_app_auth.navigate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_test_exists(test_name)
        desktop_app_auth.test_cases.delete_test_by_name(test_name)

    def test_new_testcases_no_discr(self, desktop_app_auth):
        test_name = 'hello'
        desktop_app_auth.navigate_to('Create new test')
        desktop_app_auth.create_test(test_name, '')
        desktop_app_auth.navigate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_test_exists(test_name)
        desktop_app_auth.test_cases.delete_test_by_name(test_name)

    def test_new_testcases_digits_name(self, desktop_app_auth):
        test_name = 'hello'
        desktop_app_auth.navigate_to('Create new test')
        desktop_app_auth.create_test(test_name, 'world')
        desktop_app_auth.navigate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_test_exists(test_name)
        desktop_app_auth.test_cases.delete_test_by_name(test_name)

    def teardown(self):
        print('work is done, go outside')


