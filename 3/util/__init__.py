'''
Just having an empty `__init__.py` in `util` tells Python that `util` is
a module, and then all the other `.py` files in `util` will be treated
as submodules. So since we have a file `ttests.py` in this folder `util`,
we can import functions from `ttests.py` in our main script like
```
from util.ttests import ttest_1samp
```
But if we'd still like to be able to call
```
from util import ttest_1samp
```
then we can import those functions into this `__init__.py` file
as we do below. Then, Python will let you access those functions in your
main script without referencing the submodule explicitly.
'''
from .ttests import ttest_1samp, ttest_paired
