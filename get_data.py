def main():
    for i in range(1, 54):
        lines = []
        with open('./data/Volltext/%s.txt' % i) as f:
            for line in f:
                lines.append(line.rstrip())
        with open('./data/consolidated.txt', 'a') as g:
            g.write('%s\n' % ' '.join(lines))


if __name__ == '__main__':
    main()