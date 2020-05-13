import json
import os

from lxml import etree

DIRNAME = os.path.dirname(os.path.abspath(__file__))

def get_background(theme):
    with open(os.path.join(DIRNAME, 'themes', '{}.json'.format(theme)), 'r') as infile:
        return json.load(infile)['background']

def new_pos_x(oa_x, oa_size):
    return oa_x + oa_size


def create_rect(x, y, width, height, color, ry):
    code = etree.Element('rect')
    code.set('x', str(x))
    code.set('y', str(y))
    code.set('width', str(width))
    code.set('height', str(height))
    code.set('ry', str(ry))
    code.set('fill', color)

    return code


def rounded_rect(x, y, width, height, color, tlr, trr, brr, blr):

    data = (
        "M 0 {tlr} A {tlr} {tlr} 0 0 1 {tlr} 0 L {wtrr} 0 A {trr} {trr} 0 0 1 {w} {trr}"
        "L {w} {hbrr} A {brr} {brr} 0 0 1 {wbrr} {h} L {blr} {h} A {blr} {blr} 0 0 1 0 {hblr} Z".format(
            w=width,
            h=height,
            tlr=tlr,
            trr=trr,
            brr=brr,
            blr=blr,
            wtrr=width - trr,
            hbrr=height - brr,
            wbrr=width - brr,
            hblr=height - blr,
        )
    )

    code = etree.Element('path')
    code.set('d', data)
    code.set('transform', 'translate({x},{y})'.format(x=x, y=y))
    code.set('fill', color)

    return code