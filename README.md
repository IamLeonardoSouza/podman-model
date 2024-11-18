# Podman

## O que é Podman?

O Podman é uma ferramenta de gerenciamento de containers desenvolvida para ser uma alternativa ao Docker, oferecendo funcionalidades similares, como a criação, execução e gerenciamento de containers, mas com a principal diferença de não exigir um daemon em segundo plano. Ele é completamente compatível com as APIs do Docker, permitindo que os usuários executem comandos do Docker sem modificações, mas sua arquitetura permite rodar containers como processos do usuário sem privilégios administrativos, o que aumenta a segurança. O Podman também se integra bem com outras ferramentas de gerenciamento de containers, como o Buildah (para construir imagens) e o Skopeo (para mover imagens entre repositórios), tornando-o ideal para ambientes sem necessidade de dependências de processos de sistema centralizados. Ele é amplamente utilizado em sistemas Linux, mas também possui suporte para Windows e macOS, sendo uma solução robusta e eficiente para automação de containers em ambientes de desenvolvimento e produção.

## Requisitos

- Sistema operacional com suporte ao Podman (Linux, Windows com WSL2, macOS)

## Instalar o Podman

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install -y podman
```
### RedHat/CentOS

```bash
sudo dnf install -y podman
```
### MacOS (via Homebrew)

```bash
brew install podman
```
### Windows

- Baixe o Podman Desktop do <a href="https://podman-desktop.io/downloads/windows" target="_blank">site oficial</a>.
- Siga as instruções para completar a instalação.

## Configuração Inicial do Podman

Após a instalação, execute o seguinte comando para verificar se o Podman foi instalado corretamente:

```bash
podman --version
```
## Inicializando um Podman Socket (para interfaces gráficas e outras funcionalidades)

No Linux, o Podman utiliza um socket que pode ser configurado para trabalhar de forma semelhante ao Docker. Para ativar o socket do Podman:

```bash
sudo systemctl enable --now podman.socket
```
## Inicializando uma Máquina Virtual do Podman no Windows

O Podman no Windows requer a configuração de uma máquina virtual (VM) para funcionar. Siga estes passos:

- Crie uma máquina virtual com podman machine init: Abra o terminal e execute:

```bash
podman machine init
```
Isso configurará uma VM padrão para o Podman.

- Inicie a máquina virtual com podman machine start: Após criar a VM, inicie-a:

```bash
podman machine start
```
- Verifique a conexão: Confirme que a conexão com a VM está ativa:

```bash
podman system connection list
```
- Você deverá ver algo como:

```bash
Name     Default  URI
podman   true     unix:///path/to/socket
```
## Testando o Podman

Depois de inicializar e conectar a máquina virtual, teste o comando abaixo:

```bash
podman ps
```
Se funcionar, ele exibirá a lista de containers (ou estará vazio se nenhum container estiver rodando).

## Subindo uma Imagem Python e Executando um Container com o Podman

Embora o Podman seja uma alternativa ao Docker, ele também usa os mesmos arquivos Dockerfile. Crie um arquivo Dockerfile na pasta que deseja subir:

```bash
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copie o script Python para o container
COPY app.py /app/

# Instale dependências, se houver
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o script Python
CMD ["python", "app.py"]
```
## Construindo a Imagem Python

Com o Dockerfile pronto, agora você pode criar a imagem do container. Execute o comando:

```bash
podman build -t podman-model .
```
## Executando o Container Python

Agora, vamos rodar o container baseado na imagem criada.

```bash
podman run --rm podman-model
```
## Limpando Recursos (opcional)

Para liberar espaço, remova containers ou imagens desnecessárias:

- Remover containers parados:

```bash
podman container prune
```
- Remover imagens não utilizadas:

```bash
podman image prune
```