# File: steps/hebat_login_steps.py (Disesuaikan)

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

VALID_USERNAME = ".." 
VALID_PASSWORD = ".."
LOGIN_URL = "https://hebat.elearning.unair.ac.id/login/index.php"
DASHBOARD_URL = "https://hebat.elearning.unair.ac.id/my/courses.php" 

@given('The Student is on the "Hebat" login page')
def step_impl(context):
    """Memastikan browser diarahkan ke halaman login."""
    context.driver.get(LOGIN_URL)
    login_button = context.driver.find_element(By.ID, "loginbtn")
    assert login_button.is_displayed(), "Tidak berada di halaman login Hebat"

@when('The Student enters a valid username into the "Username" field')
def step_impl(context):
    """Mengisi kolom username."""
    username_field = context.driver.find_element(By.ID, "username")
    username_field.send_keys(VALID_USERNAME)

@when('The Student enters a valid password into the "Password" field')
def step_impl(context):
    """Mengisi kolom password."""
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys(VALID_PASSWORD)

@when('The Student clicks the "Log in" button')
def step_impl(context):
    """Menekan tombol login."""
    login_button = context.driver.find_element(By.ID, "loginbtn")
    login_button.click()

@then('The Student should be redirected to the Hebat system\'s "Home" page')
def step_impl(context):
    """
    MEMPERBAIKI VERIFIKASI URL:
    Memverifikasi bahwa URL telah berubah ke halaman My courses/Dashboard.
    """
    
    WebDriverWait(context.driver, 15).until(
        EC.url_contains("/my/")
    )

    current_url = context.driver.current_url
    assert current_url != LOGIN_URL, f"Gagal dialihkan. Tetap di halaman login: {current_url}"

@then('The Student should see their courses information on the page')
def step_impl(context):
    """
    MEMPERBAIKI VERIFIKASI ELEMEN:
    Memverifikasi kehadiran elemen khas dari Dashboard, yaitu Judul 'My courses'.
    """

    page_heading_selector = (By.XPATH, "//div[@class='page-header-headings']/h1")
    
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(page_heading_selector)
        )
        
        heading_text = context.driver.find_element(*page_heading_selector).text
        assert "My courses" in heading_text, f"Header tidak menunjukkan 'My courses'. Ditemukan: {heading_text}"
        
        print("Login berhasil dan halaman 'My courses' terlihat.")
        
    except Exception as e:
        raise AssertionError(f"Gagal menemukan judul halaman 'My courses'. Error: {e}")