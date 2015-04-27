#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------
#
# IntelUniq
#               -- Intelligence shall be unique 
#
# Reform.py: #TODO DESC HERE
#
#--------------------------------------------------------------
#
# Date:     2015-04-27
#
# Author:   gewu@baidu.com
#
#

#--------------------------------------------------------------
# Globl Constants & Functions
#--------------------------------------------------------------

#--------------------------------------------------------------
# Classes
#--------------------------------------------------------------
import string
import re

import langconv 

d_map = {
         "a" : "b"
        }

class Normalize(object):
    
    def __init__(self):
        pass

    def simple(self, ustring):                           # translate to simple
        return langconv.Converter('zh-hans').convert(ustring.decode('utf-8'))

    def strQ2B(self, ustring):           # reform punctuation
        rstring = ''
        for uchar in ustring:
            inside_code = ord(uchar)
            if inside_code == 12288:     #translate for space
                inside_code = 32
            elif inside_code >= 65281 and inside_code <= 65374:
                inside_code -= 65248
                
            rstring += unichr(inside_code)
        return rstring

    def translator(self, frm='', to='', delete='', keep=None):  #delete punctuation
        if len(to) == 1:
            to = to * len(frm)
        trans = string.maketrans(frm, to)
        if keep is not None:
            allchars = string.maketrans('', '')
            delete = allchars.translate(allchars, keep.translate(allchars, delete))
        def translate(s):
            return s.translate(trans, delete)
        return translate

    def multiple_replace(self, text, addict):
        rx = re.compile('|'.join(addict.keys()))
        def one_xlat(match):
            return addict[match.group(0)]
        return rx.sub(one_xlat, text)

if __name__ == "__main__":

   test_data = "testaaa"
   print test_data
   normalize = Normalize()

   test_data = normalize.simple(test_data)            
   test_data = normalize.strQ2B(test_data.strip())
   test_data = normalize.translator(delete=string.punctuation)(test_data.encode('utf-8'))
   result = normalize.multiple_replace(test_data, d_map)
   print result



