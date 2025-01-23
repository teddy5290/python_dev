import datetime


for wk in range(0,35,7):
    start_date = "05-22"
    date_1 = datetime.datetime.strptime(start_date, "%m-%d")
    end_date = date_1 + datetime.timedelta(days=wk)
    end_date_str=str(end_date)
    #print (type (end_date_str) )
    print(end_date_str[5:10])

    d_dt=datetime.date(2020,5,20)
    print(d_dt)
    
    source_doc="C:\\Users\\Teddy\\Documents\\2020-新光人壽\\服務單-20200522.doc"
    
    find_word="05/18","05/22"
    find_word_dt = datetime.datetime.strptime(find_word[0], "%m/%d") \
                  ,datetime.datetime.strptime(find_word[1], "%m/%d")
    replace_word_dttime=str(find_word_dt[0] + datetime.timedelta(days=wk) )  \
                       ,str(find_word_dt[1] + datetime.timedelta(days=wk) )
    replace_word=str(replace_word_dttime[0][5:7]+"/"+replace_word_dttime[0][8:10]),str(replace_word_dttime[1][5:7]+"/"+replace_word_dttime[1][8:10])
    print(replace_word)
    target_doc="C:\\Users\\Teddy\\Documents\\2020-新光人壽\\服務單-2020"+ replace_word[1][0:2] + replace_word[1][3:5]+".doc"
    print(target_doc)