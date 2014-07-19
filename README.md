WhosWho
==========
A simple python library for checking if two names describe the same person.

Usage
----------

### Name Matching ###

In order to test two names, simply pass them in as strings or unicode.
```python
>>> from whoswho import who
>>> who.match('Liebowitz, R.', u'Mr. Robert Evan Liebowitz')
True
>>> who.match('Robert Liebowitz, Jr.', 'Robert Liebowitz, Sr.')
False
```

It is possible to adjust the strictness with which names are checked
```python
>>> who.match('R Liebowitz', 'Robert Liebowitz')
True
>>> who.match('R Liebowitz', 'Robert Liebowitz', 'strict')
False
```


### Fuzzy Matching ###

WhosWho can also produce a ratio based on the percent match of two names.
```python
>>> who.ratio('Robert Leibowitz', 'Robert Liebowitz')
93
>>> who.ratio('E. Robert Lebovich', 'Robert E. Liebowitz')
29
```