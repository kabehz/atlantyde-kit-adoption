
# 🧠 Microservicio Cognitivo: Seguimiento de Progreso ATLANTYDE

## 🎯 Propósito

Este microservicio permite monitorizar y registrar el **progreso cognitivo de cada persona** que interactúa con el ecosistema ATLANTYDE, en especial durante las fases de **onboarding, formación o bootcamp**.

Forma parte de la estrategia de **neurodidáctica aplicada + gamificación ética**, orientada a perfiles junior, jóvenes desarrolladores, nodos emergentes y nuevos socios fundadores.

---

## ⚙️ ¿Cómo funciona?

Está diseñado como un **workflow automatizado** alojado en `.github/workflows/cognitive-progress.yml`, y se activa mediante:

- Cambios en `setup-demo.sh`
- Interacción con carpetas como `onboarding/`, `progress/`
- Commits etiquetados con avances
- Triggers manuales vía `workflow_dispatch`

---

## 📈 ¿Qué valida?

- Presencia de pasos completados en el script de instalación
- Puntos cognitivos acumulados (`TOTAL SABIDURÍA GANADA`)
- Generación de insignia simbólica: `NODO-JOVEN-ETHICAL-2024`
- Registro individualizado por colaborador (`.github/progress/{usuario}.txt`)

---

## 🧬 Filosofía y contexto

- Alineado con valores europeos de **educación inclusiva y digital ética**
- Refuerza la **motivación, reconocimiento simbólico y aprendizaje autónomo**
- Fomenta el sentido de pertenencia a una **comunidad federada, justa y transparente**

---

## 🔁 Ciclo operativo

1. Usuario ejecuta `bash setup-demo.sh`
2. Workflow detecta progresos y los cuantifica
3. Se genera un log personal y una notificación de badge
4. El usuario es invitado a compartir su avance en Discussions o Issues
5. El equipo central puede validar y otorgar insignias reales (p.ej. mediante OpenBadges)

---

## 🔗 Archivos relacionados

- `setup-demo.sh` → script gamificado
- `.github/workflows/cognitive-progress.yml` → workflow asociado
- `.github/progress/*.txt` → bitácora individual de avance

---

📘 Este microservicio será ampliado con interacciones IA + feedback emocional + certificación por hitos en futuras versiones.

© 2024 ATLANTYDE – Desde Andalucía para una Europa más justa, creativa y soberana.
