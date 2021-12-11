#!/usr/bin/env python3

from googletrans import Translator #pip3 install googletrans==3.1.0a0


translator = Translator()


stringForEnglish = ''
results = translator.translate(stringForEnglish, src='en', dest='zh-cn')
print(results.text) #Translated(src=ko, dest=en, text=Hello., pronunciation=None, extra_data="{'translat...")




