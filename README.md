# QA Selenium Automation Test - Search Functionality

## Objective
This script automates the validation of the search functionality on the Selenium Playground Table Search Demo. It ensures that searching for "New York" filters the table correctly and displays the expected number of results.

## Approach
- Navigate to the Selenium Playground Table Search Demo.
- Locate the search box and input "New York".
- Validate that exactly 5 rows remain visible after filtering.
- Verify that each row contains "New York" in the "Office" column.
- Refresh the page and ensure the total number of entries is 24.
- Use explicit waits for stability.
- Implement assertions for robust validation.

## Prerequisites
Ensure the following are installed and configured:
- Python (>= 3.8)
- Google Chrome & ChromeDriver
- Selenium WebDriver
- Pytest

### Installation
```sh
pip install selenium pytest
```

## Running the Test
1. Clone the repository or save the script as `qa_selenium_test.py`.
2. Update the `CHROMEDRIVER_PATH` if necessary.
3. Execute the test with:
   ```sh
   pytest qa_selenium_test.py
   ```

## Best Practices Followed
- **Explicit waits** to ensure elements are interactable before proceeding.
- **Assertions** to validate expected outcomes.
- **PEP8 compliance** for clean, maintainable code.
- **Parameterized selectors** for flexibility and reusability.

## Troubleshooting
- Ensure ChromeDriver is compatible with the installed Chrome version.
- If elements are not found, increase the wait time in `WebDriverWait`.
- Run in headless mode for CI/CD by modifying:
  ```python
  options.add_argument('--headless')
  ```

