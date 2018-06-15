# coding=utf-8

import urllib2
import json
import time

now = int(time.time())
url = "http://10.99.7.1:18181/actuator/metrics"
#url = "http://132.122.232.243:18181/actuator/metrics"
req = urllib2.Request(url=url)
data = urllib2.urlopen(req).read()
jo = json.loads(data)
jvm_mem_free = {
    "endpoint": "10.99.7.1",
    "metric": "jvm.mem.free",
    "value": jo["mem.free"],
    "counterType": "GAUGE",
    "step": 10,
    "timestamp": now
    }

print(json.dumps(jvm_mem_free))