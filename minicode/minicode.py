"""Main module."""
from lxml import etree

import highlight
import utils

def generate_line(line, line_num, options):

    code = highlight.get_highlight(line, options.theme)

    code_width = options.code_width
    code_height = options.code_height
    background_color = code['background']

    previous = (options.start_position, 0, background_color) # (x_position, width of rect, background color)

    line_group = etree.Element('g', id='line_{}'.format(line_num))

    for index, item in enumerate(code['tokens']):
        next_el = index + 1
        if next_el < len(code['tokens']):
            next_color = code['tokens'][next_el]['color']
        else:
            next_color = background_color
        
        previous_color = previous[2]
        
        #print(index, item, previous_color, item['color'], next_color)

        if previous_color == background_color:
            radius_left = options.radius_rect
        else:
            radius_left = 0
        if next_color == background_color:
            radius_right = options.radius_rect
        else:
            radius_right = 0

        new_x = utils.new_pos_x(previous[0], previous[1])
        line_group.append(
            utils.rounded_rect(
                new_x,
                line_num * (code_height + options.line_spacing),
                item['size'] * code_width,
                code_height,
                item['color'],
                radius_left,
                radius_right,
                radius_right,
                radius_left,
            )
        )
        previous = (new_x, item['size'] * code_width, item['color'])

    return line_group

def generate_svg(lines, options):

    width = options.width
    height = options.height

    root = etree.Element(
        'svg', width=str(width), height=str(height), xmlns='http://www.w3.org/2000/svg'
    )

    background_group = etree.Element('g', id='background')
    background_group.append(
        utils.create_rect(-1, -1, width + 2, height + 2, utils.get_background(options.theme), 0)
    )
    root.append(background_group)

    cpt = 1
    for line in lines:
        root.append(generate_line(line, cpt, options))
        cpt += 1


    data = etree.tostring(root, pretty_print=True).decode('utf8')
    file_res = open(options.output, 'w')
    file_res.write(data)
    file_res.close()
