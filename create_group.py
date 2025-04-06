from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# --- Configuración del navegador ---
options = Options()
options.add_argument("--start-maximized")
service = Service()
driver = webdriver.Chrome(service=service, options=options)

# --- Abrir WhatsApp Web ---
driver.get("https://web.whatsapp.com")
print("📲 Escanea el código QR y presiona Enter para continuar...")
input("✅ Presiona Enter una vez escaneado el QR...")

# --- Abrir nuevo Chat ---
# Espera a que el botón 'Nuevo chat' esté visible y sea clickeable
time.sleep(3)

try:
    # Espera a que el botón 'Nuevo chat' esté presente en el DOM usando el selector CSS
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[3]/header/header/div/span/div/div[1]/button/span').click()
    print("🔍 Botón 'Nuevo chat' encontrado y clickeado.")
except Exception as e:
    print("Error: ", e)

# --- Abrir crear Nuevo Grupo ---
# Esperar que el boton 'Crear nuevo Grupo' esté visible
time.sleep(3)
try:
    # Espera a que el botón 'Crear nuevo Grupo' esté presente en el DOM usando el selector CSS
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div[1]/div[1]/div/div[2]').click()
    print("🔍 Botón 'Nuevo grupo' encontrado y clickeado.")
except Exception as e:
    print("Error: ", e)

# --- Ahora se tiene el buscador activo y escribiremos el codigo 415 veces ---
# Encontrar el campo de búsqueda y escribir lo que estamos buscando
time.sleep(3)
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/span/div/span/span/div/div/div[1]/div/div/div[2]/input')
search_box.clear()  # Limpiar el campo antes de escribir
search_box.send_keys(f"CINU_12025")  # Escribe el nombre del grupo
print(f"🔍 Buscando 'CINU_12025'...")

# --- Esperar a que se carguen los resultados ---
time.sleep(3)
false_group_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/span/div/span/span/div/div/div[2]/div/div/div/div[1]/div/div')

if false_group_element:
    print("🔍 Grupo FALSO encontrado.")
    number1 = 2
    number2 = 416
else:
    print("🔍 Grupo REAL encontrado.")
    number1 = 1
    number2 = 415

for i in range(number1, number2):
    time.sleep(0.5)  # Esperar un poco para evitar problemas de carga
    try:
        # Seleccionar el contacto encontrado
        group_element = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/span/div/span/span/div/div/div[2]/div/div/div/div[{number1}]/div/div/div[2]')
        group_element.click()
        print(f"✅ Contacto {i} seleccionado.")

        search_box.send_keys(f"CINU_12025")  # Escribe el nombre del grupo

    except Exception as e:
        print(f"Error al seleccionar el contacto {i}: ", e)

# --- Ahora configuracion de grupo ---
time.sleep(3)
try:
    # Hacemos click para ir a la configuracion del grupo
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/span/div/span/span/div/div/span/div').click()
    print("🔍 Botón 'Avanzar a configuración' encontrado y clickeado.")
except Exception as e:
    print("Error: ", e)

# --- Esperar a que se cargue la configuración del grupo ---
time.sleep(3)
print(f"🔧 Configurando el grupo...")
# --- Cambiar el nombre del grupo ---
try:
    group_name_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/span/div/span/span/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/p')
    group_name_input.clear()  # Limpiar el campo antes de escribir
    group_name_input.send_keys("Bienvenida CINU_12025")  # Cambia el nombre del grupo
    print("✅ Nombre del grupo cambiado")
except Exception as e:
    print("Error al cambiar el nombre del grupo: ", e)

# --- Guardar los cambios ---
try:
    save_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/span/div/span/span/div/div/span/div/div')
    save_button.click()
    print("✅ Cambios guardados correctamente.")
except Exception as e:
    print("Error al guardar los cambios: ", e)


# # --- Cerrar el navegador ---
time.sleep(50)  # Esperar un poco antes de cerrar
driver.quit()
