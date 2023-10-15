#pip install pdfplumber -q

import pdfplumber as pp

with pp.open("Torres-Richard-ES.pdf") as CV:
    for page_no,page in enumerate(CV.pages,start=1):
        print(f"{page_no = }")
        data = page.extract_text()
        print(data.strip())
        print("*"*100)
        