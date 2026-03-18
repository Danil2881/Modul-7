import pytest
from tools import Tools

DEFAULT_UI_TIMEOUT = 30000  # Пример значения таймаута

@pytest.fixture(scope="session")
def browser(playwright):
    chrome = playwright.chromium.launch(headless=False)
    yield chrome
    chrome.close()

@pytest.fixture(scope="function")
def context(browser):
    new_context = browser.new_context()
    new_context.tracing.start(screenshots=True, snapshots=True, sources=True)  # Трассировка для отладки
    new_context.set_default_timeout(DEFAULT_UI_TIMEOUT)
    yield new_context
    log_name = f"trace_{Tools.get_timestamp()}.zip"
    trace_path = Tools.files_dir('playwright_trace', log_name)
    new_context.tracing.stop(path=trace_path)
    new_context.close()

@pytest.fixture(scope="function")
def page(context):
    new_page = context.new_page()
    yield new_page
    new_page.close()