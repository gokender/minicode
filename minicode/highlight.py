import json
import os
import re

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatter import Formatter

import utils

class JsonFormatter(Formatter):
    def __init__(self, **options):
        Formatter.__init__(self, **options)

        self.theme = options.get('theme')
        #print(self.theme)

    def get_color(self, _id):
        with open(os.path.join(utils.DIRNAME, 'themes', '{}.json'.format(self.theme)), 'r'
        ) as infile:
            return json.load(infile)[_id]

    def format(self, tokensource, outfile):
        data = {'string': ''}
        tokens = []

        for ttype, value in tokensource:
            if value == '\n':
                continue
            elif re.match('\s', value) is not None:
                color = self.get_color('background')
            else:
                color = self.get_color(str(ttype))

            data['string'] += value

            tokens.append(
                {
                    'name': str(ttype),
                    'string': value,
                    'color': color,
                    'size': len(value),
                }
            )

        data['size'] = len(data['string'])
        data['tokens'] = tokens
        data['background'] = self.get_color('background')

        outfile.write(json.dumps(data))


def get_highlight(line, lexer_name, theme):
    lexer = get_lexer_by_name(lexer_name)
    formatter = JsonFormatter(theme=theme)
    return json.loads(highlight(line, lexer, formatter))
