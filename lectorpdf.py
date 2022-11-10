import PyPDF2  
import pathlib
from os import remove


ejemplo_dir = '/Users/Windows 10/Desktop/octavo corte/semillero'



miau= []
directorio = pathlib.Path(ejemplo_dir)
for fichero in directorio.iterdir():
    if fichero.name.endswith("pdf"):
        miau.append(fichero.name)
        

for i in range(len(miau)):
    print(miau[i])
    if(miau[i]=="pdf"):
        miau.pop(i)
        break





for i in range(len(miau)):

    pdfFileObj = open(miau[i], 'rb')  
    try:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            
            print(pageObj.extractText())  
        pdfFileObj.close()
    except:
        pdfFileObj.close()
        remove(miau[i])

    




      
