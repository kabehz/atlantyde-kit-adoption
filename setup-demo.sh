#!/bin/bash

echo "🌊 Bienvenido a ATLANTYDE-KIT · Setup Interactivo"
echo "--------------------------------------------------"
echo "🧠 Preparamos tu entorno para sumarte como Nodo Ético Federado"
echo ""
echo "🎮 ¡Modo aprendizaje activado! Cada paso completado suma puntos de sabiduría 🌟"

score=0

echo "🔍 Paso 1: Verificando dependencias..."
if command -v git &> /dev/null && command -v node &> /dev/null && command -v npm &> /dev/null; then
  echo "✅ Git, Node.js y npm detectados"
  ((score+=10))
else
  echo "❌ Faltan dependencias. Por favor instala: git, node, npm"
  exit 1
fi

echo ""
echo "📦 Paso 2: Instalando dependencias del proyecto..."
npm install
((score+=10))

echo ""
echo "🚀 Paso 3: Lanzando entorno local de desarrollo con Astro..."
npm run dev &
((score+=10))
sleep 3

echo ""
echo "📘 Paso 4: Documentación MkDocs (requiere Python y pip)..."
if command -v mkdocs &> /dev/null; then
  echo "✅ MkDocs ya instalado"
else
  echo "📥 Instalando MkDocs..."
  pip install mkdocs
fi
((score+=10))

echo ""
echo "🎯 TOTAL SABIDURÍA GANADA: $score puntos"
if [ "$score" -ge 40 ]; then
  echo "🎉 ¡Felicidades! Has completado el onboarding como aspirante a nodo ATLANTYDE"
  echo "🏅 Código para reclamar recompensa: NODO-JOVEN-ETHICAL-2024"
else
  echo "💡 Sigue los pasos y repite el script cuando estés list@"
fi

echo ""
echo "📬 Comparte tu avance en discussions y reclama tu insignia fundadora 🧬"