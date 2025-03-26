import os
import requests
from bs4 import BeautifulSoup
import zipfile
from urllib.parse import urljoin

def download_ans_anexos():
    # Configurações iniciais
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    output_dir = "anexos_ans"
    zip_filename = "anexos_ans.zip"
   
    # Criar diretório se não existir
    os.makedirs(output_dir, exist_ok=True)
   
    try:
        # 1. Acessar o site
        print(f"Acessando o site: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
       
        # 2. Parsear o conteúdo HTML
        soup = BeautifulSoup(response.text, 'html.parser')
       
        # 3. Encontrar os links para os Anexos I e II em PDF
        anexos = []
       
        # Procurar por links que contenham "Anexo I" ou "Anexo II" e terminem com .pdf
        for link in soup.find_all('a', href=True):
            href = link['href'].lower()
            text = link.get_text().lower()
           
            # Usar o nome do arquivo original para evitar duplicatas
            if ('anexo i' in text or 'anexo i' in href) and href.endswith('.pdf'):
                original_filename = os.path.basename(link['href'])
                anexos.append((original_filename, urljoin(url, link['href'])))
            elif ('anexo ii' in text or 'anexo ii' in href) and href.endswith('.pdf'):
                original_filename = os.path.basename(link['href'])
                anexos.append((original_filename, urljoin(url, link['href'])))
       
        if not anexos:
            raise Exception("Não foi possível encontrar os links para os Anexos I e II")
       
        # 4. Fazer download dos PDFs
        downloaded_files = []
        for filename, file_url in anexos:
            print(f"Baixando {filename} de {file_url}")
            file_path = os.path.join(output_dir, filename)
           
            pdf_response = requests.get(file_url, timeout=10)
            pdf_response.raise_for_status()
           
            with open(file_path, 'wb') as f:
                f.write(pdf_response.content)
           
            downloaded_files.append(file_path)
            print(f"{filename} baixado com sucesso!")
       
        # 5. Compactar os arquivos em um ZIP
        print(f"Criando arquivo compactado: {zip_filename}")
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in downloaded_files:
                zipf.write(file, os.path.basename(file))
       
        print("Processo concluído com sucesso!")
        print(f"Arquivos baixados e compactados em: {zip_filename}")
       
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
        raise

if __name__ == "__main__":
    download_ans_anexos()