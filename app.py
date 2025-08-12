import os
import time

# Chemin vers ADB (mets le chemin complet si pas dans le PATH)
ADB_PATH = "adb"

# ID de l'émulateur actif
DEVICE_ID = "emulator-5554"

# Coordonnées à cliquer
X = 500
Y = 800

# Nombre de clics
NB_CLICS = 5000

# Délai entre les clics (en secondes)
DELAI = 0.01

for i in range(NB_CLICS):
    os.system(f'{ADB_PATH} -s {DEVICE_ID} shell input tap {X} {Y}')
    print(f"Clic {i+1}/{NB_CLICS}")
    time.sleep(DELAI)

print("Terminé ✅")
