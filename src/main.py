from playwright.sync_api import sync_playwright, Page


def highlight_element(page_: Page, element_):
    page_.evaluate(
        "(element) => {element.style['border'] = '3px solid red'; element.style['background'] = 'yellow'}",
        element_
    )
    page_.screenshot(path="screenshot.png", full_page=True)


def evaluate_handle_by_xpath(page_: Page, xpath: str):
    return page_.evaluate_handle(
        "(path) => document.evaluate(path, document, null, "
        "XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;", xpath
    )


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("http://google.com")
    # element = page.evaluate_handle("document.getElementsByName('q')[0]")
    element = evaluate_handle_by_xpath(page, "//textarea[@name='q']")
    highlight_element(page, element)
    browser.close()
