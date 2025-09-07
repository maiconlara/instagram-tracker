# Instagram Tracker com Instaloader

Este script permite **monitorar seguidores e seguindo** de uma conta do Instagram, salvando snapshots em arquivos `.json` e comparando mudanças ao longo do tempo.  

Ele utiliza a biblioteca [Instaloader](https://instaloader.github.io/) para acessar dados do Instagram de forma automatizada.

---

## 🚀 Funcionalidades
- Coleta **seguidores** (`followers`) de um usuário.
- Coleta **seguidos** (`following`) de um usuário.
- Salva os dados em arquivos `.json` separados.
- Detecta e exibe:
  - **Novos seguidores/seguidos**.
  - **Seguidores/seguidos perdidos**.
- Aplica **delays aleatórios** entre as requisições para evitar bloqueios.

---

## 📦 Requisitos

- Python 3.8+
- Biblioteca Instaloader  

Instale as dependências com:

```bash
pip install instaloader
```

---

## ⚙️ Como usar

1. Clone ou baixe este repositório.
2. No código, altere:
   ```python
   USERNAME = "sua_conta_sem_@"  # Sua conta do Instagram (sem @)
   TARGET_USER = "nome_de_usuario_aqui_sem_@"  # Conta alvo (sem @)
   ```
3. Faça login no Instagram com o Instaloader e salve a sessão:
   ```bash
   instaloader -l seu_usuario
   ```
   Isso criará um arquivo de sessão que o script usará para autenticação.
4. Execute o script:
   ```bash
   python tracker.py
   ```

---

## 📂 Saída

Ao rodar, o script cria dois arquivos JSON:
- `nome_de_usuario_aqui_sem_@_followers.json`
- `nome_de_usuario_aqui_sem_@_following.json`

Cada execução compara os dados atuais com os snapshots anteriores e mostra mudanças no terminal, por exemplo:

```
Novos seguidores detectados:
- usuario_novo

Seguidores que deixaram de aparecer:
- usuario_antigo
```

---

## ⚠️ Observações

- O uso excessivo pode resultar em **bloqueio temporário** pelo Instagram.  
- Os delays (`time.sleep(random.uniform(...))`) ajudam a reduzir o risco.  
- Recomenda-se **usar com moderação** e apenas em contas que você tem permissão de monitorar.  
