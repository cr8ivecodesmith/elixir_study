How you should think about Elixir
=================================

Elixir is primarily a functional programming language which brings about
a whole different way of thinking about programming (if you're coming from an
OOP background).

Many of your instincts about how programs should work and structured or even
it's underlying principles will be wrong/challenged.

The best way is to approach the learning process with an empty cup!


```
- Object orientation is not the only way to design code.
- Functional programming need not be complex or mathematical.
- The foundations of programming are not assignments, if statements, and loops.
- Concurrency does not need locks, semaphores, monitors, and the like.
- Processes are not necessarily expensive resources.
- Metaprogramming is not just something tacked onto a language.
- Even if it is work, programming should be fun.

Thomas, Dave (2016-02-25). Programming Elixir 1.2: Functional |> Concurrent |> Pragmatic |> Fun
(Kindle Locations 563-567). Pragmatic Bookshelf. Kindle Edition.
```


## A basic approach

- Programming should be approached as a series of data transformations
- Functions will be the basic building blocks
- Each function ideally does one thing and do it well.
- A function would accept an input, transform it into a desired state, then
  return the transformed data
- The transformed data could then possibly be input for the another function
- Much like the UNIX tools and piping them:

```
ls `pwd` | grep "hello"
```
