# Code organization workshop

In this repository, we work through progressively better ways to organize some analysis code. 

1. Starts by writing the code in a "one big script" manner, and ends by abstracting into clean, well-documented functions.
2. Moves the functions into a seperate utility module, which both cleans up your main script/notebook and facilitates re-using code between projects. 
3. Breaks up the utility module into submodules and adds a _unit test_ module; this is how you make sure your code works as intended (not just now, but after any changes in the future)!
