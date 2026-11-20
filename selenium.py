from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

URL = "https://demoqa.com/text-box"


def get_user_input():
    print("Enter the details")

    return {
        "name": input("Full Name: ").strip(),
        "email": input("Email: ").strip(),
        "current": input("Current Address: ").strip(),
        "permanent": input("Permanent Address: ").strip()
    }


def fill_form(driver, wait, data):
    fields = {
        "userName": data["name"],
        "userEmail": data["email"],
        "currentAddress": data["current"],
        "permanentAddress": data["permanent"]
    }

    for field_id, value in fields.items():
        element = wait.until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        element.clear()
        element.send_keys(value)

    submit = driver.find_element(By.ID, "submit")

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});", submit
    )

    driver.execute_script("arguments[0].click();", submit)


def verify_output(wait, data):
    wait.until(EC.visibility_of_element_located((By.ID, "output")))

    def value_of(element_id):
        text = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f"#output #{element_id}")
            )
        ).text

        return text.split(":", 1)[1].strip()

    checks = [
        ("Full Name", "name", data["name"]),
        ("Email", "email", data["email"]),
        ("Current Address", "currentAddress", data["current"]),
        ("Permanent Address", "permanentAddress", data["permanent"])
    ]

    print("\n===== VERIFICATION =====")

    all_ok = True

    for label, element_id, expected in checks:
        actual = value_of(element_id)
        ok = actual == expected
        all_ok = all_ok and ok

        print(label, ":", "PASS" if ok else "FAIL")

    print("\nResult:",
          "All details displayed correctly." if all_ok
          else "Some details do not match.")

    return all_ok


def main():
    data = get_user_input()
    driver = None

    try:
        driver = webdriver.Chrome()
        driver.maximize_window()

        wait = WebDriverWait(driver, 15)

        driver.get(URL)

        print("Opened:", driver.title)

        fill_form(driver, wait, data)
        verify_output(wait, data)

    except TimeoutException:
        print("Error: Page element did not appear in time.")

    except WebDriverException as e:
        print("Browser/WebDriver error:", e.msg)

    finally:
        if driver:
            driver.quit()
            print("Browser closed.")


if __name__ == "__main__":
    main()
