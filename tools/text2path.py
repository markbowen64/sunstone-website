import sys
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
def path(text, wght, size, x0, y0, tracking=0):
    f = instancer.instantiateVariableFont(TTFont('/home/claude/fonts/M.ttf'), {"wght": wght})
    gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
    s = size/upm; x = x0; out=[]
    for ch in text:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        tp = TransformPen(pen, (s,0,0,-s,x,y0))
        gs[g].draw(tp); out.append(pen.getCommands())
        x += gs[g].width*s + tracking
    return " ".join(out), x - tracking - x0
if __name__=="__main__":
    t,w,sz,tr = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
    d, width = path(t,w,sz,0,0,tr)
    print(width); print(d)
