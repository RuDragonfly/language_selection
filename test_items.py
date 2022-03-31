import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button(browser):
    
    browser.get(link)
    browser.implicitly_wait(50)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    time.sleep(5)
    assert button
