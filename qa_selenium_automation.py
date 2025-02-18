import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL of the Table Search Demo page
URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"


@pytest.fixture(scope="module")
def driver():
    """Fixture to initialize and quit the WebDriver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run tests in headless mode
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_functionality(driver):
    """Test to validate search functionality on Selenium Playground"""
    driver.get(URL)
    time.sleep(5)  # Temporary solution

    # Locate search box and enter "New York"
    search_box = driver.find_element(By.XPATH, "//input[ @type = 'search']")
    search_box.send_keys("New York")

    # Get filtered table rows
    rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr[not(contains(@style,'display: none'))]")

    # Validate that 5 rows are displayed
    assert len(rows) == 5, f"Expected 5 rows, but got {len(rows)}"

    # Validate total entries remain 24
    total_rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr[not(contains(@style,'display: none'))]")
    assert len(total_rows) == 24, f"Expected total 24 rows, but got {len(total_rows)}"
