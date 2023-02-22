# 1-Python Program to Check if a Key Exists in a Dictionary or Not


def key_exists(dict):
    dict={"a":1,"b":2,"c":3}
    n=input()
    if n in dict:
        return("Exists")
    else:
        return("Not exists")
    
print(key_exists(dict))
