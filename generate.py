import sys


def main():
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    with open('00_games_{}_{}.txt'.format(start, end), 'w') as f:
        f.write('\n'.join(['games:{}-{}'.format(i, i+3999)
                           for i in range(start, end, 4000)]))

if __name__ == '__main__':
    main()

