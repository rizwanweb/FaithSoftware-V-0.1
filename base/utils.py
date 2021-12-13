import datetime
from struct import error
import PyPDF2
import urllib.request
import io

#-----------------------------------------------#
#Setting up date
today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)
mydate = yesterday.strftime('%d-%m-%Y')

if today.today().weekday() == 6:
    yesterday = today - datetime.timedelta(days=2)
    mydate = yesterday.strftime('%d-%m-%Y')


if today.today().weekday() == 0:
    yesterday = today - datetime.timedelta(days=3)
    mydate = yesterday.strftime('%d-%m-%Y')



#-----------------------------------------------#

#Getting remote file
downloadurl = 'https://www.nbp.com.pk/RateSheetFiles/NBP-RateSheet-'+mydate+'.pdf'
#downloadurl = 'https://www.nbp.com.pk/RateSheetFiles/NBP-RateSheet-31-08-2021.pdf'


if downloadurl:

    
    req = urllib.request.Request(downloadurl, headers={'User-Agent' : "Magic Browser"})
    pdf_file = urllib.request.urlopen(req).read()
    if pdf_file:
        print("Connected to NBP ----Getting Todays Exchange Rate")
    else:
        print("Network Error.. Check Internet Connection")
    pdf_file_byte = io.BytesIO(pdf_file)
    sheet = PyPDF2.PdfFileReader(pdf_file_byte)

    text = sheet.getPage(0).extractText()
    def getUSD(string):
        li = list(string.split("\n"))
        usd = li[17]
        return usd
    usd = getUSD(text)
else:
    pass
