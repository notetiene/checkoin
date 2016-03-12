#!/usr/bin/env python

import markdown2

header = open('header.html').read()
readme = open('README.md').read()
footer = open('footer.html').read()

render = '\n'.join((header,
                    markdown2.markdown(readme, extras=['fenced-code-blocks']),
                    footer))

open('index.html', 'w').write(render)
