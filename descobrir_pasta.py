# descobrir_pasta.py
import os

base_path = r"C:\Users\Kezia\OneDrive"

print("🔍 Verificando pastas dentro de OneDrive...\n")

# Lista todas as pastas no OneDrive
for pasta in os.listdir(base_path):
    caminho_completo = os.path.join(base_path, pasta)
    if os.path.isdir(caminho_completo):
        print(f"📁 {pasta}")
        
        # Verifica se contém "trabalho" ou "desktop"
        if "trabalho" in pasta.lower() or "desktop" in pasta.lower():
            print(f"   ⚠️ POSSÍVEL PASTA DE TRABALHO: {pasta}")

print("\n" + "="*50)
print("💡 Dica: Anote o nome EXATO da pasta 'Área de Trabalho'")
print("="*50)