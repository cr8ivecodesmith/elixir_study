Modules
=======

See:

```
./src/geometry1.ex
./src/geometry2.ex
```


## Do blocks

See:

```
./src/geometry3.ex
```

Here, Elixir will execute the first function that matches the argument list.

The `when` clause is also called a `guard` in this case if the inbound
parameters doesn't satisfy the condition it will try the next definition. If
none of the parameter patterns matches, Elixir will throw an error.

Running the module produces this:

```bash
$ docker-compose run --rm shell elixir src/geometry3.ex 
The area of the rectangle {3, 4} is 12
The area of the square {4} is 16
** (FunctionClauseError) no function clause matching in Square.area/1
    src/geometry3.ex:10: Square.area({3, 4})
        src/geometry3.ex:30: (file)
            (elixir) lib/code.ex:363: Code.require_file/2
```


## The development approach

Through creative combinations of functions, modules, and pipes; we can break
bigger problems into smaller functions, grouped into modules, and them compose
the output with pipes.
