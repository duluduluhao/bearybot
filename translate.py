#encoding:utf-8
from googletrans import Translator
import sys

#input: 字符串

#output: 字符串

#使用方式:
'''
    tran = translate("输出很高")
    print tran.text
'''

class translate(object):

    my_translator = None

    def __init__(self,str):
        self.my_translator = Translator()
        src_lang = self.my_translator.detect(str).lang
        if src_lang.lower() == 'zh-cn':
            self.text = self.my_translator.translate(str, dest='en').text
        else:
            self.text = self.my_translator.translate(str, dest='zh-cn').text


if __name__ == '__main__':
        tran = translate("输出很高")
        print tran.text