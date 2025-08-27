def main():
    name = input("what's your name? ")
    hello(name)

def hello(to="World"):
    to = to.strip().title()
    first, last = to.split(" ")
    print("Hello,", first)

main()
