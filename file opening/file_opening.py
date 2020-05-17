def add_to_dict(name, value, dic=None):
    if dic is None:
        dic = {}
    dic[name] = value
    return dic


def test():
    dic1 = {'albert': 'cute', }
    print (add_to_dict('barry', 'funny', dic1))
    print (add_to_dict('charlene', 'smart', dic1))
    print (add_to_dict('darryl', 'outrageous'))
    print (add_to_dict('eddie', 'friendly'))
    print (add_to_dict('bob', 'asshole'))
    print (add_to_dict('tim', 'idiot', dic1))

    
test()




'''
test_file = open("texty.txt", "w")


def write_to_file(file_to_open, string = ""):
    file_to_open.write(string)
    

write_to_file(test_file, "12")
write_to_file(test_file)
write_to_file(test_file, "123")
write_to_file(test_file)
write_to_file(test_file, "1234")


try:
    test_file = open("texty.txt", "r")
    print(test_file.readlines())
except FileNotFoundError:
    print("missing file")
'''
