f = open("vuyani.txt", "w")
f.write("You Are so handsome Vuyani \n")
f.write("You wanted Amanda to work for you \n")
f.write("Nothing")
f.close()


g = open("vuyani.txt", "r")
for x in g:
    print(x, end="")


with open("Amanda.txt", "w") as myfile:
    myfile.write("wabhora")
