from behave import given, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

VALID_USERNAME = "nim"
VALID_PASSWORD = "password"
LOGIN_URL = "https://hebat.elearning.unair.ac.id/login/index.php"
DASHBOARD_URL = "https://hebat.elearning.unair.ac.id/my/courses.php"

PPL_COURSE_NAME = "Pembangunan Perangkat Lunak"
ASSIGNMENT_NAME = "Penugasan PPT"

@given('The Student is logged into the Hebat platform')
def step_impl_login_prerequisite(context):
    current_url = context.driver.current_url
    if "/my/" in current_url or "/course/" in current_url:
        print("Sudah login, lanjut ke langkah berikutnya.")
        return

    context.driver.get(LOGIN_URL)
    try:
        username_field = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys(VALID_USERNAME)

        password_field = context.driver.find_element(By.ID, "password")
        password_field.send_keys(VALID_PASSWORD)

        login_button = context.driver.find_element(By.ID, "loginbtn")
        login_button.click()

        WebDriverWait(context.driver, 15).until(EC.url_contains("/my/"))
        print("✅ Login berhasil.")
    except Exception as e:
        raise AssertionError(f"Gagal melakukan login. Error: {e}")

@given('The Student is on the "Pembangunan Perangkat Lunak (PPL) course" page')
def step_impl_on_course_page(context):
    if "/my/" not in context.driver.current_url:
        context.driver.get(DASHBOARD_URL)
        WebDriverWait(context.driver, 10).until(EC.url_contains("/my/"))

    try:
        course_link_selector = (By.PARTIAL_LINK_TEXT, PPL_COURSE_NAME)
        course_link = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable(course_link_selector)
        )
        print(f"Menemukan mata kuliah: {course_link.text}")
        course_link.click()

        WebDriverWait(context.driver, 15).until(EC.url_contains("/course/view.php"))
        print(f"✅ Berhasil masuk ke halaman '{PPL_COURSE_NAME}'.")
    except Exception as e:
        raise AssertionError(f"Gagal membuka mata kuliah '{PPL_COURSE_NAME}'. Error: {e}")

@when('The Student clicks on a specific "Assignment Title" link')
def step_impl_click_assignment_link(context):
    try:
        assignment_selector = (
            By.XPATH,
            f"//div[contains(@class, 'activity-item')]"
            f"[.//span[contains(normalize-space(.), '{ASSIGNMENT_NAME}')]]"
            f"//a[contains(@href, 'mod/assign/view.php')]"
        )

        assignment_link = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable(assignment_selector)
        )

        print(f"Menemukan tugas: '{ASSIGNMENT_NAME}'. Mengklik...")
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", assignment_link)
        time.sleep(1)
        assignment_link.click()

        WebDriverWait(context.driver, 15).until(
            EC.url_contains("/mod/assign/view.php")
        )
        print("✅ Halaman tugas berhasil dibuka.")

        time.sleep(3)
        context.driver.quit()
        print("🛑 Browser ditutup otomatis setelah membuka halaman tugas.")
    except Exception as e:
        print(f"DEBUG: XPath dicoba: {assignment_selector[1]}")
        try:
            context.driver.quit()
        except:
            pass
        raise AssertionError(f"Gagal membuka tugas '{ASSIGNMENT_NAME}'. Error: {e}")
