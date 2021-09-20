from pytest import  fixture
from playwright.sync_api import  sync_playwright
from page_objects.application import App
import setting

@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture(scope='session')
def desktop_app(get_playwright):
    app = App(get_playwright, base_url=setting.BASE_URL)
    app.goto('/')
    yield app
    app.close()

@fixture(scope='session')
def desktop_app_auth(desktop_app):
    desktop_app.goto('/login')
    desktop_app.login(**setting.USER)
    yield desktop_app


    

# @fixture()
# def ultimate_answer():
#     return 42
#
# @fixture()
# def new_answer(ultimate_answer):
#     return ultimate_answer+1
