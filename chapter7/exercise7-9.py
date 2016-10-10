import re
# exercise 7

mammoth = '''We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
'''

# exercise 8

words = r'\bc\w*'
re.findall(words, mammoth)                                          # output: ['cheese', 'city', 'cheese', 'cheek', 'could', 'cheese', 'cast', 'crush']

# exercise 9
words = r'\bc...\b'
re.findall(words, mammoth)                                          # output: ['chee', 'city', 'chee', 'chee', 'coul', 'chee', 'cast', 'crus']
