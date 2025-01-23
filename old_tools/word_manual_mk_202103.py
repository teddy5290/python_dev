"""
開word替換字串 另存新檔
功能:用list填文書中的函式名稱
"""
# -*- coding: utf-8 -*-
import win32com.client
import win32com.client.dynamic
import datetime
import os 

f = open("C:\\Users\\Teddy\\Documents\\2020-期交所\\UDF_manual\\udf_list_01-17.txt","r",encoding="UTF-8")


source_doc="C:\\Users\\Teddy\\Documents\\2020-期交所\\UDF_manual\\00_manual_funcname.doc"
find_word="$funcname","$funcfeature"

def ReadWrod(fileName):
    app  = win32com.client.Dispatch("Word.Application")
    #app.Visible = True
    app.Documents.Open(fileName)#開啟舊檔
    #app.Documents.Add(filename)#New 一個新檔
    return app
 
def MS_Word_Find_Replace(app, Search_Word, replace_str):
    wdStory = 6
    app.Selection.HomeKey(Unit=wdStory)
    find = app.Selection.Find
    find.Text = Search_Word
    while app.Selection.Find.Execute():
        app.Selection.TypeText(Text=replace_str)
        print ("Find It ", Search_Word ,"Replce to",replace_str)
 
 
def MS_Wrod_SaveAS(app, fileName):
    print ("Save as ",fileName)
    app.ActiveDocument.SaveAs(fileName)
    app.ActiveDocument.Close()
 
 
def main():
    ##讀取list檔 txt[]=01,函式名稱,功能說明
    ##替換word中的變數
    find_word="$funcname","$funcfeature"
    for line in f:
        txt=line.split("\t") 
        print(txt[0],txt[1],txt[2])
        target_doc="C:\\Users\\Teddy\\Documents\\2020-期交所\\UDF_manual\\"+ txt[0] +"_manual_"+txt[1]+".doc"
        AppWord = ReadWrod(source_doc)
        MS_Word_Find_Replace(AppWord, find_word[0], txt[1])
        MS_Word_Find_Replace(AppWord, find_word[1], txt[2])
        MS_Wrod_SaveAS(AppWord, target_doc)
    f.close()
        
if __name__ == '__main__':
    main()
