import httplib

conn = httplib.HTTPConnection('svc.lifemapper.org/services/sdm/experiments/json?afterTime=2015-09-03&beforeTime=2016-09-04&status=6212&perPage=2147483647')
conn.request("GET", "/")
res = conn.getresponse()
print res.status