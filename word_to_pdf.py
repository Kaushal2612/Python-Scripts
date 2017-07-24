import sys
import os
import comtypes.client

wdFormatPDF = 17

in_file = "C:\\Users\\Kaushal Jhawar\\Desktop\\kaushal.docx"
out_file = "C:\\Users\\Kaushal Jhawar\\Desktop\\Kaushal.pdf"

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()
