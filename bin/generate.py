# fontforge -lang=py -script generate.py

import os

import fontforge

svg_inputdir = './svg'
files = os.listdir(svg_inputdir)

font = fontforge.font()

code = 6000
for e in files:
    try:
        glyph = font.createChar(code, e)
        glyph.importOutlines(svg_inputdir + '/' + e)
    except:
        print('Error', e)

    code = code + 1
    break

font.generate('../fonts/Ionicons.ttf')
