import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_orangehrm_add_employee():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10) # Asteptare inteligenta pentru elemente

    try:
        # 1.Login
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # 2.Navigare catre modulul PIM
        print("\nNavigam catre modulul PIM...")

        driver.find_element(By.XPATH, "//a[contains(@href, 'viewPimModule')]").click()
        time.sleep(2)

        # 3.Click pe butonul Add Employee
        print("Adaugam un angajat nou...")
        driver.find_element(By.XPATH, "//button[contains(., 'Add')]").click()
        time.sleep(2)

        # 4.Completare date angajat
        # Folosim un ID fix (ex. 9988) pentr a-l putea cauta ulterior
        employee_id = "9988"
        driver.find_element(By.NAME, "firstName").send_keys("QA_Gaby")
        driver.find_element(By.NAME, "lastName").send_keys("Tester")

        id_field = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        id_field.clear()
        time.sleep(5)
        id_field.send_keys(employee_id)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print(f"Angajatul cu ID-ul {employee_id} a fost salvat.")
        time.sleep(4)

        #5.Verificare: Ne intoarcem la lista de angajati si il cautam dupa ID
        driver.find_element(By.XPATH, "//a[contains(., 'Employee List')]").click()
        time.sleep(2)
        
        # Introducem ID-ul în câmpul de căutare
        search_id_field = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        search_id_field.send_keys(employee_id)
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

        # Verificăm dacă ID-ul apare în tabelul cu rezultate
        table_html = driver.page_source
        assert employee_id in table_html, f"Eroare: Angajatul cu ID-ul {employee_id} nu a fost găsit în tabel!"
        print("TEST REUSIT: Angajatul a fost creat și găsit cu succes în PIM!")

    finally:
        driver.quit()

