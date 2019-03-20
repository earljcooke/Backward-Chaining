# Assignment 2
## Running
To run the backward chaining algorithm, ensure that you have one command line argument.
That argument should be an input file. In the example below, it is 'input.txt' 
In your argument/input file, there should be a list of rules for your program to run.

Commandline: 
    >>> python3 app.py input.txt

The program will then ask for you to input a query.
It will then tell you whether or not it is a result of logical consequence of the set of rules. 
After the query is done it will ask for another query to perform the same task. 

## Exiting the program
To exit the program, type `exit` instead of another query. 

e.g. 
```
Please enter an atom.
exit
```

## Overview
The basic algorithm for performing backward chaining is given below. Where solve is initially called with the query as the parameter.
```
solve(goals):
    if goals = () then return(succeed)
    let a := f irst(goals)
    let goals := rest(goals)
    for each r ∈ R where head(r) = a
        if solve(append(body(r), goals)) = succeed
        return(succeed)
    return(fail)
```

## Limitations
If there is a rule such as `p ∧ q ⇒ p` and you also have the fact `q` , then algorithm will end up going into a infinite loop.  This will cause a stack overflow if you try to give the query `p`. 

Another example where a cycle can occur is if you give the rules `p ⇒ q`, `q ⇒ p` and give the program the queries `q` or `p` because the algorithm will continuously be looking for `p` then `q` and `q` then `p`.
