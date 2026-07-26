import argparse
import json

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
                        help='set format of output')
    
    args = parser.parse_args()

    data1 = json.load(open(args.first_file))
    data2 = json.load(open(args.second_file))
    
    print(data1)
    print(data2)


if __name__ == '__main__':
    main()