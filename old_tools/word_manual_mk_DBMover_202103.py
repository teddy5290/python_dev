"""
開word替換字串 另存新檔
功能:用list填文書中的函式名稱
版本:dbmover版 多了替換參數
"""
# -*- coding: utf-8 -*-
import win32com.client
import win32com.client.dynamic
import datetime
import os 

f = open("C:\\Users\\Teddy\\Documents\\2020-期交所\\DBMover_manual\\list.csv","r",encoding="UTF-8")


source_doc="C:\\Users\\Teddy\\Documents\\2020-期交所\\DBMover_manual\\DM000_公版.doc"


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

    find_word="$funcnum","$funcname","$funccode","$funcfeature","$param1","$paramtype1","$param2","$paramtype2","$param3","$paramtype3","$$$","$$$"
    for line in f:
        txt=line.split("\t") 
        print(txt)
        print (len(txt))
        target_doc="C:\\Users\\Teddy\\Documents\\2020-期交所\\DBMover_manual\\DM"+ txt[0] +"_manual_"+txt[2]+".doc"
        AppWord = ReadWrod(source_doc)
        for j in range(10):
            if j>=len(txt): 
                MS_Word_Find_Replace(AppWord, find_word[j], " ")
            else:
                MS_Word_Find_Replace(AppWord, find_word[j], txt[j])
        MS_Wrod_SaveAS(AppWord, target_doc)

       
    f.close()

if __name__ == '__main__':
    main()
