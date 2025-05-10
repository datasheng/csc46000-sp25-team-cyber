from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

#website for all 10-K and 10-Q : https://www.sec.gov/edgar/browse/?CIK=320193&owner=exclude

#We can't access the page directly because it is not allowing us. It is an interactive page and using javascript in real time
#So, we will be using selenium to make an active chrome page open to access the data and then scraping the data.
#Remember to install pandas, chromedriver, BeautifulSoup, and selenium.

#we ae going to create a function that will allow us to put a url, and extract the data. We can avoid repetition.

def extract_revenue(url,low,high,look):
    options=Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    driver= webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(0.25)
    soc=driver.page_source
    driver.quit()
    
    soup1=BeautifulSoup(soc,"html.parser")
    info=[]
    for saved in soup1.find_all(look):
        Era=saved.get_text(strip=True)
        Era=Era.replace('\t',"")
        Era=Era.replace(',',"")
        if Era.isdigit() and int(Era) > low and int(Era) < high:
            info.append(Era)
    return info

'''

Let's make a function to make it easier for extracting the Q4
'''
def get_quarters(year1,year2,Revenue,i,j):
    year1Q4=int(Revenue[i]) - (int(year1[0])+int(year1[1])+int(year1[2]))
    year2Q4=int(Revenue[j])-(int(year2[0])+int(year2[1])+int(year2[2]))
    QFours= [year1Q4,year2Q4]
    return QFours


'''
The Following code is used to extract the apple revenue of iphones from the government website
Reminder: They will be static html pages of the original html page.

To ensure that the latest net sales/revenue is used, we will go down by year for the 10-k.
'''

Years=["2024","2023","2022","2021","2020","2019","2018","2017","2016","2015","2014"]
Revenue=[]   


#from 2024-2022
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019324000123/aapl-20240928.htm",200000,300000,"span")
for i in range((len(Space)-5), (len(Space)-2)):
    Revenue.append(Space[i])

#from 2021-2019
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019321000105/aapl-20210925.htm",137000,191990,"span")
for i in range(1,4):
    Revenue.append(Space[i])


# from 2019-2017
Space= extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019319000119/a10-k20199282019.htm",139000,165000,"span")
for i in range(1,3):
    Revenue.append(Space[i])


#from 2016-2014
Space= extract_revenue("https://www.sec.gov/Archives/edgar/data/320193/000162828016020309/a201610-k9242016.htm",101000,155100,"font")
for i in range(8,11):
    Revenue.append(Space[i])

print("Revenue: ",Revenue,'\n'+"Years: ",Years)

'''
We will be taking the quarterly revenue from 2024-2014.
The fourth quarter will be extracting by subtracting the yearly revenue from the sum of the first three quarters.

'''
sum=0
year1=[]
year2=[]
Quarters=[]
#2024-2023
#Q3
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019324000081/aapl-20240629.htm",39200,39700,"ix:nonfraction")
year1.append(Space[1])
year2.append(Space[2])
#Q2

Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019324000069/aapl-20240330.htm",45900,51500,"ix:nonfraction")

year1.append(Space[6])
year2.append(Space[7])

#Q1
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019324000006/aapl-20231230.htm",65700,69710,"ix:nonfraction")

year1.append(Space[3])
year2.append(Space[4])
print(year1)
print(year2)
#Q4
'''
Just some old code where I created my Q4
#The Q4 for the two years.
year1Q4=int(Revenue[0]) - (int(year1[0])+int(year1[1])+int(year1[2]))
year2Q4=int(Revenue[1])-(int(year2[0])+int(year2[1])+int(year2[2]))
#Now reverse the years because they are going from Q3-Q1
year1.reverse()
year2.reverse()
#add Q4 to the list
year1.append(year1Q4)
year2.append(year2Q4)
#Let's check
print(year1)
print(year2)
'''
All4=get_quarters(year1,year2,Revenue,0,1)


year1.reverse()
year2.reverse()
year1.append(All4[0])
year2.append(All4[1])

Quarters.extend(year1)
Quarters.extend(year2)
print(Quarters)
year1=[]
year2=[]

#2022-2021
#Q3
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019322000070/aapl-20220625.htm",39500,40700,"ix:nonfraction")

year1.append(Space[2])
year2.append(Space[3])
#Q2
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019322000059/aapl-20220326.htm",47900,50600,"ix:nonfraction")

year1.append(Space[3])
year2.append(Space[4])
#Q1
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019322000007/aapl-20211225.htm",65500,71700,"ix:nonfraction")

year1.append(Space[3])
year2.append(Space[4])
#Q4
print(year1)
print(year2)

All4=get_quarters(year1,year2,Revenue,2,3)


year1.reverse()
year2.reverse()
year1.append(All4[0])
year2.append(All4[1])

Quarters.extend(year1)
Quarters.extend(year2)
print(Quarters)
year1=[]
year2=[]
#2020-2019
#Q3
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019320000062/aapl-20200627.htm",25900,26500,"ix:nonfraction")

year1.append(Space[2])
year2.append(Space[3])
#Q2
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019320000052/a10-qq220203282020.htm",28900,31100,"ix:nonfraction")

year1.append(Space[0])
year2.append(Space[1])
#Q1
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/0000320193/000032019320000010/a10-qq1202012282019.htm",51900,56000,"ix:nonfraction")

year1.append(Space[3])
year2.append(Space[4])
#Q4
All4=get_quarters(year1,year2,Revenue,4,5)


year1.reverse()
year2.reverse()
year1.append(All4[0])
year2.append(All4[1])

Quarters.extend(year1)
Quarters.extend(year2)
print(Quarters)
year1=[]
year2=[]
#2018-2017
#Q3
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/320193/000032019318000100/a10-qq320186302018.htm",24840,29920,"font")

year1.append(Space[8])
year2.append(Space[9])
#Q2
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/320193/000032019318000070/a10-qq220183312018.htm",33200,38100,"font")

year1.append(Space[21])
year2.append(Space[22])
#Q1
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/320193/000032019318000007/a10-qq1201812302017.htm",54300,61600,"font")

year1.append(Space[7])
year2.append(Space[8])
#Q4
All4=get_quarters(year1,year2,Revenue,6,7)


year1.reverse()
year2.reverse()
year1.append(All4[0])
year2.append(All4[1])

Quarters.extend(year1)
Quarters.extend(year2)
print(Quarters)
year1=[]
year2=[]

#2016-2015
#Q3
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/320193/000162828016017809/a10-qq320166252016.htm",24000,31400,"font")

year1.append(Space[20])
year2.append(Space[21])
#Q2
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/320193/000119312516559625/d165350d10q.htm",32800,40300,"td")

year1.append(Space[24])
year2.append(Space[25])
#Q1
Space=extract_revenue("https://www.sec.gov/Archives/edgar/data/320193/000119312516439878/d66145d10q.htm",51100,51700,"td")

year1.append(Space[1])
year2.append(Space[2])
#Q4
All4=get_quarters(year1,year2,Revenue,8,9)


year1.reverse()
year2.reverse()
year1.append(All4[0])
year2.append(All4[1])

Quarters.extend(year1)
Quarters.extend(year2)
print(Quarters)
year1=[]
year2=[]

#2014
thisQuarter=['32498','26064','19751']
fourth= int(Revenue[10]) - (32498 + 26064 + 19751)
thisQuarter.append(fourth)
Quarters.extend(thisQuarter)
print(Quarters)


#Now, we have the Revenue of each year, and the Revenue each quarter. Both are in the millions range.

'''
Time to make it into a csv for the database
'''
Names=[]
values=[]
ind=0
qart=Quarters
for i in Years:
    Names.append(i)
    values.append(Revenue[ind])
    for q in range(4,0,-1):
        Names.append(f"{i} Q{q}")
        values.append(qart.pop(0))
    ind=ind+1
    
df= pd.DataFrame({
    "Timeline": Names,
    "Revenue":values,
})

df.set_index("Timeline",inplace=True)
df.to_csv("apple_Revenue.csv")
    

