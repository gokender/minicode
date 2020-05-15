"""Console script for minicode."""
import os
import sys

import configargparse

import minicode
import utils

def main():
    parser = configargparse.ArgParser(default_config_files=[os.path.join(utils.DIRNAME, 'config.ini')])

    parser.add('--width', required=False, type=int, help='SVG width')
    parser.add('--height', required=False, type=int, help='SVG height')
    parser.add('--theme', required=False, type=str, help='Syntax highlighting theme')
    parser.add('--input', required=False, type=str, help='Input filepath')
    parser.add('--output', required=False, type=str, help='Output filepath')

    parser.add('--code_width', required=False, type=int, help='Width in pixel of character')
    parser.add('--code_height', required=False, type=int, help='Height in pixel of character')
    parser.add('--start_position', required=False, type=int, help='Starting pixel position')
    parser.add('--radius_rect', required=False, type=int, help='Radius for rounded corner')
    parser.add('--line_spacing', required=False, type=int, help='Line spacing')

    parser.add('-a', '--auto_size', required=False, action='store_true', default=False, help='Choose width & height for you')
    parser.add('--lexer', required=False, type=str, help='Code parser')
    

    # TODO : Add Random
    # TODO : Config File
    # parser.add('-c', '--my-config', required=True, is_config_file=True, help='Config file path')
    
    options = parser.parse_args()
    
    with open(options.input, 'r') as infile:
        code_lines = infile.readlines()

    if options.auto_size:
        options.width = (max(len(line) for line in code_lines) * options.code_width) + options.start_position
        options.height = (len(code_lines) + 2) * (options.code_height + options.line_spacing)

    options.theme = options.theme.lower()
    
    print(options)

    minicode.generate_svg(code_lines, options)

    return 0


if __name__ == '__main__':
    sys.exit(main())
