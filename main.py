import pdfplumber as pp
from gtts import gTTS

pdf_text=''

with pp.open('LalluviaAutorArturoUslarPietri.pdf') as pdf:
    for page in pdf.pages:
        pdf_text+=page.extract_text()

tts = gTTS(text=pdf_text, lang='es')
tts.save('pdftomp3.mp3')
