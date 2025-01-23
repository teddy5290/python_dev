###104 crawler
###動機: 在104上瀏覽很方便 但是每天看會發現一直再重複瀏覽重複資料
###希望能排除掉不必要的資訊
###首先要建立黑名單 因104上只能設一個黑名單而已 很不方便
###然後就懶了

import requests
import bs4
import csv
import random,time
import os 
from datetime import datetime


now = datetime.now()
# dd/mm/YY
dt_str = now.strftime("%Y%m%d_%H%M")
# datetime object containing current date and time
print("now =", dt_str)


fn='104人力銀行職缺內容共5頁_'+dt_str+'.csv'   

url_A ='https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007001000%2C2007002000&keyword=%E8%B3%87%E6%96%99%E5%80%89%E5%84%B2%20etl%20%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B%20&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=1&asc=0&page='
url_B = '&mode=s&jobsource=n_my104_search'

# https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007001000%2C2007002000&keyword=sql%20%E8%B3%87%E6%96%99%E5%80%89%E5%84%B2%20etl&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=1&asc=0&page=1&mode=s&jobsource=n_my104_search
# https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007001000%2C2007002000&keyword=%E8%B3%87%E6%96%99%E5%80%89%E5%84%B2%20etl%20%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B%20&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=1&asc=0&page=1&mode=s&jobsource=n_my104_search
all_job_datas=[]

## Block list
block_job_name=['網頁前端','PHP','.NET','前端工程師','資料庫工程師']
block_job_company=['歐立威','精誠','新加坡商鈦坦','億力','創代科技','海棠','中華工程','文德福','金財通','宏虹電子','關貿','廣晉','一騰資訊']

def extract_salary(job):
    salary_tags = job.find_all('a', class_='b-tag--default', string=lambda text: '薪' in text if text else False)
    for tag in salary_tags:
        text = tag.get_text(strip=True)
        if '年薪' in text or '月薪' in text:
            return text
    return '無薪資資訊'


with open('jobs.txt', 'w', encoding='utf-8') as file:
    for page in range(1,5+1):
        url = url_A+str(page)+url_B
        print(url)
        htmlFile = requests.get(url)
        ObjSoup=bs4.BeautifulSoup(htmlFile.text,'lxml')
        jobs = ObjSoup.find_all('article',class_='js-job-item')                 #搜尋所有職缺  
        
        for job in jobs:
            block =False
            job_name=job.find('a',class_="js-job-link").text                    #職缺內容
            job_company=job.get('data-cust-name')                               #公司名稱
            job_loc=job.find('ul', class_='job-list-intro').find('li').text     #地區            
            job_pay = extract_salary(job)                                       #薪資
            job_url=job.find('a').get('href')                                   #網址
            hyperlink_formula = f'=HYPERLINK("http://{job_url}")'               #超連結網址(方便excel點選)
            job_info=job.find ('p', class_='job-list-item__info b-clearfix b-content').text #工作內容
            job_indcat=job['data-indcat-desc']                                  #產業別


            ### 
            job_data={'職缺內容':job_name,
                      '公司名稱':job_company, 
                      '產業別':job_indcat,
                      '工作內容':job_info,
                      '地區':job_loc,
                      '薪資':job_pay,
                      '網址':hyperlink_formula} 

            ### block list check
            for job_substr in block_job_name:
                if job_substr in job_name :
                    print ("block:"+job_name)
                    block =True
                    break
            for company_substr in block_job_company:
                if company_substr in job_company :
                    print ("block:"+job_company)
                    block =True
                    break
            ### if not block : append
            if block == False:
                all_job_datas.append(job_data)
            # 另存原始檔
            file.write(str(job) + '\n\n')
        time.sleep(random.randint(1,3))


columns_name=['職缺內容','公司名稱','產業別','工作內容','地區','薪資','網址']          #第一欄的名稱 #有工作內容版

with open('104\\'+fn,'w',newline='',encoding='utf_8_sig') as csvFile:               #定義CSV的寫入檔,並且每次寫入完會換下一行
    dictWriter = csv.DictWriter(csvFile,fieldnames=columns_name,quoting=csv.QUOTE_NONNUMERIC)            #定義寫入器
    dictWriter.writeheader()       
    for data in all_job_datas:
        dictWriter.writerow(data)
        