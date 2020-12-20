from googletrans import Translator

def googletran(text, src, dest):
    translator = Translator(service_urls=[
      'translate.googleapis.com',
      'translate.google.co.kr',
    ])
    translator= Translator()
    if src=='' :
        result = translator.translate(text, dest=dest)
        return result.text
    result = translator.translate(text, src=src, dest=dest)
    return result.text
