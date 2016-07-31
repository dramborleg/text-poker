import parser

p = parser.Parser()
input = ['-c mango', '--create mango', 'c mango', '-c Uguisu',
         '--create kiwi c guava lemon', '--create']

for i in input:
    ret = p.parse(i, 0)
    print('--------')
    print(i)
    print(ret)
    print('--------')
