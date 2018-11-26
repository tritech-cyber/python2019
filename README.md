<pre>
Python Lists, Tuples, Dictionaries and Sets
https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set
<hr />
<tt>
When you want an unordered collection of unique elements, use a set. (For example, when you want the set of all the words used in a document).

When you want to collect an immutable ordered list of elements, use a tuple. (For example, when you want a (name, phone_number) pair that you wish to use as an element in a set, you would need a tuple rather than a list since sets require elements be immutable).

When you want to collect a mutable ordered list of elements, use a list. (For example, when you want to append new phone numbers to a list: [number1, number2, ...]).

When you want a mapping from keys to values, use a dict. (For example, when you want a telephone book which maps names to phone numbers: {'John Smith' : '555-1212'}). Note the keys in a dict are unordered. (If you iterate through a dict (telephone book), the keys (names) may show up in any order).
</tt>

</pre>

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
