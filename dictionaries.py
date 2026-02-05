# dictionaries 
# dict = { "key" : "value" }
dict = {
    "pernambuco": "recife",
    "bahia": "salvador",
    }

## to return the value of key in the dict
print(dict.get("pernambuco"))
## or we can do the same thing like this:
print(dict["pernambuco"])

## you can create a new key there
## there is not problem if you want to create an list, number or string
dict["list"] = [1,2,3,4,5,6,7,8]
dict["string"] = "this is a string"
dict[1] = 2
print(dict)

## remove an key-value
dict.pop("bahia")
print(dict)

## remove the key-value in the end
dict.popitem()
print(dict)

## you can update them
dict.update({"pernambuco": "brasil"})
print(dict)

## or you can do like this
dict["pernambuco"] = "candeias"
print(dict)

## printing the keys and items
for key, value in dict.items():
    print(f"{key} {value}")