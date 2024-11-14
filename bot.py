
# RODAR: 
# "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\DEVNEMO\AppData\Local\Microsoft\Edge\User Data"

import json
import time
import re
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

with open("config.json", "r") as file:
    config = json.load(file)

SPOTIFY_CLIENT_ID = config["spotify"]["client_id"]
SPOTIFY_CLIENT_SECRET = config["spotify"]["client_secret"]
SPOTIFY_REDIRECT_URI = config["spotify"]["redirect_uri"]
SPOTIFY_PLAYLIST_ID = config["spotify"]["playlist_id"]
SPOTIFY_SCOPE = config["spotify"]["scope"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=SPOTIFY_SCOPE
))

options = Options()
options.debugger_address = "localhost:9222"
driver = webdriver.Edge(options=options)
driver.get(config["selenium"]["live_link"])
wait = WebDriverWait(driver, 10)

padrao_musica = re.compile(r'!musica\s+(.+)', re.IGNORECASE)
padrao_comandos = re.compile(r'!comandos', re.IGNORECASE)
padrao_musica_atual = re.compile(r'!musica_atual', re.IGNORECASE)
padrao_jogo = re.compile(r'!jogo', re.IGNORECASE)
padrao_add_jogo = re.compile(r'!add_jogo\s+(.+)', re.IGNORECASE)
padrao_sobre = re.compile(r'!sobre', re.IGNORECASE)

musicas = []
jogos = []
jogo_atual = "Nenhum jogo definido"
musica_atual = "Nenhuma musica definida"
processed_messages = set()

diretorio_musicas = "MusicaTikTok"
os.makedirs(diretorio_musicas, exist_ok=True)

def search_spotify_track(query):
    """
    Search for a track on Spotify and return its URI
    """
    try:
        results = sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            return {
                'uri': track['uri'],
                'name': track['name'],
                'artists': ', '.join([artist['name'] for artist in track['artists']])
            }
        return None
    except Exception as e:
        print(f"Erro ao buscar música no Spotify: {e}")
        return None

def add_to_spotify_playlist(track_uri):
    """
    Add a track to the specified Spotify playlist
    """
    try:
        sp.playlist_add_items(SPOTIFY_PLAYLIST_ID, [track_uri])
        return True
    except Exception as e:
        print(f"Erro ao adicionar música à playlist: {e}")
        return False

def enviar_mensagem(mensagem):
    try:
        input_field = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-1kvtqrg-DivEditor"))
        )
        input_field.clear()
        input_field.send_keys(mensagem)
      
        send_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "css-1dgtn4b-DivPostButton"))
        )
        send_button.click()
        time.sleep(1)
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def get_chat_messages():
    try:
        elementos_chat = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "css-1kue6t3-DivComment"))
        )
        return elementos_chat
    except (TimeoutException, StaleElementReferenceException) as e:
        print(f"Erro ao obter mensagens do chat: {e}")
        return []

def process_message(elemento):
    try:
        texto = elemento.text
        message_id = hash(texto)
        
        if message_id in processed_messages:
            return
        
        processed_messages.add(message_id)
        
        texto = texto.replace("ú", "u").replace("Ú", "U")
        texto = texto.replace("! musica", "!musica")
        
        match = padrao_musica.search(texto)
        if match:
            musica = match.group(1)
            if musica not in musicas:
                track_info = search_spotify_track(musica)
                if track_info:
                    if add_to_spotify_playlist(track_info['uri']):
                        musicas.append(musica)
                        musica_atual = f"{track_info['name']} - {track_info['artists']}"
                        print(f"Música adicionada ao Spotify: {musica_atual} ==== {time.ctime()}")
                        
                        caminho_arquivo = os.path.join(diretorio_musicas, f"{musica}.txt")
                        with open(caminho_arquivo, "w", encoding='utf-8') as arquivo:
                            arquivo.write(f"Música: {musica_atual}")
                        
                        enviar_mensagem(f"Música '{musica_atual}' adicionada à playlist do Spotify!")
                else:
                    enviar_mensagem(f"Música '{musica}' não encontrada no Spotify.")

        if padrao_musica_atual.search(texto):
            enviar_mensagem(f"Musica atual: {musica_atual}")

        if padrao_jogo.search(texto):
            enviar_mensagem(f"Jogo atual: {jogo_atual}")

        match_jogo = padrao_add_jogo.search(texto)
        if match_jogo:
            jogo = match_jogo.group(1)
            if jogo not in jogos:
                jogos.append(jogo)
                enviar_mensagem(f"Jogo '{jogo}' adicionado a lista de sugestoes!")

        if padrao_sobre.search(texto):
            sobre_msg = ""
            enviar_mensagem(sobre_msg)
            
    except StaleElementReferenceException:
        print("Elemento do chat ficou obsoleto durante o processamento")
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")

def limpar_mensagens_antigas():
    if len(processed_messages) > 1000:
        processed_messages.clear()

try:
    while True:
        elementos_chat = get_chat_messages()
        
        for elemento in elementos_chat:
            process_message(elemento)
            
        limpar_mensagens_antigas()
        time.sleep(5)

except KeyboardInterrupt:
    print("Parando o monitoramento.")

finally:
    driver.quit()