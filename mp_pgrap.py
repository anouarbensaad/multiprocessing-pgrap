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
      print("phone: %s data: " % (phone,str(parse_info(data))}))
      output_data = {
          "name": parse_info(data)["name"],
          "address": parse_info(data)["address"],
          "phone": phone
      }
      with open('data/details.json', 'a', encoding='utf-8') as f:
          json.dump(output_data, f, ensure_ascii=False, indent=4)
    else:
      print(f"phone: {phone} data: None")

start = time.perf_counter()

#multiprocessing_executions blocks.
# process one to run filter loop from prefix : 100000000 to 200000000
processus1 = mp.Process(target=loop_filter, args=[200000000,300000000])
processus2 = mp.Process(target=loop_filter, args=[200000000,300050000])
processus3 = mp.Process(target=loop_filter, args=[200050000,300100000])
processus4 = mp.Process(target=loop_filter, args=[200100000,300150000])
processus5 = mp.Process(target=loop_filter, args=[200150000,300200000])
processus6 = mp.Process(target=loop_filter, args=[200200000,300250000])
processus7 = mp.Process(target=loop_filter, args=[200250000,300300000])
processus8 = mp.Process(target=loop_filter, args=[200300000,300350000])
processus9 = mp.Process(target=loop_filter, args=[200350000,300400000])
processus10 = mp.Process(target=loop_filter, args=[200400000,301000000])
processus11 = mp.Process(target=loop_filter, args=[201000000,310000000])
processus12 = mp.Process(target=loop_filter, args=[210000000,300000000])

# start process.
processus1.start()
processus2.start()
processus3.start()
processus4.start()
processus5.start()
processus6.start()
processus7.start()
processus8.start()
processus9.start()
processus10.start()
processus11.start()
processus12.start()

# join process.
processus1.join()
processus2.join()
processus3.join()
processus4.join()
processus5.join()
processus6.join()
processus7.join()
processus8.join()
processus9.join()
processus10.join()
processus11.join()
processus12.join()

finish = time.perf_counter()

print(f"time elapsed {round(finish-start,2)}")
