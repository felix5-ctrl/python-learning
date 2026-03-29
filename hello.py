#CS50P Lection 0 work along
#easy return variable function, comments
#used: input(), print(), assignment operator "="

#variable request, internally defined as "name"
#string-variable request
name = input("What's your 'name'? ")

#return variable
#"+" doesn't add space
#alternate function would be ","
#e.g. print("hello,", name) -> spacing added auto
#override arguments of basic func
#alternating '' & ""
#formatting string 'f'
print(f"hello, {name}", end="\n")

#print(*objects, sep=' ', end='\n', file=None, flush=False)
#official python doc of print(), argument expl.

# *objects -> any number of obj can be inserted
# sep=' ' -> separator when multiple arguments get printed
# end='\n' -> end is ending the line, \n means new line

#cs50 p minute 44:55 https://www.youtube.com/watch?v=JP7ITIXGpHk