import random
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet =['a','b','c','d', 'e', 'f', 'g', 'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nums = [1,2,3,4,5,6,7,8,9]
special_characters = ['!','@','#','$',"%",'^',"&","*","-","<",">",",",".","/",'?',"'",]
def password_generate():
        for password in alphabet,nums,special_characters:
                print((random.choice(special_characters)))
                print(random.choice(nums))
                print(random.choice(alphabet or ALPHABET))

print("Hello And Welcome To The PassWord Maker Program")
password_make = input("To Continue Type '!password': ")
if password_make != "!password":
        print("ERROR \nProbably You Typed Wrong!")
        password_make
if password_make == "!password":
        password_generate()

        print("Want Another One?")
        for i in range(100000000):
                another_one = input("If You Want Another One Type !another one: ")
                if another_one != "!another one":
                        print("Sure You Are Not Interest For Another Password?")
                        quit_or_not =input("If You Were Wrong Type Again: ")
                        if quit_or_not != "!another one":
                                quit("Ok! \nSee You Next Time")
                        if quit_or_not == "!another one":
                                password_generate()
                if another_one == "!another one":
                        password_generate()
