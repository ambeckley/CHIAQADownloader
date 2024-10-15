#Python 3.11.9
#Oct 14 2024
#Aaron Beckley
#
#Merge all pdfs into one pdf that downloaded from CHIA

from PyPDF2 import PdfReader, PdfWriter
import os

writer = PdfWriter()


for i in os.listdir("chiafiles"):
    #print(i)
    if ".pdf" in i:
        filepath = "chiafiles/"+i
        print("reading:" + i)
        reader = PdfReader(open(filepath, "rb"))
        for page in reader.pages:
            writer.add_page(page)

print("writing...")
with open("combined.pdf", "wb") as fh:
    writer.write(fh)