Composing Functions
===================

Ideally we want functions that work together. By running functions in sequence,
one's output becomes input for another.

Using our `dec` and `inc` functions, let's move values 2 steps forward and 1
step back:

```
iex(73)> dec.(inc.(inc.(10))) 
11
```


## The Pipe operator

If you work your way out in the previous example you'll see that we tried to
increase the 2x then decrease 1x but it's not very clear. Using pipes is better.

```
iex(77)> 10 |> inc.() |> inc.() |> dec.()
11
```
