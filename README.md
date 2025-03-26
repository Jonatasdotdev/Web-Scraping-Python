# Web Scraping - ANS (Agência Nacional de Saúde Suplementar)

Script Python para baixar automaticamente os Anexos I e II (PDFs) do Rol de Procedimentos da ANS e compactá-los em um arquivo ZIP.

## 📌 Funcionalidades

- Acessa o portal oficial da ANS
- Identifica os links dos Anexos I e II em PDF
- Faz o download dos arquivos preservando os nomes originais
- Compacta todos os PDFs em um único arquivo ZIP
- Tratamento de erros e logs de progresso

## ⚙️ Pré-requisitos

- Python 3.6+
- Bibliotecas 
  ```bash
  pip install requests beautifulsoup4
