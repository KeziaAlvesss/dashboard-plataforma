# atualizar_banco.py
import os
import shutil
import git

# ================================================================
# CONFIGURAÇÃO AUTOMÁTICA PARA SEU SISTEMA
# ================================================================
# Base do OneDrive (sem sufixo)
ONE_DRIVE_BASE = r"C:\Users\Kezia\OneDrive"

# Possíveis nomes para "Área de Trabalho" (testamos todos)
POSSIVEIS_NOMES_AREA_TRABALHO = [
    "Area de Trabalho",    # Sem acento (mais comum no Windows)
    "Área de Trabalho",    # Com acento (menos comum)
    "Desktop"              # Nome em inglês (padrão OneDrive)
]

def encontrar_pasta_trabalho():
    """Encontra automaticamente a pasta correta de trabalho"""
    for nome in POSSIVEIS_NOMES_AREA_TRABALHO:
        caminho_teste = os.path.join(ONE_DRIVE_BASE, nome)
        if os.path.exists(caminho_teste):
            return nome, caminho_teste
    raise FileNotFoundError(
        f"❌ Nenhuma pasta de trabalho encontrada em {ONE_DRIVE_BASE}\n"
        f"Tente renomear sua pasta para 'Area de Trabalho' (sem acento)"
    )

def main():
    # Encontra a pasta de trabalho correta
    nome_pasta, caminho_pasta = encontrar_pasta_trabalho()
    print(f"✅ Pasta de trabalho encontrada: '{nome_pasta}'")
    
    # Monta os caminhos completos
    PASTA_TCC = os.path.join(caminho_pasta, "ControleProducao", "instance")
    PASTA_DASHBOARD = os.path.join(caminho_pasta, "dashboard_plataforma")
    
    print(f"📁 TCC: {PASTA_TCC}")
    print(f"📁 Dashboard: {PASTA_DASHBOARD}\n")
    
    # Valida pastas
    if not os.path.exists(PASTA_TCC):
        raise FileNotFoundError(f"❌ Pasta TCC não encontrada: {PASTA_TCC}")
    
    if not os.path.exists(PASTA_DASHBOARD):
        raise FileNotFoundError(f"❌ Pasta Dashboard não encontrada: {PASTA_DASHBOARD}")
    
    # Copia o banco
    source = os.path.join(PASTA_TCC, "producao.db")
    dest = os.path.join(PASTA_DASHBOARD, "producao.db")
    
    if not os.path.exists(source):
        raise FileNotFoundError(f"❌ Arquivo não encontrado: {source}")
    
    shutil.copy2(source, dest)
    print(f"✅ Banco copiado: {dest}")
    
    # Commit e push
    repo = git.Repo(PASTA_DASHBOARD)
    if repo.is_dirty(untracked_files=True):
        repo.git.add("producao.db")
        repo.index.commit("Atualiza banco de dados - " + os.path.basename(source))
        origin = repo.remote("origin")
        origin.push()
        print("✅ Banco atualizado no GitHub!")
    else:
        print("ℹ️  Nenhuma alteração detectada no banco.")

if __name__ == "__main__":
    try:
        main()
        input("\n✅ Concluído! Pressione Enter para fechar...")
    except Exception as e:
        print(f"\n❌ Erro: {str(e)}")
        input("\nPressione Enter para fechar...")