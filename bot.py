import calendar
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def select_date(dates,bit,from_to,dN):
    dN1 = calendar.weekday(dates, 12, 1)
    dN1+=1
    dN1%=7
    r = 1 + ((bit*(31 + dN1))//7)
    c = 1 + (dN + 1)%7
    driver.find_elements(By.CSS_SELECTOR,'.wc-date-container')[bit].click()
    if(bit==0):
        driver.find_element(By.XPATH,'//*[@id="date"]/angular2-date-picker/div/div[2]/div[1]/div[4]/div/span').click()
        driver.find_element(By.XPATH,'//*[@id="date"]/angular2-date-picker/div/div[2]/div[5]/div[2]/div/button[1]').click()
        driver.find_element(By.XPATH,'//*[@id="date"]/angular2-date-picker/div/div[2]/div[5]/div[1]/div[1]/input').clear()
        driver.find_element(By.XPATH,'//*[@id="date"]/angular2-date-picker/div/div[2]/div[5]/div[1]/div[1]/input').send_keys("12")
        driver.find_element(By.XPATH,'//*[@id="date"]/angular2-date-picker/div/div[2]/div[5]/div[1]/div[3]/input').clear()
        driver.find_element(By.XPATH,'//*[@id="date"]/angular2-date-picker/div/div[2]/div[5]/div[1]/div[3]/input').send_keys("0")
        driver.find_element(By.XPATH,'//*[@id="date"]/angular2-date-picker/div/div[2]/div[5]/div[3]/button').click()
    else:
        driver.find_element(By.XPATH,'//*[@id="date2"]/angular2-date-picker/div/div[2]/div[1]/div[4]/div/span').click()
        driver.find_element(By.XPATH,'//*[@id="date2"]/angular2-date-picker/div/div[2]/div[5]/div[2]/div/button[2]').click()
        driver.find_element(By.XPATH,'//*[@id="date2"]/angular2-date-picker/div/div[2]/div[5]/div[1]/div[1]/input').clear()
        driver.find_element(By.XPATH,'//*[@id="date2"]/angular2-date-picker/div/div[2]/div[5]/div[1]/div[1]/input').send_keys("11")
        driver.find_element(By.XPATH,'//*[@id="date2"]/angular2-date-picker/div/div[2]/div[5]/div[1]/div[3]/input').clear()
        driver.find_element(By.XPATH,'//*[@id="date2"]/angular2-date-picker/div/div[2]/div[5]/div[1]/div[3]/input').send_keys("59")
        driver.find_element(By.XPATH,'//*[@id="date2"]/angular2-date-picker/div/div[2]/div[5]/div[3]/button').click()

    driver.find_elements(By.CSS_SELECTOR,'.year-dropdown')[bit].click()
    from_year = driver.find_element(By.CSS_SELECTOR,'.years-list-view')
    least_year = from_year.find_elements(By.CSS_SELECTOR,'span')
    while(dates<int(least_year[0].text)):
        driver.find_element(By.XPATH,'//*[@id="{}"]/angular2-date-picker/div/div[2]/div[5]/div[1]'.format(from_to)).click()
        from_year = driver.find_element(By.CSS_SELECTOR,'.years-list-view')
        least_year = from_year.find_elements(By.CSS_SELECTOR,'span')
    
    while(dates>int(least_year[8].text)):
        from_year.find_element(By.XPATH,'//*[@id="{}"]/angular2-date-picker/div/div[2]/div[5]/div[2]'.format(from_to)).click()
        from_year = driver.find_element(By.CSS_SELECTOR,'.years-list-view')
        least_year = from_year.find_elements(By.CSS_SELECTOR,'span')

    yr = dates-int(least_year[0].text)
    least_year[yr].click()
    if(bit==0):
        month = driver.find_element(By.CSS_SELECTOR,'.month-year')
        while(month.text!='January'):
            driver.find_element(By.XPATH,'//*[@id="{}"]/angular2-date-picker/div/div[2]/div[2]/i[1]'.format(from_to)).click()
            month = driver.find_element(By.CSS_SELECTOR,'.month-year')
    else:
        month = driver.find_element(By.XPATH,'//*[@id="date2"]/angular2-date-picker/div/div[2]/div[2]/div')
        while(month.text!='December'):
            driver.find_element(By.XPATH,'//*[@id="{}"]/angular2-date-picker/div/div[2]/div[2]/i[2]'.format(from_to)).click()
            month = driver.find_element(By.XPATH,'//*[@id="date2"]/angular2-date-picker/div/div[2]/div[2]/div')

    
    driver.find_element(By.XPATH,'//*[@id="{}"]/angular2-date-picker/div/div[2]/table[2]/tbody/tr[{}]/td[{}]'.format(from_to,r,c)).click()

def s_c_s(n):
    driver.find_elements(By.CLASS_NAME,'toggle')[n].click()

given_state = ["Punjab"] #input().split()
given_state.sort()
s_ind = 0
given_city = ["Amritsar","Ludhiana","Khanna"] #input().split()
given_city.sort()
not_visited =[]
c_ind = 0
given_parameters = ['PM2.5','NOx','RH','WS','WD','BP','SP','AT','Temp']
from_date = 2019
to_date = 2019
options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=r"C:\Users\Sourav\Downloads\chromedriver.exe",chrome_options=options)

url ="https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data"

driver.get(url)
cnt = 1
b = True
while(b):
    cnt+=1
    try:
        s_c_s(0)
        b = False
    except:
        if(cnt%10==0):
            driver.refresh()
        time.sleep(1)
states = driver.find_element(By.CSS_SELECTOR,'.options')
state_count = len(states.find_elements(By.CSS_SELECTOR,'li'))
for i in range(state_count):
    state = states.find_elements(By.CSS_SELECTOR,'li')[i]
    if(s_ind>=len(given_state)):
        break   
    if(state.text==given_state[s_ind]):
        state.click()
        time.sleep(2)
        s_ind +=1
        s_c_s(1)
        cities = driver.find_element(By.CSS_SELECTOR,'.options')
        city_count = len(cities.find_elements(By.CSS_SELECTOR,'li'))
        for j in range(city_count):
            city = cities.find_elements(By.CSS_SELECTOR,'li')[j]
            if(c_ind>=len(given_city)):
                break
            if(city.text==given_city[c_ind]):
                city.click()
                time.sleep(2)
                s_c_s(2)
                stations = driver.find_element(By.CSS_SELECTOR,'.options')
                station_count = len(stations.find_elements(By.CSS_SELECTOR,'li'))
                k = 0
                while(k<station_count):
                    station = stations.find_elements(By.CSS_SELECTOR,'li')[k]
                    station.click()
                    time.sleep(2)
                    driver.find_element(By.XPATH,"//*[text()='Select Parameter']").click()
                    for param in given_parameters:
                        try:
                            driver.find_element(By.XPATH,"//*[text()='"+ param +"']").click()
                        except:
                            print("Error")
                    s_c_s(3)
                    format = driver.find_element(By.CSS_SELECTOR,'.options')
                    format.find_elements(By.CSS_SELECTOR,'li')[0].click()
                    s_c_s(4)
                    criteria = driver.find_element(By.CSS_SELECTOR,'.options')
                    criteria.find_elements(By.CSS_SELECTOR,'li')[1].click()
                    dN = calendar.weekday(from_date, 1, 1)
                    select_date(from_date,0,"date",dN)
                    dN = calendar.weekday(to_date, 12, 31)
                    select_date(to_date,1,"date2",dN)
                    driver.find_element(By.XPATH,'/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data/div/div/div[5]/button').click()
                    b = True
                    cnt1 = 0
                    while(b):
                        cnt1+=1
                        try:
                            driver.find_element(By.XPATH,'/html/body/app-root/app-caaqm-dashboard/div[1]/div/main/section/app-caaqm-view-data-report/div[2]/div[1]/div[2]/div/div/a[2]/i').click()
                            b = False
                        except:
                            # not_visited.append(station.text)
                            # print("Not visisted",station.text)
                            if(cnt1%10==0):
                                driver.refresh()
                            time.sleep(1)
                    time.sleep(2)
                    driver.back()
                    b = True
                    cnt1 = 0
                    while(b):
                        cnt1+=1
                        try:
                            s_c_s(0)
                            b = False
                        except:
                            if(cnt1%10==0):
                                driver.refresh()
                            time.sleep(1)
                    states = driver.find_element(By.CSS_SELECTOR,'.options')
                    states.find_elements(By.CSS_SELECTOR,'li')[i].click()
                    time.sleep(2)
                    s_c_s(1)
                    cities = driver.find_element(By.CSS_SELECTOR,'.options')
                    if(station_count>(k+1)):
                        cities.find_elements(By.CSS_SELECTOR,'li')[j].click()
                        k+=1
                    else:
                        c_ind+=1
                        if(c_ind>=len(given_city)):
                            break
                        k = 0
                        for ji in range(city_count):
                            city = cities.find_elements(By.CSS_SELECTOR,'li')[ji]
                            print(city.text)
                            if(city.text==given_city[c_ind]):
                                city.click()
                                break
                    time.sleep(2)
                    s_c_s(2)
                    stations = driver.find_element(By.CSS_SELECTOR,'.options')
                    station_count = len(stations.find_elements(By.CSS_SELECTOR,'li'))