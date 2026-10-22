import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_orangehrm_login_success():
    # Configuram browserul sa ruleze in fundal (Headless), ideal pentru Linux WSL
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Pornim browserul
    print("\nDeschidem browserul Chrome...")
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # 1. Navigam catre site
        print("Navigam catre OrangeHRM Live Demo...")
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(3) # Asteptam sa se incarce pagina
        
        # 2. Gasim campurile de Login si introducem datele
        print("Introducem datele de autentificare...")
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        
        # 3. Dam click pe butonul de Login
        print("Apasam butonul de Login...")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3) # Asteptam tranzitia paginii
        
        # 4. Verificam (Assertion) ca am ajuns pe Dashboard
        print("Verificam rezultatul...")
        assert "dashboard" in driver.current_url.lower(), "Eroare: Nu am ajuns pe pagina de Dashboard!"
        print("TEST REUSIT: Autentificarea s-a realizat cu succes!")
        
    finally:
        # Inchidem intotdeauna browserul la final
        driver.quit()

