Whos Who
==========
A simple python library for checking if two names describe the same person.

Usage
----------
In order to test two names, simply pass them in as strings or unicode.

```python
>>> from whoswho import who
>>> who.match('R Liebowitz', u'Mr. Robert Evan Liebowitz')
True
>>> who.match('Robert Liebowitz, Jr.', 'Robert Liebowitz, Sr.')
False
```