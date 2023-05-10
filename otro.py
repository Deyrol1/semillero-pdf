from PyPDF2 import PdfReader

reader = PdfReader('ejemplo.pdf')

print(len(reader.pages))
  
# getting a specific page from the pdf file
page = reader.pages[0]
  
# extracting text from page
text = page.extract_text()
print(text)

