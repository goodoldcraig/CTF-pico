import sys
import subprocess
import session_cookie_manage

session = ".eJwlz0FqAzEMQNG7eJ2FJFuylMsE2ZJoKbQwk6xK756BHuDB_7_tUUeeH-3-PF55a4_PaPcWBLacyRAZbMTMYt8IxCQmQy1wOQxIwlUiU2v"
"yRLVcHjQQq1fvLuSUkR2m9WS-iE6TzJkSc2PFhDBAF3BiThVdc6-B5u3W9nnU4_nzld9XD2rYZZJgS9japAG6kVCqmMKNdGzpdrnXmcf_BLe_NxZrPg0."
"Dtc20g.JHifiX9Dy78rCNoqpq_dcZUM1eE"

cookie = session_cookie_manage('decode', '-c', session, '-s', 'a155eb4e1743baef085ff6ecfed943f2')
print cookie
