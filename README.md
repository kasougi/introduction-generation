# introduction-generation
Сервис для генерации введения.

<img width="1280" alt="Снимок экрана 2023-12-20 в 15 01 38" src="https://github.com/kasougi/introduction-generation/assets/62507503/6db03e32-5d7b-4ebe-b879-2db760f90543">

Для проекта требуется:
* Python >=3.8
* pdm 2.4.9

### Установка пакетов c помощью asdf

---
Про asdf можно почитать [тут](https://github.com/asdf-vm/asdf) 

#### python
```sh
asdf plugin add python
asdf install python 3.8.9
asdf global python 3.8.9
```

#### pdm
```sh
asdf plugin add pdm
asdf install pdm 2.9.2
asdf global pdm 2.9.2
```

## установка pdm
Про pdm можно почитать [тут](https://github.com/pdm-project/pdm) 

### Установка зависимостей

```sh
pdm install --verbose
```

### Активация виртуального окружения

```sh
source .venv/bin/activate
```
