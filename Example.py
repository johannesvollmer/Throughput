from Throughput_public import *
import json

print ('permanent suggestions:')
try:
    data = json.load(open("throughput-data-all.json"))
except Exception as e:
    raise "can not find the json file"

t = Throughput(data)
print ('throughput: 	%.3f' % t.throughput)
print ('WPM:	%.3f' % (t.wpm)) 
print ('uncorrected error rate:	%.3f' % (t.uncorrectedErrRate) )


print ('\n\nno suggestions:')
try:
    data2 = json.load(open("throughput-data-none.json"))
except Exception as e:
    raise "can not find the json file"


t2 = Throughput(data2)
print ('throughput: 	%.3f' % t2.throughput)
print ('WPM:	%.3f' % (t2.wpm)) 
print ('uncorrected error rate:	%.3f' % (t2.uncorrectedErrRate) )

