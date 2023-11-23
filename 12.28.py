# for i in range(25006,25997,10):
#     if i%37==0 or i%67==0:
#         print(i)

input=input()
output=''
for i in input:
    tmp=''
    match i:
        case 'o':
            tmp='0'
        case 'i':
            tmp='1'
        case 'g':
            tmp='9'
        case 'b':
            tmp='6'
    output+=tmp
print(output)

