# DESAFIO TODOS - PYTHON
> Aviso usei o Python 3.10

## INSTALACAO

### GIT CLONE

```
$ git clone https://github.com/gladson/desafio-todos-jsonplaceholder.git todos_framework
$ cd todos_framework
```

### POETRY

[Poetry](https://python-poetry.org/docs/#installation)

> Caso queira instalar pelo poetry

```
$ poetry shell
$ poetry install
```

### VENV - Python 3
> Caso nao queira o Poetry

```
$ python -m .venv
```
![image](https://user-images.githubusercontent.com/1013698/154902352-37db9dd6-7fbd-4ea9-a105-b38f42bd2178.png)
> Automaticamente o vscode vai pedir para selecionar a pasta para trabalho.

#### Para ativar e instalar o ambiente de desenvolvimento

```
$ .\.venv\Scripts\Activate.ps1
ou
$.\.venv\Scripts\Activate.bat
ou
$ source .\.venv\Scripts\activate

$ (.venv) PS C:\Users\Eu\Documents\projetos\python\flask\todos_framework> pip install -r .\requirements-dev.txt
Collecting aniso8601==9.0.1
  Downloading aniso8601-9.0.1-py2.py3-none-any.whl (52 kB)
     |████████████████████████████████| 52 kB 975 kB/s
...
Successfully installed aniso8601-9.0.1 anyio-3.5.0 asttokens-2.0.5 atomicwrites-1.4.0 attrs-21.4.0 backcall-0.2.0 black-22.1.0 certifi-2021.10.8 charset-normalizer-2.0.12 click-8.0.4 colorama-0.4.4 decorator-5.1.1 executing-0.8.2 flake8-4.0.1 flask-2.0.3 flask-restx-0.5.1 h11-0.12.0 h2-4.1.0 hpack-4.0.0 httpcore-0.14.7 httpx-0.22.0 hyperframe-6.0.1 idna-3.3 ipython-8.0.1 itsdangerous-2.1.0 jedi-0.18.1 jinja2-3.0.3 jsonschema-4.4.0 markupsafe-2.1.0 matplotlib-inline-0.1.3 mccabe-0.6.1 more-itertools-8.12.0 mypy-0.931 mypy-extensions-0.4.3 packaging-21.3 parso-0.8.3 pathspec-0.9.0 pickleshare-0.7.5 platformdirs-2.5.1 pluggy-0.13.1 prompt-toolkit-3.0.28 pure-eval-0.2.2 py-1.11.0 pycodestyle-2.8.0 pydantic-1.9.0 pyflakes-2.4.0 pygments-2.11.2 pyparsing-3.0.7 pyrsistent-0.18.1 pytest-5.4.3 pytz-2021.3 rfc3986-1.5.0 six-1.16.0 sniffio-1.2.0 stack-data-0.2.0 tomli-2.0.1 traitlets-5.1.1 typing-extensions-4.1.1 wcwidth-0.2.5 werkzeug-2.0.3
```
> Pronto ta lindao...

### RODAR PROJETO

```
$ cd todos_framework
$ $Env:FLASK_APP = "main.py"
$ $Env:FLASK_ENV = "development"
$ flask run
 * Serving Flask app 'main.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 999-999-999
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

> Ou voce pode rodar pelo vscode tambem... 

> F5 - teclado... que eu acho mais facil...

![image](https://user-images.githubusercontent.com/1013698/154903812-2051d76c-7da1-4c12-bd9c-facdb5e54282.png)


### RODAR PROJETO NO DOCKER

> Windows - Caso voce ainda nao instalou

[DOCKER ENGINE](https://docs.docker.com/engine/install/)

[DOCKER WINDOWS](https://docs.docker.com/desktop/windows/install/)

[DOCKER COMPOSE](https://docs.docker.com/compose/install/)

> Acesse onde contem esses aquivivos abaixo

![image](https://user-images.githubusercontent.com/1013698/154904740-9735b896-c3ec-418c-bac3-d2ba5f4f0c71.png)

```
$ docker-compose up -d
[+] Building 1.3s (10/10) FINISHED
 => [internal] load build definition from flask_dockerfile                                                              0.0s
 => => transferring dockerfile: 38B                                                                                     0.0s
 => [internal] load .dockerignore                                                                                       0.0s
 => => transferring context: 2B                                                                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.10-alpine                                                   1.1s
 => [internal] load build context                                                                                       0.0s
 => => transferring context: 2.57kB                                                                                     0.0s
 => [1/5] FROM docker.io/library/python:3.10-alpine@sha256:9f107fb8f0d64669f3cc857dd3b62e7f3b72e70b91a8f055868f1d0bad0  0.0s
 => CACHED [2/5] WORKDIR /todos_framework                                                                               0.0s
 => CACHED [3/5] COPY ./todos_framework .                                                                               0.0s
 => CACHED [4/5] COPY requirements-prod.txt requirements.txt                                                            0.0s
 => CACHED [5/5] RUN pip install -r requirements.txt                                                                    0.0s
 => exporting to image                                                                                                  0.0s
 => => exporting layers                                                                                                 0.0s
 => => writing image sha256:361692a0d3e7eebaf063d72a1a0fd50ef355d4f3d4db1446ddc6e9e3d318c7f0                            0.0s
 => => naming to docker.io/library/todos_framework_flask                                                                0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
[+] Running 1/1
 - Container todos_framework_container  Started
```

> Moleza... agora e so acessar a pagina

[LOCALHOST - 8080](http://localhost:8080)

![image](https://user-images.githubusercontent.com/1013698/154905378-408f478c-99b6-4442-87f6-3715eec82e53.png)

> PS.: Faltou a autenticacao e testes... 

> PS.: Nao ficou do jeito que eu queria mas to cansado ja...

