from python_sample_xlsx_report.src.python_generate_xlsx_report import add_numeric_sheet_to_file, gera_metrica
import streamlit as st


def handle_file(file) -> st.file_uploader:
    if file is not None:
        content = file.getvalue()
        return content
    else:
        st.write("Nenhum arquivo foi carregado.")
    

if __name__ == "__main__":
    st.title("Upload de Arquivo com Função e Streamlit")
    uploaded_file = st.file_uploader("Escolha um arquivo para upload")
    if uploaded_file: 
        file = handle_file(uploaded_file)
        add_numeric_sheet_to_file(file)
        gera_metrica(file)
        #TODO: entender como manipular o arquivo