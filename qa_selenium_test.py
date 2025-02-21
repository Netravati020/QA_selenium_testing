
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run without UI
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_functionality(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)

    # Locate search box and enter "New York"
    search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='search']")))
    search_box.send_keys("New York")

    time.sleep(3)  # Allow table to filter
    total_rows = 0

    while True:
        # Get visible rows after search
        rows = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr[not(contains(@style,'display: none'))]")

        for row in rows:
            office_column = row.find_element(By.XPATH, ".//td[3]")  # Office column
            assert office_column.text.strip() == "New York", f"Expected 'New York', but got {office_column.text.strip()}"

        total_rows += len(rows)

        # Locate "Next" button
        next_button = driver.find_element(By.ID, "example_next")

        # Check if "Next" button is disabled (last page)
        if "disabled" in next_button.get_attribute("class"):
            break  # Stop loop

        # Click "Next" and wait for new rows
        next_button.click()
        wait.until(lambda d: len(
            d.find_elements(By.XPATH, "//table[@id='example']/tbody/tr[not(contains(@style,'display: none'))]")) > 0)

    # Validate total number of filtered rows
    assert total_rows == 5, f"Expected 5 'New York' rows, but got {total_rows}"
