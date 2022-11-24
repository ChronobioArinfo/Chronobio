# CHRONOBIO IA PLAYER

## Installation:
On windows, in a terminal of VS code, run:

### User:
```console
 python3 -m venv .venv
 .venv\Scripts\python.exe -m pip install --upgrade pip
 .venv\Scripts\python.exe -m pip install .
```

### Devs:
```console
 python3 -m venv .venv
 .venv\Scripts\python.exe -m pip install --upgrade pip
 .venv\Scripts\python.exe -m pip install .[test]
```

## Execution
In a terminal, run:

```console
python.exe -m player.player -a {host} -p {port}
```

## Pytest:
In a terminal, run:
```console
 pytest
```
