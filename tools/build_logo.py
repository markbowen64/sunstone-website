import sys
sys.path.insert(0,'.')
from text2path import path
NAVY="#0B2350"; BLUE="#1E6FD9"; WHITE="#FFFFFF"; SKY="#8CCBFF"
MARK_DEFS='''<linearGradient id="stone" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1E7BE6"/><stop offset="1" stop-color="#0B2350"/></linearGradient>
<linearGradient id="sun" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC24A"/><stop offset="1" stop-color="#F28A1C"/></linearGradient>
<clipPath id="above"><rect x="0" y="0" width="120" height="76"/></clipPath>'''
MARK_BODY='''<path d="M60 6 L107 33 L107 87 L60 114 L13 87 L13 33 Z" fill="url(#stone)" stroke="url(#stone)" stroke-width="6" stroke-linejoin="round"/>
<path d="M13 33 L60 46 L60 6 Z" fill="#fff" opacity=".14"/>
<path d="M60 6 L107 33 L60 46 Z" fill="#fff" opacity=".06"/>
<g stroke="#3FD0FF" stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M60 52 V30"/><path d="M47 57 L39 49 V38"/><path d="M73 57 L81 49 V38"/><path d="M40 66 H30 L25 61"/><path d="M80 66 H90 L95 61"/></g>
<g fill="#3FD0FF"><circle cx="60" cy="26" r="4"/><circle cx="39" cy="34" r="4"/><circle cx="81" cy="34" r="4"/><circle cx="22" cy="58" r="4"/><circle cx="98" cy="58" r="4"/></g>
<circle cx="60" cy="76" r="18" fill="url(#sun)" clip-path="url(#above)"/>
<g stroke="#fff" stroke-width="3.2" stroke-linecap="round"><path d="M28 82 H92"/><path d="M38 90 H82" opacity=".75"/><path d="M48 98 H72" opacity=".5"/></g>'''
def svg(w,h,body,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" role="img" aria-label="{title}"><title>{title}</title><defs>{MARK_DEFS}</defs>{body}</svg>\n'
def words(size1=60, size2=25):
    d1,w1 = path("SUNSTONE",800,size1,0,0,1.5)
    # fit DATA SYSTEMS to SUNSTONE width
    _,w2 = path("DATA SYSTEMS",600,size2,0,0,0)
    tr = (w1-w2)/11
    d2,w2 = path("DATA SYSTEMS",600,size2,0,0,tr)
    return d1,w1,d2,w2
T="Sunstone Data Systems"
d1,w1,d2,w2 = words()
def horizontal(c1,c2,name):
    mh=120; gap=22; W=mh+gap+w1+4; H=120
    body=f'<g>{MARK_BODY}</g><g transform="translate({mh+gap},66)"><path d="{d1}" fill="{c1}"/></g><g transform="translate({mh+gap},96)"><path d="{d2}" fill="{c2}"/></g>'
    open(name,'w').write(svg(W,H,body,T))
def stacked(c1,c2,name):
    W=w1+20; mx=(W-120)/2
    body=f'<g transform="translate({mx},0)">{MARK_BODY}</g><g transform="translate(10,186)"><path d="{d1}" fill="{c1}"/></g><g transform="translate(10,218)"><path d="{d2}" fill="{c2}"/></g>'
    open(name,'w').write(svg(W,228,body,T))
import os; os.makedirs('out',exist_ok=True)
horizontal(NAVY,BLUE,'out/sunstone-logo-horizontal.svg')
horizontal(WHITE,SKY,'out/sunstone-logo-horizontal-white.svg')
stacked(NAVY,BLUE,'out/sunstone-logo-stacked.svg')
stacked(WHITE,SKY,'out/sunstone-logo-stacked-white.svg')
open('out/sunstone-mark.svg','w').write(svg(120,120,MARK_BODY,"Sunstone Data Systems mark"))
FAV='''<path d="M60 6 L107 33 L107 87 L60 114 L13 87 L13 33 Z" fill="url(#stone)" stroke="url(#stone)" stroke-width="8" stroke-linejoin="round"/>
<g stroke="#3FD0FF" stroke-width="7" fill="none" stroke-linecap="round"><path d="M60 46 V24"/><path d="M38 54 L28 44"/><path d="M82 54 L92 44"/></g>
<circle cx="60" cy="80" r="24" fill="url(#sun)" clip-path="url(#abovef)"/>
<path d="M26 86 H94" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'''
open('out/favicon.svg','w').write(svg(120,120,FAV.replace('abovef','above2'),"Sunstone").replace('</defs>','<clipPath id="above2"><rect width="120" height="78"/></clipPath></defs>'))
