class Caps:
    import camelcase
    x=camelcase.CamelCase()
    d = str(input("Enter a list of name:"))
    print("The req list is",(list(x.hump(d))))