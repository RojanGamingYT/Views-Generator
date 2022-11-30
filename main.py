import requests, time, threading
from fake_useragent import UserAgent

num_of_views = int(input('Enter the amount of views you would like to generate: '))
link = input('Enter Link: ')

start_time = time.time()
ua = UserAgent()
agent = ua.random

headers = {
    "User-Agent":
    agent
}

def view_item():
        s = requests.Session()
        visiting_url = s.get(link, headers=headers)

for i in range(num_of_views):
    t = threading.Thread(target=view_item)
    t.start()
    print ('Item Viewed Successfully {}/{}'.format(i,num_of_views))
    i += 1

print ('{} Views Successfully Completed in {} seconds!'.format(num_of_views, time.time()-start_time))
