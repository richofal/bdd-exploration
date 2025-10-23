from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL Halaman "My courses" (Course Overview)
COURSES_URL = "https://hebat.elearning.unair.ac.id/my/courses.php"

# --- Step Definitions untuk Skenario Pencarian ---

@given('The Student is logged in and on the "Course Overview" page')
def step_impl(context):
    """
    Memverifikasi bahwa mahasiswa sudah login dan berada di halaman "Course Overview".
    Step ini berasumsi login telah ditangani (misalnya di environment.py atau skenario sebelumnya).
    Step ini akan mengarahkan ke halaman kursus jika belum, dan gagal jika tidak login.
    """
    if COURSES_URL not in context.driver.current_url:
        context.driver.get(COURSES_URL)

    try:
        # Verifikasi kita berada di halaman yang benar (bukan login)
        # dengan menunggu elemen search box (berdasarkan HTML yang diberikan)
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-region='input']"))
        )
        
        # Pastikan kita tidak dialihkan kembali ke halaman login
        current_url = context.driver.current_url
        assert "login/index.php" not in current_url, "Gagal memuat halaman Course Overview. Mahasiswa belum login."
        print("Berhasil diverifikasi: Mahasiswa berada di 'Course Overview' page.")
    
    except Exception as e:
        raise AssertionError(f"Gagal menemukan elemen 'Course Overview' page. Mungkin belum login. Error: {e}")

@when('The Student enters "{search_term}" into the "Search" field')
def step_impl(context, search_term):
    """
    Menemukan search box dan memasukkan teks pencarian.
    """
    # Berdasarkan HTML: <input ... data-region="input" ... placeholder="Search">
    search_box_selector = (By.CSS_SELECTOR, "input[data-region='input']")
    
    try:
        search_box = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located(search_box_selector)
        )
        search_box.clear()
        search_box.send_keys(search_term)
        
        # Catatan: Platform ini kemungkinan menggunakan AJAX untuk refresh list.
        # Kita tidak perlu wait di sini; step 'Then' akan menangani 'wait' untuk hasilnya.
        print(f"Memasukkan teks '{search_term}' ke 'Search' field.")

    except Exception as e:
        raise AssertionError(f"Gagal menemukan atau mengisi 'Search' field. Error: {e}")

@then('The Student should see the course "{course_name}" in the results')
def step_impl(context, course_name):
    """
    Memverifikasi bahwa mata kuliah yang dicari muncul dalam daftar hasil.
    Step ini akan menunggu (WebDriverWait) hingga hasil pencarian AJAX muncul.
    """

    xpath_selector = f"//li[@data-region='course-content']//a[contains(@class, 'coursename') and contains(normalize-space(), '{course_name}')]"
    
    try:
        # Menunggu hingga 10 detik sampai hasil filter AJAX muncul
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_selector))
        )
        
        # Jika wait berhasil, elemen ditemukan
        print(f"Berhasil menemukan mata kuliah: {course_name}")
        assert True # Menandakan step berhasil

    except Exception as e:
        # Jika wait timeout, elemen tidak ditemukan
        raise AssertionError(f"Gagal menemukan mata kuliah '{course_name}' di hasil pencarian. Error: {e}")
