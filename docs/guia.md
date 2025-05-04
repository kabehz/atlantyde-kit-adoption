# Guía de Uso del Repositorio Plantilla ATLANTYDE-KIT

Bienvenido/a a la base fundacional de ATLANTYDE. Este repositorio es una **plantilla validada** que cualquier nodo o socio cooperativista puede utilizar como punto de partida para desarrollar, desplegar y contribuir al ecosistema federado ATLANTYDE.

## 🧭 ¿Qué contiene esta plantilla?

- 🌐 Sitio visual en Astro con navegación y hero institucional
- 📘 Documentación técnica y legal en MkDocs (Material Theme)
- 🎨 Identidad visual: logo, íconos, tipografías y mockups
- ⚙️ Flujo CI/CD para despliegue automático en GitHub Pages
- 🔐 Blindaje ético y gobernanza cooperativa ya integrada

---

## 🌀 Cómo usar esta plantilla

### 1. Crear tu fork como nodo independiente

1. Haz clic en **"Use this template"**.
2. Crea tu repositorio nuevo (ej. `atlantyde-nodo-cordoba`).
3. Activa GitHub Pages y Actions según indicaciones de esta guía.

### 2. Personaliza tus datos

Modifica los siguientes archivos:
- `astro.config.mjs` → URL base de tu nodo
- `mkdocs.yml` → URL y nombre de tu sede federada
- `docs/index.md` → Preséntate como nodo o socio
- `README.md` → Especifica tu enfoque territorial o temático

---

## 🚀 Despliegue automático

Este repositorio viene preconfigurado para desplegar automáticamente:

- `/astro-site/` como interfaz web institucional
- `/docs/` como documentación accesible desde `/docs/`
- `GitHub Pages` como hosting universal federado

Puedes activar el flujo manual desde **Actions > Deploy > Run workflow**.

---

## 🤝 Buenas prácticas para nodos ATLANTYDE

✅ Mantén la coherencia con el Manifiesto Fundacional  
✅ Usa siempre licencias libres (AGPLv3, MIT o similares)  
✅ Participa mediante issues, forks o pull requests  
✅ Preserva la trazabilidad, la ética y el propósito  

---

## 🌍 ¿Por qué esta guía?

Para asegurar que **todas las células federadas de ATLANTYDE** puedan escalar con autonomía, identidad y coordinación desde el primer commit.


## 🧠 Media Cognitiva Estratégica

ATLANTYDE incorpora un flujo de validación cognitiva manual para asegurar que cada iteración de desarrollo o contribución esté alineada con la visión fundacional, trazabilidad estratégica y enfoque ético del proyecto.

### 📋 ¿Cuándo ejecutarlo?

Este flujo debe activarse al comienzo de una sesión o bloque de trabajo relevante (por ejemplo, una tarea importante, revisión de PR, diseño legal o despliegue técnico).

### ⚙️ Flujo de trabajo involucrado
- `.github/workflows/cognitive-strategy.yml`

### 🧾 ¿Qué datos recopila?

| Campo         | Descripción                                     |
|---------------|-------------------------------------------------|
| `user_id`     | Identificador del socio, colaborador o nodo     |
| `focus_area`  | Área de enfoque de esta iteración (`visual`, `legal`, `docs`, etc.) |
| `iteration_goal` | (Opcional) Meta o resultado esperado         |

Cada ejecución genera un archivo de log en `.github/cognition-logs/` con trazabilidad completa.

### ✅ Resultado

Este proceso garantiza la alineación ética y operativa de todas las contribuciones, funcionando como contrato blando entre el contribuyente y el propósito de ATLANTYDE.