# atualizar_banco.py
import shutil
import os
import git

# Caminhos das pastas
PASTA_TCC = r"C:\Users\Kezia\OneDrive\Área de Trabalho\ControleProducao\instance"
PASTA_DASHBOARD = r"C:\Users\Kezia\OneDrive\Área de Trabalho\dashboard_plataforma"

# Copia o banco atualizado
shutil.copy2(
    os.path.join(PASTA_TCC, "producao.db"),
    os.path.join(PASTA_DASHBOARD, "producao.db")
)

# Faz commit e push
repo = git.Repo(PASTA_DASHBOARD)
repo.git.add("producao.db")
repo.index.commit("Atualiza banco de dados")
origin = repo.remote("origin")
origin.push()

print("✅ Banco atualizado e enviado para o Streamlit Cloud!")