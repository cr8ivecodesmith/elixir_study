Maps
====

Maps are pretty much key-value pair data types like a Python dictionary.

Here's how we declare and get values from it:

```
iex(3)> record = %{ :first_name => "Tyrion", :last_name => "Lannister" }
%{first_name: "Tyrion", last_name: "Lannister"}
iex(4)> record[:first_name]
"Tyrion"
iex(5)> record.last_name
"Lannister"
iex(6)>
```

If your keys are `atoms`, there's an added shortcut to use the colons to the
end instead:

```
iex(6)> location = %{ continent: "Westeros", kingdom: "Castle Rock" }   
%{continent: "Westeros", kingdom: "Castle Rock"}
iex(7)> location[:continent]
"Westeros"
iex(8)> location.kingdom
"Castle Rock"
```

#### Updating key values

Since Elixir is a functional programming language, variables are immutable even
the values they hold so updating them is not so straight forward.

```
iex(9)> put_in record.first_name, "Tyrion" 
%{first_name: "Tyrion", last_name: "Lannister"}
iex(10)> put_in record.first_name, "Cerce" 
%{first_name: "Cerce", last_name: "Lannister"}
```
