#!/bin/python3

import os
import argparse
import logging
import jieba as jb

DAOLI_PATH = 'daolis'
MAX_LEN_EACH_LINE = 40

def draw_dialog(words: str) -> None:
    print(f'+{'-' * (MAX_LEN_EACH_LINE - 2)}+')

    if len(words) < MAX_LEN_EACH_LINE:
        print('|', words.center(MAX_LEN_EACH_LINE - len(words)), '|')
    else:
        # Cut the words into pieces
        words_list = jb.cut(words)
        buffer = ''
        for word in words_list:
            if len(buffer) + len(word) > MAX_LEN_EACH_LINE:
                print('|', buffer.center(MAX_LEN_EACH_LINE - len(buffer)), '|')
                buffer = ''
            buffer += f'{word}'

    print(f'+{'-' * (MAX_LEN_EACH_LINE - 2)}+')
    print('\\/'.center(MAX_LEN_EACH_LINE))

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Daoli say.')
    parser.add_argument('-f', '--file', type=str, help='Which daoli?')
    parser.add_argument('-d', '--description', type=str, help='Say something.')
    return parser.parse_args()

def main():
    jb.setLogLevel(logging.NOTSET)
    args = parse_args()
    if args.file:
        file = f'{args.file}.daoli'
        path = os.path.join(DAOLI_PATH, file)
        if os.path.exists(path):
            if args.description:
                description = args.description
                draw_dialog(description)
        # cat the daoli
        with open(path, 'r') as f:
            for line in f:
                print(line, end='')

if __name__ == '__main__':
    main()