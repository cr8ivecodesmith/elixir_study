Pattern Matching
================


## It's not an assignment operator

There's no such thing as variable assignment in Elixir but rather a concept
called `pattern matching`.

Take this expression for example

```
a = 1
```

Normally you would say,

Assign the value `1` to the variable `a`

But Elixir instead was asking the question,

Does the value on the left match the value on the right?

Then if necessary, assign unbounded variables on the left to match values
on the right.

```
iex(32)> a = "hello there"
"hello there"
iex(33)> "hello there" = a
"hello there"
iex(34)> 1 = a
** (MatchError) no match of right hand side value: "hello there"
```


## Data types

Usual suspects:

- String
- Integer
- Boolean (`true`, `false`)
- Null-type (`nil`)
- Lists (`[]`, `[1, "peanutbro"]`)


Not so usual:

Tuple

```
> {}
> {1, 2}
```

Atoms

```
:hello
```


## Type checking

We can check the type of a variable with the `is_` function

```
iex(22)> is_    
is_atom/1         is_binary/1       is_bitstring/1    is_boolean/1      
is_float/1        is_function/1     is_function/2     is_integer/1      
is_list/1         is_map/1          is_nil/1          is_number/1       
is_pid/1          is_port/1         is_reference/1    is_tuple/1
```


## Destructuring

This concept is similar to Python's value unpacking


```
iex(23)> coordinates = {123.45, 234.123}
{123.45, 234.123}
iex(24)> {long, lat} = coordinates
{123.45, 234.123}
iex(25)> long
123.45
iex(26)> lat
234.123
```


## No, that's not a variable reassignment

One foundation of a functional programming language is `immutability`.
Since Elixir is running on an Erlang VM, this:

```
iex(28)> life = "peanut butter"
"peanut butter"
iex(29)> life = "butter"
"butter"
iex(30)> life = "peanut"
"peanut"
```

doesn't mean that we are reassigning the variable `life` with different values.

The compiler *implicitly* marks each `life` as `life'` for each time a new
value is assigned. So internally, the variables have only been assigned a value
once.

This is one of the many syntactic sugar the Elixir has built on top of Erlang
to make it a bit more friendly.
