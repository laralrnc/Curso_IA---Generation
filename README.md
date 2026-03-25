# 🎙️ Audio Transcription with Whisper

## 📌 Descrição

Este projeto utiliza o modelo Whisper para realizar **transcrição
automática de arquivos de áudio para texto** utilizando Python.

O script carrega um modelo de reconhecimento de fala, processa um
arquivo de áudio e gera: - A transcrição exibida no terminal - Um
arquivo `.txt` contendo o texto transcrito

Possíveis usos: - Transcrever entrevistas - Converter gravações em
texto - Criar legendas automáticas - Analisar conteúdo de áudio

------------------------------------------------------------------------

## ⚙️ Tecnologias utilizadas

-   Python
-   Biblioteca Whisper
-   Processamento de áudio

------------------------------------------------------------------------

## 📦 Instalação

Clone o repositório:

``` bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Entre na pasta do projeto:

``` bash
cd nome-do-repositorio
```

Instale as dependências:

``` bash
pip install openai-whisper
```

------------------------------------------------------------------------

## ▶️ Como usar

1.  Coloque o arquivo de áudio na pasta do projeto.

2.  No código, altere o nome do arquivo:

``` python
audio_file = "input.mp3"
```

3.  Execute o script:

``` bash
python transcribe.py
```

------------------------------------------------------------------------

## 📄 Saída

O programa irá:

-   Mostrar a transcrição no terminal
-   Criar um arquivo chamado:

```{=html}
<!-- -->
```
    transcript.txt

com o conteúdo do áudio convertido em texto.

------------------------------------------------------------------------

## 🧠 Modelos disponíveis

Você pode alterar o modelo usado na linha:

``` python
model = whisper.load_model("tiny")
```

Modelos disponíveis:

-   tiny (mais rápido)
-   base
-   small
-   medium
-   large (mais preciso)

------------------------------------------------------------------------

## 📁 Estrutura do projeto

    📂 projeto
     ├── transcribe.py
     ├── input.mp3
     └── transcript.txt

------------------------------------------------------------------------

## 👩‍💻 Autora

Projeto desenvolvido por **Lara** para aprendizado de **Inteligência
Artificial e processamento de áudio com Python**.
