s = "hello"
print(dir(s))
useful_methods = [m for m in dir(s) if "__" not in  m]
print(useful_methods)
print(help(s.capitalize))
print(s.capitalize())
print("HELLO".casefold())

print("hello".center(50))
print("i see a little dove".count("e"))

