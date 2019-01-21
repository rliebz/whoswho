WhosWho
==========
[![PyPI version](https://badge.fury.io/py/whoswho.svg)](https://badge.fury.io/py/whoswho)
[![Build Status](https://travis-ci.org/rliebz/whoswho.svg?branch=master)](https://travis-ci.org/rliebz/whoswho)

A simple python library for determining whether two names describe the same 
person.


Installation
----------

```bash
$ pip install whoswho
```
Requires Python >= 2.6 or >= 3.3 with pip.


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


License
-------

MIT licensed. See the bundled 
[LICENSE](https://github.com/rliebz/whoswho/blob/master/LICENSE) 
file for more details.
