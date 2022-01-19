data = eval(input("Enter the dictionary: "))
result = {}
new_key = ""

def flatten(data):
    global new_key
    for key in data:
        if type(data.get(key)) != type(data):
            new_key += key + "."
            result[new_key] = data.get(key)
            new_key = new_key.replace(key + ".", "")

        else:
            new_key += key + "."
            flatten(data.get(key))

flatten(data)
print(result)
