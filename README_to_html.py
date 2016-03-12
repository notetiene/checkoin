# -*- coding: utf-8 -*-
#!/usr/bin/env python

import markdown2

header = open('header.html').read().decode('utf-8')
readme = open('README.md').read().decode('utf-8')
footer = open('footer.html').read().decode('utf-8')

render = u'\n'.join((header,
                     markdown2.markdown(readme, extras=['fenced-code-blocks']),
                     footer))

open('index.html', 'w').write(render.encode('utf-8'))
