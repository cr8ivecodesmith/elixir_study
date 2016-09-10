Functions
=========

Functions are the building blocks of a functional programming language.

There are several ways functions are declared in Elixir. The simplest one is
writing `anonymous functions`.


## Anonymous functions

We can assign functions to variables and invoke it with the `.` character:

```
iex(56)> is_even = fn(x) -> rem(x, 2) == 0 end 
#Function<6.50752066/1 in :erl_eval.expr/5>
iex(57)> is_even.(5)
false
iex(58)> is_even.(24)
true
```


## Higher-order functions

As expected, we can pass functions as parameters too:

```
iex(60)> inc = fn(x) -> x + 1 end
#Function<6.50752066/1 in :erl_eval.expr/5>
iex(61)> inc.(2)
3
iex(62)> double = fn(x, f) -> f.(f.(x)) end
#Function<12.50752066/2 in :erl_eval.expr/5>
iex(63)> double.(2, inc)
4
```

The `double` here is called a [higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)


## Alternative Shortcut

Alternatively we can assign functions like this:

```
iex(65)> add = &(&1 + &2)
&:erlang.+/2
iex(66)> add.(5, 5)
10
```


## Partially applied functions

A partially applied function takes in a function and only applies a subset of
its parameters.

In the case below, `inc` and `dec` only applied the second parameter of `add`:

```
iex(67)> inc = &(add.(&1, 1)) 
#Function<6.50752066/1 in :erl_eval.expr/5>
iex(68)> inc.(5)
6
iex(69)> dec = &(add.(&1, -1))
#Function<6.50752066/1 in :erl_eval.expr/5>
iex(70)> dec.(5)
4
```
