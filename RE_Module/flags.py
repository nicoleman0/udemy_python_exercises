# Without Verbose Flag...
# pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')
import re

pattern = re.compile(r"""
	^([a-z0-9_\.-]+)	#first part of email	
	@					#single @ sign
	([0-9a-z\.-]+)		#email provider
	\.					#single period
	([a-z\.]{2,6})$		#com, org, net, etc.
""", re.X | re.I)  # re.X = Verbose Flag, re.I = Ignore Case Flag


match = pattern.search("ThomaS123@Yahoo.com")

if match:
    print(match.group())
    print(match.groups())
else:
    print("No match found")
