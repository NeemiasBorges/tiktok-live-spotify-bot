# TikTok Live Spotify Bot 🎵

> Bot que integra chat de lives do TikTok com o Spotify, permitindo que espectadores adicionem músicas a uma playlist em tempo real.

## 📋 Sobre o Projeto

Este bot monitora o chat de uma live no TikTok e permite que os espectadores interajam através de comandos específicos para adicionar músicas a uma playlist do Spotify, verificar a música atual e participar de outras interações relacionadas ao stream.

### ✨ Funcionalidades Principais

- 🤖 Monitoramento em tempo real do chat do TikTok
- 🎵 Integração automática com Spotify para busca e adição de músicas
- 💬 Sistema de resposta automática no chat
- 📝 Registro de logs das músicas adicionadas
- 🎮 Sistema de gerenciamento de jogos em andamento

## 🎯 Comandos do Chat

| Comando | Descrição |
|---------|-----------|
| `!musica <nome>` | Adiciona música à playlist do Spotify |
| `!musica_atual` | Exibe a música em reprodução |
| `!jogo` | Mostra o jogo atual do stream |
| `!add_jogo <nome>` | Sugere um novo jogo |
| `!sobre` | Exibe informações sobre o bot |

## 🔧 Tecnologias

- ![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
- ![Selenium](https://img.shields.io/badge/Selenium-Latest-green.svg)
- ![Spotipy](https://img.shields.io/badge/Spotipy-Latest-brightgreen.svg)
- ![Regex](https://img.shields.io/badge/Regex-Built--in-lightgrey.svg)

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Microsoft Edge com suporte a debugging remoto
- Conta de desenvolvedor Spotify
- Conexão estável com a internet

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/tiktok-live-spotify-bot.git
cd tiktok-live-spotify-bot
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

### Variáveis de Ambiente

1. Crie um arquivo `config.py` na raiz do projeto:
```python
SPOTIFY_CLIENT_ID = 'sua_client_id_aqui'
SPOTIFY_CLIENT_SECRET = 'seu_client_secret_aqui'
SPOTIFY_REDIRECT_URI = 'sua_redirect_uri_aqui'
SPOTIFY_PLAYLIST_ID = 'sua_playlist_id_aqui'
TIKTOK_LIVE_URL = 'sua_url_da_live_aqui'
```

### Configuração do Microsoft Edge

Execute o Edge com debugging remoto habilitado:
```bash
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\[SeuUsuario]\AppData\Local\Microsoft\Edge\User Data"
```

## 📁 Estrutura do Projeto

```
├── config.py              # Configurações e credenciais
├── tiktok_spotify_bot.py  # Código principal
├── requirements.txt       # Dependências
└── MusicaTikTok/         # Diretório de logs
```

## 🎮 Como Usar

1. Configure todas as variáveis necessárias em `config.py`
2. Inicie o Microsoft Edge com debugging remoto
3. Execute o bot:
```bash
python tiktok_spotify_bot.py
```

## ❗ Solução de Problemas

| Problema | Solução |
|----------|---------|
| Erro de autenticação Spotify | Verifique as credenciais em `config.py` e as permissões do app |
| Falha na conexão TikTok | Confirme se o Edge está rodando com debugging na porta correta |
| Erro ao adicionar músicas | Verifique as permissões da playlist e conexão com internet |

## 🤝 Como Contribuir

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📫 Contato

Neemias - [@dev_nemo]([https://twitter.com/seutwitter](https://x.com/dev_nemo))
