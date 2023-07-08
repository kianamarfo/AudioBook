import pyttsx3
from PyPDF2 import PdfReader

book = open('Holiness-J.C.Ryle.pdf', 'rb')
pdfReader = PdfReader(book)
pages = len(pdfReader.pages)
print(pages)

speaker = pyttsx3.init()

for num in range(2, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
