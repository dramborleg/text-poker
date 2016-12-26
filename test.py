import parser
import testbot

game_creation = [('-c mango', 0), ('--create mango', 0), ('c mango', 0),
                 ('-c Uguisu', 0), ('--create kiwi c guava lemon', 0),
                 ('--create GAME_4', 0), ('-c', 0)]
add_players = [('-c mango', 0), ('-j', 0), ('--join mango', 0), ('j mango', 0),
               ('-j mango', 'dramborleg'), ('-j mang0', 1), ('-j mango', 0),
               ('-t ringil', 'dramborleg'), ('-t kiwi -j mango', 1)]
game_ops = [('-c mango -j mango -t せんぱい', 0), ('-j mango -t こうはい', 1),
            ('-s --deal 2 -f -o', 0), ('-o -p', 0), ('-q', 1), ('-q', 0),
            ('-r', 0), ('-r', 1), ('-q', 0), ('-q', 1)]
full_game = [('-c mango -j mango -t せんぱい', 0), ('-j mango -t こうはい', 1),
             ('-s -d 2', 0), ('-m I\'ll be the dealer', 0), ('-f', 0),
             ('-o', 0), ('-o', 0), ('-q', 0), ('-q', 1), ('-r', 0), ('-r', 1),
             ('-s -d 2', 1), ('-m Now I\'m the dealer', 1), ('-f', 1),
             ('-o', 1), ('-o', 1), ('-q', 0), ('-q', 1), ('-r', 0), ('-r', 1),
             ('-a 16', 0), ('-q', 0), ('-s', 0), ('-o 3', 0), ('-b 2', 1),
             ('-b 4', 0), ('-q', 0), ('-q', 1), ('-o 2', 0), ('-b 4', 0),
             ('-w 8', 1), ('-m まぬけ！give me my pies back!', 0),
             ('-q', 0), ('-q', 1)]

tests = [('GAME CREATION', game_creation), ('ADDING PLAYERS', add_players),
         ('GAME OPERATIONS', game_ops), ('FULL GAME', full_game)]

bot = testbot.TestBot()
for test in tests:
    p = parser.Parser()
    print('TESTING TEST: %s' % test[0])
    for i in test[1]:
        ret = p.parse(i[0], i[1], bot)
        print('--------')
        print(i)
        print(ret)
        print('--------')
    print('\n\n')
