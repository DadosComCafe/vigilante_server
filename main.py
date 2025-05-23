from python_sample_xlsx_report.src.python_generate_xlsx_report import add_numeric_sheet_to_file, gera_metrica
from typing import Any

import gradio as gr


def generate_report(file: Any) -> str:
    """This function receive the file and call `add_numeric_sheet_to_file` function to generates a new 
    xlsx file report.

    Args:
        file (Any): The input file

    Returns:
        str: The output file path
    """

    path_in :str = file.name
    add_numeric_sheet_to_file(path_in)
    #TODO: chamar a função gera_metrica, passando como parâmetro `path_in.replace('.xlsx', '_numeric.xlsx')`
    #gera_metrica()
    return path_in.replace('.xlsx', '_numeric.xlsx')

with gr.Blocks() as demo:
    file_in = gr.File(label="Envie um arquivo XLSX", file_types=['.xlsx'])
    btn_download = gr.DownloadButton(label="Download Report")
    
    file_in.change(fn=generate_report, inputs=file_in, outputs=btn_download)

demo.launch()