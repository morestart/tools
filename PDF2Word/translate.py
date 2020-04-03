import pdfminer.high_level
from io import BytesIO as StringIO
from pdfminer.layout import LAParams


data = (pdfminer.high_level.extract_text("/Users/cattree/PycharmProjects/tools/PDF2Word/刺参-夏季高温影响.pdf"))

with open('data.txt', 'w') as f:
    f.write(data)

output_string = StringIO()
with open('/Users/cattree/PycharmProjects/tools/PDF2Word/刺参-夏季高温影响.pdf', 'rb') as fin:
    pdfminer.high_level.extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='html', codec=None)