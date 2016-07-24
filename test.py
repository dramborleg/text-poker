import parser

p = parser.Parser()
input = ['-c mango', '--create mango', 'c mango',
         '--create kiwi c guava lemon', '--create']

for i in input:
    ret = p.parse(i)
    print('--------')
    print(i)
    print(ret)
    print('--------')
