from pdf2docx import parse
from typing import Tuple


def convert_pdf2docs(input_file: str, output_file: str, pages: Tuple = None):

    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file = input_file, docx_file = output_file, pages = pages)


    summary = {
        "File" : input_file, "Pages" : str(pages), "Output file" : output_file
    }

    print("## summary #############################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("##########################################################################")

    return result
if __name__ == "__main__":
    import sys
    input_file = "Доверенность.pdf"
    output_file = "Доверенность.docx"
    convert_pdf2docs(input_file, output_file)
