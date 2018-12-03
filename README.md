python 2018-2019 -181202
_____ vars.py
_____ types1.py (numbers)
_____ casting.py
_____ strings.py 
_____ operators.py
_____ binarystring.py
_____ dechexbin_loop.py
_____ example-ord.py
_____ list123.py
_____ nato-tuple.py
_____ dictionaries.py
_____ sets_1.py, sets_2.py, sets_3.py & sets_4.py
_____ if_and_or.py	
_____ ifcondition.py
		https://www.w3schools.com/python/python_strings.asp
_____ while_break.py
_____ for_loops.py

MATH
_____ convertkmmi.py	
_____ find_factors.py	
_____ math_outputs.txt	
_____ multiplication.py	
_____ quadratic.py


for x in range(0,11):
	print (x, x*x, x*x*x)

for x in range(0,11):
	print ('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))



Please read the Wiki. You need to be logged into to github.
# **Python Lists, Tuples, Dictionaries and Sets **
https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set

When you want an unordered collection of unique elements, use a set. (For example, when you want the set of all the words used in a document).

When you want to collect an immutable ordered list of elements, use a tuple. (For example, when you want a (name, phone_number) pair that you wish to use as an element in a set, you would need a tuple rather than a list since sets require elements be immutable).

When you want to collect a mutable ordered list of elements, use a list. (For example, when you want to append new phone numbers to a list: [number1, number2, ...]).

When you want a mapping from keys to values, use a dict. (For example, when you want a telephone book which maps names to phone numbers: {'John Smith' : '555-1212'}). Note the keys in a dict are unordered. (If you iterate through a dict (telephone book), the keys (names) may show up in any order).
References:
https://www.w3schools.com/python/python_sets.asp
https://www.programiz.com/python-programming/set
<pre>
git commands
Here are some git commands so you can pull python resources from this repo
* The following will set up a users for github
git config --global --list
user.user=icebowl
user.username=icebowl
user.email=???

git config --global user.user "username"
git config --global user.username "username"
git config --global user.email "?@?"
* The following will push files a repos
repo commands
git add --all
git commit -m "aa"
git push
</pre>
