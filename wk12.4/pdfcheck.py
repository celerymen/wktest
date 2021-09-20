import codecs
import re
import sys
from io import BytesIO

from pdfminer import high_level

pdf_path = sys.argv[1]
with open(pdf_path, 'rb') as pdf_file:
    pdf_data = pdf_file.read()
    extracted_text = high_level.extract_text(BytesIO(pdf_data), "", [0])
    print(re.findall(r'\w+\t\w+', extracted_text))
