# File: features/steps/login.py (INI YANG SUDAH DIPERBAIKI)

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ubah nim dan password sesuai kebutuhan
VALID_USERNAME = "xxx"  # GANTI DENGAN NIM ANDA
VALID_PASSWORD = "xxx" # GANTI DENGAN PASSWORD ANDA
LOGIN_URL = "https://hebat.elearning.unair.ac.id/login/index.php"

# === PERBAIKAN DI SINI: Tambahkan WebDriverWait ===
@given('The Student is on the "Hebat" login page')
def step_impl(context):
    """Memastikan browser diarahkan ke halaman login."""
    context.driver.get(LOGIN_URL)
    try:
        # Kita harus MENUNGGU tombol login muncul
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginbtn"))
        )
    except Exception as e:
        raise AssertionError(f"Tidak berada di halaman login Hebat atau tombol 'loginbtn' tidak ditemukan. Error: {e}")

@when('The Student enters a valid username into the "Username" field')
def step_impl(context):
    """Mengisi kolom username."""
    # Menunggu field username muncul
    username_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
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
    """Memverifikasi bahwa URL telah berubah ke halaman My courses/Dashboard."""
    try:
        WebDriverWait(context.driver, 15).until(
            EC.url_contains("/my/")
        )
        current_url = context.driver.current_url
        assert "login/index.php" not in current_url, f"Gagal dialihkan. Tetap di halaman login: {current_url}"
    except Exception as e:
        raise AssertionError(f"Timeout menunggu pengalihan ke Halaman 'Home' (my courses). Error: {e}")

@then('The Student should see their courses information on the page')
def step_impl(context):
    """Memverifikasi kehadiran elemen khas dari Dashboard."""
    page_heading_selector = (By.XPATH, "//div[@class='page-header-headings']/h1")
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(page_heading_selector)
        )
        heading_text = context.driver.find_element(*page_heading_selector).text
        assert "My courses" in heading_text, f"Header tidak menunjukkan 'My courses'. Ditemukan: {heading_text}"
    except Exception as e:
        raise AssertionError(f"Gagal menemukan judul halaman 'My courses'. Error: {e}")