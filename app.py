import pyautogui
from time import sleep
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

TEMPO_ESPERA = 0
TEMPO_CARREGAMENTO = 2 

def clicar(x, y, duracao=TEMPO_ESPERA):
  pyautogui.click(x, y, duration=duracao)

def digitar(texto):
  pyautogui.write(texto)

def realizar_login(usuario, senha):
  logging.info('Iniciando login...')
  clicar(966, 539)
  digitar(usuario)
  clicar(971, 565)
  digitar(senha)
  clicar(870, 594)
  sleep(TEMPO_CARREGAMENTO)
  logging.info("Login realizado com sucesso!")

def cadastrar_produto(nome, quantidade, preco):
  clicar(663, 527)
  digitar(nome)
  clicar(663, 551)
  digitar(quantidade)
  clicar(663, 579)
  digitar(preco)
  clicar(590, 738)

def processar_arquivo_produtos(nome_arquivo):
  logging.info(f"Lendo arquivo: {nome_arquivo}")
  with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
      dados = linha.strip().split(',')
      if len(dados) == 3:
        logging.info(f"Cadastrando produto: {dados[0]}")
        cadastrar_produto(*dados)

if __name__ == "__main__":
  realizar_login('lucas', '123')
  processar_arquivo_produtos('produtos.txt')