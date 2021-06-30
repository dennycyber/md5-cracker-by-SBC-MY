import hashlib
from termcolor import colored


flag = 0

print()
print()
print(colored(""" 
░██████╗██████╗░░█████╗░  ███╗░░░███╗██╗░░░██╗
██╔════╝██╔══██╗██╔══██╗  ████╗░████║╚██╗░██╔╝
╚█████╗░██████╦╝██║░░╚═╝  ██╔████╔██║░╚████╔╝░
░╚═══██╗██╔══██╗██║░░██╗  ██║╚██╔╝██║░░╚██╔╝░░
██████╔╝██████╦╝╚█████╔╝  ██║░╚═╝░██║░░░██║░░░
╚═════╝░╚═════╝░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░ """, 'magenta'))
print()
print()

hash_pass = input("masukkan md5 hash: ")

wordlist = input("masukkan wordlist: ")

try:
	pass_wordlist = open (wordlist, "r")
except:
	print("tiada file yang dijumpai")
	quit()

for word in pass_wordlist:
	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()
	
	if digest == hash_pass:
		print("Password berjaya di Crack")
		print("Password adalah " + word)
		flag = 1
		break
if flag == 0:
	print("Password tidak dijumpai, sila cuba wordlist lain")