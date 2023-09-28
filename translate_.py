from translate import Translator
class my_translate():
    
    def translateText(self, strString, strTolang):
        self.strString = strString
        self.strTolang = strTolang
        translator = Translator(to_lang=self.strTolang)
        translation = translator.translate(self.strString)
        return (str(translation))
   
#def translateText_ts(Text,src_lang,dest_lang):
 #       translator= Translator(from_lang=src_lang,to_lang=dest_lang)
  #      translated = translator.translate(Text)
   #     return translated
# Create a Class object and call the Translate function

#objTrans=my_translate()
#strTranslatedText= objTrans.translateText('How are you', 'de')
#print(strTranslatedText)
#print(my_translate.translateText_("Guten Morgen",'de','en'))
