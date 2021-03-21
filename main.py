import pyttsx3
import PyPDF2
book=open('joiningAnnexure.pdf','rb')
reader=PyPDF2.PdfFileReader(book)
pages=reader.numPages
speaker=pyttsx3.init()
for num in range(1,pages):
    page=reader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()