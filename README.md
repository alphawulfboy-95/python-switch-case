# python-switch-case
An implementation of switch-case structures in python.

##
This git repo contains code that allows you to use switch-case structures into your python code.

##Why use switch-case?

Why not use if-elif-else statements? 

When you port code like this:

```
switch(var) {
    case 1:     x += 5;
    case 3:     y += 10;
                break;
    case 2:     x += 4;
    case 4:     y += 5;
    case 0:     z += 6;
                break;
}
```

It world look like this in Python:

```python
if var == 0:
    z += 6
elif var == 1:
    x += 5
    y += 10
elif var == 2:
    x += 4
    y += 5
    z += 6
elif var == 3:
    y += 10
elif var == 4:
    y += 5
    z += 6
```

Notice that there are lines of code would have to be duplicated when using if-elif-else statements instead of switch-case statements for this particular case.

##Example usage:

There are two ways to use this python script.

1.  Using the Switch function:

```python
import switch

def func0():
    print("Variable = 0")

def func1():
    print("1 + 1 = 2")

case0 = switch.Case(0, func0)
case1 = switch.Case(1, function = func1, True)
case2 = switch.Case(2, breaker = True)
case3 = switch.Case(3, function = func2, True)

for n in range(4):
    print("n = " + str(n))
    Switch(n, case0, case1, case2, case3)
    print("")
```

2.  Using the Switcher object:

```python
import switch

def func0():
    print("Variable = 0")

def func1():
    print("1 + 1 = 2")

case0 = switch.Case(0, func0)
case1 = switch.Case(1, function = func1, True)
case2 = switch.Case(2, breaker = True)
case3 = switch.Case(3, function = func2, True)

a_switch = switch.Switcher(None, case0, case1, case2, case3)

for n in range(4):
    print("n = " + str(n))
    a_switch.set_variable(n)
    a_switch.switch()
    print("")

del a_switch
```
