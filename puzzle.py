import re

text = '''
	"Travelled" or "traveled".
	Well, its "travelled" in Britian
	and "traveled" in the US
'''
pattern_1 = 'traveled'
pattern_2 = 'travell?ed'

result_1 = re.findall(pattern_1, text, flags=re.IGNORECASE)
result_2 = re.findall(pattern_2, text, flags=re.IGNORECASE)

print(len(result_1))
print(len(result_2))