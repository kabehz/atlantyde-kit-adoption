# 🌐 API Intel Sync · GitHub Action

Este microservicio ejecuta una extracción periódica de datos desde APIs públicas como GitHub, Medium o X para analizar:

- Tendencias de adopción
- Estilos de contribución abiertos
- Visibilidad de repositorios éticos

## 📘 Cómo usar

```yaml
on:
  schedule:
    - cron: '0 9 * * 1'
  workflow_dispatch:
jobs:
  fetch-api-intel:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: python3 .github/actions/api-intel-sync/intel_fetch.py
```

## 🧠 Propósito

Protegernos de la manipulación algorítmica mediante datos abiertos y trazables.

Autor: Jaime Silva · @kabehz · Proyecto ATLANTYDE