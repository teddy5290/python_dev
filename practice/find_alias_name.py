# -*- coding: utf-8 -*-
###列出可能有用到alias_name的欄位
###EX.SELECT ...,sum(a) as a_alias, row_number() (order by a_alias) as show_seq_no FROM ...
###目的:GP 不能用alias_name,要取代掉

import re
import glob



#攤平list用func
def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])
#print(flatten([[1, 2, 3, 4], [5, 6, 7], [8, 9], 10]))




def find_alias_name(file_path):
    #CREATE TEMP TABLE T(\d) AS(((?!;).|\r\n)+?)row_number\(\) OVER \(order by (((?!;).|\r\n)+?)\) as show_seq_no +FROM(((?!;).|\r\n)+?)order *by (((?!;).)+);
    ##本來正邏輯是抓create temp table一整段 再把show_seq_no的order by擷取出來用
    ##    但找不到個別取配對結果group參數(例如$4)的方式
    ##    故改成分開抓兩種pattern

    #pattern1 create t1 as ...
    create_tx_pattern = re.compile(r"CREATE TEMP TABLE T(\d) AS(((?!;).|\r\n)+?)row_number\(\) OVER \(order by (((?!;).|\r\n)+?)\) as show_seq_no +FROM(((?!;).|\r\n)+?)order *by (((?!;).)+);",flags = re.S | re.I)
    #pattern2 (order by ...) as show_seq_no
    show_seq_no_pattern = re.compile(r"(?<=row_number\(\) OVER \(order by)(((?!;).|\r\n)+?)(?=\) as show_seq_no)")

    #寫死範例檔
    #file_path="C:\\Users\\Teddy\\Documents\\2020-期交所\\202104_order by alias name\\範例目標檔\\DB_OWNER.fun_proc_gen_NEWM_C7_106.sql"
    file = open(file_path ,"r",encoding="UTF-8").read()


    tx_re=create_tx_pattern.findall(file)
    order_by_re=show_seq_no_pattern.findall(file)


    ##多加一個[0] ,因為[1]都會有一個'E' 不確定是什麼參數
    ##print(order_by_re[1][0])

    total_list=[]

    for i in range (len(order_by_re)):
        
        order_list=order_by_re[i][0].replace(" ","").split(",")
        total_list.append(order_list)
        # print (str(i)+":")
        # print (order_list )
        

    total_list=flatten(total_list)
    # print(total_list)

    #以total_list取匹配 ( AS col) 若有匹配則print
    for col in total_list:
        is_as_col = re.search("AS "+col,file)
        if is_as_col:
            print(file_path)
            print (col)


#find_alias_name("C:\\Users\\Teddy\\Documents\\2020-期交所\\202104_order by alias name\\範例目標檔\\DB_OWNER.fun_proc_gen_NEWM_C7_106.sql")

file_list=glob.glob("C:\\Users\\Teddy\\Documents\\psql\\*.sql")

for file in file_list:
   find_alias_name(file)