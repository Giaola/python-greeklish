# Greeklish Converter
This Python library converts any given Greek string to Greeklish.

## Install
```sudo python setup.py install```

or

```sudo pip install -e git+https://github.com/bkbilly/python-greeklish.git#egg=python-greeklish```

## How to use it
```python
from greeklish.converter import Converter
myconverter = Converter(max_expansions=4, generate_greek_variants=False)
print myconverter.convert(u'μια φορά και έναν καιρό.')
```

## Credits
 * Forked from [Giaola](https://github.com/Giaola/python-greeklish).
 * Based on [Skroutz's Ruby Greeklish Converter](https://github.com/skroutz/greeklish).
