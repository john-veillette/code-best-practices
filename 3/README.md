
In this version of our analysis code, we've broken `util.py` up into submodules. Python will treat any folder as a module if it contains a file called `__init__.py`, just like it treats all `.py` files as modules. Any module within a module will be treated as a submodule.

So now, we have a module called `util` that contains a submodule called `ttests`, which contains our _t_-test functions. This is handy, even though we only have one submodule, because it allows us to add unit tests.

The unit tests are hiding in `util/tests/test_ttests.py`. If this folder is your working directory, and you have `pytest` installed (or first run `pip install pytest`), then you can run the unit tests by simply typing `pytest` into Terminal.

Why make unit tests, even if you're confident your code works?
1. As Gretchen Wieners once said, "you could be wrong."
2. If you ever break your code accidentally, your unit tests will notify you (assuming that you run them).

"Assuming that you run them" is a big assumption in practice, as we're all busy people. Luckily, [GitHub Actions](https://github.com/features/actions) allows you to configure your unit tests to run every time you push a new commit. For instance, [here](https://github.com/john-veillette/niseq/blob/6f172b2efa211c07b802285655d8d5bd0e014f38/.github/workflows/pytest.yml) is a config file from one of my repositories that tell GitHub to run my unit tests on Windows, Mac OS, and Ubuntu instances every time I make changes, and then generate a [Codecov](https://about.codecov.io/) report detailing which -- and how many -- lines of code in each module were actually used when running my unit tests. This is called a _continuous integration pipeline_, and software developers use them to make sure that nobody breaks core functionality of projects when they're adding features.

One last note: you may notice that Python is treating modules like `util` very similarly to how it treats packages. In fact, all you'd need to do to make `util` a `pip` installable package is add a `setup.py` file saying where to look for the module (the `util` folder) and a `requirement.txt` file saying what packages already need to be installed (in this case, `numpy` and `scipy` are sufficient). Then you can tell `pip` to install it directly from GitHub, or upload it to PyPI (where most `pip` packages live). _I bet you didn't see that one coming when you sat down for this tutorial. I tricked you._ See, making re-usable code is easy!
