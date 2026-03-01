# Party Rank Video Generator

Gerador de vídeos para Party Rank. O projeto gera imagens e vídeos a partir dos dados em `images.json` e `video.json`.

## Pré-requisitos

- **Python 3.8+** instalado na máquina
- **FFmpeg** (usado pelo MoviePy para processamento de áudio/vídeo) — verifique se está no PATH do sistema

## Instalação

### 1. Clone ou acesse o repositório do projeto

```bash
cd party-rank-video-generator
```

### 2. (Recomendado) Crie um ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

Com o ambiente virtual ativado (ou no Python global, se preferir):

```bash
pip install -r requirements.txt
```

Isso instalará todas as bibliotecas necessárias, incluindo MoviePy, Pillow, OpenCV, NumPy, Pydub, entre outras.

## Como rodar o projeto

Após instalar as dependências:

```bash
python main.py
```

O programa abre um menu no terminal. Digite o número da opção desejada:

| Opção | Descrição |
|-------|-----------|
| **0** | Sair |
| **1** | Gerar Imagens |
| **2** | Gerar Vídeo |
| **3** | Preparar ambiente Google Colab |

- **Gerar Imagens**: gera as imagens a partir de `images.json`.
- **Gerar Vídeo**: gera o vídeo final a partir de `video.json` e dos recursos em `assets/`.
- **Preparar ambiente Google Colab**: ajusta dependências para uso no Colab (não use localmente).

## Estrutura esperada

- `images.json` e `video.json` na raiz do projeto
- Pasta `assets/` com fontes, imagens de participantes e capas (conforme `configs/config.py`)
- Pasta `result/` para saída de imagens e vídeos gerados

## Resumo dos comandos

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar o projeto
python main.py
```
