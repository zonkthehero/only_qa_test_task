import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://only.digital/"


@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\nQuit browser..")
    browser.quit()

def load_page_and_wait_element(browser, url, locator, timeout=10):
    browser.get(url)
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.visibility_of_element_located(locator))
    return element

def scroll_to_element(browser, element):
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

class TestMainPage():
    def test_guest_should_see_footer(self, browser):
        footer = load_page_and_wait_element(browser, link, (By.CSS_SELECTOR, ".Footer_grid__lfZ34"))
        scroll_to_element(browser, footer)
        assert footer.is_displayed()

    def test_guest_should_see_logo_in_footer(self, browser):
        footer = load_page_and_wait_element(browser, link, (By.CSS_SELECTOR, ".Footer_logo__2QEhf"))
        scroll_to_element(browser, footer)
        assert footer.is_displayed()

    def test_guest_should_see_tg_button_in_footer(self, browser):
        tg_button = load_page_and_wait_element(browser, link, (By.XPATH, "//*[contains(@class, 'Socials_socialsWrap__DPtp_ Footer_socials__C39yX')]/descendant::*[contains(@class, 'buttons SocialButton_root__MjR_H ')][3]"))
        scroll_to_element(browser, tg_button)
        assert tg_button.is_displayed()


    def test_guest_should_see_pdf_button_in_footer(self, browser):
        pdf_xpath = (
            "//*[contains(@class, 'Documents_documentsWrap__iNfwU') and contains(@class, 'Footer_documents___mRvU')]"
            "//*[contains(@class, 'Documents_documents__Ly1Oa')]"
            "//*[contains(@class, 'buttons') and contains(@class, 'Button_root__GbzzH') and contains(@class, 'Button_short__tCZ24') and contains(@class, 'Button_primary__swzAa')][1]"
        )
        pdf_button = load_page_and_wait_element(browser, link, (By.XPATH, pdf_xpath))
        scroll_to_element(browser, pdf_button)
        assert pdf_button.is_displayed()
