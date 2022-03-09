import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tagged_path', type=str)
    args = parser.parse_args()
    tagged_path = args.tagged_path

    examples = []
    with open(tagged_path, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            sp = line.rstrip('\n').split(' ')
            word, pos = [], []
            for tok in sp:
                t = tok.split('_')
                word.append(''.join(t[:-1]))
                pos.append(t[-1])

            example = {'word': word, 'pos': pos}
            examples.append(example)
    
    print(examples)

if __name__ == '__main__':
    main()