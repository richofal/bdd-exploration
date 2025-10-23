# File: steps/hebat_login_steps.py (Disesuaikan)

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Kredensial dan URL tetap di sini (sesuai input Anda)
VALID_USERNAME = "187231108" 
VALID_PASSWORD = "e#LHrC!A9!Xi"
LOGIN_URL = "https://hebat.elearning.unair.ac.id/login/index.php"
DASHBOARD_URL = "https://hebat.elearning.unair.ac.id/my/courses.php" # URL Target yang Disesuaikan

@given('The Student is on the "Hebat" login page')
def step_impl(context):
    """Memastikan browser diarahkan ke halaman login."""
    context.driver.get(LOGIN_URL)
    # Verifikasi bahwa kita berada di halaman login dengan mencari tombol login
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
    # Menunggu hingga URL berubah ke halaman kursus atau dashboard
    WebDriverWait(context.driver, 15).until( # Naikkan wait time sedikit untuk memastikan navigasi
        # Menggunakan partial_url_to_be lebih fleksibel
        EC.url_contains("/my/")
    )
    # Verifikasi URL saat ini BUKAN URL login
    current_url = context.driver.current_url
    assert current_url != LOGIN_URL, f"Gagal dialihkan. Tetap di halaman login: {current_url}"

@then('The Student should see their courses information on the page')
def step_impl(context):
    """
    MEMPERBAIKI VERIFIKASI ELEMEN:
    Memverifikasi kehadiran elemen khas dari Dashboard, yaitu Judul 'My courses'.
    """
    # Berdasarkan HTML yang diberikan, judul My courses ada di H1 dalam div.page-header-headings
    page_heading_selector = (By.XPATH, "//div[@class='page-header-headings']/h1")
    
    try:
        # Menunggu hingga elemen judul halaman 'My courses' muncul
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(page_heading_selector)
        )
        
        # Ambil teks H1 dan pastikan itu 'My courses'
        heading_text = context.driver.find_element(*page_heading_selector).text
        assert "My courses" in heading_text, f"Header tidak menunjukkan 'My courses'. Ditemukan: {heading_text}"
        
        print("Login berhasil dan halaman 'My courses' terlihat.")
        
    except Exception as e:
        raise AssertionError(f"Gagal menemukan judul halaman 'My courses'. Error: {e}")
