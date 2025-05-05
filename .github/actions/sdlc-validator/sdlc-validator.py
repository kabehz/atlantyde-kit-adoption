import os
import re
import json
from datetime import datetime

# Cargar configuraciones desde un archivo JSON
with open("config/sdlc_config.json") as config_file:
    SDLC_CHECKS = json.load(config_file)

def validate_file_exists(path):
    if not os.path.exists(path):
        print(f"❌ FALTA: {path}")
        return False
    print(f"✅ OK: {path}")
    return True

def validate_version_format():
    try:
        with open(SDLC_CHECKS["version_file"]) as f:
            version = f.read().strip()
            if re.match(r"^v?\d+\.\d+\.\d+(-[a-z]+)?$", version):
                print(f"✅ Versión válida: {version}")
                return True
            else:
                print(f"❌ Formato de versión inválido: {version}")
                return False
    except FileNotFoundError:
        print("❌ version.txt no encontrado")
        return False

def run_sdlc_checks():
    print("🔍 Validando SDLC...")
    all_ok = True
    for key, path in SDLC_CHECKS.items():
        if not validate_file_exists(path):
            all_ok = False
    if not validate_version_format():
        all_ok = False
    if all_ok:
        print("🎉 Validación SDLC completa y exitosa.")
    else:
        print("⚠️ Validación incompleta. Revisa los errores anteriores.")

if __name__ == "__main__":
    run_sdlc_checks()