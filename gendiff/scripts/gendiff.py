import argparse

from gendiff.parser import parse_file
from gendiff.formatters.format_diff import format_diff
from gendiff.build_diff import build_diff


def generate_diff(file_path1: str, file_path2: str, 
                  format_name='stylish') -> str:
    if format_name is None:
        format_name = 'stylish'
        
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    
    diff_tree = build_diff(data1, data2)

    return format_diff(diff_tree, format_name)


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', 
                        default='stylish', 
                        choices=['stylish', 'plain', 'json'], 
                        metavar='FORMAT',
                        help='set format of output')
    
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)

    print(diff)


if __name__ == '__main__':
    main()