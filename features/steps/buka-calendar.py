from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Selektor Kalender ---
USER_MENU_TOGGLE_ID = "action-menu-toggle-0"
CALENDAR_LINK_XPATH = "//a[@aria-labelledby='actionmenuaction-3']"
PAGE_HEADING_SELECTOR = (By.XPATH, "//div[@class='page-header-headings']/h1")
CALENDAR_PAGE_URL_FRAGMENT = "/calendar/view.php"

@when('The Student clicks their name in the "User Menu"')
def step_impl(context):
    """Mengklik tombol menu pengguna (toggle) untuk membuka dropdown."""
    try:
        user_menu_toggle = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, USER_MENU_TOGGLE_ID))
        )
        user_menu_toggle.click()
    except Exception as e:
        raise AssertionError(f"Gagal menemukan atau mengklik user menu toggle (ID: {USER_MENU_TOGGLE_ID}). Error: {e}")

@when('The Student clicks the "Calendar" option from the dropdown menu')
def step_impl(context):
    """Mengklik link 'Calendar' di dalam dropdown yang sudah terbuka."""
    try:
        calendar_link = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, CALENDAR_LINK_XPATH))
        )
        calendar_link.click()
    except Exception as e:
        raise AssertionError(f"Gagal menemukan atau mengklik link 'Calendar' (XPATH: {CALENDAR_LINK_XPATH}). Error: {e}")

@then('The Student should be redirected to the "Calendar" page')
def step_impl(context):
    """Memverifikasi bahwa URL telah berubah ke halaman Kalender."""
    try:
        WebDriverWait(context.driver, 15).until(
            EC.url_contains(CALENDAR_PAGE_URL_FRAGMENT)
        )
        current_url = context.driver.current_url
        assert CALENDAR_PAGE_URL_FRAGMENT in current_url, \
            f"Tidak dialihkan ke halaman Kalender. URL Saat Ini: {current_url}"
            
    except Exception as e:
        raise AssertionError(f"Timeout menunggu pengalihan ke halaman Kalender. Error: {e}")

@then('The Student should see the header containing the text "Calendar"')
def step_impl(context):
    """Memverifikasi bahwa header H1 di halaman baru berisi teks 'Calendar'."""
    try:
        WebDriverWait(context.driver, 10).until(
            EC.text_to_be_present_in_element(PAGE_HEADING_SELECTOR, "Calendar")
        )
        heading_text = context.driver.find_element(*PAGE_HEADING_SELECTOR).text
        assert "Calendar" in heading_text, f"Header tidak menunjukkan 'Calendar'. Ditemukan: {heading_text}"
        
        print("Navigasi ke halaman 'Calendar' berhasil diverifikasi.")
        
    except Exception as e:
        raise AssertionError(f"Gagal menemukan judul halaman 'Calendar' (Selektor: {PAGE_HEADING_SELECTOR}). Error: {e}")