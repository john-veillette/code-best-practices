
In this folder, we've moved our _t_-test functions out of the main script and into a file called `util.py` (it doesn't have to be called this), which Python will treat as a _module_ when it's in your working directory.

Three advantages of this:
1. It cleans up our main script, so code in the main script is at the level of detail/abstraction you'd care about when writing a methods section.
2. If you want to use these functions in a later project, you can just copy and paste `util.py` into the new project, instead of fishing it out of the project-specific code in your main script.
3. Since we've described our functions so nicely in their docstrings, we can use tools like [Sphinx](https://www.sphinx-doc.org/en/master/tutorial/index.html) to automatically generate documentation for our code. For instance, for one of my projects, [this config file](https://github.com/john-veillette/niseq/blob/main/docs/index.rst) is all I needed to write to generate [this documentation](https://niseq.readthedocs.io/en/latest/). As you build out your personal library of code that you re-use, project after project, generating this kind of documentation for your frequently used routines is extremely helpful.
