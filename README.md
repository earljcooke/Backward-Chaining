# Assignment 2
## Running
To run the backward chaining algorithm ensure that you have one command line argument that is the input file with a set of the rules.
> python3 app.py input.txt

The program will then ask for you to input a query and then tell you whether or not it is a result of logical consequence of the set of rules. After the query is done it will ask for another where it will do the same thing.

## Exiting
To exit the program simply type `exit` when you are asked to type a query.

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
If there is a rule such as `p ∧ q ⇒ p` and the fact `q` then algorithm will end up going into a cycle causing a stack overflow if you try to give the query `p`. 

Another example where a cycle can occur is if you give the rules `p ⇒ q`, `q ⇒ p` and give the program the queries `q` or `p` because the algorithm will continuously be looking for `p` then `q` and `q` then `p`.