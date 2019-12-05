import http
import webbrowser
import urllib.request
import urllib.response
import webbrowser
import os
import calendar
print ("NOTE:REQUERMENTS:GOOGLE CHROME,PYTHON 3,INTERNET MIN500KB/S")
print("are you 18+")
print ("enter your age:")
ver=int(input ("input your birthday date:"))
ver1=int(input ("input your birthday month:"))
ver2=int(input ("input your birthday year:"))
ver3=int(input ("input current date:"))
ver4=int(input ("input current month:"))
ver5=int(input ("input current year:"))
ver6=ver5 - ver2

if ver6>=18:
	print ("         #### ################# ## ####################")
	print ("         ##  ####  ########### #### ######################")
	print ("         ##  ######  ######## ##  ## #####################")
	print ("         ##  ####  ######### ##    ## ####################")
	print ("         ##  ##  ########## ___________ ###################")
	print ("         ##  ####  ####### ##        ## ##################")
	print ("         ##  #######  ### ##          ## #################")
	print('first cracking script ..created by rahul')

	#here you enter your tergated profile username/user numaric id
	var =  (input("input the numaric id:"))
	#print vunarable link

	#starting web browser
	chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	webbrowser.get(chromedir).open("https://graph.facebook.com/"+ var + "/picture?width=800"  )
	input ("press enter to exit")
	os.system("pause")
else:
	print("you cannot use this tool")
	os.system("pause")
