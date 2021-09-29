import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_scenario_one_case_five():
    # Test: User attempts to login with a valid email address, but not linked to any valid voxy accounts
    # Step 1: Access voxy's login page: https://web-stage.voxy.com/v2/#/login/
    # Step 2: Click on the “Email” option (should be checked by default)
    # Step 3: Input a valid email address NOT linked to a voxy account
    # Step 4: Click on “continue”
    # Expected result: an unable to login message pop up will show, login will not continue

    print("Scenario: User attempts to login via email\n"
          "Test case: 5\n"
          "Test description: User attempts to login with a valid email address,"
          " but not linked to any valid voxy accounts")
    success = True
    driver = webdriver.Chrome()
    driver.get('https://web-stage.voxy.com/v2/#/login')
    # Waits for the page to load
    try:
        email_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '// *[ @ id = "login_form_field_email"] / label / i'))
        )
    finally:
        email_button.click()

    email_bar = driver.find_element_by_xpath('// *[ @ id = "login_form_email_input_field"]')
    email_bar.send_keys('test@tesmail.com')
    continue_button = driver.find_element_by_xpath('//*[@id="login_form_submit_button"]/span')
    continue_button.click()
    # Waits for error pop up to show
    try:
        pop_up = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="modals-container"]/div/div/div[2]/div'))
        )
    except selenium.common.exceptions.NoSuchElementException:
        print('Test failed: pop up not found\n\n')
        success = False
    finally:
        if success:
            print('Test completed successfully\n\n')
        driver.close()


def test_scenario_one_case_six():
    # Test: User attempts to input data on the "email" field while having the "mobile number" option selected
    # Step 1: Access voxy's login page: https://web-stage.voxy.com/v2/#/login/
    # Step 2: Click on the “Mobile Number” option (should NOT be checked by default)
    # Step 3: Attempt to input data on the “email” field
    # Expected result: The user will be unable to input data

    print("Scenario: User attempts to login via email\n"
          "Test case: 6\n"
          'Test description: ser attempts to input data on the '
          '"email" field while having the "mobile number" option selected')
    success = False
    driver = webdriver.Chrome()
    driver.get('https://web-stage.voxy.com/v2/#/login')
    # Waits for the page to load
    try:
        mobile_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login_form_field_phone"]/label/i'))
        )
    finally:
        mobile_button.click()
    try:
        driver.find_element_by_xpath('// *[ @ id = "login_form_email_input_field"]')
    except selenium.common.exceptions.NoSuchElementException:
        print('Test completed successfully\n\n')
        success = True
    finally:
        driver.close()
        if not success:
            print("Test failed: User was able to input in the email field\n\n")


def main():
    test_scenario_one_case_five()
    test_scenario_one_case_six()


if __name__ == '__main__':
    main()
