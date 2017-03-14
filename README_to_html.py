# -*- coding: utf-8 -*-
#!/usr/bin/env python

import markdown2, commands
from slugify import slugify

header  = open('header.html').read().decode('utf-8')
readme  = open('README.md').read().decode('utf-8').split('\n')
title   = u'\n'.join(readme[0:2])
content = u'\n'.join(readme[3:])
footer  = open('footer.html').read().decode('utf-8')

title_html = markdown2.markdown(title).replace('<h1', '<h1 id="top"')

content_html = markdown2.markdown(content, extras=['fenced-code-blocks'])
content_html_lines = content_html.split('\n')

version_count = commands.getstatusoutput('git log README.md | grep Author: | wc -l')[1]
version_uuid  = commands.getstatusoutput('git log README.md | cut -d " " -f2 | head -c 7')[1]
version       = u'pre-rfc_rev%s-%s' % (version_count, version_uuid)

navs = [u'<li class="list-group-item"><a href="#top">Checkoin</a></li>']
defs = []

current_h = None
for i in range(0, len(content_html_lines)):
    line = content_html_lines[i]
    line_strip = line.strip()
    if line.startswith(u'<h'):
        h = line[1:3]
        text = line[4:-5]
        slug = slugify(text)
        current_h = slug
        defs.append((text, slug,))
        content_html_lines[i] = u'<%s id="%s"><a name="%s"></a>%s</%s>' % (h, slug, slug, text, h)
        if h == u'h2':
            navs.append(u'<li class="list-group-item"><a href="#%s">%s</a></li>' % (slug, text))
    if line_strip.startswith(u'<li><code>'):
        slug = u"%s__%s" % (current_h, line_strip[10:].split(u'</code>')[0])
        content_html_lines[i] = line.replace(u'<li><code>', u'<li><a name="%s"></a><code>' % slug)

responsive_images = (u'/media/scan.gif',
                     u'/media/coin_circuit.png',
                     u'/media/coin_vin.jpg',
                     u'/media/coin_kraft.jpg',
                     u'/media/coin_gold.png')

content_html = u'\n'.join(content_html_lines)
content_html = content_html.replace(u'pre-RFC_VERSION', version)

for i in responsive_images:
    content_html = content_html.replace(
        u'<img src="%s"' % i,
        u'<img src="%s" class="img-responsive"' % i
    )

for d in defs:
    text, slug = d
    content_html = content_html.replace(u'<em>%s</em>' % text, u'<em><a href=#%s>%s</a></em>' % (slug, text,))
    content_html = content_html.replace(u'<em>%ss</em>' % text, u'<em><a href=#%s>%ss</a></em>' % (slug, text,)) # Plural

body = u"""
<header>%s</header>

<div class="container">
    <div class="row">

        <div class="col-md-3 hidden-xs hidden-sm">
            <div id="float_column">
                <div id="menu" role="navigation">
                    <ul class="nav list-group table-of-contents" role="tablist">
                        %s
                    </ul>
                </div>
                <div id="doc_info">
                    <a href="http://creativecommons.org/licenses/by-nd/4.0/"><img src="/media/cc-by-nd_88x31.png" /></a>
                    <br />
                    <label class="label label-primary">Version</label><span class="label label-default">%s</span>
                    <a id="twitter" href="https://twitter.com/checkoin">@checkoin</a>
                </div>
            </div>
        </div>

        <div class="col-md-9 col-sm-12">
        %s
        </div>

    </div>
</div>
""" % (title_html, u'\n                    '.join(navs), version, content_html)

home = u'\n'.join((header, body, footer))
open('home.html', 'w').write(home.encode('utf-8'))