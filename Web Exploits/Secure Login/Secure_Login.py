from pwn import *
import json

cookie = {}
cookie['password'] = 'test'
cookie['username'] = 'test'
cookie['admin'] = 0
json.dumps(cookie, sort_keys=True)
json.dumps(cookie, sort_keys=True).index('0')
print json.dumps(cookie, sort_keys=True).index('0')
c = '.eJwlz0FqAzEMQNG7eJ2FJFuylMsE2ZJoKbQwk6xK756BHuDB_7_tUUeeH-3-PF55a4_PaPcWBLacyRAZbMTMYt8IxCQmQy1wOQxIwlUiU2vyRLVcHjQQq1fvLuSUkR2m9WS-iE6TzJkSc2PFhDBAF3BiThVdc6-B5u3W9nnU4_nzld9XD2rYZZJgS9japAG6kVCqmMKNdGzpdrnXmcf_BLe_NxZrPg0.Dtc20g.JHifiX9Dy78rCNoqpq_dcZUM1eE'.decode('base64')

c = c[:10] + xor(c[10], '0', '1') + c[11:]

print c.encode('base64').replace('\n','')


