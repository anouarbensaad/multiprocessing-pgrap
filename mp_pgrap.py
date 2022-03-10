import requests
import re
import multiprocessing as mp
import time


# HTTP request header.
headers={
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
}

"""
using regular expression get name and address of user from phone.
:data : response from url.
"""
def parse_info(data):
  regxp=r'<div class="col-md-8 plusinfoCol"><div class="row row-abonne"><div class="col-md-6"><h1>(.+)</h1><h2>(.+)</h2>'
  recompiled=re.compile(regxp)
  matched=re.search(recompiled,data)
  try:
    info = {
    "name": matched.group(1),
    "address": matched.group(2).replace("<br>"," - ")
    }
    return info
  except Exception as error:
    return None

"""
function to get phone number from loop and make request to the url.
:phone : the phone number
"""
def phone_requester(phone):
  URL=f"https://www.pages-annuaire.net/annuaire-inverse/recherche?number=0{phone}"
  response = requests.get(URL,headers=headers)
  return response.text


"""
This function to make a loop filter from the first index to the index.
:prefix : the start of loop
:suffix : the end of loop
"""
def loop_filter(prefix,suffix):
  for phone in range(prefix,suffix,1):
    data = phone_requester(phone)
    if parse_info(data) is not None:
      print(f"phone: {phone} data: {parse_info(data)}")
    else:
      print(f"phone: {phone} data: None")


start = time.perf_counter()

#multiprocessing_executions blocks.
# process one to run filter loop from prefix : 100000000 to 200000000
processus1 = mp.Process(target=loop_filter, args=[100000000,200000000])

# process one to run filter loop from prefix : 300000000 to 400000000
processus2 = mp.Process(target=loop_filter, args=[300000000,400000000])

# process one to run filter loop from prefix : 500000000 to 600000000
processus3 = mp.Process(target=loop_filter, args=[500000000,600000000])

# process one to run filter loop from prefix : 700000000 to 800000000
processus4 = mp.Process(target=loop_filter, args=[700000000,800000000])

# process one to run filter loop from prefix : 800000000 to 900000000
processus5 = mp.Process(target=loop_filter, args=[800000000,900000000])

# process one to run filter loop from prefix : 900000000 to 999999999
processus6 = mp.Process(target=loop_filter, args=[900000000,999999999])

# start all process.
processus1.start()
processus2.start()
processus3.start()
processus4.start()
processus5.start()
processus6.start()

# join process.
processus1.join()
processus2.join()
processus3.join()
processus4.join()
processus5.join()
processus6.join()

finish = time.perf_counter()
print(f"time elapsed {round(finish-start,2)}")