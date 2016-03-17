# -*- coding: utf-8 -*-
#!/usr/bin/env python

import markdown2, commands
from slugify import slugify

header  = open('header.html').read().decode('utf-8')
readme  = open('README.md').read().decode('utf-8').split('\n')
title   = u'\n'.join(readme[0:2])
content = u'\n'.join(readme[3:])
footer  = open('footer.html').read().decode('utf-8')

title_html   = markdown2.markdown(title)
content_html = markdown2.markdown(content, extras=['fenced-code-blocks'])
content_html_lines = content_html.split('\n')

version_count = commands.getstatusoutput('git log README.md | grep Author: | wc -l')[1]
version_uuid  = commands.getstatusoutput('git log README.md | cut -d " " -f2 | head -c 7')[1]
version       = u'pre-rfc_rev%s-%s' % (version_count, version_uuid)

navs = []

for i in range(0, len(content_html_lines)):
    line = content_html_lines[i]
    if line.startswith('<h2>') and line.endswith('</h2>'):
        text = line[4:-5]
        slug = slugify(text)
        content_html_lines[i] = u'<h2 id="%s"><a name="%s"></a>%s</h2>' % (slug, slug, text)
        navs.append(u'<li class="list-group-item"><a href="#%s">%s</a></li>' % (slug, text))

content_html = u'\n'.join(content_html_lines).replace('pre-RFC_VERSION', version)

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
                    <label class="label label-primary">Version</label><span class="label label-default">%s</span>
                    <br />
                    <a href="http://creativecommons.org/licenses/by-nd/4.0/"><img src="medias/cc-by-nd_88x31.png" /></a>
                </div>
            </div>
        </div>

        <div class="col-md-9 col-sm-12">
        %s
        </div>

    </div>
</div>
""" % (title_html, u'\n                    '.join(navs), version, content_html)

render = u'\n'.join((header, body, footer))

open('index.html', 'w').write(render.encode('utf-8'))
