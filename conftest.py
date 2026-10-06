# conftest.py
import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    """整个测试会话共享一个浏览器"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, request):
    """每个用例独立 context + 失败自动截图"""
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()
    yield page

    # 关键：用 getattr 做防御，即使钩子没设置也不会崩
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call is not None and rep_call.failed:
        try:
            allure.attach(
                page.screenshot(full_page=True),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            pass  # 截图本身出错也不能影响用例结果

    context.close()


@pytest.hookimpl(wrapper=True, tryfirst=True)   # ← 用 pytest 8 新式写法
def pytest_runtest_makereport(item, call):
    rep = yield                                 # 只 yield 一次，接收 report
    setattr(item, f"rep_{rep.when}", rep)
    return rep