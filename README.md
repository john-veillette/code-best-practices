# Code organization workshop

In this repository, we work through progressively better ways to organize some analysis code. 

1. Starts by writing the code in a "one big script" manner, and ends by abstracting into clean, well-documented functions.
2. Moves the functions into a seperate utility module, which both cleans up your main script/notebook and facilitates re-using code between projects. 
3. Breaks up the utility module into submodules and adds a _unit test_ module; this is how you make sure your code works as intended (not just now, but after any changes in the future)!

## Some general things

### Environment files

You can see an example of an environment file in `environment.yml`. Environment files specify what packages need to be installed in your environment to run your code (and whether to install them using `pip` or `conda`). If you have [conda](https://docs.conda.io/en/latest/) installed (or [mamba](https://mamba.readthedocs.io/en/latest/installation.html), a faster version of conda), you can create an environment from the environment file by running
```
conda env create --file environment.yml
```
This will create an environment called "tutorial" (I specified that name in the `.yml` file -- it doesn't have to be that), which you can activate as follows.
```
conda activate tutorial
```
And then you can exit the environment using:
```
conda deactivate
```
This way, you can have a different, isolated environment for each project. _Please_ do this, or you'll start running into impossible-to-debug package version issues and your life will be chaos. 

An environment file like `environment.yml` specifies dependencies, and then conda finds package versions of those dependencies that play nicely with each other. However, it is best to share the exact package versions you used when you share code to make your project maximally reproducible. 

If you run
```
conda env export > manifest.yml
```
it will export your current environment configuration (with exact package versions) to a file called `manifest.yml`. It's best practice to share both the original and the final environment file with your project code. 

Conda can also manage R environments, though a bit worse -- I recommend using another solution like [groundhog](https://groundhogr.com/) if you only use R and still using conda if you use R and Python together in the same project. If you use MATLAB, package version control is hopeless and you might as well give up. (This is a little hyperbolic, but _only_ a little.)

## Style guides

Making your code pretty isn't just an exercise in vanity; poorly formatted code is hard to read. I didn't explicitly cover code style here (though Folder 1 starts out with some pretty poorly styled code). 

I highly recommend finding a style guide for your programming language ([here is one for Python](https://peps.python.org/pep-0008/)) and following it as closely as practical. 

Seriously, I know it sounds silly, but this is important. So important that a lot of open source projects will actually reject your (otherwise functioning) contribution just because it isn't styled correctly. Maintaining code is hard enough, and it's often easier to rewrite code from scratch than to parse someone else's incomprehensible spaghetti code. 

Remeber -- evey line of code is written just once, but read quite a few more times than that.
