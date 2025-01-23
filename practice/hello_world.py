"""
替換日期
"""
# -*- coding: utf-8 -*-
import win32com.client
import win32com.client.dynamic
import datetime

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
    ##week 0~5
    for wk in range(0,5,1):
        
        source_doc="C:\\Users\\Teddy\\Documents\\2020-新光人壽\\服務單-20200522.doc"
        ##替換日期 周一跟周五
        find_word="05/18","05/22"
        find_word_dt = datetime.datetime.strptime(find_word[0], "%m/%d")               \
                      ,datetime.datetime.strptime(find_word[1], "%m/%d")
        replace_word_dttime=str(find_word_dt[0] + datetime.timedelta(days=wk*7) )      \
                           ,str(find_word_dt[1] + datetime.timedelta(days=wk*7) )       #add week * 7 days      
        replace_word=str(replace_word_dttime[0][5:7]+"/"+replace_word_dttime[0][8:10]) \
                    ,str(replace_word_dttime[1][5:7]+"/"+replace_word_dttime[1][8:10])
        print(replace_word)
        target_doc="C:\\Users\\Teddy\\Documents\\2020-新光人壽\\服務單-2020"+ replace_word[1][0:2] + replace_word[1][3:5]+".doc"
  

        AppWord = ReadWrod(source_doc)
        MS_Word_Find_Replace(AppWord, find_word[0], replace_word[0])
        MS_Word_Find_Replace(AppWord, find_word[1], replace_word[1])
        MS_Wrod_SaveAS(AppWord, target_doc)
 
if __name__ == '__main__':
    main()

