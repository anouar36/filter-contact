@echo off
title Email Campaign Menu
color 0B

:: Aller automatiquement dans le dossier du projet, peu importe d'où la commande est lancée
cd /d "C:\Users\dell\Desktop\filter-contact"

echo =======================================================
echo        Activation de l'environnement Python...
echo =======================================================

if not exist ".venv\Scripts\activate.bat" (
    echo [ERREUR] L'environnement virtuel .venv n'a pas ete trouve.
    pause
    exit /b 1
)

call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERREUR] Impossible d'activer l'environnement virtuel.
    pause
    exit /b 1
)

python menu.py
