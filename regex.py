import re

code = '''
import re

code = 'import re'

x = len(re.findall('re', code))

# Frequency of 're' in code
print(str(x))
'''

x = len(re.findall('re', code))

# Frequency of 're' in code
print(str(x)) 


character_set = '''
	The best way to describe a character set is, unsurpris-
	ingly, as a set of characters.
'''

# print(re.findall('[de]', character_set)) 
# # This OR relation between the characters is represented by the square brackets around them ([])
# print(re.findall('de', character_set))

# print(re.findall('[a-eA-E0-4]', 'hello WORLD 42!')) 
# # so both start and stop symbols are included in the range

# print(re.findall('[^a-e]+', 'hello world'))


def special_name(s):
	return True if re.match('j[a-z]+n', s) else False

# print(special_name('chris'))
# print(special_name('johanna'))
# print(special_name('joan'))
# print(special_name('j00n'))

def special_unname(s):
	return True if re.match('j[^a-z]+n', s) else False
	
# print(special_unname('chris'))
# print(special_unname('johanna'))
# print(special_unname('joan'))
# print(special_unname('j00n'))

text = 'Python is superior to Python'
m = re.match('Py...n', text)
# print(m)
# print(m.span(), m.span()[0], m.span()[1])
# print(text[m.start():m.end()])
# print(re.findall('Py...n', text))


# text = 'More with less'
# print(re.match('More', text))
# print(re.fullmatch('More', text))
# print(re.fullmatch('More(.|\s)*', text))
# print(re.fullmatch('(.|\n)*less', text))
# print(re.match('(.|\n)*w[a-z]+h', text))

# print(re.match('(.|\n)*w..h', text))
# print(re.match('(.|\n)*w...h', text))


# text = 'Python. Is. Great. Period.'
# print(re.findall('[st]\.', text)) # to match the period character
# print(re.findall('[st].', text))

text = 'Speedy Gonzalez'
matches = re.findall('.', text)
result = len(matches) == len(text)
print(result)

matches = re.findall('..', text)
print(matches, len(matches))


famous_tweet = '''
I'm going give someone random who retweets this
tweet $10,000 because it's my birthday and I feel
like being nice (you have to be following me so
I can dm you the code if you win)
@MrBeastYT
#Twitter
'''
user = re.findall('@.*', famous_tweet)
# print(user[0])


print(re.findall('\wwe+', famous_tweet) == re.findall('[a-z]we+', famous_tweet))
print(re.findall('[0-9]+', famous_tweet) == re.findall('\d+', famous_tweet))

import re
website = '''
<!doctype html>
	<html>
		<head>
			<meta charset="utf-8">
		</head>
		<body>
			hello world
		</body>
	</html>
'''
print(len(re.findall('<.+>', website)))


fruits = [
	"apple",
	"banana",
	"orange",
	"kiwi"
]
lx = lambda x: re.match(".?a", x)
result = list(filter(lx, fruits))
# print(result, len(result))


s = 'xyyy'
# print(re.findall('xy?', s)[0])
# print(re.findall('xy*', s)[0])
# print(re.findall('xy+', s)[0])


matches = re.findall('finxter+?r', 'finxterrrr')
print(matches[0][:-1])


regex = "e."
string = "Spiderman"
result = re.split(regex, string)
print(result[1])


text = 'C++ is the best language. C++ rocks!'
print(re.sub('C\+\+', 'Python', text))


texts = ["I'm not happy.", "I don't want to dance.", "I don't love ice cream."]
pattern = re.compile("not |don't ")
print(pattern.sub('', texts[0]))
print(pattern.sub('', texts[1]))
print(pattern.sub('', texts[2]))