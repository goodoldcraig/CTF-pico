import json
from pwn import *

def RemoveDuplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


r = remote('2018shell.picoctf.com', 54782)

print(r.recv());

with open("incidents.json") as json_data:
    data = json.load(json_data)


def GetCommonSrc(json):
    ips = []
    for element in json["tickets"]:
        ips.append(element["src_ip"])
    common = max(set(ips), key=ips.count)
    return common


r.sendline(GetCommonSrc(data))

response = r.recv()
print(response)
ip = str(re.findall(r'[0-9]+(?:\.[0-9]+){3}', response))


def GetCountUniqueDestFromSrc(json, ip):
    uniqueips = []
    for element in json["tickets"]:
        if str(element["src_ip"]) in ip and element["dst_ip"] not in uniqueips:
            uniqueips.append(element["dst_ip"])
    return len(uniqueips)


r.sendline(str(GetCountUniqueDestFromSrc(data, ip)))
print(r.recv())


def GetAverageNumOfDstIps(json):
    hashes = []
    uniqueIps = []
    for ticket in json["tickets"]:
        hashes.append(ticket["file_hash"])
    hashes = RemoveDuplicates(hashes)
    for hash in hashes:
        for ticket in json["tickets"]:
            if ticket["file_hash"] == hash and ticket["dst_ip"] not in uniqueIps:
                uniqueIps.append(ticket["dst_ip"])
    return '{0:.2f}'.format(float(len(hashes)) / float(len(uniqueIps)))


r.sendline(str(GetAverageNumOfDstIps(data)))
print(r.recv())

