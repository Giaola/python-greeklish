# Greeklish Converter
This Python library converts any given Greek string to Greeklish.

## How to use it
```
from greeklish.converter import Converter
asdf = Converter(max_expansions=4, generate_greek_variants=False)
print asdf.convert(u'μια φορά και έναν καιρό.')
```

## Credits
Greeklish converter based on [Skroutz's Ruby Greeklish Converter](https://github.com/skroutz/greeklish)
