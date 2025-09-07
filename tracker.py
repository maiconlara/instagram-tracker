import instaloader
import json
import os
import time
import random

L = instaloader.Instaloader()

USERNAME = "sua_conta_sem_@"  # Substitua pelo seu nome de usuário sem o @
L.load_session_from_file(USERNAME)

TARGET_USER = "nome_de_usuario_aqui_sem_@"  # Substitua pelo nome de usuário alvo sem o @

def check_and_save(data, filename, tipo):
    """Compara snapshot salvo com o atual e escreve o novo JSON."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            old_data = json.load(f)

        novos = set(data) - set(old_data)
        perdidos = set(old_data) - set(data)

        if novos:
            print(f"Novos {tipo} detectados:")
            for n in novos:
                print("-", n)

        if perdidos:
            print(f"{tipo.capitalize()} que deixaram de aparecer:")
            for p in perdidos:
                print("-", p)

        if not novos and not perdidos:
            print(f"Nenhuma mudança nos {tipo}.")
    else:
        print(f"Primeira execução: criando snapshot inicial de {tipo}.")

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

# Pegar perfil
profile = instaloader.Profile.from_username(L.context, TARGET_USER)

# # --- Seguidores ---
followers_file = f"{TARGET_USER}_followers.json"
current_followers = []

print("Coletando seguidores da pessoa...")
for f in profile.get_followers():
    current_followers.append(f.username)
    time.sleep(random.uniform(2, 3))  # Delay  entre cada usuário

check_and_save(current_followers, followers_file, "seguidores")

# Delay entre operações
time.sleep(random.uniform(3, 5))

# --- Seguindo ---
following_file = f"{TARGET_USER}_following.json"
current_following = []

print("Coletando quem a pessoa segue...")
for f in profile.get_followees():
    current_following.append(f.username)
    time.sleep(random.uniform(2, 3))  # Delay  entre cada usuário

check_and_save(current_following, following_file, "seguindo")