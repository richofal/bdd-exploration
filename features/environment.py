from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # Menggunakan WebDriver Manager untuk inisialisasi driver
    service = ChromeService(ChromeDriverManager().install())
    
    # Inisialisasi WebDriver
    context.driver = webdriver.Chrome(service=service)
    
    context.driver.implicitly_wait(10)

def after_all(context):
    """Menutup browser jika objek driver berhasil diinisialisasi."""
    if hasattr(context, 'driver'): 
        context.driver.quit()