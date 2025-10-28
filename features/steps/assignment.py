# File: features/steps/assignment.py (INI YANG SUDAH DIPERBAIKI)

from behave import given, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === 1. KONSTANTA (SUDAH BENAR) ===
DASHBOARD_URL = "https://hebat.elearning.unair.ac.id/my/courses.php"
PPL_COURSE_NAME = "Pembangunan Perangkat Lunak"
ASSIGNMENT_NAME = "Penugasan PPT" 

# =======================================================

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

        # Tunggu URL berubah
        WebDriverWait(context.driver, 15).until(EC.url_contains("/course/view.php"))
        
        # === INI PERBAIKANNYA ===
        # Tunggu juga sampai daftar materi (ul data-for='cmlist') muncul
        # Ini untuk mengatasi race condition
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-for='cmlist']"))
        )
        
        print(f"✅ Berhasil masuk ke halaman '{PPL_COURSE_NAME}' dan konten dimuat.")
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
        time.sleep(1) # Diberi jeda singkat agar scroll selesai
        assignment_link.click()

        WebDriverWait(context.driver, 15).until(
            EC.url_contains("/mod/assign/view.php")
        )
        print("✅ Halaman tugas berhasil dibuka.")

        time.sleep(3)
        print("🛑 Skenario assignment selesai.")
    
    except Exception as e:
        print(f"DEBUG: XPath dicoba: {assignment_selector[1]}")
        raise AssertionError(f"Gagal membuka tugas '{ASSIGNMENT_NAME}'. Error: {e}")