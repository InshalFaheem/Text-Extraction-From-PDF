import fitz
pdf = "CV.pdf"
doc = fitz.open(pdf)
for page in doc:
    text = page.getText("text")
    print(text)