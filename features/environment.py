# File: features/environment.py (INI YANG BENAR-BENAR FINAL)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    """Berjalan sekali sebelum semua tes dimulai."""
    print("Mencoba membuat browser...")
    service = ChromeService(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.implicitly_wait(10)
    print("Browser (context.driver) berhasil dibuat.")

def after_scenario(context, scenario):
    """
    Berjalan setelah SETIAP skenario selesai.
    Ini akan me-reset browser (membuatnya "logout").
    """
    if hasattr(context, 'driver'):
        # === INI PERBAIKANNYA ===
        # 1. Hapus semua cookie sesi untuk 'logout' paksa
        context.driver.delete_all_cookies()
        
        # 2. Reset halaman ke 'about:blank'
        context.driver.get("about:blank")

def after_all(context):
    """
    Berjalan sekali setelah semua tes selesai.
    Ini akan menutup browser secara otomatis.
    """
    if hasattr(context, 'driver'): 
        context.driver.quit()