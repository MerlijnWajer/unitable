# encoding: utf-8

# Horizontal seperator
hs = u'─'


# Horizonal/Vertical top
hlt = u'┌'
hrt = u'┐'

# Horizonal/Vertical bottom
hlb = u'└'
hrb = u'┘'

# All mighty
hm = u'┼'

# Horizontal T
ht = u'┬'
# Horizonal perp
hb = u'┴'

# Right vert
vr = u'┤'

# Left vert
vl = u'├'

# Vert sep
vs = u'│'

#hs, ht, hlt, hrt, hlb, hrb, hm, hb, vr, vl, vs = u' ' * 11

def row_top(si):
    _ = u''
    for x in si:
        _ += hs * x + ht

    _ = hlt + _[0:-1] + hrt

    return _

def row_middle(si):
    _ = vl
    for x in si:
        _ += x * hs
        _ += hm

    _ = _[0:-1] + vr

    return _

def row_bottom(si):
    _ = u''
    for x in si:
        _ += hs * x + hb

    _ = hlb + _[0:-1] + hrb

    return _


def row_data(si, data, pos='m'):
    _ = ''
    for x in range(len(data)):
        _ += vs
        spacefree = (si[x] - len(data[x]))
        if pos == 'm':
            _ += ' ' * (spacefree / 2)
        elif pos == 'r':
            _ += ' ' * (spacefree)
        _ += data[x]
        if pos == 'm':
            _ += ' ' * (spacefree / 2)
        elif pos == 'l':
            _ += ' ' * (spacefree)

    _ += vs

    return _

def tableize(headers, info, pos='m'):
    rs = u''

    # Normalise headers. (length needs to be even)
    for x in range(len(headers)):
        if len(headers[x]) % 2 == 1:
            headers[x] += ' '

    # Normalise info. (length needs to be even)
    for x in range(len(info)):
        for y in range(len(info[x])):
            if len(info[x][y]) % 2 == 1:
                info[x][y] += ' '


    # Split/length
    hd = []

    # Get header length, and split points
    for x in range(len(headers)):
        s = max(len(headers[x]), max(map(lambda y: len(y[x]), info)))

        if s % 2 == 1:
            s += 1

        # Add a space on either side of the word (looks nicer)
        s += 2

        hd.append(s)

    rs += row_top(hd) + u'\n'
    rs += row_data(hd, headers, pos) + u'\n'
    rs += row_middle(hd) + u'\n'

    for i in info:
        rs += row_data(hd, i, pos) + u'\n'

    rs += row_bottom(hd) + u'\n'

    return rs

if __name__ == '__main__':
    print tableize(['Foo', 'Bar', 'Quux'],
        [
            ['Baz', 'Wubble', 'Wobble'],
            ['Baz', 'Wubble', 'Wobble'],
            ['Baz', 'Wubble', 'Wobble'],
            ['Baz', 'Wubble', 'Wobble'],
            ['Baz', 'Wubble', 'WobbleWobbleWobbleWobble']
        ])
