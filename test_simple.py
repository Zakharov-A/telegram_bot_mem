def hello(name):
    if name == "":
        print("Hello world!")
    else:
        print(f"Hello {name}")


hello("Sam")
hello('')            


def hello2(name):
    if name:
        print(f"Hello {name}")
    else:
        print("Hello world!")


hello2([])
hello2("Sam")