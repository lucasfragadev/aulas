import pyautogui  # Importa a biblioteca pyautogui para automação de GUI
import time  # Importa a biblioteca time para usar funções de delay
import os  # Importa a biblioteca os para interagir com o sistema operacional

# Pressiona a tecla 'win' para abrir o menu iniciar
pyautogui.press('win')
# Digita 'chrome' para procurar o navegador Chrome
pyautogui.write('chrome')
# Pressiona 'enter' para abrir o Chrome
pyautogui.press('enter')
# Espera 2 segundos para o Chrome abrir
time.sleep(2)

# Digita o URL do site que quero acessar
pyautogui.write('https://www.infinityschool.app/')
# Pressiona 'enter' para ir para o site
pyautogui.press('enter')

# Espera 2 segundos para o site carregar
time.sleep(2)
# Clica na posição do botão de login (coordenadas x=975, y=535)
pyautogui.click(975, 535, duration=1)

# Clica na posição do campo de usuário (coordenadas x=941, y=547)
pyautogui.click(941, 547, duration=1)
# Digita o número de telefone como usuário
pyautogui.write('05331236588')

# Clica na posição do campo de senha (coordenadas x=965, y=614)
pyautogui.click(965, 614, duration=1)
# Digita a senha
pyautogui.write('23051990')

# Clica no botão de login (coordenadas x=972, y=657)
pyautogui.click(972, 657, duration=1)
# Espera 5 segundos para o login ser processado
time.sleep(5)

# Tira um screenshot da tela
screenshot = pyautogui.screenshot()
# Define o diretório onde o screenshot será salvo
screenshot_dir = r'c:/Documentos/DevFraga/testes/automacao/'
# Define o nome base do arquivo de screenshot
screenshot_base_name = 'screenshot'
# Define a extensão do arquivo de screenshot
screenshot_extension = '.png'

# Inicializa o contador de screenshots
i = 1
# Verifica se o arquivo de screenshot já existe e incrementa o contador até encontrar um nome disponível
while os.path.exists(os.path.join(screenshot_dir, f"{screenshot_base_name}{i:03d}{screenshot_extension}")):
  i += 1

# Salva o screenshot com um nome único
screenshot.save(os.path.join(screenshot_dir, f"{screenshot_base_name}{i:03d}{screenshot_extension}"))







