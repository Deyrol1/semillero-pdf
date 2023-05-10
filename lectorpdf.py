from PyPDF2 import PdfReader
import pathlib
from os import remove


ejemplo_dir = '/Users/Windows 10/Desktop/octavo corte/semillero'



miau= []
directorio = pathlib.Path(ejemplo_dir)
for fichero in directorio.iterdir():
    if fichero.name.endswith("pdf"):
        miau.append(fichero.name)
        


for i in range(len(miau)):
    if(miau[i]=="pdf"):
        miau.pop(i)
        break
    
print(miau)
for i in range(len(miau)):

    try:
        reader = PdfReader(miau[i])
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            print(text)
    except:
        print(miau[i],"da error")
        remove(miau[i])






    




      
