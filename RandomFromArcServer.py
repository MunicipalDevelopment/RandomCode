import requests,json, random
url="http://gisdmd.cabq.gov/dmdview/rest/services/Traffic/SignalizedIntersections/MapServer/0/query?where=1=1&outFields=*&f=json"
r=requests.get(url).json()
oids=[]
for x in r['features']:
    oids.append(x['attributes']['OBJECTID'])
rand = random.sample(oids,12)
sample = ','.join(str(x) for x in rand)

newurl='http://gisdmd.cabq.gov/dmdview/rest/services/Traffic/SignalizedIntersections/MapServer/0/query?where=OBJECTID in ('+sample+')&outFields=*&f=json'
newr=requests.get(newurl).json()
newr
#now you have all the infor in your random sample.
