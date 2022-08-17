import re
# text = input('Enter your Age:')

# result =re.match('^[0-9]{1,3}',text)
# if result:
#     print(result)
# else:
#     print(result)


text= "Nigeria"
pattern = re.compile('^[A-Za-z0-9]+$')

rs= pattern.search(text)

print(rs)
