import ast
import base64
import bz2
import copy
import hashlib
import json
import lzma
import marshal
import math
import os
import sys
import time
import secrets
import unicodedata
import warnings
import zlib
warnings.filterwarnings('ignore', category=DeprecationWarning)
try:
    from pystyle import Col, Colorate, Colors
except:
    Col = None
    Colorate = None
    Colors = None
if sys.version_info < (3, 10):
    print("Python 3.10+ required")
    sys.exit(1)
try: sys.setrecursionlimit(max(sys.getrecursionlimit(), 500000))
except: pass
def __slate__():
   if Colorate is None:
        print(); [print(row) for row in ("      ______________________________________________________________", "     /\\                                                             \\", "    /##\\      OOOOO   BBBBB    SSSSS  III  DDDDD   III   AAAA  NN  NN", "   /####\\    OO   OO  BB  BB  SS       I   DD  DD   I   AA  AA NNN NN", "  /######\\   OO   OO  BBBBB    SSSS    I   DD  DD   I   AAAAAA NN NNN", " /###/\\###\\  OO   OO  BB  BB      SS   I   DD  DD   I   AA  AA NN  NN", "/___/  \\___\\  OOOOO   BBBBB   SSSSS  III  DDDDD   III  AA  AA NN  NN", "\\   \\  /   /______________________________________________________/", " \\___\\/___/        [Obsidian] Premium Protect  |  Owner: yeppp")]; print("  >> Ready"); print(); return
   mix = Colors.DynamicMIX((Col.cyan, Col.pink, Col.light_gray)); glow = Colors.DynamicMIX((Col.pink, Col.cyan, Col.light_gray)); hot = Colors.DynamicMIX((Col.blue, Col.cyan, Col.pink)); print()
   for row in ("      ______________________________________________________________", "     /\\                                                             \\", "    /##\\      OOOOO   BBBBB    SSSSS  III  DDDDD   III   AAAA  NN  NN", "   /####\\    OO   OO  BB  BB  SS       I   DD  DD   I   AA  AA NNN NN", "  /######\\   OO   OO  BBBBB    SSSS    I   DD  DD   I   AAAAAA NN NNN", " /###/\\###\\  OO   OO  BB  BB      SS   I   DD  DD   I   AA  AA NN  NN", "/___/  \\___\\  OOOOO   BBBBB   SSSSS  III  DDDDD   III  AA  AA NN  NN", "\\   \\  /   /______________________________________________________/"): print(Colorate.Diagonal(mix, row))
   for row in (" \\___\\/___/        [Obsidian] Premium Protect  |  Owner: yeppp", "             [Mode] Heavy Obfuscation  |  [Status] Ready", "             >> Dung co deobf em yeu a <<"): print(Colorate.Diagonal(glow if '>>' not in row else hot, row))
   print()
def __mist__(seed, need):
   if isinstance(seed, str): seed = seed.encode('utf-8')
   elif not isinstance(seed, (bytes, bytearray)): seed = repr(seed).encode('utf-8')
   bag = bytearray(); last = hashlib.sha256(seed).digest(); slot = 0
   while len(bag) < need:
        last = hashlib.sha256(last + seed + slot.to_bytes(8, 'little')).digest(); last and bag.extend(last); slot += 1
   return bytes(bag[:need])
def __spark__(seed, low, high):
   if high <= low:
        return low
   fog = __mist__(seed, 8)
   return low + (int.from_bytes(fog, 'little') % (high - low + 1))
def __hide__(text, seed):
   mix = __grout__(seed + b'hidemix', 2)
   rot = 7 + ((__spark__(seed + b'rot', 7, 87) ^ mix[0]) % 81)
   span = 233 + ((__spark__(seed + b'span', 233, 997) ^ mix[1]) % 765)
   rows = tuple(''.join(chr(32 + ((ord(ch) - 32 + rot) % 95)) for ch in text[at:at + span][::-1]) for at in range(0, len(text), span))
   return rows, rot
def __show__(rows, rot, name=None):
   var = name or '__'
   src = ''.join(chr(32 + i) for i in range(95))
   dst = ''.join(chr(32 + ((i - rot) % 95)) for i in range(95))
   salt = repr((rows, rot, var)).encode('utf-8', 'replace');uni=''.join(one for one, _ in __marble__(salt+b'showuni',2)).encode('utf-8','surrogatepass');salt += uni
   salt += repr((__flint__(salt + b'showflint', 2), __hill__(salt + b'showhill', 3))).encode('utf-8','replace')
   cls = __spell__('str', salt + b'showstr')
   make = __spell__('maketrans', salt + b'showmake')
   val=__rune__(set([var]),hashlib.sha256(salt+b'showv').digest(),b'v')
   return f"(lambda {var}:''.join(map(lambda {val}:{val}.translate({var})[::-1],{rows!r})))(__import__({__spell__('builtins', salt + b'showbuilt')}).__dict__[{cls}].__dict__[{make}]({src!r},{dst!r}))"
def __scatter__(text, seed):
   fog = __mist__(seed + b'scatter', 24); cut = 1 + fog[0] % max(1, len(text))
   real = (text[:cut], text[cut:]); used = set(); names = [__rune__(used, seed + b'scattername', slot.to_bytes(2, 'little')) for slot in range(2)]
   rows = [(0, __show__(*__hide__(real[0], seed + b'scatterpart0'), names[0])), (1, __show__(*__hide__(real[1], seed + b'scatterpart1'), names[1]))]
   rows.sort(key=lambda item: fog[item[0] + 3])
   args = ','.join(expr for _, expr in rows); params = ','.join(names)
   return f"(lambda {params}:{names[[idx for idx,(mark,_) in enumerate(rows) if mark==0][0]]}+{names[[idx for idx,(mark,_) in enumerate(rows) if mark==1][0]]})({args})"
def __spell__(text, seed):
   rows = []
   seed = hashlib.sha256(seed + __shrine__(seed + b'spellshrine', text) + repr(__desert__(seed + b'spelldesert', 2)).encode('ascii')).digest()
   fog = __mist__(seed + text.encode('utf-8', 'replace'), max(16, len(text) * 8))
   for slot, char in enumerate(text):
      left = 1 + (fog[(slot * 3) % len(fog)] & 1); right = 1 + (fog[(slot * 3 + 1) % len(fog)] & 1); bag = []
      for at in range(left):
         base = (0x3041, 0x4e00, 0x0370, 0x1200)[(fog[(slot + at) % len(fog)] + at) & 3]; bag.append(chr(base + (fog[(slot * 5 + at) % len(fog)] & 127)))
      pos = len(bag); bag.append(char)
      for at in range(right):
         base = (0x30a1, 0xac00, 0x0400, 0x10a0)[(fog[(slot + at + 7) % len(fog)] + at) & 3]; bag.append(chr(base + (fog[(slot * 7 + at) % len(fog)] & 127)))
      rows.append(f"{bag!r}[{pos}]")
   out = "(" + repr('%s' * len(rows)) + " % (" + ",".join(rows) + ("," if len(rows) == 1 else "") + "))"
   if text and len(text) <= 16:
      uni=''.join(one for one, _ in __marble__(seed + text.encode('utf-8', 'replace') + b'spelluni', 2)).encode('utf-8','surrogatepass');name=__sigil__(seed + text.encode('utf-8', 'replace') + b'spell' + uni, 1)[0];out=f"(lambda {name}:{name})({out})"
   return out
def __flare__(blob):
   glow = 0
   at = 0
   while at < len(blob):
        row = blob[at:at + 16]
        for one in row:
             glow = (glow + one) & 0xffffffff
             glow = ((glow << 7) | (glow >> 25)) & 0xffffffff
             glow ^= (one * 131) & 0xffffffff
        at += 16
   return glow
def __mint__(used, seed, mint):
   ring = ((0x4e00, 0x9faf), (0x3400, 0x4dbf), (0x3041, 0x3096), (0x30a1, 0x30fa), (0xac00, 0xd7a3), (0x0400, 0x04ff), (0x0370, 0x03ff), (0x10a0, 0x10ff), (0x1200, 0x137f), (0x0e00, 0x0e7f), (0x0980, 0x09ff), (0x0a00, 0x0a7f), (0x0b00, 0x0b7f), (0x0c00, 0x0c7f), (0x0d00, 0x0d7f), (0x13a0, 0x13ff), (0x1400, 0x167f), (0x1680, 0x169f), (0x16a0, 0x16ff), (0x1700, 0x171f), (0x1780, 0x17ff), (0x1800, 0x18af), (0x1e00, 0x1eff), (0x1f00, 0x1fff), (0x2c00, 0x2c5f), (0x2d00, 0x2d2f), (0xa000, 0xa48f), (0xa500, 0xa63f), (0xa800, 0xa82f), (0x1000, 0x109f), (0x0f00, 0x0fff), (0xaa00, 0xaa5f), (0x0900, 0x097f), (0xa980, 0xa9df), (0x1b00, 0x1b7f))
   while True:
        fog = hashlib.sha256(seed + mint[0].to_bytes(4, 'little')).digest(); wide = 2 + (fog[0] & 3); rows = ['__']; slot = 0; at = 1
        while slot < wide:
            if at + 2 >= len(fog):
                  fog += hashlib.sha256(fog + seed + mint[0].to_bytes(4, 'little')).digest()
            left, right = ring[fog[at] % len(ring)]; one = chr(left + (int.from_bytes(fog[at + 1:at + 3], 'little') % (right - left + 1))); at += 3
            if not one.isidentifier(): continue
            rows.append(one); slot += 1
        tail = chr(0x3041 + (fog[29 % len(fog)] % (0x3096 - 0x3041 + 1)))
        tail.isidentifier() and rows.append(tail)
        rows.append('__'); name = ''.join(rows); mint[0] += 1
        norm = unicodedata.normalize('NFKC', name)
        if norm != name or name in used or norm in used: continue
        if name.isidentifier(): used.add(name); return name
def __rune__(used, seed, mark):
   ring = ((0x4e00, 0x9faf), (0x3400, 0x4dbf), (0x3041, 0x3096), (0x30a1, 0x30fa), (0xac00, 0xd7a3), (0x0400, 0x04ff), (0x0370, 0x03ff), (0x10a0, 0x10ff), (0x1200, 0x137f), (0x0e00, 0x0e7f), (0x0980, 0x09ff), (0x0a00, 0x0a7f), (0x0b00, 0x0b7f), (0x0c00, 0x0c7f), (0x0d00, 0x0d7f), (0x13a0, 0x13ff), (0x1400, 0x167f), (0x16a0, 0x16ff), (0x1700, 0x171f), (0x1780, 0x17ff), (0x1800, 0x18af), (0x1e00, 0x1eff), (0x1f00, 0x1fff), (0x2c00, 0x2c5f), (0x2d00, 0x2d2f), (0xa000, 0xa48f), (0xa500, 0xa63f), (0xa800, 0xa82f), (0x1000, 0x109f), (0x0f00, 0x0fff), (0xaa00, 0xaa5f), (0x0900, 0x097f), (0xa980, 0xa9df), (0x1b00, 0x1b7f))
   salt = mark if isinstance(mark, bytes) else repr(mark).encode('utf-8')
   turn = 0
   while True:
        fog = __mist__(seed + salt + turn.to_bytes(4, 'little'), 96)
        wide = 2 + (fog[0] % 5)
        rows = ['__']
        at = 1
        while len(rows) <= wide:
             left, right = ring[fog[at % len(fog)] % len(ring)]
             char = chr(left + (int.from_bytes(fog[(at + 1) % len(fog):(at + 3) % len(fog)] or fog[:2], 'little') % (right - left + 1)))
             at += 3
             if char.isidentifier():
                  rows.append(char)
        rows.append('__')
        name = ''.join(rows)
        turn += 1
        norm = unicodedata.normalize('NFKC', name)
        if norm != name or name in used or norm in used:
              continue
        if name.isidentifier() and not __import__('keyword').iskeyword(name):
             used.add(name)
             return name
def __sigil__(seed, count):
   used = set()
   rows = []
   for slot in range(count):
        rows.append(__rune__(used, seed, slot.to_bytes(4, 'little')))
   return rows
def __crown__(raw):
   glow = 0
   bend = 0
   for slot, byte in enumerate(raw):
        glow = (glow + byte + slot) & 0xffffffff
        bend ^= ((byte + 1) * (slot + 3)) & 0xffffffff
        bend = ((bend << 5) | (bend >> 27)) & 0xffffffff
   return (len(raw), sum(raw) & 0xffffffff, raw[:1], raw[-1:], glow, bend)
def __chant__(text, seed):
   raw = text.encode('utf-8')
   mix = repr((__flint__(seed + raw + b'chantflint', 2), __grout__(seed + raw + b'chantgrout', 3))).encode('ascii')
   fog = __mist__(seed + raw + len(raw).to_bytes(4, 'little') + mix, len(raw) or 1)
   key = __spark__(seed + raw + b'chant' + mix, 1, 255)
   rows = tuple((byte ^ fog[slot] ^ key) for slot, byte in enumerate(raw))
   return (rows, key, fog.hex(), __crown__(raw))
def __prism__(name, data):
    row, key, fog, mark = data
    uni=''.join(one for one, _ in __marble__(name.encode('utf-8','surrogatepass')+b'prismuni',2)).encode('utf-8','surrogatepass');a,b,c,d=__sigil__(name.encode('utf-8','surrogatepass')+b'prism'+uni,4)
    mask=(key+len(row)*11+73)&255;step=((key^len(fog))&31)+3;wide=(mask<<8)|mask
    row=tuple((one^mask^((slot*step)&255))&255 for slot,one in enumerate(row))
    row=f"tuple(({b}^{mask}^(({a}*{step})&255))&255 for {a},{b} in enumerate({row!r}))"
    turn=(key%17)+5;fog=''.join(chr(32+((ord(ch)-32+turn)%95)) for ch in fog[::-1])
    fog=f"''.join(chr(32+((ord({c})-32-{turn})%95)) for {c} in {fog!r})[::-1]"
    left="b''" if not mark[2] else f"bytes(({mark[2][0]^mask}^{mask},))";right="b''" if not mark[3] else f"bytes(({mark[3][0]^mask}^{mask},))"
    mark=f"({mark[0]}^{mask}^{mask},{mark[1]^wide}^{wide},{left},{right},{mark[4]^wide}^{wide},{mark[5]^wide}^{wide})"
    return f"(lambda {d}:{d})({name}({row},{key^mask}^{mask},{fog},{mark}))"
def __iris__(name, way):
    uni=''.join(one for one, _ in __marble__(name.encode('utf-8','surrogatepass')+bytes([way])+b'irisuni',2)).encode('utf-8','surrogatepass');tail = ".decode('utf-8')" if way else ""; a, b, c, d, e, f, g, h, i, j = __sigil__(name.encode('utf-8', 'surrogatepass') + bytes([way]) + b'iris' + uni, 10)
    return f"{name}=lambda {a},{b},{c},{d}:(lambda {e}:(lambda {f}:((len({e}),sum({e})&0xffffffff,{e}[:1],{e}[-1:],{f}[0],{f}[1])!={d} and 1/0,{e}{tail})[-1])(__import__('functools').reduce(lambda {g},{h}:(({g}[0]+{h}[1]+{h}[0])&0xffffffff,((({g}[1]^((({h}[1]+1)*({h}[0]+3))&0xffffffff))<<5)|(({g}[1]^((({h}[1]+1)*({h}[0]+3))&0xffffffff))>>27))&0xffffffff),enumerate({e}),(0,0))))(bytes(({i}^{b}^bytes.fromhex({c})[{j}]) for {j},{i} in enumerate({a})))"
def __plume__(name):
   way = 1
   return __iris__(name, way)
def __ivory__(seed, used, words, func):
   rows = []
   book = {}
   for slot, word in enumerate(words):
        name = __rune__(used, seed, word.encode('utf-8') + slot.to_bytes(4, 'little'))
        data = __chant__(word, seed + slot.to_bytes(4, 'little'))
        rows.append(f"{name}={__prism__(func, data)}")
        book[word] = name
   return rows, book
def __script__(seed, words):
   used = set()
   func = __rune__(used, seed, b'func')
   rows = [__plume__(func)]
   hold, book = __ivory__(seed + b'book', used, words, func)
   rows.extend(hold)
   return ';'.join(rows), book
def __lotus__(book, name):
   return book[name]
def __lily__(seed, text):
   used = set()
   func = __rune__(used, seed, b'lily')
   data = __chant__(text, seed + b'text')
   return __plume__(func), __prism__(func, data)
def __opal__(seed, raw):
   mix = repr((__flint__(seed + raw[:32] + b'opalflint', 2), __grout__(seed + raw[:32] + b'opalgrout', 3))).encode('ascii')
   fog = __mist__(seed + b'opal' + mix, len(raw) or 1)
   key = __spark__(seed + b'opalkey' + mix, 1, 255)
   rows = tuple(byte ^ fog[slot] ^ key for slot, byte in enumerate(raw))
   return rows, key, fog.hex(), __crown__(raw)
def __orchid__(name):
   return __iris__(name, 0)
__dripbag__ = {}
__dumpbag__ = {}
__tuffbag__ = {}
__shapebag__ = {}
__gaskbag__ = {}
__rawbag__ = {}
def __tuff__(code):
   mark = id(code); row = __tuffbag__.get(mark)
   if row is None:
        row = (code.co_code, code.co_consts, code.co_names, code.co_varnames, code.co_freevars, code.co_cellvars); __tuffbag__[mark] = row
        if len(__tuffbag__) > 2048: __tuffbag__.clear()
   return row
def __dump__(code):
   mark = id(code); row = __dumpbag__.get(mark)
   if row is None:
        row = marshal.dumps(code); __dumpbag__[mark] = row
        if len(__dumpbag__) > 2048: __dumpbag__.clear()
   return row
def __raw__(code):
   mark = id(code); row = __rawbag__.get(mark)
   if row is None:
        row = __vine__(__tuff__(code)); __rawbag__[mark] = row
        if len(__rawbag__) > 2048: __rawbag__.clear()
   return row
def __vine__(data):
   if isinstance(data, (list, tuple)): return b''.join(__vine__(one) for one in data)
   if isinstance(data, bytes): return data
   if isinstance(data, str): return data.encode('utf-8')
   if isinstance(data, int): return data.to_bytes(max(1, (data.bit_length() + 8) // 8), 'little', signed=True)
   if data is None: return b'N'
   if isinstance(data, float): return __import__('struct').pack('<d', data)
   if isinstance(data, bool): return b'T' if data else b'F'
   if isinstance(data, type(Ellipsis)): return b'E'
   if isinstance(data, complex): return __import__('struct').pack('<dd', data.real, data.imag)
   if isinstance(data, type((lambda: 1).__code__)): return __vine__(__tuff__(data))
   return str(data).encode('utf-8')
def __glow__(code):
   mark = 2166136261
   for one in __raw__(code): mark ^= one; mark *= 16777619; mark &= 0xffffffff
   return mark
def __drip__(code):
   root = id(code); hit = __dripbag__.get(root)
   if hit is not None: return hit
   kind = type(code); hold = [code]; seen = set(); rows = []
   while hold:
        one = hold.pop()
        if not isinstance(one, kind): continue
        mark = id(one)
        if mark in seen: continue
        seen.add(mark); rows.append(one)
        for item in one.co_consts:
             if isinstance(item, kind): hold.append(item)
   rows = tuple(rows); __dripbag__[root] = rows
   if len(__dripbag__) > 512: __dripbag__.clear()
   return rows
def __skulk__(code):
   return tuple((len(one.co_code), one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount, one.co_nlocals, one.co_stacksize, one.co_flags, len(one.co_consts), len(one.co_names), len(one.co_varnames), len(one.co_freevars), len(one.co_cellvars), one.co_firstlineno) for one in __drip__(code))
def __bloom__(code):
   mark = 1469598103934665603
   for row in __skulk__(code):
        for one in row: mark ^= one & 0xffffffffffffffff; mark *= 1099511628211; mark &= 0xffffffffffffffff
   return mark
def __torch__(code):
   rows = bytearray()
   for one in __drip__(code):
        rows.extend(len(one.co_code).to_bytes(4, 'little')); rows.extend(one.co_code); rows.extend(len(one.co_consts).to_bytes(4, 'little')); rows.extend(len(one.co_names).to_bytes(4, 'little')); rows.extend(len(one.co_varnames).to_bytes(4, 'little')); rows.extend(len(one.co_freevars).to_bytes(4, 'little')); rows.extend(len(one.co_cellvars).to_bytes(4, 'little'))
   return bytes(rows)
def __echo__(code):
   blob = __torch__(code); return (len(blob), hashlib.sha256(blob).hexdigest(), hashlib.sha1(blob).hexdigest(), zlib.adler32(blob), zlib.crc32(blob))
def __magma__(code):
   rows = []
   for one in __drip__(code):
        rows.extend((len(one.co_code), len(one.co_consts), len(one.co_names), len(one.co_varnames), len(one.co_freevars), len(one.co_cellvars), one.co_stacksize, one.co_flags))
   if not rows: return (0, 0, 0, 0, 0, 0)
   return (len(rows), sum(rows) & 0xffffffff, min(rows), max(rows), rows[0], rows[-1])
def __soul__(code):
   rows = []
   for one in __drip__(code): rows.extend(one.co_names); rows.extend(one.co_varnames)
   blob = __vine__(tuple(rows)); return (len(rows), hashlib.sha256(blob).hexdigest(), hashlib.sha1(blob).hexdigest())
def __wisp__(code):
   rows = []
   for one in __drip__(code): rows.append((one.co_name, one.co_filename, one.co_argcount, one.co_firstlineno, len(one.co_consts)))
   blob = __vine__(tuple(rows)); return (len(rows), hashlib.sha256(blob).hexdigest(), hashlib.sha1(blob).hexdigest())
def __gasket__(blob):
   hit = __gaskbag__.get(blob)
   if hit is not None: return hit
   rows = ((0, zlib.compress(blob, 1)), (0, zlib.compress(blob, 4)), (0, zlib.compress(blob, 6)), (0, zlib.compress(blob, 9)), (1, bz2.compress(blob, 9)), (2, lzma.compress(blob, format=lzma.FORMAT_ALONE, preset=3)))
   pick = min(rows, key=lambda row: (len(row[1]), row[0])); fast = min((row for row in rows if row[0] == 0), key=lambda row: len(row[1]))
   if len(fast[1]) <= (len(pick[1]) * 115) // 100: pick = fast
   out = bytes([pick[0]]) + pick[1]
   if len(__gaskbag__) > 1024: __gaskbag__.clear()
   __gaskbag__[blob] = out
   return out
def __weld__(blob, key):
   rows = bytearray(); glow = key & 255; drift = ((key >> 8) & 255) or 73; tint = ((key >> 16) & 255) or 19
   for slot, byte in enumerate(blob):
        glow = (glow + drift + slot + tint) & 255; rows.append(byte ^ glow ^ ((tint + slot) & 255))
   return bytes(rows)
def __snare__(blob, add, step): return bytes((byte + add + ((slot + 1) * step)) & 255 for slot, byte in enumerate(blob))
def __unsnare__(blob, add, step): return bytes((byte - add - ((slot + 1) * step)) & 255 for slot, byte in enumerate(blob))
def __whorl__(blob, spin):
   rows = bytearray(); spin &= 7
   for slot, byte in enumerate(blob):
        turn = (spin + slot) & 7; rows.append(byte if not turn else (((byte << turn) & 255) | (byte >> (8 - turn))))
   return bytes(rows)
def __unwhorl__(blob, spin):
   rows = bytearray(); spin &= 7
   for slot, byte in enumerate(blob):
        turn = (spin + slot) & 7; rows.append(byte if not turn else (((byte >> turn) | ((byte << (8 - turn)) & 255)) & 255))
   return bytes(rows)
def __spine__(blob, span):
   rows = []; slot = 0
   while slot < len(blob):
        rows.append(blob[slot:slot + span][::-1]); slot += span
   return b''.join(rows)
def __scald__(blob, salt):
   rows = bytearray(); tilt = (salt & 15) + 3
   for slot, byte in enumerate(blob):
        rows.append(byte ^ ((salt + slot * tilt) & 255))
   return bytes(rows)
def __pair__(blob):
   rows = bytearray(blob); slot = 0
   while slot + 1 < len(rows):
        rows[slot], rows[slot + 1] = rows[slot + 1], rows[slot]; slot += 2
   return bytes(rows)
def __shroud__(blob, salt):
   rows = bytearray(); tilt = ((salt >> 3) & 15) + 1
   for slot, byte in enumerate(blob):
        fog = byte ^ ((salt + slot * tilt + (slot >> 1)) & 255); rows.append(((fog << 4) & 240) | (fog >> 4))
   return bytes(rows)
def __unshroud__(blob, salt):
   rows = bytearray(); tilt = ((salt >> 3) & 15) + 1
   for slot, byte in enumerate(blob):
        fog = ((byte >> 4) | ((byte << 4) & 255)) & 255; rows.append(fog ^ ((salt + slot * tilt + (slot >> 1)) & 255))
   return bytes(rows)
def __ravel__(blob, span):
   rows = []; slot = 0; span = max(2, span)
   while slot < len(blob):
        part = blob[slot:slot + span]; rows.append(part[1::2] + part[::2]); slot += span
   return b''.join(rows)
def __unravel__(blob, span):
   rows = []; slot = 0; span = max(2, span)
   while slot < len(blob):
        part = blob[slot:slot + span]; left = part[:len(part) // 2]; right = part[len(part) // 2:]; out = bytearray(len(part)); out[::2] = right; out[1::2] = left
        rows.append(bytes(out)); slot += span
   return b''.join(rows)
def __thorn__(blob, span):
   rows = []; slot = 0; span = max(2, span); flip = 0
   while slot < len(blob):
        part = blob[slot:slot + span]; rows.append(part[::-1] if flip & 1 else part); slot += span; flip += 1
   return b''.join(rows)
def __crest__(blob):
   if not blob:
        return (0, 0, b'', b'')
   return (len(blob), sum(blob) & 0xffff, blob[:1], blob[-1:])
def __grain__(blob, span):
   rows = []; slot = 0
   while slot < len(blob):
        rows.append(__crest__(blob[slot:slot + span])); slot += span
   return rows
def __pulse__(rows):
   glow = 0; slot = 0
   for row in rows:
        glow = (glow + ((slot + 1) * ((row[1] or 1) & 0xffff))) & 0xffffffff; slot += 32
   return glow
def __first__(rows):
   return rows[0] if rows else (0, 0, b'', b'')
def __last__(rows):
   return rows[-1] if rows else (0, 0, b'', b'')
def __chaff__(blob):
   rows = __grain__(blob, 32)
   return (len(blob), len(rows), __first__(rows), __last__(rows), __pulse__(rows))
def __packa__(blob, slag, ashk, gritk, lavak, smeltk, veilk, weftk, thornk): return __pair__(__thorn__(__ravel__(__shroud__(__scald__(__whorl__(__snare__(__weld__(__gasket__(blob), slag), ashk, gritk), lavak), smeltk), veilk), weftk), thornk))
def __packb__(blob, smoke, crustk, emberk, cinderk, veilk, weftk, thornk): return __pair__(__thorn__(__ravel__(__shroud__(__snare__(__spine__(__weld__(__gasket__(blob), smoke), crustk), emberk, cinderk), veilk ^ 0x5A), weftk + 1), thornk + 1))
def __peeka__(blob, smoke, crustk, emberk, cinderk, veilk, weftk, thornk): peek=__weld__(__spine__(__unsnare__(__unshroud__(__unravel__(__thorn__(__pair__(blob), thornk + 1), weftk + 1), veilk ^ 0x5A), emberk, cinderk), crustk), smoke); way=peek[0]; return (zlib.decompress, bz2.decompress, lzma.decompress)[way](peek[1:])
def __peekb__(blob, slag, ashk, gritk, lavak, smeltk, veilk, weftk, thornk): return __weld__(__unsnare__(__unwhorl__(__scald__(__unshroud__(__unravel__(__thorn__(__pair__(blob), thornk), weftk), veilk), smeltk), lavak), ashk, gritk), slag)
def __corea__(blob, leftk, rightk, mistk, dustk, cloakk, lanek, spurk): return __thorn__(__ravel__(__shroud__(__snare__(__weld__(__gasket__(__weld__(blob, leftk)), rightk), mistk, dustk), cloakk), lanek), spurk)
def __coreb__(blob, leftk, rightk, mistk, dustk, cloakk, lanek, spurk): peek=__weld__(__unsnare__(__unshroud__(__unravel__(__thorn__(blob, spurk), lanek), cloakk), mistk, dustk), rightk); way=peek[0]; return __weld__((zlib.decompress, bz2.decompress, lzma.decompress)[way](peek[1:]), leftk)
def __wrapa__(blob, shellk, glassk, forgek, stampk): return __snare__(__weld__(__gasket__(__weld__(blob, shellk)), glassk), forgek, stampk)
def __wrapb__(blob, shellk, glassk, forgek, stampk): peek=__weld__(__unsnare__(blob, forgek, stampk), glassk); way=peek[0]; return __weld__((zlib.decompress, bz2.decompress, lzma.decompress)[way](peek[1:]), shellk)
def __nexus__(raw, seed, plan, face, loom):
    src = raw if isinstance(raw, bytes) else raw.encode('utf-8', 'replace')
    head = src[:4096]; tail = src[-4096:] if src else b''; size = len(src).to_bytes(8, 'little'); core = head + tail + size
    bag = bytearray(); bag.extend(hashlib.sha512(seed + core[:256]).digest()); bag.extend(hashlib.blake2b(core[:512] + seed, digest_size=64).digest()); bag.extend(hashlib.blake2s(seed + core[-512:], digest_size=32).digest())
    one = zlib.compress(core, 9); two = bz2.compress(core, 9); thr = lzma.compress(core, preset=6); best = min((one, two, thr, core), key=len); bag.extend(hashlib.sha512(best + seed).digest())
    hist = bytearray(256)
    for byte in core: hist[byte] = (hist[byte] + 1) & 255
    bag.extend(hist); bag.extend(zlib.crc32(src).to_bytes(4, 'little')); bag.extend(zlib.adler32(src).to_bytes(4, 'little'))
    view = repr((plan[:64] if isinstance(plan, tuple) else plan, face[:64] if isinstance(face, tuple) else face, loom[:64] if isinstance(loom, tuple) else loom)).encode('utf-8', 'replace')
    bag.extend(hashlib.sha512(view + seed).digest()); cur = hashlib.sha512(seed + bytes(bag[-256:]) + size).digest()
    funcs = (hashlib.sha512, hashlib.blake2b, hashlib.sha3_512, hashlib.sha256)
    for num in range(1, 521):
        fun = funcs[(num - 1) & 3]; win = 64 + ((num - 1) % 96); raw = cur + bag[-win:] + num.to_bytes(2, 'little')
        bit = fun(raw, digest_size=64).digest() if fun is hashlib.blake2b else fun(raw).digest(); cur = hashlib.blake2s(bit + cur + size, digest_size=32).digest(); bag.extend(cur)
    pack = zlib.compress(bytes(bag), 9); mark = marshal.dumps((len(src), len(best), zlib.crc32(pack) & 0xffffffff, hashlib.sha256(pack).digest()))
    return hashlib.sha512(pack + mark + cur + seed).digest()
def __mark__(code): return __glow__(code), __bloom__(code), __echo__(code), __magma__(code), __soul__(code), __wisp__(code)
def __keys__(seed, spec):
   return tuple(__spark__(seed + tag, low, high) for tag, low, high in spec)
def __brand__(blob):
    return hashlib.sha256(blob).hexdigest(), hashlib.sha1(blob).hexdigest(), hashlib.md5(blob).hexdigest(), __flare__(blob), zlib.adler32(blob) ^ zlib.crc32(blob)
def __carapace__(raw, seed, kind):
    salt = __mist__(seed + kind + b'salt', len(raw) or 1); off = __spark__(seed + kind + b'off', 0x3040, 0x30ff); lift = __spark__(seed + kind + b'lift', 0x120, 0x780); key = __spark__(seed + kind + b'key', 11, 251)
    wide = ''.join(chr((one ^ salt[slot]) + off) for slot, one in enumerate(raw)); ring = [((one ^ key) + lift) for one in raw]; text = raw.hex(); fog = __mist__(seed + kind + b'weave', len(text) or 1).hex()[:len(text)]
    weave = ''.join(one + two for one, two in zip(fog, text)); veil = base64.b85encode(bytes(one ^ salt[slot] for slot, one in enumerate(raw))).decode('ascii'); shot, coal, soot, ember, glass = __brand__(raw)
    mask = __mist__(seed + kind + b'mask', len(raw) or 1)
    glyph = ''.join(chr((one ^ mask[slot]) + off + 257) for slot, one in enumerate(raw))
    maze = ''.join(chr((one ^ mask[slot]) + off + 257) + chr(0x3041 + ((mask[slot] + one + slot) % 80)) for slot, one in enumerate(raw))
    cord = tuple((one + key + slot * 3) & 255 for slot, one in enumerate(raw))
    path = base64.b85encode(bytes((one + key + slot) & 255 for slot, one in enumerate(raw))).decode('ascii')
    crest = __crown__(raw)
    return (kind.decode('ascii'), wide, off, salt.hex(), weave, ring, lift, key, veil, shot, coal, soot, ember, glass, glyph, off + 257, mask.hex(), maze, cord, path, crest)
def __scarp__(text, seed):
    salt = __mist__(seed + b'scarp', 16)
    bag = []
    for slot, ch in enumerate(text.encode('utf-8')):
        bag.append(ch ^ salt[slot % 16])
    return bytes(bag), salt
def __mire__(text, seed):
    raw = text.encode('utf-8')
    fog = __mist__(seed + b'mire', len(raw) or 1)
    weave = bytearray()
    for slot, byte in enumerate(raw):
        weave.append(fog[slot] & 0xFF)
        weave.append(byte)
    return base64.b85encode(bytes(weave)).decode('ascii')
def __stone__(code, expected):
    glow = __glow__(code)
    bloom = __bloom__(code)
    echo = __echo__(code)
    magma = __magma__(code)
    soul = __soul__(code)
    wisp = __wisp__(code)
    actual = (glow, bloom, echo, magma, soul, wisp)
    if actual != expected:
        raise ValueError('integrity')
    return actual
def __gravel__(seed):
    ring = ((0x4e00, 0x9faf), (0x3041, 0x3096), (0x30a1, 0x30fa), (0xac00, 0xad00), (0x0400, 0x04ff))
    bag = []
    for slot in range(12):
        fog = hashlib.sha256(seed + b'gravel' + slot.to_bytes(2, 'little')).digest()
        left, right = ring[fog[0] % len(ring)]
        ch = chr(left + (int.from_bytes(fog[1:3], 'little') % (right - left + 1)))
        if ch.isidentifier():
            bag.append(ch)
    return ''.join(bag) if len(bag) >= 4 else 'ãªã«ã“ã‚Œ'
def __loam__(seed):
    fog = __mist__(seed + b'loam', 32)
    names = []
    ring = ((0x3041, 0x3096), (0x30a1, 0x30fa), (0x4e00, 0x9faf))
    for slot in range(4):
        left, right = ring[fog[slot * 2] % len(ring)]
        ch = chr(left + (fog[slot * 2 + 1] % (right - left + 1)))
        names.append(ch)
    return ''.join(names)
def __silt__(seed, depth):
    fog = __mist__(seed + b'silt', 8)
    off = int.from_bytes(fog[:4], 'little') % 100
    return depth + off
def __clay__(seed, modules):
    fog = __mist__(seed + b'clay', 32)
    bag = []
    for slot, mod in enumerate(modules):
        key = fog[slot % 32]
        bag.append((mod, key ^ len(mod)))
    return bag
def __marl__(name, seed):
    import unicodedata
    norm = unicodedata.normalize('NFKC', name)
    if norm != name:
        fog = __mist__(seed + b'marl' + name.encode('utf-8', 'replace'), 8)
        return norm, int.from_bytes(fog, 'little') & 0xFFFF
    return name, 0
def __quarry__(text, seed):
    raw = text.encode('utf-8')
    fog = __mist__(seed + b'quarry', len(raw) or 1)
    bag = bytearray()
    for slot, byte in enumerate(raw):
        bag.append((byte ^ fog[slot]) & 0xFF)
    return base64.b85encode(zlib.compress(bytes(bag), 9)).decode('ascii'), fog.hex()
def __coral__(seed, count):
    ring = ((0x4e00, 0x9faf), (0x3041, 0x3096), (0x30a1, 0x30fa), (0xac00, 0xd7a3), (0x0400, 0x04ff), (0x0370, 0x03ff), (0x10a0, 0x10ff), (0x0900, 0x097f), (0x0e00, 0x0e7f))
    fog = __mist__(seed + b'reefgen', count * 3)
    bag = []
    for slot in range(count):
        left, right = ring[fog[slot * 3] % len(ring)]
        ch = chr(left + (int.from_bytes(fog[slot * 3 + 1:slot * 3 + 3], 'little') % (right - left + 1)))
        bag.append(ch)
    return ''.join(bag)
def __desert__(seed, depth):
    bag = []
    for slot in range(depth):
        fog = __mist__(seed + b'dunegen' + slot.to_bytes(2, 'little'), 16)
        val = int.from_bytes(fog[:8], 'little') & 0x7FFFFFFF
        bag.append(val)
    return tuple(bag)
def __shrine__(seed, text):
    raw = text.encode('utf-8')
    fog = __mist__(seed + b'cairngen', len(raw) or 1)
    return bytes(b ^ fog[s % len(fog)] for s, b in enumerate(raw))
def __hill__(seed, width):
    ring = ((0x4e00, 0x9faf), (0x3041, 0x3096), (0x30a1, 0x30fa), (0xac00, 0xd7a3))
    fog = __mist__(seed + b'knollgen', width * 4)
    bag = []
    for slot in range(width):
        left, right = ring[fog[slot * 4] % len(ring)]
        ch = chr(left + (int.from_bytes(fog[slot * 4 + 1:slot * 4 + 4], 'little') % (right - left + 1)))
        bag.append(ch)
    return ''.join(bag)
def __pebble__(seed, count, width):
    ring = ((0x4e00, 0x9faf), (0x3041, 0x3096), (0x30a1, 0x30fa), (0xac00, 0xd7a3), (0x0400, 0x04ff), (0x0370, 0x03ff), (0x10a0, 0x10ff), (0x0900, 0x097f), (0x0e00, 0x0e7f), (0x0980, 0x09ff), (0x0a00, 0x0a7f), (0x0b00, 0x0b7f), (0x0c00, 0x0c7f), (0x0d00, 0x0d7f), (0x1200, 0x137f))
    bag = []
    for row in range(count):
        fog = __mist__(seed + b'pebble' + row.to_bytes(4, 'little'), width * 3)
        text = []
        for slot in range(width):
            left, right = ring[fog[slot * 3] % len(ring)]
            ch = chr(left + (int.from_bytes(fog[slot * 3 + 1:slot * 3 + 3], 'little') % (right - left + 1)))
            text.append(ch)
        bag.append(''.join(text))
    return bag
def __cobble__(data, seed, layers):
    raw = data if isinstance(data, bytes) else data.encode('utf-8')
    for layer in range(layers):
        fog = __mist__(seed + b'cobble' + layer.to_bytes(2, 'little'), len(raw) or 1)
        raw = bytes(b ^ fog[s % len(fog)] for s, b in enumerate(raw))
        raw = zlib.compress(raw, 9)
    return base64.b85encode(raw).decode('ascii')
def __shingle__(seed, length):
    zwj = '\u200d'
    zwnj = '\u200c'
    fog = __mist__(seed + b'shingle', length)
    bag = []
    for slot in range(length):
        bag.append(zwj if fog[slot] & 1 else zwnj)
    return ''.join(bag)
def __rubble__(seed, count):
    templates = [
        lambda s, i: ''.join(chr(__spark__(s + b'cjk' + i.to_bytes(2, 'little') + j.to_bytes(2, 'little'), 0x4e00, 0x9faf)) for j in range(8)),
        lambda s, i: ''.join(chr(__spark__(s + b'kor' + i.to_bytes(2, 'little') + j.to_bytes(2, 'little'), 0xac00, 0xd7a3)) for j in range(6)),
        lambda s, i: ''.join(chr(__spark__(s + b'grk' + i.to_bytes(2, 'little') + j.to_bytes(2, 'little'), 0x0370, 0x03ff)) for j in range(10)),
        lambda s, i: ''.join(chr(__spark__(s + b'cyr' + i.to_bytes(2, 'little') + j.to_bytes(2, 'little'), 0x0400, 0x04ff)) for j in range(7)),
        lambda s, i: ''.join(chr(__spark__(s + b'thai' + i.to_bytes(2, 'little') + j.to_bytes(2, 'little'), 0x0e00, 0x0e7f)) for j in range(9)),
        lambda s, i: ''.join(chr(__spark__(s + b'beng' + i.to_bytes(2, 'little') + j.to_bytes(2, 'little'), 0x0980, 0x09ff)) for j in range(5)),
        lambda s, i: ''.join(chr(__spark__(s + b'ethi' + i.to_bytes(2, 'little') + j.to_bytes(2, 'little'), 0x1200, 0x137f)) for j in range(8)),
        lambda s, i: ''.join(chr(__spark__(s + b'geo' + i.to_bytes(2, 'little') + j.to_bytes(2, 'little'), 0x10a0, 0x10ff)) for j in range(6)),
    ]
    bag = []
    for slot in range(count):
        tmpl = templates[slot % len(templates)]
        bag.append(tmpl(seed, slot))
    return bag
def __rime__(seed, used, slot):
    name = __rune__(used, seed + b'name', slot.to_bytes(4, 'little'))
    text = __coral__(seed + b'text' + slot.to_bytes(4, 'little'), 6 + (slot % 5))
    mask = __shingle__(seed + b'zero' + slot.to_bytes(4, 'little'), 3 + (slot % 4))
    key = __spark__(seed + b'num' + slot.to_bytes(4, 'little'), 1000, 999999)
    fog = __mist__(seed + b'fog' + slot.to_bytes(4, 'little'), len(text.encode('utf-8', 'replace')) or 1)
    return name, text, mask, key, fog.hex()
def __sleet__(seed, used, count):
    rows = []
    for slot in range(count):
        rows.append(__rime__(seed, used, slot))
    return rows
def __frill__(name, text, mask, key, fog):
    rows = []
    rows.append(f"{name}=({text!r},{mask!r},{key},{fog!r})")
    rows.append(f"{name}=(lambda {name}:{name})({name})")
    return rows
def __lumen__(seed, used, slot):
    name = __rune__(used, seed + b'lumen', slot.to_bytes(4, 'little'))
    text = __coral__(seed + b'lumenrow' + slot.to_bytes(4, 'little'), 4 + (slot % 7))
    vals = tuple(ord(ch) for ch in text)
    return name, vals
def __thatch__(name, vals):
    text = ''.join(chr(val) for val in vals)
    return [f"{name}={text!r}", f"{name}=(lambda {name}:{name})({name})"]
def __mote__(seed, used, slot):
    left = __rune__(used, seed + b'left', slot.to_bytes(4, 'little'))
    right = __rune__(used, seed + b'right', slot.to_bytes(4, 'little'))
    mark = __rune__(used, seed + b'mark', slot.to_bytes(4, 'little'))
    a = __spark__(seed + b'a' + slot.to_bytes(4, 'little'), 10000, 999999)
    b = __spark__(seed + b'b' + slot.to_bytes(4, 'little'), 10000, 999999)
    while a == b:
        b = __spark__(seed + b'c' + slot.to_bytes(4, 'little') + b.to_bytes(4, 'little'), 10000, 999999)
    c = a ^ b
    return f"(lambda {left},{right},{mark}:({left}^{right})=={mark} or (_ for _ in ()).throw(SystemExit))({a},{b},{c})"
def __spool__(seed, count):
    used = set()
    rows = []
    for name, text, mask, key, fog in __sleet__(seed + b'sleet', used, count):
        rows.extend(__frill__(name, text, mask, key, fog))
    for slot in range(count // 2):
        name, vals = __lumen__(seed + b'lumen', used, slot)
        rows.extend(__thatch__(name, vals))
    for slot in range(count // 3):
        rows.append(__mote__(seed + b'mote', used, slot))
    return rows
def __spray__(seed, count):
    return ';'.join(__spool__(seed, count))
def __flint__(seed, depth):
    fog = __mist__(seed + b'flint', depth * 8)
    bag = []
    for slot in range(depth):
        val = int.from_bytes(fog[slot * 8:(slot + 1) * 8], 'little') & 0x7FFFFFFFFFFFFFFF
        bag.append(val)
    return tuple(bag)
def __basalt__(seed, count, used):
    bag = []
    mint = [0]
    for slot in range(count):
        name = __mint__(used, seed + b'basaltgen' + slot.to_bytes(4, 'little'), mint)
        bag.append(name)
    return bag
def __chalk__(seed, depth):
    bag = []
    prev = seed
    for slot in range(depth):
        h = hashlib.sha256(prev + slot.to_bytes(4, 'little')).digest()
        bag.append(h.hex())
        prev = h
    return bag
def __marble__(seed, count):
    scripts = ((0x4e00, 0x9faf, 'CJK'), (0x3041, 0x3096, 'Hiragana'), (0x30a1, 0x30fa, 'Katakana'), (0xac00, 0xd7a3, 'Korean'), (0x0400, 0x04ff, 'Cyrillic'), (0x0370, 0x03ff, 'Greek'), (0x0900, 0x097f, 'Devanagari'), (0x0e00, 0x0e7f, 'Thai'), (0x0980, 0x09ff, 'Bengali'), (0x0f00, 0x0fff, 'Tibetan'), (0x1000, 0x109f, 'Myanmar'), (0x1200, 0x137f, 'Ethiopic'), (0x10a0, 0x10ff, 'Georgian'), (0x13a0, 0x13ff, 'Cherokee'), (0x1400, 0x167f, 'UCAS'), (0x1700, 0x171f, 'Tagalog'), (0x1780, 0x17ff, 'Khmer'), (0x1680, 0x169f, 'Ogham'), (0x16a0, 0x16ff, 'Runic'))
    bag = []
    for slot in range(count):
        fog = __mist__(seed + b'slategen' + slot.to_bytes(4, 'little'), 16);mix = __grout__(seed + b'slatemix' + slot.to_bytes(4, 'little'), 4);left, right, name = scripts[(fog[0] ^ mix[0]) % len(scripts)];width = 4 + ((fog[1] ^ mix[1]) % 6)
        bag.append((''.join(chr(left + ((int.from_bytes(fog[2 + char * 2:4 + char * 2], 'little') ^ mix[char & 3]) % (right - left + 1))) for char in range(width)), name))
    return bag
def __mortar__(seed, data):
    fog = __mist__(seed + b'mortar', 32)
    red = int.from_bytes(fog[:8], 'little')
    blue = int.from_bytes(fog[8:16], 'little')
    green = int.from_bytes(fog[16:24], 'little')
    raw = data if isinstance(data, bytes) else data.encode('utf-8')
    zinc = bytes(b ^ ((red >> (s % 64)) & 0xFF) for s, b in enumerate(raw))
    iron = bytes(b ^ ((blue >> (s % 64)) & 0xFF) for s, b in enumerate(zinc))
    gold = bytes(b ^ ((green >> (s % 64)) & 0xFF) for s, b in enumerate(iron))
    return gold, (red, blue, green)
def __grout__(seed, count):
    fog = __mist__(seed + b'grout', count * 4)
    bag = []
    for slot in range(count):
        val = int.from_bytes(fog[slot * 4:(slot + 1) * 4], 'little')
        bag.append(val)
    return bag
def __render__(seed, text):
    raw = text.encode('utf-8')
    fog = __mist__(seed + b'render', len(raw) + 16)
    xored = bytes(b ^ fog[s] for s, b in enumerate(raw))
    compressed = zlib.compress(xored, 9)
    return base64.b85encode(compressed).decode('ascii'), fog[:len(raw)].hex()
def __temper__(seed, value):
    fog = __mist__(seed + b'temper', 16)
    sand = int.from_bytes(fog[:4], 'little') | 1
    rock = int.from_bytes(fog[4:8], 'little')
    dust = int.from_bytes(fog[8:12], 'little')
    encoded = ((value * sand) + rock) ^ dust
    return encoded, (sand, rock, dust)
def __anneal__(seed, items):
    fog = __mist__(seed + b'anneal', len(items) * 2 + 16)
    perm = list(range(len(items)))
    for slot in range(len(perm) - 1, 0, -1):
        j = int.from_bytes(fog[slot * 2:slot * 2 + 2], 'little') % (slot + 1)
        perm[slot], perm[j] = perm[j], perm[slot]
    shuffled = [items[i] for i in perm]
    return shuffled, perm
def __batch__(paths, seed):
    bag = []
    for slot, path in enumerate(paths):
        fog = __mist__(seed + b'forgebatch' + slot.to_bytes(4, 'little'), 32)
        key = int.from_bytes(fog[:8], 'little')
        bag.append((path, key))
    return bag
def __kiln__(seed, depth, width):
    bag = []
    for layer in range(depth):
        row = []
        for slot in range(width):
            fog = __mist__(seed + b'kilngen' + layer.to_bytes(2, 'little') + slot.to_bytes(2, 'little'), 8)
            val = int.from_bytes(fog, 'little') & 0xFFFFFFFF
            row.append(val)
        bag.append(tuple(row))
    return tuple(bag)
def __metadata__(seed):
    watermarks = __pebble__(seed + b'meta', 3, 8)
    chain = __chalk__(seed + b'meta', 5)
    traps = __flint__(seed + b'meta', 6)
    marks = __shingle__(seed + b'meta', 16)
    stones = __marble__(seed + b'meta', 4)
    rubble = __rubble__(seed + b'meta', 4)
    grout = __grout__(seed + b'meta', 8)
    return (watermarks, chain, traps, marks, stones, rubble, grout)
def __clasp__(clay):
    bag = bytearray()
    for mod, key in clay:
        raw = mod.encode('utf-8', 'replace')
        bag.extend(len(raw).to_bytes(2, 'little'))
        bag.extend(raw)
        bag.append(key & 255)
    return bytes(bag)
def __plain__(desert):
    bag = bytearray()
    for val in desert:
        bag.extend(int(val).to_bytes(8, 'little', signed=False))
    return bytes(bag)
def __cline__(hill):
    raw = hill.encode('utf-8', 'replace')
    bag = bytearray()
    for slot, byte in enumerate(raw):
        bag.append(byte ^ ((slot * 29 + len(raw)) & 255))
    return bytes(bag)
def __amber__(mortar, trio):
    bag = bytearray(mortar)
    for val in trio:
        bag.extend(int(val).to_bytes(8, 'little', signed=False))
    return bytes(bag)
def __lacquer__(render, shade):
    raw = render.encode('ascii', 'ignore') + shade.encode('ascii', 'ignore')
    bag = bytearray()
    for slot, byte in enumerate(raw):
        bag.append(((byte << (slot & 3)) | (byte >> (8 - (slot & 3)))) & 255 if slot & 3 else byte)
    return bytes(bag)
def __alloy__(temper, metal):
    bag = bytearray()
    bag.extend(int(temper & ((1 << 96) - 1)).to_bytes(12, 'little', signed=False))
    for val in metal:
        bag.extend(int(val).to_bytes(4, 'little', signed=False))
    return bytes(bag)
def __shuffle__(anneal, perm):
    bag = bytearray()
    for val in anneal:
        if isinstance(val, str): bag.extend(val.encode('utf-8', 'replace'))
        elif isinstance(val, int): bag.extend(int(val).to_bytes(4, 'little', signed=False))
        else: bag.extend(repr(val).encode('utf-8', 'replace'))
        bag.append(0)
    for val in perm:
        bag.extend(int(val).to_bytes(2, 'little', signed=False))
    return bytes(bag)
def __relic__(meta):
    bag = bytearray()
    for row in meta:
        raw = __vine__(row)
        bag.extend(len(raw).to_bytes(4, 'little'))
        bag.extend(hashlib.sha256(raw).digest())
        bag.extend(raw[:64])
    return bytes(bag)
def __petal__(blob):
    bag = bytearray()
    for slot in range(0, len(blob), 32):
        row = blob[slot:slot + 32]
        bag.extend(len(row).to_bytes(2, 'little'))
        bag.extend((sum(row) & 0xffff).to_bytes(2, 'little'))
        bag.extend(hashlib.blake2s(row, digest_size=8).digest())
    return bytes(bag)
def __grainmap__(blob):
    bag = bytearray()
    for step in (3, 5, 7, 11):
        glow = 0
        for slot, byte in enumerate(blob[::step][:512]):
            glow = (glow + ((slot + 1) * (byte + step))) & 0xffffffff
            glow = ((glow << 3) | (glow >> 29)) & 0xffffffff
        bag.extend(glow.to_bytes(4, 'little'))
    return bytes(bag)
def __ribbon__(blob):
    bag = bytearray()
    for slot in range(0, min(len(blob), 4096), 64):
        row = blob[slot:slot + 64]
        left = row[:32]
        right = row[32:]
        bag.extend(hashlib.blake2s(left, digest_size=8).digest())
        bag.extend(hashlib.blake2s(right, digest_size=8).digest())
        bag.extend((sum(left) ^ sum(right)).to_bytes(2, 'little'))
    return bytes(bag)
def __needle__(blob):
    bag = bytearray()
    top = {}
    for byte in blob[:8192]:
        top[byte] = top.get(byte, 0) + 1
    for byte, count in sorted(top.items(), key=lambda row: (-row[1], row[0]))[:32]:
        bag.append(byte)
        bag.extend(count.to_bytes(2, 'little'))
    return bytes(bag)
def __pin__(blob):
    bag = bytearray()
    head = blob[:256]
    tail = blob[-256:]
    for slot, pair in enumerate((head, tail, blob[::2][:256], blob[1::2][:256])):
        bag.extend(slot.to_bytes(1, 'little'))
        bag.extend(len(pair).to_bytes(2, 'little'))
        bag.extend(hashlib.sha1(pair).digest()[:10])
        bag.extend(hashlib.blake2s(pair, digest_size=6).digest())
        bag.extend((zlib.crc32(pair) & 0xffffffff).to_bytes(4, 'little'))
    return bytes(bag)
def __braid__(tree):
    bag = bytearray()
    rows = [type(one).__name__ for one in ast.walk(tree)]
    for slot in range(0, min(len(rows), 2048) - 1):
        raw = (rows[slot] + '>' + rows[slot + 1]).encode('utf-8', 'replace')
        bag.extend(zlib.crc32(raw).to_bytes(4, 'little'))
    return bytes(bag)
def __tangle__(code):
    bag = bytearray()
    for one in __drip__(code):
        raw = one.co_code
        bag.extend(len(raw).to_bytes(4, 'little'))
        bag.extend(hashlib.blake2s(raw[:128], digest_size=16).digest())
        bag.extend(len(one.co_consts).to_bytes(2, 'little'))
        bag.extend(len(one.co_names).to_bytes(2, 'little'))
    return bytes(bag)
def __knot__(tree, code, stem):
    part = (__braid__(tree), __tangle__(code), __grainmap__(stem), __ribbon__(stem), __needle__(stem), __pin__(stem))
    raw = b''.join(len(one).to_bytes(4, 'little') + one for one in part)
    return hashlib.sha512(raw).digest() + raw[:512]
def __resin__(seed, parts):
    raw = b''.join(len(part).to_bytes(4, 'little') + part for part in parts)
    fog = hashlib.sha512(seed + raw).digest()
    for slot, part in enumerate(parts):
        fog = hashlib.sha512(fog + slot.to_bytes(2, 'little') + hashlib.sha256(part).digest()).digest()
    return fog + hashlib.blake2b(raw, digest_size=64).digest()
def __permute__(seed):
    fog = bytearray(__mist__(seed + b'permute', 1024))
    tab = list(range(256))
    for slot in range(255, 0, -1):
        at = fog[slot] ^ fog[(slot * 7) & 1023] ^ fog[(slot * 13) & 1023]
        pick = at % (slot + 1)
        tab[slot], tab[pick] = tab[pick], tab[slot]
    return bytes(tab)
def __mirror__(tab):
    inv = [0] * 256
    for slot, byte in enumerate(tab):
        inv[byte] = slot
    return bytes(inv)
def __stride__(seed, raw):
    fog = __mist__(seed + raw[:64], 32)
    return ((fog[0] | 1), (fog[1] | 1), fog[2], fog[3], int.from_bytes(fog[4:8], 'little') | 1, int.from_bytes(fog[8:12], 'little') | 1)
def __codex__(seed, clay, desert, hill, mortar, trio, render, shade, temper, metal, anneal, perm, meta, stem, knot):
    parts = (__clasp__(clay), __plain__(desert), __cline__(hill), __amber__(mortar, trio), __lacquer__(render, shade), __alloy__(temper, metal), __shuffle__(anneal, perm), __relic__(meta), __petal__(stem), knot)
    root = __resin__(seed, parts)
    tab = __permute__(root)
    inv = __mirror__(tab)
    pace = __stride__(root, stem)
    salt = hashlib.sha512(root + tab + stem[:128]).digest()
    sig = hashlib.sha256(tab + inv + salt + __vine__(pace)).hexdigest()
    return (tab, inv, salt, pace, sig)
def __veil__(blob, plan):
    tab, inv, salt, pace, sig = plan
    add, step, twist, turn, drift, mask = pace
    rows = bytearray()
    glow = drift & 255
    for slot, byte in enumerate(blob):
        key = salt[slot % len(salt)]
        glow = (glow + add + slot * step + key) & 255
        val = byte ^ glow ^ ((mask >> (slot & 7)) & 255)
        val = (val + twist + ((slot * turn) & 255)) & 255
        rows.append(tab[val])
    return bytes(rows)
def __unveil__(blob, plan):
    tab, inv, salt, pace, sig = plan
    add, step, twist, turn, drift, mask = pace
    rows = bytearray()
    glow = drift & 255
    for slot, byte in enumerate(blob):
        key = salt[slot % len(salt)]
        glow = (glow + add + slot * step + key) & 255
        val = inv[byte]
        val = (val - twist - ((slot * turn) & 255)) & 255
        rows.append(val ^ glow ^ ((mask >> (slot & 7)) & 255))
    return bytes(rows)
def __seal__(plan):
    tab, inv, salt, pace, sig = plan
    return (base64.b85encode(tab).decode('ascii'), base64.b85encode(inv).decode('ascii'), base64.b85encode(salt).decode('ascii'), pace, sig)
def __audit__(plan):
    tab, inv, salt, pace, sig = plan
    if len(tab) != 256 or len(inv) != 256 or len(salt) < 16:
        raise ValueError('codex')
    if tuple(inv[tab[slot]] for slot in range(256)) != tuple(range(256)):
        raise ValueError('codex')
    if __mirror__(tab) != inv:
        raise ValueError('codex')
    if sorted(tab) != list(range(256)) or sorted(inv) != list(range(256)):
        raise ValueError('codex')
    if hashlib.sha256(tab + inv + salt + __vine__(pace)).hexdigest() != sig:
        raise ValueError('codex')
    probe = bytes(range(256))
    if __unveil__(__veil__(probe, plan), plan) != probe:
        raise ValueError('codex')
    return sig
def __facet__(tree, code, stem, plan, seed):
    rows = []
    tab, inv, salt, pace, sig = plan
    rows.append((len(tab), len(set(tab)), len(inv), len(set(inv))))
    rows.append((zlib.crc32(tab) & 0xffffffff, zlib.adler32(inv) & 0xffffffff, zlib.crc32(salt) & 0xffffffff))
    rows.append(tuple(pace))
    rows.append(sig)
    rows.append(__shapeid__(tree, seed + b'facet'))
    rows.append(__op__(code, seed + b'facet'))
    rows.append((len(stem), hashlib.sha256(stem[:2048]).hexdigest()))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __loom__(tree, code, stem, seed, clay, desert, hill, mortar, trio, render, shade, temper, metal, anneal, perm, meta):
    knot = __knot__(tree, code, stem)
    plan = __codex__(seed, clay, desert, hill, mortar, trio, render, shade, temper, metal, anneal, perm, meta, stem, knot)
    sig = __audit__(plan)
    face = __facet__(tree, code, stem, plan, seed)
    raw = __vine__((sig, face, knot, __seal__(plan)))
    mark = hashlib.sha512(seed + raw).digest()
    return plan, face, mark
def __mix__(seed, row):
    if not isinstance(row, bytes):
        row = __vine__(row)
    return hashlib.blake2b(seed + row, digest_size=32).digest()
def __hist__(rows):
    bag = {}
    for one in rows:
        bag[one] = bag.get(one, 0) + 1
    return tuple(sorted(bag.items(), key=lambda row: (str(row[0]), row[1])))
def __shape__(tree):
    mark = id(tree); row = __shapebag__.get(mark)
    if row is None:
        row = __hist__(type(node).__name__ for node in ast.walk(tree)); __shapebag__[mark] = row
        if len(__shapebag__) > 128: __shapebag__.clear()
    return row
def __walk__(tree):
    bag = []
    edge = []
    deep = []
    hold = [(tree, 0, 'root')]
    while hold:
        node, depth, name = hold.pop()
        kind = type(node).__name__
        bag.append(kind)
        deep.append((kind, depth, name))
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in reversed(value):
                    if isinstance(item, ast.AST):
                        edge.append((kind, field, type(item).__name__))
                        hold.append((item, depth + 1, field))
            elif isinstance(value, ast.AST):
                edge.append((kind, field, type(value).__name__))
                hold.append((value, depth + 1, field))
    return tuple(bag), tuple(edge), tuple(deep)
def __shapeid__(tree, seed):
    bag, edge, deep = __walk__(tree)
    wide = max((row[1] for row in deep), default=0)
    head = tuple(row[0] for row in deep[:32])
    tail = tuple(row[0] for row in deep[-32:])
    fog = __mix__(seed, (__hist__(bag), __hist__(edge), wide, head, tail))
    return (len(bag), len(edge), wide, zlib.crc32(__vine__(head)) & 0xffffffff, zlib.adler32(__vine__(tail)) & 0xffffffff, fog.hex())
def __literal__(tree, seed):
    nums = []
    texts = []
    raw = []
    flags = [0, 0, 0, 0]
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            val = node.value
            raw.append(type(val).__name__)
            if isinstance(val, str):
                texts.append((len(val), zlib.crc32(val.encode('utf-8', 'replace')) & 0xffffffff))
            elif isinstance(val, bytes):
                texts.append((len(val), zlib.crc32(val) & 0xffffffff))
            elif isinstance(val, bool):
                flags[0 if val else 1] += 1
            elif isinstance(val, int):
                nums.append((val.bit_length(), val & 0xffff, (val >> 16) & 0xffff))
            elif isinstance(val, float):
                flags[2] += 1
            elif isinstance(val, complex):
                flags[3] += 1
    fog = __mix__(seed, (tuple(nums[:256]), tuple(texts[:256]), __hist__(raw), tuple(flags), len(nums), len(texts)))
    return (len(nums), len(texts), tuple(flags), __hist__(raw), fog.hex())
def __label__(tree, seed):
    load = []
    store = []
    attr = []
    call = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Store):
                store.append(node.id)
            elif isinstance(node.ctx, ast.Load):
                load.append(node.id)
        elif isinstance(node, ast.Attribute):
            attr.append(node.attr)
        elif isinstance(node, ast.Call):
            call.append(type(node.func).__name__)
    fog = __mix__(seed, (__hist__(load), __hist__(store), __hist__(attr), __hist__(call), len(load), len(store), len(attr), len(call)))
    return (len(set(load)), len(set(store)), len(set(attr)), len(call), fog.hex())
def __flow__(tree, seed):
    bag = []
    span = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.IfExp)):
            bag.append('if')
        elif isinstance(node, (ast.For, ast.AsyncFor)):
            bag.append('for')
        elif isinstance(node, ast.While):
            bag.append('while')
        elif isinstance(node, ast.Try):
            bag.append('try'); span.append((len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody)))
        elif isinstance(node, (ast.With, ast.AsyncWith)):
            bag.append('with'); span.append((len(node.items), len(node.body)))
        elif isinstance(node, (ast.Match,)):
            bag.append('match'); span.append((len(node.cases), 0))
        elif isinstance(node, (ast.BoolOp, ast.Compare)):
            bag.append(type(node).__name__)
    fog = __mix__(seed, (__hist__(bag), tuple(span[:256]), len(bag), len(span)))
    return (len(bag), len(span), __hist__(bag), fog.hex())
def __op__(code, seed):
    raw = bytearray()
    freq = {}
    steps = []
    for one in __drip__(code):
        data = one.co_code
        raw.extend(data)
        steps.append((len(data), one.co_stacksize, one.co_flags, len(one.co_consts), len(one.co_names)))
        for byte in data:
            freq[byte] = freq.get(byte, 0) + 1
    pairs = {}
    data = bytes(raw)
    for i in range(max(0, len(data) - 1)):
        pair = data[i] << 8 | data[i + 1]
        pairs[pair] = pairs.get(pair, 0) + 1
    top = tuple(sorted(freq.items(), key=lambda row: (-row[1], row[0]))[:64])
    chain = tuple(sorted(pairs.items(), key=lambda row: (-row[1], row[0]))[:64])
    fog = __mix__(seed, (top, chain, tuple(steps), len(data), zlib.crc32(data) & 0xffffffff, zlib.adler32(data) & 0xffffffff))
    return (len(data), top, chain, tuple(steps), fog.hex())
def __constant__(code, seed):
    kind = []
    lens = []
    nums = []
    for one in __drip__(code):
        for val in one.co_consts:
            kind.append(type(val).__name__)
            if isinstance(val, (str, bytes)):
                lens.append(len(val))
            elif isinstance(val, int):
                nums.append((val.bit_length(), val & 0xffff))
            elif isinstance(val, type(one)):
                lens.append(len(val.co_code))
    fog = __mix__(seed, (__hist__(kind), tuple(lens[:512]), tuple(nums[:512]), len(kind)))
    return (len(kind), __hist__(kind), tuple(lens[:128]), fog.hex())
def __call__(tree, seed):
    bag = []
    argc = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            argc.append((len(node.args), len(node.keywords)))
            if isinstance(node.func, ast.Name):
                bag.append(('n', node.func.id))
            elif isinstance(node.func, ast.Attribute):
                bag.append(('a', node.func.attr))
            else:
                bag.append(('x', type(node.func).__name__))
    fog = __mix__(seed, (__hist__(bag), tuple(argc[:512]), len(bag)))
    return (len(bag), __hist__(bag), tuple(argc[:128]), fog.hex())
def __scope__(tree, seed):
    funcs = []
    cls = []
    args = []
    deco = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            funcs.append((node.name, len(node.body), len(node.decorator_list), len(node.args.args), len(node.args.kwonlyargs)))
            args.extend(one.arg for one in node.args.args + node.args.kwonlyargs)
            node.args.vararg and args.append(node.args.vararg.arg)
            node.args.kwarg and args.append(node.args.kwarg.arg)
            deco.extend(type(one).__name__ for one in node.decorator_list)
        elif isinstance(node, ast.ClassDef):
            cls.append((node.name, len(node.body), len(node.bases), len(node.decorator_list)))
    fog = __mix__(seed, (tuple(funcs), tuple(cls), __hist__(args), __hist__(deco)))
    return (len(funcs), len(cls), __hist__(args), fog.hex())
def __module__(tree, seed):
    bag = []
    alias = []
    levels = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for one in node.names:
                bag.append(one.name)
                alias.append(one.asname or '')
        elif isinstance(node, ast.ImportFrom):
            bag.append(node.module or '')
            levels.append(node.level)
            for one in node.names:
                alias.append((one.name, one.asname or ''))
    fog = __mix__(seed, (__hist__(bag), __hist__(alias), tuple(levels), len(bag)))
    return (len(bag), len(alias), __hist__(bag), fog.hex())
def __set__(tree, seed):
    bag = []
    dims = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            bag.append(('assign', len(node.targets)))
            dims.append((len(node.targets), type(node.value).__name__))
        elif isinstance(node, ast.AnnAssign):
            bag.append(('ann', int(node.value is not None)))
            dims.append((1, type(node.annotation).__name__))
        elif isinstance(node, ast.AugAssign):
            bag.append(('aug', type(node.op).__name__))
            dims.append((1, type(node.value).__name__))
        elif isinstance(node, ast.NamedExpr):
            bag.append(('walrus', type(node.value).__name__))
    fog = __mix__(seed, (__hist__(bag), tuple(dims[:512]), len(dims)))
    return (len(bag), tuple(dims[:128]), fog.hex())
def __sub__(tree, seed):
    bag = []
    dims = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript):
            bag.append(type(node.slice).__name__)
            dims.append((type(node.value).__name__, type(node.slice).__name__, type(node.ctx).__name__))
        elif isinstance(node, ast.Slice):
            dims.append((int(node.lower is not None), int(node.upper is not None), int(node.step is not None)))
    fog = __mix__(seed, (__hist__(bag), tuple(dims[:512]), len(dims)))
    return (len(bag), tuple(dims[:128]), fog.hex())
def __bin__(tree, seed):
    bag = []
    unary = []
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp):
            bag.append((type(node.op).__name__, type(node.left).__name__, type(node.right).__name__))
        elif isinstance(node, ast.UnaryOp):
            unary.append(type(node.op).__name__)
    fog = __mix__(seed, (__hist__(bag), __hist__(unary), len(bag), len(unary)))
    return (len(bag), len(unary), __hist__(bag), fog.hex())
def __cmp__(tree, seed):
    bag = []
    lens = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare):
            bag.append(tuple(type(one).__name__ for one in node.ops))
            lens.append(len(node.comparators))
    fog = __mix__(seed, (__hist__(bag), tuple(lens), len(bag)))
    return (len(bag), __hist__(bag), fog.hex())
def __form__(tree, seed):
    bag = []
    spec = []
    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr):
            bag.append(len(node.values))
        elif isinstance(node, ast.FormattedValue):
            spec.append((node.conversion, type(node.value).__name__, int(node.format_spec is not None)))
    fog = __mix__(seed, (tuple(bag[:512]), tuple(spec[:512]), len(bag), len(spec)))
    return (len(bag), len(spec), tuple(spec[:128]), fog.hex())
def __trap__(tree, seed):
    bag = []
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            bag.append((len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody)))
        elif isinstance(node, ast.ExceptHandler):
            names.append((type(node.type).__name__ if node.type else '', node.name or '', len(node.body)))
        elif isinstance(node, ast.Raise):
            names.append(('raise', type(node.exc).__name__ if node.exc else '', type(node.cause).__name__ if node.cause else ''))
    fog = __mix__(seed, (tuple(bag[:256]), tuple(names[:256]), len(bag), len(names)))
    return (len(bag), len(names), fog.hex())
def __pat__(tree, seed):
    bag = []
    vals = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Match):
            bag.append(('match', len(node.cases)))
        elif type(node).__name__.startswith('Match'):
            bag.append(type(node).__name__)
            if hasattr(node, 'name'):
                vals.append(getattr(node, 'name') or '')
            if hasattr(node, 'rest'):
                vals.append(getattr(node, 'rest') or '')
    fog = __mix__(seed, (__hist__(bag), __hist__(vals), len(bag)))
    return (len(bag), __hist__(bag), fog.hex())
def __ret__(tree, seed):
    bag = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Return):
            bag.append(('return', type(node.value).__name__ if node.value else ''))
        elif isinstance(node, ast.Yield):
            bag.append(('yield', type(node.value).__name__ if node.value else ''))
        elif isinstance(node, ast.YieldFrom):
            bag.append(('yieldfrom', type(node.value).__name__))
        elif isinstance(node, ast.Await):
            bag.append(('await', type(node.value).__name__))
    fog = __mix__(seed, (__hist__(bag), len(bag)))
    return (len(bag), __hist__(bag), fog.hex())
def __loop__(tree, seed):
    bag = []
    marks = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.For, ast.AsyncFor)):
            bag.append(('for', type(node.target).__name__, type(node.iter).__name__, len(node.body), len(node.orelse)))
        elif isinstance(node, ast.While):
            bag.append(('while', type(node.test).__name__, len(node.body), len(node.orelse)))
        elif isinstance(node, (ast.Break, ast.Continue)):
            marks.append(type(node).__name__)
    fog = __mix__(seed, (tuple(bag[:256]), __hist__(marks), len(bag), len(marks)))
    return (len(bag), len(marks), fog.hex())
def __comp__(tree, seed):
    bag = []
    gens = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            bag.append((type(node).__name__, len(node.generators)))
            for gen in node.generators:
                gens.append((type(gen.target).__name__, type(gen.iter).__name__, len(gen.ifs), int(gen.is_async)))
    fog = __mix__(seed, (tuple(bag[:256]), tuple(gens[:512]), len(bag), len(gens)))
    return (len(bag), len(gens), fog.hex())
def __ann__(tree, seed):
    bag = []
    for node in ast.walk(tree):
        if isinstance(node, ast.arg) and node.annotation is not None:
            bag.append(('arg', node.arg, type(node.annotation).__name__))
        elif isinstance(node, ast.AnnAssign):
            bag.append(('ann', type(node.target).__name__, type(node.annotation).__name__))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.returns is not None:
            bag.append(('ret', node.name, type(node.returns).__name__))
    fog = __mix__(seed, (__hist__(bag), len(bag)))
    return (len(bag), __hist__(bag), fog.hex())
def __line__(code, seed):
    bag = []
    pos = []
    for one in __drip__(code):
        bag.append((one.co_firstlineno, len(one.co_linetable), len(one.co_exceptiontable)))
        try:
            for item in one.co_positions():
                pos.append(tuple(-1 if v is None else v for v in item))
        except:
            pass
    fog = __mix__(seed, (tuple(bag), tuple(pos[:1024]), len(pos)))
    return (len(bag), len(pos), fog.hex())
def __free__(code, seed):
    bag = []
    names = []
    for one in __drip__(code):
        bag.append((len(one.co_freevars), len(one.co_cellvars), len(one.co_varnames), len(one.co_names)))
        names.extend(one.co_freevars)
        names.extend(one.co_cellvars)
    fog = __mix__(seed, (tuple(bag), __hist__(names), len(names)))
    return (len(bag), len(set(names)), fog.hex())
def __window__(code, seed):
    bag = []
    for one in __drip__(code):
        data = one.co_code
        for at in range(0, max(0, len(data) - 3), 2):
            bag.append(data[at:at + 4])
            if len(bag) >= 2048:
                break
        if len(bag) >= 2048:
            break
    fog = __mix__(seed, (tuple(bag), len(bag)))
    return (len(bag), zlib.crc32(b''.join(bag)) & 0xffffffff if bag else 0, fog.hex())
def __ref__(tree, seed):
    pairs = []
    stack = [(tree, '')]
    while stack:
        node, last = stack.pop()
        now = type(node).__name__
        if last:
            pairs.append((last, now))
        for child in ast.iter_child_nodes(node):
            stack.append((child, now))
    fog = __mix__(seed, (__hist__(pairs), len(pairs)))
    return (len(pairs), __hist__(pairs), fog.hex())
def __depth__(tree, seed):
    levels = {}
    hold = [(tree, 0)]
    while hold:
        node, depth = hold.pop()
        levels[depth] = levels.get(depth, 0) + 1
        for child in ast.iter_child_nodes(node):
            hold.append((child, depth + 1))
    rows = tuple(sorted(levels.items()))
    fog = __mix__(seed, rows)
    return (len(rows), rows, fog.hex())
def __tile__(tree, seed):
    bag = []
    rows = list(ast.walk(tree))
    for at in range(0, max(0, len(rows) - 2), 3):
        bag.append(tuple(type(one).__name__ for one in rows[at:at + 3]))
        if len(bag) >= 1024:
            break
    fog = __mix__(seed, (__hist__(bag), len(rows)))
    return (len(rows), len(bag), fog.hex())
def __vmap__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount, one.co_nlocals, one.co_stacksize, one.co_flags))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), tuple(rows[:256]), fog.hex())
def __pool__(code, seed):
    names = []
    vars = []
    files = []
    for one in __drip__(code):
        names.extend(one.co_names)
        vars.extend(one.co_varnames)
        files.append((one.co_name, one.co_filename))
    fog = __mix__(seed, (__hist__(names), __hist__(vars), __hist__(files)))
    return (len(set(names)), len(set(vars)), len(files), fog.hex())
def __salt__(tree, code, seed):
    a = __depth__(tree, seed + b'a')
    b = __tile__(tree, seed + b'b')
    c = __vmap__(code, seed + b'c')
    d = __pool__(code, seed + b'd')
    return __mix__(seed + b'salt', (a, b, c, d))
def __context__(tree, seed):
    bag = []
    for node in ast.walk(tree):
        ctx = getattr(node, 'ctx', None)
        if ctx is not None:
            bag.append((type(node).__name__, type(ctx).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(bag), len(bag)))
    return (len(bag), __hist__(bag), fog.hex())
def __discard__(tree, seed):
    bag = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Delete):
            bag.append(('del', len(node.targets), tuple(type(one).__name__ for one in node.targets)))
        elif isinstance(node, ast.Pass):
            bag.append(('pass', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Assert):
            bag.append(('assert', type(node.test).__name__, type(node.msg).__name__ if node.msg else ''))
        elif isinstance(node, ast.Expr):
            bag.append(('expr', type(node.value).__name__))
        elif isinstance(node, (ast.Break, ast.Continue)):
            bag.append((type(node).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(bag), len(bag)))
    return (len(bag), __hist__(bag), fog.hex())
def __wth__(tree, seed):
    bag = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.With, ast.AsyncWith)):
            for item in node.items:
                bag.append((type(item.context_expr).__name__, type(item.optional_vars).__name__ if item.optional_vars else '', len(node.body)))
    fog = __mix__(seed, (__hist__(bag), len(bag)))
    return (len(bag), __hist__(bag), fog.hex())
def __body__(tree, seed):
    bag = []
    for node in ast.walk(tree):
        body = getattr(node, 'body', None)
        if isinstance(body, list):
            bag.append((type(node).__name__, len(body), tuple(type(one).__name__ for one in body[:8])))
        orelse = getattr(node, 'orelse', None)
        if isinstance(orelse, list) and orelse:
            bag.append((type(node).__name__ + 'else', len(orelse), tuple(type(one).__name__ for one in orelse[:8])))
    fog = __mix__(seed, (tuple(bag[:1024]), len(bag)))
    return (len(bag), tuple(bag[:128]), fog.hex())
def __ring__(tree, code, seed):
    left = __context__(tree, seed + b'l')
    right = __discard__(tree, seed + b'r')
    mid = __wth__(tree, seed + b'm')
    core = __body__(tree, seed + b'c')
    bits = []
    for one in __drip__(code):
        bits.append((hashlib.sha1(one.co_code).hexdigest(), len(one.co_consts), len(one.co_names)))
    fog = __mix__(seed, (left, right, mid, core, tuple(bits)))
    return (len(bits), fog.hex())
def __ord__(code, seed):
    rows = []
    for one in __drip__(code):
        names = tuple((slot, name, len(name), zlib.crc32(name.encode('utf-8', 'replace')) & 0xffffffff) for slot, name in enumerate(one.co_names))
        vars = tuple((slot, name, len(name), zlib.adler32(name.encode('utf-8', 'replace')) & 0xffffffff) for slot, name in enumerate(one.co_varnames))
        const = []
        for slot, val in enumerate(one.co_consts):
            if isinstance(val, (str, bytes)):
                raw = val.encode('utf-8', 'replace') if isinstance(val, str) else val
                const.append((slot, type(val).__name__, len(raw), zlib.crc32(raw) & 0xffffffff))
            elif isinstance(val, int):
                const.append((slot, 'int', val.bit_length(), val & 0xffffffff))
            else:
                const.append((slot, type(val).__name__, 0, 0))
        rows.append((one.co_name, names[:128], vars[:128], tuple(const[:128])))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __glyph__(tree, seed):
    import unicodedata as uni
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name): rows.append(node.id)
        elif isinstance(node, ast.Attribute): rows.append(node.attr)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)): rows.append(node.name)
        elif isinstance(node, ast.arg): rows.append(node.arg)
        elif isinstance(node, ast.alias): rows.append(node.asname or node.name)
    bag = []
    for name in rows:
        cat = []
        for ch in name[:64]:
            try: cat.append((uni.category(ch), uni.name(ch).split()[0], ord(ch) & 0xff))
            except: cat.append(('?', '?', ord(ch) & 0xff))
        bag.append((len(name), tuple(cat)))
    wide = sum(any(ord(ch) > 127 for ch in name) for name in rows)
    high = max((len(name) for name in rows), default=0)
    fog = __mix__(seed, (__hist__(bag), len(rows), len(set(rows)), wide, high))
    return (len(rows), len(set(rows)), wide, high, fog.hex())
def __alph__(tree, seed):
    text = []
    raw = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str): text.append(node.value)
        elif isinstance(node, ast.Constant) and isinstance(node.value, bytes): raw.append(node.value)
    bag = []
    for val in text[:512]:
        enc = base64.b85encode(zlib.compress(val.encode('utf-8', 'replace'), 6))
        bag.append((len(val), __hist__(val[:128]), __hist__(enc[:128]), zlib.crc32(enc) & 0xffffffff))
    for val in raw[:512]:
        enc = base64.b85encode(zlib.compress(val, 6))
        bag.append((len(val), __hist__(val[:128]), __hist__(enc[:128]), zlib.adler32(enc) & 0xffffffff))
    fog = __mix__(seed, (__hist__(bag), len(text), len(raw)))
    return (len(text), len(raw), fog.hex())
def __span__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        rows.append((type(node).__name__, getattr(node, 'lineno', 0), getattr(node, 'col_offset', 0), getattr(node, 'end_lineno', 0) or 0, getattr(node, 'end_col_offset', 0) or 0))
    fog = __mix__(seed, (tuple(rows[:2048]), len(rows), __hist__((row[0], row[3] - row[1], row[4] - row[2]) for row in rows)))
    return (len(rows), fog.hex())
def __gram__(tree, seed):
    rows = [type(one).__name__ for one in ast.walk(tree)]
    pair = tuple(zip(rows, rows[1:]))[:2048]
    trio = tuple(zip(rows, rows[1:], rows[2:]))[:2048]
    fog = __mix__(seed, (__hist__(pair), __hist__(trio), len(rows)))
    return (len(rows), fog.hex())
def __tok__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name): rows.append(('name', node.id, type(node.ctx).__name__))
        elif isinstance(node, ast.Attribute): rows.append(('attr', node.attr, type(node.ctx).__name__))
        elif isinstance(node, ast.alias): rows.append(('alias', node.name, node.asname or ''))
        elif isinstance(node, ast.arg): rows.append(('arg', node.arg, type(node.annotation).__name__ if node.annotation else ''))
    fog = __mix__(seed, (__hist__(rows), len(rows), len(set(rows))))
    return (len(rows), len(set(rows)), fog.hex())
def __atom__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            val = node.value
            if isinstance(val, str): rows.append(('s', len(val), zlib.crc32(val.encode('utf-8', 'replace')) & 0xffffffff, val[:32]))
            elif isinstance(val, bytes): rows.append(('b', len(val), zlib.crc32(val) & 0xffffffff, val[:32]))
            elif isinstance(val, int): rows.append(('i', val.bit_length(), val & 0xffffffff, (val >> 32) & 0xffffffff))
            elif isinstance(val, float): rows.append(('f', repr(val)))
            elif isinstance(val, complex): rows.append(('c', repr(val.real), repr(val.imag)))
            elif isinstance(val, bool): rows.append(('bool', int(val)))
            elif val is None: rows.append(('none', 0))
            elif val is Ellipsis: rows.append(('dots', 0))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __num__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            val = node.value; rows.append((val.bit_length(), val & 255, (val >> 8) & 255, int(val < 0), zlib.crc32(str(val).encode()) & 0xffffffff))
    fog = __mix__(seed, (tuple(rows[:1024]), __hist__(row[0] for row in rows), len(rows)))
    return (len(rows), fog.hex())
def __txt__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            val = node.value; rows.append((len(val), val.count('\n'), val.count('{'), val.count('}'), val.count('%'), val[:16], val[-16:]))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __bop__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp): rows.append((type(node.op).__name__, type(node.left).__name__, type(node.right).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.BoolOp): rows.append((type(node.op).__name__, len(node.values), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.UnaryOp): rows.append((type(node.op).__name__, type(node.operand).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __cmpr__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare):
            rows.append((type(node.left).__name__, tuple(type(one).__name__ for one in node.ops), tuple(type(one).__name__ for one in node.comparators), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __dial__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name): head = ('n', node.func.id)
            elif isinstance(node.func, ast.Attribute): head = ('a', node.func.attr, type(node.func.value).__name__)
            else: head = ('x', type(node.func).__name__)
            rows.append((head, len(node.args), tuple(one.arg or '*' for one in node.keywords), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __asgn__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign): rows.append(('assign', len(node.targets), tuple(type(one).__name__ for one in node.targets), type(node.value).__name__))
        elif isinstance(node, ast.AnnAssign): rows.append(('ann', type(node.target).__name__, type(node.annotation).__name__, type(node.value).__name__ if node.value else ''))
        elif isinstance(node, ast.AugAssign): rows.append(('aug', type(node.target).__name__, type(node.op).__name__, type(node.value).__name__))
        elif isinstance(node, ast.NamedExpr): rows.append(('named', type(node.target).__name__, type(node.value).__name__))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __river__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.If): rows.append(('if', type(node.test).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.While): rows.append(('while', type(node.test).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.For, ast.AsyncFor)): rows.append(('for', type(node.target).__name__, type(node.iter).__name__, len(node.body), len(node.orelse)))
        elif isinstance(node, ast.IfExp): rows.append(('ifexp', type(node.test).__name__, type(node.body).__name__, type(node.orelse).__name__))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __catch__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Try): rows.append(('try', len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody)))
        elif isinstance(node, ast.ExceptHandler): rows.append(('except', type(node.type).__name__ if node.type else '', node.name or '', len(node.body)))
        elif isinstance(node, ast.Raise): rows.append(('raise', type(node.exc).__name__ if node.exc else '', type(node.cause).__name__ if node.cause else ''))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __mask__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.With, ast.AsyncWith)):
            for item in node.items: rows.append((type(item.context_expr).__name__, type(item.optional_vars).__name__ if item.optional_vars else '', len(node.body), int(isinstance(node, ast.AsyncWith))))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __coil__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp)): rows.append((type(node).__name__, type(node.elt).__name__, len(node.generators)))
        elif isinstance(node, ast.DictComp): rows.append(('DictComp', type(node.key).__name__, type(node.value).__name__, len(node.generators)))
        elif isinstance(node, ast.comprehension): rows.append(('gen', type(node.target).__name__, type(node.iter).__name__, len(node.ifs), int(node.is_async)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __fmt__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr): rows.append(('join', len(node.values), tuple(type(one).__name__ for one in node.values)))
        elif isinstance(node, ast.FormattedValue): rows.append(('fmt', node.conversion, type(node.value).__name__, type(node.format_spec).__name__ if node.format_spec else ''))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __match__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Match): rows.append(('match', type(node.subject).__name__, len(node.cases)))
        elif isinstance(node, ast.match_case): rows.append(('case', type(node.pattern).__name__, type(node.guard).__name__ if node.guard else '', len(node.body)))
        elif type(node).__name__.startswith('Match'): rows.append((type(node).__name__, getattr(node, 'name', '') or '', getattr(node, 'rest', '') or ''))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __imp__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for one in node.names: rows.append(('import', one.name, one.asname or ''))
        elif isinstance(node, ast.ImportFrom):
            for one in node.names: rows.append(('from', node.module or '', node.level, one.name, one.asname or ''))
    fog = __mix__(seed, (__hist__(rows), len(rows), len(set(rows))))
    return (len(rows), len(set(rows)), fog.hex())
def __func__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            rows.append((node.name, int(isinstance(node, ast.AsyncFunctionDef)), len(node.body), len(node.decorator_list), len(node.args.defaults), len(node.args.kw_defaults), type(node.returns).__name__ if node.returns else ''))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __arg__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            arg = node.args
            rows.append((len(arg.posonlyargs), len(arg.args), len(arg.kwonlyargs), int(arg.vararg is not None), int(arg.kwarg is not None), len(arg.defaults), len(arg.kw_defaults)))
            rows.extend(('a', one.arg, type(one.annotation).__name__ if one.annotation else '') for one in arg.posonlyargs + arg.args + arg.kwonlyargs)
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __clan__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            rows.append((node.name, len(node.bases), len(node.keywords), len(node.decorator_list), len(node.body), tuple(type(one).__name__ for one in node.body[:16])))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __deco__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            rows.extend((type(one).__name__, getattr(node, 'name', ''), getattr(one, 'id', getattr(one, 'attr', ''))) for one in node.decorator_list)
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __anno__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.arg) and node.annotation: rows.append(('arg', node.arg, type(node.annotation).__name__))
        elif isinstance(node, ast.AnnAssign): rows.append(('ann', type(node.target).__name__, type(node.annotation).__name__, int(node.simple)))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.returns: rows.append(('ret', node.name, type(node.returns).__name__))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __out__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Return): rows.append(('return', type(node.value).__name__ if node.value else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Yield): rows.append(('yield', type(node.value).__name__ if node.value else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.YieldFrom): rows.append(('yieldfrom', type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Await): rows.append(('await', type(node.value).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __slice__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript): rows.append(('sub', type(node.value).__name__, type(node.slice).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Slice): rows.append(('slice', int(node.lower is not None), int(node.upper is not None), int(node.step is not None)))
        elif isinstance(node, ast.Starred): rows.append(('star', type(node.value).__name__, type(node.ctx).__name__))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __seq__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)): rows.append((type(node).__name__, len(node.elts), type(getattr(node, 'ctx', None)).__name__, tuple(type(one).__name__ for one in node.elts[:32])))
        elif isinstance(node, ast.Dict): rows.append(('Dict', len(node.keys), tuple(type(one).__name__ if one else '' for one in node.keys[:32]), tuple(type(one).__name__ for one in node.values[:32])))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __paper__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            doc = ast.get_docstring(node, clean=False)
            rows.append((type(node).__name__, getattr(node, 'name', ''), len(doc or ''), zlib.crc32((doc or '').encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __lineage__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if hasattr(node, 'lineno'):
            rows.append((type(node).__name__, node.lineno, getattr(node, 'end_lineno', node.lineno), getattr(node, 'col_offset', 0), getattr(node, 'end_col_offset', 0) or 0))
    diff = tuple((row[0], row[2] - row[1], row[4] - row[3]) for row in rows[:2048])
    fog = __mix__(seed, (__hist__(diff), len(rows)))
    return (len(rows), fog.hex())
def __tree__(tree, seed):
    rows = []
    hold = [(tree, 0, 'root')]
    while hold:
        node, depth, field = hold.pop()
        child = list(ast.iter_child_nodes(node))
        rows.append((type(node).__name__, depth, field, len(child)))
        for one in reversed(child): hold.append((one, depth + 1, type(node).__name__))
    fog = __mix__(seed, (tuple(rows[:4096]), len(rows), max((row[1] for row in rows), default=0)))
    return (len(rows), fog.hex())
def __leaf__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        child = list(ast.iter_child_nodes(node))
        if not child: rows.append((type(node).__name__, getattr(node, 'lineno', 0), getattr(node, 'col_offset', 0)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __edge__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        for field, val in ast.iter_fields(node):
            if isinstance(val, ast.AST): rows.append((type(node).__name__, field, type(val).__name__))
            elif isinstance(val, list):
                rows.extend((type(node).__name__, field, type(one).__name__) for one in val if isinstance(one, ast.AST))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __order__(tree, seed):
    rows = []
    for slot, node in enumerate(ast.walk(tree)):
        rows.append((slot & 2047, type(node).__name__, getattr(node, 'lineno', 0), getattr(node, 'col_offset', 0)))
        if slot > 4096: break
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __nom__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name): rows.append((node.id, len(node.id), zlib.crc32(node.id.encode('utf-8', 'replace')) & 0xffffffff, type(node.ctx).__name__))
    fog = __mix__(seed, (__hist__(rows), len(rows), len(set(row[0] for row in rows))))
    return (len(rows), fog.hex())
def __attr__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            rows.append((node.attr, len(node.attr), zlib.adler32(node.attr.encode('utf-8', 'replace')) & 0xffffffff, type(node.value).__name__, type(node.ctx).__name__))
    fog = __mix__(seed, (__hist__(rows), len(rows), len(set(row[0] for row in rows))))
    return (len(rows), fog.hex())
def __kwd__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.keyword): rows.append((node.arg or '*', type(node.value).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __place__(tree, seed):
    rows = []
    stack = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)):
            stack.append(type(node).__name__)
            body = getattr(node, 'body', [])
            rows.append((type(node).__name__, getattr(node, 'name', ''), len(stack), len(body) if isinstance(body, list) else 1))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __sym__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Global): rows.append(('global', tuple(node.names)))
        elif isinstance(node, ast.Nonlocal): rows.append(('nonlocal', tuple(node.names)))
        elif isinstance(node, ast.Name): rows.append(('use', node.id, type(node.ctx).__name__))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __api__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ('getattr', 'setattr', 'hasattr', 'delattr', '__import__', 'eval', 'exec', 'compile', 'open'): rows.append((node.func.id, len(node.args), len(node.keywords)))
            elif isinstance(node.func, ast.Attribute) and node.func.attr in ('format', 'join', 'append', 'extend', 'update', 'items', 'keys', 'values'): rows.append((node.func.attr, type(node.func.value).__name__, len(node.args)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __lit__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            val = node.value
            rows.append((type(val).__name__, len(repr(val)), zlib.crc32(repr(val).encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __blend__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        rows.append((type(node).__name__, len(list(ast.iter_child_nodes(node))), getattr(node, 'lineno', 0), getattr(node, 'col_offset', 0)))
    a = zlib.crc32(__vine__(tuple(rows[:2048]))) & 0xffffffff
    b = zlib.adler32(__vine__(tuple(rows[-2048:]))) & 0xffffffff
    fog = __mix__(seed, (a, b, len(rows), __hist__(row[0] for row in rows)))
    return (len(rows), a, b, fog.hex())
def __block__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        body = getattr(node, 'body', None)
        if isinstance(body, list): rows.append((type(node).__name__, len(body), tuple(type(one).__name__ for one in body[:24])))
        final = getattr(node, 'finalbody', None)
        if isinstance(final, list) and final: rows.append((type(node).__name__ + 'final', len(final), tuple(type(one).__name__ for one in final[:24])))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __expr__(tree, seed):
    rows = []
    pick = (ast.Lambda, ast.IfExp, ast.Dict, ast.Set, ast.List, ast.Tuple, ast.Subscript, ast.Attribute, ast.Call, ast.Compare, ast.BoolOp, ast.BinOp, ast.UnaryOp)
    for node in ast.walk(tree):
        if isinstance(node, pick): rows.append((type(node).__name__, getattr(node, 'lineno', 0), len(list(ast.iter_child_nodes(node)))))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __stmt__(tree, seed):
    rows = []
    pick = (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.For, ast.AsyncFor, ast.While, ast.If, ast.With, ast.AsyncWith, ast.Try, ast.Return, ast.Raise, ast.Delete, ast.Assert, ast.Expr)
    for node in ast.walk(tree):
        if isinstance(node, pick): rows.append((type(node).__name__, getattr(node, 'lineno', 0), len(list(ast.iter_child_nodes(node)))))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __hash__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        body = ast.dump(node, include_attributes=False)
        rows.append((type(node).__name__, len(body), hashlib.sha1(body.encode('utf-8', 'replace')).hexdigest()[:16]))
        if len(rows) >= 2048: break
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __trace__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        rows.append((type(node).__name__, getattr(node, 'lineno', 0) or 0, getattr(node, 'end_lineno', 0) or 0))
    head = tuple(rows[:128])
    tail = tuple(rows[-128:])
    fog = __mix__(seed, (head, tail, len(rows), zlib.crc32(__vine__(tuple(rows))) & 0xffffffff))
    return (len(rows), fog.hex())
def __sig__(code, seed):
    rows = []
    for one in __drip__(code):
        tab = one.co_linetable if hasattr(one, 'co_linetable') else getattr(one, 'co_lnotab', b''); exc = getattr(one, 'co_exceptiontable', b'')
        arg = (one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount, one.co_nlocals, one.co_stacksize, one.co_flags)
        raw = (hashlib.sha256(one.co_code).hexdigest(), hashlib.sha1(tab).hexdigest(), hashlib.sha1(exc).hexdigest())
        con = tuple((slot, type(val).__name__, len(val.co_code) if isinstance(val, type(one)) else len(val) if isinstance(val, (str, bytes, tuple)) else val.bit_length() if isinstance(val, int) else 0) for slot, val in enumerate(one.co_consts[:128]))
        rows.append((getattr(one, 'co_qualname', one.co_name), one.co_name, one.co_filename, one.co_firstlineno, arg, raw, con, tuple(one.co_freevars), tuple(one.co_cellvars)))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __ctor__(code, seed):
    rows = []
    kind = type(code)
    for one in __drip__(code):
        tab = one.co_linetable if hasattr(one, 'co_linetable') else getattr(one, 'co_lnotab', b'')
        exc = getattr(one, 'co_exceptiontable', b'')
        args = (one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount, one.co_nlocals, one.co_stacksize, one.co_flags)
        cols = (len(one.co_code), len(one.co_consts), len(one.co_names), len(one.co_varnames), len(one.co_freevars), len(one.co_cellvars), len(tab), len(exc))
        refs = tuple((slot, len(val.co_code), len(val.co_consts), len(val.co_names)) for slot, val in enumerate(one.co_consts[:96]) if isinstance(val, kind))
        vals = tuple((slot, type(val).__name__, len(val) if isinstance(val, (str, bytes, tuple)) else val.bit_length() if isinstance(val, int) else 0) for slot, val in enumerate(one.co_consts[:96]) if not isinstance(val, kind))
        rows.append((one.co_name, getattr(one, 'co_qualname', one.co_name), args, cols, hashlib.sha256(one.co_code + tab + exc).hexdigest(), refs, vals))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows), sys.version_info[:2]))
    return (len(rows), fog.hex())
def __made__(code, seed):
    rows = []
    kind = type(code)
    for one in __drip__(code):
        ok = int(callable(getattr(one, 'replace', None)))
        try:
            new = one.replace(co_code=one.co_code) if ok else one
            same = int(isinstance(new, kind) and new.co_code == one.co_code and new.co_consts == one.co_consts)
        except Exception:
            same = 0
        raw = __dump__(one); rows.append((one.co_name, kind.__name__, ok, same, len(raw), zlib.crc32(raw[:4096]) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __byte__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((len(one.co_code), one.co_stacksize, one.co_flags, one.co_nlocals, one.co_firstlineno, hashlib.sha256(one.co_code).hexdigest()))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __blob__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code
        rows.append((len(data), zlib.crc32(data) & 0xffffffff, zlib.adler32(data) & 0xffffffff, tuple(data[:64]), tuple(data[-64:])))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __opcode__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code
        rows.extend((data[i], data[i + 1] if i + 1 < len(data) else 0) for i in range(0, min(len(data), 512), 2))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __quad__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code
        for i in range(0, max(0, min(len(data), 1024) - 3), 4): rows.append(tuple(data[i:i + 4]))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __const__(code, seed):
    rows = []
    kind = type(code)
    for one in __drip__(code):
        for slot, val in enumerate(one.co_consts[:256]):
            if isinstance(val, kind): rows.append((slot, 'code', len(val.co_code), len(val.co_consts), len(val.co_names)))
            elif isinstance(val, str): rows.append((slot, 'str', len(val), zlib.crc32(val.encode('utf-8', 'replace')) & 0xffffffff))
            elif isinstance(val, bytes): rows.append((slot, 'bytes', len(val), zlib.crc32(val) & 0xffffffff))
            elif isinstance(val, int): rows.append((slot, 'int', val.bit_length(), val & 0xffffffff))
            else: rows.append((slot, type(val).__name__, len(repr(val)), zlib.crc32(repr(val).encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __nam__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.extend((slot, name, len(name), zlib.crc32(name.encode('utf-8', 'replace')) & 0xffffffff) for slot, name in enumerate(one.co_names))
    fog = __mix__(seed, (__hist__(rows), len(rows), len(set(row[1] for row in rows))))
    return (len(rows), fog.hex())
def __var__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.extend((one.co_name, slot, name, len(name), one.co_argcount, one.co_nlocals, zlib.adler32((one.co_name + ':' + name).encode('utf-8', 'replace')) & 0xffffffff) for slot, name in enumerate(one.co_varnames))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows), len(set(row[2] for row in rows))))
    return (len(rows), fog.hex())
def __cell__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.extend(('free', slot, name) for slot, name in enumerate(one.co_freevars))
        rows.extend(('cell', slot, name) for slot, name in enumerate(one.co_cellvars))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __tab__(code, seed):
    rows = []
    for one in __drip__(code):
        tab = getattr(one, 'co_linetable', getattr(one, 'co_lnotab', b''))
        rows.append((one.co_firstlineno, len(tab), zlib.crc32(tab) & 0xffffffff, tuple(tab[:128])))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __except__(code, seed):
    rows = []
    for one in __drip__(code):
        exc = getattr(one, 'co_exceptiontable', b'')
        rows.append((len(exc), zlib.crc32(exc) & 0xffffffff, tuple(exc[:128])))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __coord__(code, seed):
    rows = []
    for one in __drip__(code):
        try:
            rows.extend(tuple(-1 if val is None else val for val in pos) for pos in list(one.co_positions())[:512])
        except:
            rows.append(('no', one.co_name))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __fname__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((one.co_filename, one.co_name, getattr(one, 'co_qualname', one.co_name), one.co_firstlineno))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __argv__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount, one.co_nlocals, len(one.co_varnames), len(one.co_names)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __flag__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((one.co_flags, one.co_stacksize, one.co_nlocals, one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __mar__(code, seed):
    rows = []
    for one in __drip__(code):
        raw = __dump__(one)
        rows.append((len(raw), zlib.crc32(raw) & 0xffffffff, hashlib.sha1(raw).hexdigest()))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __slot__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((len(one.co_consts), len(one.co_names), len(one.co_varnames), len(one.co_freevars), len(one.co_cellvars), len(one.co_code)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __ordr__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.extend((one.co_name, slot, byte) for slot, byte in enumerate(one.co_code[:512]))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __pack__(code, seed):
    rows = []
    for one in __drip__(code):
        data = __raw__(one)
        rows.append((one.co_name, len(data), zlib.crc32(data) & 0xffffffff, zlib.adler32(data) & 0xffffffff))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __dig__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((hashlib.sha256(__raw__(one)).hexdigest(), hashlib.sha1(one.co_code).hexdigest(), one.co_name))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __pond__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((one.co_name, tuple(one.co_names[:128]), tuple(one.co_varnames[:128]), tuple(one.co_freevars), tuple(one.co_cellvars)))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __stk__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((one.co_name, one.co_stacksize, len(one.co_code), sum(one.co_code) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __qual__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((getattr(one, 'co_qualname', one.co_name), len(getattr(one, 'co_qualname', one.co_name)), zlib.crc32(getattr(one, 'co_qualname', one.co_name).encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __size__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((one.co_name, len(__dump__(one)), len(one.co_code), len(one.co_consts), len(one.co_names), len(one.co_varnames)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __rng__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code
        rows.append((one.co_name, min(data) if data else 0, max(data) if data else 0, len(set(data)), len(data)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __duo__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code
        rows.extend((data[i], data[i + 1]) for i in range(0, min(len(data) - 1, 1024), 2))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __tri__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code
        rows.extend((data[i], data[i + 1], data[i + 2]) for i in range(0, min(len(data) - 2, 1024), 3))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __oct__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code
        rows.extend(tuple(data[i:i + 8]) for i in range(0, max(0, min(len(data), 1024) - 7), 8))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __cnt__(code, seed):
    rows = []
    kind = type(code)
    for one in __drip__(code):
        rows.append((one.co_name, sum(1 for val in one.co_consts if isinstance(val, kind)), sum(1 for val in one.co_consts if isinstance(val, str)), sum(1 for val in one.co_consts if isinstance(val, int))))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __dep__(code, seed):
    rows = []
    for pos, one in enumerate(__drip__(code)):
        rows.append((pos, one.co_name, len(one.co_code), len(one.co_consts), len(one.co_names), one.co_firstlineno))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __kind__(code, seed):
    rows = []
    for one in __drip__(code):
        vals = []
        for val in one.co_consts[:64]:
            vals.append(type(val).__name__)
        rows.append((one.co_name, tuple(vals), zlib.crc32(__vine__(tuple(vals))) & 0xffffffff))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __pak__(code, seed):
    rows = []
    for one in __drip__(code):
        raw = __dump__(one)
        pack = __gasket__(raw)
        rows.append((one.co_name, len(raw), len(pack), pack[0], hashlib.sha1(pack).hexdigest()))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __trail__(code, seed):
    rows = []
    for one in __drip__(code):
        blob = (one.co_name + '|' + one.co_filename + '|' + getattr(one, 'co_qualname', one.co_name)).encode('utf-8', 'replace')
        rows.append((len(blob), zlib.crc32(blob) & 0xffffffff, hashlib.sha1(blob).hexdigest()))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __split__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code
        left = data[::2][:256]
        right = data[1::2][:256]
        rows.append((one.co_name, zlib.crc32(left) & 0xffffffff, zlib.adler32(right) & 0xffffffff, len(left), len(right)))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __xor__(code, seed):
    rows = []
    for one in __drip__(code):
        val = 0
        for slot, byte in enumerate(one.co_code[:2048]): val ^= ((byte + slot) << (slot & 7)) & 0xffffffff
        rows.append((one.co_name, val, len(one.co_code)))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __sum__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code
        rows.append((one.co_name, sum(data) & 0xffffffff, sum((slot + 1) * byte for slot, byte in enumerate(data[:4096])) & 0xffffffff))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __layout__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((one.co_name, len(one.co_consts), tuple(type(val).__name__ for val in one.co_consts[:32]), tuple(one.co_names[:32])))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __flat__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            val = node.value
            if isinstance(val, str): rows.append(('s', len(val), zlib.crc32(val.encode('utf-8', 'replace')) & 0xffffffff, getattr(node, 'lineno', 0)))
            elif isinstance(val, bytes): rows.append(('b', len(val), zlib.crc32(val) & 0xffffffff, getattr(node, 'lineno', 0)))
            elif isinstance(val, bool): rows.append(('o', int(val), getattr(node, 'lineno', 0)))
            elif val is None: rows.append(('n', getattr(node, 'lineno', 0)))
            elif isinstance(val, int): rows.append(('i', val.bit_length(), val & 0xffffffff, getattr(node, 'lineno', 0)))
            elif isinstance(val, float): rows.append(('f', repr(val), getattr(node, 'lineno', 0)))
            elif isinstance(val, complex): rows.append(('c', repr(val.real), repr(val.imag), getattr(node, 'lineno', 0)))
            elif isinstance(val, type(Ellipsis)): rows.append(('e', getattr(node, 'lineno', 0)))
            else: rows.append((type(val).__name__, len(repr(val)), getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)): rows.append(('d', type(node).__name__, len(node.name), zlib.crc32(node.name.encode('utf-8', 'replace')) & 0xffffffff, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Import): rows.append(('m', tuple((one.name, one.asname) for one in node.names), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.ImportFrom): rows.append(('r', node.module or '', node.level, tuple((one.name, one.asname) for one in node.names), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __fvn__(code, seed):
    rows = []
    for one in __drip__(code):
        glow = 2166136261
        for byte in __raw__(one):
            glow ^= byte
            glow = (glow * 16777619) & 0xffffffff
        rows.append((one.co_name, glow, len(one.co_code), len(one.co_consts), len(__dump__(one))))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __rill__(tree, seed):
    rows = []
    last = 0
    for slot, node in enumerate(ast.walk(tree)):
        line = getattr(node, 'lineno', 0); col = getattr(node, 'col_offset', 0)
        rows.append((slot & 255, type(node).__name__, line - last, col, len(list(ast.iter_child_nodes(node)))))
        last = line
        if len(rows) >= 4096: break
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __tor__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        base = type(node).__name__
        for one in ast.iter_child_nodes(node):
            rows.append((base, type(one).__name__, getattr(one, 'lineno', 0), getattr(one, 'col_offset', 0)))
            if len(rows) >= 4096: break
        if len(rows) >= 4096: break
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __dell__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        line = getattr(node, 'lineno', 0); end = getattr(node, 'end_lineno', line); col = getattr(node, 'col_offset', 0); fin = getattr(node, 'end_col_offset', col)
        if line or end or col or fin: rows.append((type(node).__name__, line, end, col, fin, max(0, end - line), max(0, fin - col)))
        if len(rows) >= 4096: break
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __fell__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            gens = tuple((len(one.ifs), int(one.is_async), type(one.target).__name__, type(one.iter).__name__) for one in node.generators)
            rows.append((type(node).__name__, gens, getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.comprehension,)):
            rows.append(('comp', len(node.ifs), int(node.is_async), type(node.target).__name__, type(node.iter).__name__))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __crux__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.For, ast.AsyncFor, ast.While, ast.Try, ast.With, ast.AsyncWith, ast.Match)):
            rows.append((type(node).__name__, len(getattr(node, 'body', ())), len(getattr(node, 'orelse', ())), len(getattr(node, 'finalbody', ())), len(getattr(node, 'handlers', ())), getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.Break, ast.Continue, ast.Return, ast.Raise, ast.Yield, ast.YieldFrom, ast.Await)):
            rows.append((type(node).__name__, getattr(node, 'lineno', 0), getattr(node, 'col_offset', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __vane__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fun = type(node.func).__name__
            if isinstance(node.func, ast.Name): fun = ('n', len(node.func.id), zlib.crc32(node.func.id.encode('utf-8', 'replace')) & 0xffffffff)
            elif isinstance(node.func, ast.Attribute): fun = ('a', len(node.func.attr), zlib.crc32(node.func.attr.encode('utf-8', 'replace')) & 0xffffffff, type(node.func.value).__name__)
            rows.append((fun, len(node.args), len(node.keywords), sum(1 for one in node.keywords if one.arg is None), getattr(node, 'lineno', 0)))
            if len(rows) >= 4096: break
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __pinion__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            arg = node.args
            name = getattr(node, 'name', '<lambda>')
            rows.append((type(node).__name__, len(name), len(arg.posonlyargs), len(arg.args), len(arg.kwonlyargs), int(arg.vararg is not None), int(arg.kwarg is not None), len(arg.defaults), len(arg.kw_defaults), len(getattr(node, 'decorator_list', ())), type(getattr(node, 'returns', None)).__name__))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __ochre__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            raw = node.value.encode('utf-8', 'replace')
            rows.append((len(node.value), len(raw), sum(raw) & 0xffffffff, len(set(raw)), raw[:3], raw[-3:], getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Constant) and isinstance(node.value, bytes):
            raw = node.value
            rows.append((len(raw), zlib.crc32(raw) & 0xffffffff, len(set(raw)), raw[:3], raw[-3:], getattr(node, 'lineno', 0)))
        if len(rows) >= 4096: break
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __prong__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            rows.append(('n', type(node.ctx).__name__, len(node.id), zlib.crc32(node.id.encode('utf-8', 'replace')) & 0xffffffff, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Attribute):
            rows.append(('a', type(node.ctx).__name__, len(node.attr), zlib.crc32(node.attr.encode('utf-8', 'replace')) & 0xffffffff, type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            rows.append(('i', type(node).__name__, len(getattr(node, 'names', ())), getattr(node, 'module', '') or '', getattr(node, 'level', 0), getattr(node, 'lineno', 0)))
        if len(rows) >= 4096: break
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __gauze__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr):
            rows.append(('j', len(node.values), sum(isinstance(one, ast.FormattedValue) for one in node.values), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.FormattedValue):
            rows.append(('f', node.conversion, type(node.value).__name__, type(node.format_spec).__name__ if node.format_spec else '', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __pylon__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            rows.append((len(node.name), len(node.bases), len(node.keywords), len(node.decorator_list), len(node.body), tuple(type(one).__name__ for one in node.body[:32]), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __keel__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            vals = getattr(node, 'targets', None)
            if vals is None: vals = [getattr(node, 'target', None)]
            rows.append((type(node).__name__, tuple(type(one).__name__ for one in vals if one is not None), type(getattr(node, 'value', None)).__name__, type(getattr(node, 'op', None)).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __mast__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            rows.append(('try', len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.ExceptHandler):
            rows.append(('ex', type(node.type).__name__ if node.type else '', len(node.name or ''), len(node.body), getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.Assert, ast.Raise)):
            rows.append((type(node).__name__, type(getattr(node, 'exc', None)).__name__, type(getattr(node, 'msg', None)).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __rivet__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code; bag = []
        for at in range(0, min(len(data) - 1, 2048), 2): bag.append((data[at], data[at + 1]))
        rows.append((one.co_name, len(data), __hist__(bag), tuple(bag[:64])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __hinge__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code; bag = []; at = 0
        while at < len(data) and len(bag) < 256:
            byte = data[at]; run = 1; at += 1
            while at < len(data) and data[at] == byte and run < 255: run += 1; at += 1
            bag.append((byte, run))
        rows.append((one.co_name, len(data), tuple(bag), zlib.crc32(bytes(sum(([a, b] for a, b in bag), []))) & 0xffffffff if bag else 0))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __nickel__(code, seed):
    rows = []
    kind = type(code)
    for one in __drip__(code):
        bag = []
        for slot, val in enumerate(one.co_consts[:128]):
            if isinstance(val, kind): bag.append((slot, 'code', len(val.co_code), len(val.co_consts), len(val.co_names)))
            elif isinstance(val, (str, bytes, tuple)): bag.append((slot, type(val).__name__, len(val), zlib.crc32(repr(val[:16] if isinstance(val, tuple) else val[:16]).encode('utf-8', 'replace')) & 0xffffffff))
            elif isinstance(val, int): bag.append((slot, 'int', val.bit_length(), val & 0xffffffff))
            else: bag.append((slot, type(val).__name__, len(repr(val))))
        rows.append((one.co_name, __hist__(bag), tuple(bag[:64])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __tin__(code, seed):
    rows = []
    for one in __drip__(code):
        bag = []
        for vals in (one.co_names, one.co_varnames, one.co_freevars, one.co_cellvars):
            raw = '|'.join(vals).encode('utf-8', 'replace')
            bag.append((len(vals), len(raw), zlib.crc32(raw) & 0xffffffff, sum(raw) & 0xffffffff))
        rows.append((one.co_name, tuple(bag), len(one.co_names), len(one.co_varnames)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __rope__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((one.co_name, tuple((slot, name, name in one.co_names, name in one.co_varnames) for slot, name in enumerate(one.co_freevars[:64])), tuple((slot, name, name in one.co_names, name in one.co_varnames) for slot, name in enumerate(one.co_cellvars[:64]))))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __sail__(code, seed):
    rows = []
    for one in __drip__(code):
        tab = one.co_linetable if hasattr(one, 'co_linetable') else getattr(one, 'co_lnotab', b'')
        bag = []
        for at in range(0, min(len(tab), 2048), 8):
            row = tab[at:at + 8]; bag.append((len(row), sum(row) & 0xffff, zlib.crc32(row) & 0xffffffff))
        rows.append((one.co_name, len(tab), tuple(bag[:256])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __anchor__(code, seed):
    rows = []
    for one in __drip__(code):
        raw = __dump__(one); bag = []
        for at in range(0, min(len(raw), 4096), 32):
            row = raw[at:at + 32]; bag.append((len(row), row[:2], row[-2:], zlib.adler32(row) & 0xffffffff))
        rows.append((one.co_name, len(raw), zlib.crc32(raw) & 0xffffffff, tuple(bag[:128])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __wheel__(tree, seed):
    rows = [type(one).__name__ for one in ast.walk(tree)]
    bag = []
    for i in range(0, max(0, len(rows) - 4), 5): bag.append(tuple(rows[i:i + 5]))
    fog = __mix__(seed, (__hist__(bag), len(rows)))
    return (len(rows), fog.hex())
def __level__(tree, seed):
    rows = []
    hold = [(tree, 0)]
    while hold:
        node, deep = hold.pop(); rows.append((deep, type(node).__name__, len(list(ast.iter_child_nodes(node)))))
        for one in ast.iter_child_nodes(node): hold.append((one, deep + 1))
    fog = __mix__(seed, (__hist__(rows), max((row[0] for row in rows), default=0), len(rows)))
    return (len(rows), fog.hex())
def __wrap__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        kids = [type(one).__name__ for one in ast.iter_child_nodes(node)]
        if kids: rows.append((type(node).__name__, tuple(kids[:16]), len(kids)))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __source__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        part = ast.dump(node, include_attributes=False)
        rows.append((type(node).__name__, len(part), zlib.crc32(part.encode('utf-8', 'replace')) & 0xffffffff))
        if len(rows) >= 4096: break
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __middle__(tree, seed):
    rows = list(ast.walk(tree))
    mid = len(rows) // 2
    pick = rows[max(0, mid - 512):mid + 512]
    data = tuple((type(one).__name__, getattr(one, 'lineno', 0), len(list(ast.iter_child_nodes(one)))) for one in pick)
    fog = __mix__(seed, data)
    return (len(rows), fog.hex())
def __tail__(tree, seed):
    rows = list(ast.walk(tree))
    data = tuple((type(one).__name__, getattr(one, 'lineno', 0), getattr(one, 'end_lineno', 0) or 0) for one in rows[-1024:])
    fog = __mix__(seed, data)
    return (len(rows), fog.hex())
def __field__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        vals = []
        for field, val in ast.iter_fields(node):
            if isinstance(val, list): vals.append((field, len(val)))
            elif isinstance(val, ast.AST): vals.append((field, type(val).__name__))
            elif isinstance(val, (str, int, type(None))): vals.append((field, type(val).__name__, str(val)[:32]))
        rows.append((type(node).__name__, tuple(vals[:16])))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __wide__(tree, seed):
    rows = {}
    hold = [(tree, 0)]
    while hold:
        node, deep = hold.pop(); rows[deep] = rows.get(deep, 0) + 1
        for one in ast.iter_child_nodes(node): hold.append((one, deep + 1))
    data = tuple(sorted(rows.items()))
    fog = __mix__(seed, data)
    return (len(data), fog.hex())
def __den__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        kids = list(ast.iter_child_nodes(node))
        rows.append((type(node).__name__, len(kids), sum(1 for one in kids if isinstance(one, ast.expr)), sum(1 for one in kids if isinstance(one, ast.stmt))))
    fog = __mix__(seed, (__hist__(rows), len(rows)))
    return (len(rows), fog.hex())
def __mesh__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code; names = __vine__(tuple(one.co_names)); const = __vine__(tuple(type(val).__name__ for val in one.co_consts))
        rows.append((one.co_name, zlib.crc32(data + names) & 0xffffffff, zlib.adler32(data + const) & 0xffffffff, len(data), len(names), len(const)))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __gate__(code, seed):
    rows = []
    for one in __drip__(code):
        mark = 0
        for byte in one.co_code[:2048]: mark = ((mark << 5) - mark + byte) & 0xffffffff
        rows.append((one.co_name, mark, len(one.co_code), one.co_flags))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __fold__(code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code; half = len(data) // 2
        alt = data[::3]
        mix = data[1::3]
        tail = data[2::3]
        rows.append((one.co_name, hashlib.sha1(data[:half]).hexdigest(), hashlib.sha1(data[half:]).hexdigest(), zlib.crc32(alt + mix) & 0xffffffff, zlib.adler32(tail) & 0xffffffff, half, len(data) - half))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __crestcall__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            chain = []
            cur = node.func
            while isinstance(cur, ast.Attribute):
                chain.append(cur.attr)
                cur = cur.value
            if isinstance(cur, ast.Name): chain.append(cur.id)
            else: chain.append(type(cur).__name__)
            rows.append((tuple(reversed(chain)), len(node.args), tuple(kw.arg or '*' for kw in node.keywords), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __crestattr__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            cur = node
            chain = []
            while isinstance(cur, ast.Attribute):
                chain.append(cur.attr)
                cur = cur.value
            if isinstance(cur, ast.Name): chain.append(cur.id)
            else: chain.append(type(cur).__name__)
            rows.append((tuple(reversed(chain)), type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), len(rows), tuple(rows[:512])))
    return (len(rows), fog.hex())
def __crestimp__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                rows.append(('i', alias.name, alias.asname or '', alias.name.count('.')))
        elif isinstance(node, ast.ImportFrom):
            rows.append(('f', node.module or '', node.level, tuple((one.name, one.asname or '') for one in node.names)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __creststr__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            val = node.value
            top = {}
            for ch in val[:512]: top[ch] = top.get(ch, 0) + 1
            rows.append((len(val), val.count('\n'), val.count('\\'), val.count('{'), val.count('}'), val[:8], val[-8:], tuple(sorted(top.items())[:32])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __crestbytes__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, bytes):
            val = node.value
            rows.append((len(val), val[:8], val[-8:], zlib.crc32(val) & 0xffffffff, zlib.adler32(val) & 0xffffffff, len(set(val[:512]))))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __crestnum__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and not isinstance(node.value, bool):
            val = node.value
            rows.append((int(val < 0), abs(val).bit_length(), val & 0xff, (val >> 8) & 0xff, (val >> 16) & 0xffff, zlib.crc32(str(val).encode()) & 0xffffffff))
        elif isinstance(node, ast.Constant) and isinstance(node.value, float):
            rows.append(('f', repr(node.value), hash(repr(node.value)) & 0xffffffff))
        elif isinstance(node, ast.Constant) and isinstance(node.value, complex):
            rows.append(('c', repr(node.value.real), repr(node.value.imag)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __crestseq__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
            rows.append((type(node).__name__, len(node.elts), type(getattr(node, 'ctx', None)).__name__, tuple(type(one).__name__ for one in node.elts[:48])))
        elif isinstance(node, ast.Dict):
            rows.append(('Dict', len(node.keys), tuple(type(one).__name__ if one else '' for one in node.keys[:48]), tuple(type(one).__name__ for one in node.values[:48])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __crestbranch__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            rows.append(('if', type(node.test).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.IfExp):
            rows.append(('ifexp', type(node.test).__name__, type(node.body).__name__, type(node.orelse).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.While):
            rows.append(('while', type(node.test).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.For, ast.AsyncFor)):
            rows.append(('for', type(node.target).__name__, type(node.iter).__name__, len(node.body), len(node.orelse), int(isinstance(node, ast.AsyncFor))))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __cresttry__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            rows.append(('try', len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.ExceptHandler):
            rows.append(('except', type(node.type).__name__ if node.type else '', node.name or '', len(node.body), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Raise):
            rows.append(('raise', type(node.exc).__name__ if node.exc else '', type(node.cause).__name__ if node.cause else '', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __crestfunc__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            args = node.args
            name = getattr(node, 'name', '<lambda>')
            rows.append((type(node).__name__, name, len(args.posonlyargs), len(args.args), len(args.kwonlyargs), int(args.vararg is not None), int(args.kwarg is not None), len(args.defaults), len(args.kw_defaults), len(getattr(node, 'body', [])) if isinstance(getattr(node, 'body', []), list) else 1))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __crestclass__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            rows.append((node.name, len(node.bases), len(node.keywords), len(node.decorator_list), len(node.body), tuple(type(one).__name__ for one in node.body[:32])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:128]), len(rows)))
    return (len(rows), fog.hex())
def __crestcomp__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp)):
            rows.append((type(node).__name__, type(node.elt).__name__, len(node.generators)))
        elif isinstance(node, ast.DictComp):
            rows.append(('DictComp', type(node.key).__name__, type(node.value).__name__, len(node.generators)))
        elif isinstance(node, ast.comprehension):
            rows.append(('gen', type(node.target).__name__, type(node.iter).__name__, len(node.ifs), int(node.is_async)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __crestpat__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Match):
            rows.append(('match', type(node.subject).__name__, len(node.cases), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.match_case):
            rows.append(('case', type(node.pattern).__name__, type(node.guard).__name__ if node.guard else '', len(node.body)))
        elif type(node).__name__.startswith('Match'):
            rows.append((type(node).__name__, getattr(node, 'name', '') or '', getattr(node, 'rest', '') or ''))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __crestfmt__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr):
            rows.append(('join', len(node.values), tuple(type(one).__name__ for one in node.values), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.FormattedValue):
            rows.append(('fmt', node.conversion, type(node.value).__name__, type(node.format_spec).__name__ if node.format_spec else '', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __crestscope__(tree, seed):
    rows = []
    hold = [(tree, 0, 'root')]
    while hold:
        node, deep, field = hold.pop()
        kids = list(ast.iter_child_nodes(node))
        rows.append((type(node).__name__, deep, field, len(kids), getattr(node, 'lineno', 0)))
        for one in reversed(kids): hold.append((one, deep + 1, type(node).__name__))
    wide = max((row[1] for row in rows), default=0)
    fog = __mix__(seed, (__hist__((row[0], row[1], row[3]) for row in rows), tuple(rows[:1024]), len(rows), wide))
    return (len(rows), wide, fog.hex())
def __crestname__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name): rows.append(('name', node.id, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.arg): rows.append(('arg', node.arg, type(node.annotation).__name__ if node.annotation else ''))
        elif isinstance(node, ast.alias): rows.append(('alias', node.name, node.asname or ''))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)): rows.append(('def', node.name, type(node).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows), len(set(row[1] for row in rows if len(row) > 1))))
    return (len(rows), fog.hex())
def __crestop__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp): rows.append(('bin', type(node.op).__name__, type(node.left).__name__, type(node.right).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.BoolOp): rows.append(('bool', type(node.op).__name__, len(node.values), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.UnaryOp): rows.append(('unary', type(node.op).__name__, type(node.operand).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Compare): rows.append(('cmp', type(node.left).__name__, tuple(type(one).__name__ for one in node.ops), len(node.comparators), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __crestline__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if hasattr(node, 'lineno'):
            rows.append((type(node).__name__, node.lineno, getattr(node, 'end_lineno', node.lineno), getattr(node, 'col_offset', 0), getattr(node, 'end_col_offset', 0) or 0))
    spans = tuple((row[0], row[2] - row[1], row[4] - row[3]) for row in rows[:2048])
    fog = __mix__(seed, (__hist__(spans), tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __crestapi__(tree, seed):
    keys = ('exec','eval','compile','open','__import__','getattr','setattr','delattr','globals','locals','vars','dir','type','isinstance','issubclass','input','print','len','list','bytearray','subprocess','socket','requests','requests.sessions','requests.api','httpx','aiohttp','urllib','urllib3','ssl','pystyle','ctypes','marshal','base64','zlib','bz2','lzma')
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in keys: rows.append(('n', node.id, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Attribute) and node.attr in keys: rows.append(('a', node.attr, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            low = node.value.lower()
            hit = tuple(one for one in keys if one in low)
            if hit: rows.append(('s', hit, len(low), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __crestio__(tree, seed):
    keys = ('open','read','write','flush','close','exists','isfile','isdir','join','abspath','dirname','basename','remove','rename','replace')
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in keys: rows.append((node.attr, type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Name) and node.id in keys: rows.append((node.id, 'name', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:384]), len(rows)))
    return (len(rows), fog.hex())
def __crestnet__(tree, seed):
    keys = ('get','post','request','connect','send','recv','socket','urlopen','urlparse','wrap_socket','AsyncClient','Client','Session','HTTPConnectionPool','HTTPSConnectionPool','SSLContext','timeout','headers','proxy','proxies')
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in keys: rows.append(('a', node.attr, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.keyword) and node.arg in keys: rows.append(('k', node.arg, type(node.value).__name__))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:384]), len(rows)))
    return (len(rows), fog.hex())
def __cresttime__(tree, seed):
    keys = ('time','sleep','monotonic','datetime','now','timedelta','wait','wait_for','gather')
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in keys: rows.append((node.attr, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in keys: rows.append((node.func.id, len(node.args)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:384]), len(rows)))
    return (len(rows), fog.hex())
def __cresterr__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler): rows.append((type(node.type).__name__ if node.type else '', node.name or '', len(node.body), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Try): rows.append(('try', len(node.body), len(node.handlers), len(node.finalbody), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __crestasync__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.AsyncFunctionDef, ast.AsyncFor, ast.AsyncWith, ast.Await)): rows.append((type(node).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in ('run','create_task','gather','wait_for','sleep'): rows.append(('call', node.func.attr, len(node.args)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __crestui__(tree, seed):
    keys = ('print','input','Panel','Table','Text','Console','Live','Progress','add_row','append','stylize')
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in keys: rows.append(('n', node.id, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Attribute) and node.attr in keys: rows.append(('a', node.attr, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __crestpack__(tree, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.List): rows.append(('list', len(node.elts), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Tuple): rows.append(('tuple', len(node.elts), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Dict): rows.append(('dict', len(node.keys), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Set): rows.append(('set', len(node.elts), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __crestcode__(code, seed):
    rows = []
    for one in __drip__(code):
        raw = one.co_code
        head = raw[:64]
        tail = raw[-64:]
        rows.append((one.co_name, len(raw), len(one.co_consts), len(one.co_names), len(one.co_varnames), zlib.crc32(head) & 0xffffffff, zlib.adler32(tail) & 0xffffffff, hashlib.blake2s(raw[:512], digest_size=16).hexdigest()))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __crestconst__(code, seed):
    rows = []
    kind = type(code)
    for one in __drip__(code):
        for slot, val in enumerate(one.co_consts[:256]):
            if isinstance(val, str):
                raw = val.encode('utf-8', 'replace')
                rows.append((one.co_name, slot, 's', len(raw), zlib.crc32(raw) & 0xffffffff, raw[:16]))
            elif isinstance(val, bytes):
                rows.append((one.co_name, slot, 'b', len(val), zlib.crc32(val) & 0xffffffff, val[:16]))
            elif isinstance(val, int):
                rows.append((one.co_name, slot, 'i', int(val < 0), abs(val).bit_length(), val & 0xffffffff))
            elif isinstance(val, float):
                rows.append((one.co_name, slot, 'f', repr(val)))
            elif isinstance(val, kind):
                rows.append((one.co_name, slot, 'c', val.co_name, len(val.co_code), len(val.co_consts)))
            else:
                rows.append((one.co_name, slot, type(val).__name__, len(repr(val))))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __crestpool__(code, seed):
    rows = []
    for one in __drip__(code):
        names = tuple((slot, val, len(val), zlib.crc32(val.encode('utf-8', 'replace')) & 0xffffffff) for slot, val in enumerate(one.co_names[:256]))
        vars = tuple((slot, val, len(val), zlib.adler32(val.encode('utf-8', 'replace')) & 0xffffffff) for slot, val in enumerate(one.co_varnames[:256]))
        free = tuple((slot, val) for slot, val in enumerate(one.co_freevars))
        cell = tuple((slot, val) for slot, val in enumerate(one.co_cellvars))
        rows.append((one.co_name, names, vars, free, cell))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:128]), len(rows)))
    return (len(rows), fog.hex())
def __cresttable__(code, seed):
    rows = []
    for one in __drip__(code):
        line = getattr(one, 'co_linetable', getattr(one, 'co_lnotab', b''))
        exc = getattr(one, 'co_exceptiontable', b'')
        rows.append((one.co_name, one.co_firstlineno, len(line), len(exc), zlib.crc32(line) & 0xffffffff, zlib.adler32(exc) & 0xffffffff, line[:32], exc[:32]))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __crestmar__(code, seed):
    rows = []
    for one in __drip__(code):
        raw = __dump__(one)
        pack = __gasket__(raw)
        rows.append((one.co_name, len(raw), len(pack), pack[0], hashlib.sha256(raw[:1024]).hexdigest(), hashlib.sha1(pack[:1024]).hexdigest()))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:128]), len(rows)))
    return (len(rows), fog.hex())
def __vex__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fun = node.func
            chain = []
            while isinstance(fun, ast.Attribute):
                chain.append(fun.attr); fun = fun.value
            if isinstance(fun, ast.Name): chain.append(fun.id)
            else: chain.append(type(fun).__name__)
            rows.append((tuple(reversed(chain)), len(node.args), tuple(kw.arg or '*' for kw in node.keywords), getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __zod__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            cur = node
            chain = []
            while isinstance(cur, ast.Attribute):
                chain.append(cur.attr); cur = cur.value
            if isinstance(cur, ast.Name): chain.append(cur.id)
            else: chain.append(type(cur).__name__)
            rows.append((tuple(reversed(chain)), type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __kiv__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for one in node.names: rows.append(('i', one.name, one.asname or '', one.name.count('.'), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.ImportFrom):
            rows.append(('f', node.module or '', node.level, tuple((one.name, one.asname or '') for one in node.names), getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __mav__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            val = node.value; raw = val.encode('utf-8', 'replace')
            rows.append(('s', len(raw), raw[:16], raw[-16:], val.count('\n'), val.count('{'), zlib.crc32(raw) & 0xffffffff, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Constant) and isinstance(node.value, bytes):
            val = node.value
            rows.append(('b', len(val), val[:16], val[-16:], len(set(val[:512])), zlib.adler32(val) & 0xffffffff, getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __night__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and not isinstance(node.value, bool):
            val = node.value
            rows.append(('i', int(val < 0), abs(val).bit_length(), val & 0xffff, zlib.crc32(str(val).encode()) & 0xffffffff, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Constant) and isinstance(node.value, float): rows.append(('f', repr(node.value), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Constant) and isinstance(node.value, complex): rows.append(('c', repr(node.value.real), repr(node.value.imag), getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __pyr__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.If): rows.append(('if', type(node.test).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.While): rows.append(('while', type(node.test).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.For, ast.AsyncFor)): rows.append(('for', type(node.target).__name__, type(node.iter).__name__, len(node.body), len(node.orelse), int(isinstance(node, ast.AsyncFor))))
        elif isinstance(node, ast.IfExp): rows.append(('ifexp', type(node.test).__name__, type(node.body).__name__, type(node.orelse).__name__, getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __qel__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Try): rows.append(('try', len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.ExceptHandler): rows.append(('except', type(node.type).__name__ if node.type else '', node.name or '', len(node.body), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Raise): rows.append(('raise', type(node.exc).__name__ if node.exc else '', type(node.cause).__name__ if node.cause else '', getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __rice__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            args = node.args; name = getattr(node, 'name', '<lambda>')
            rows.append((type(node).__name__, name, len(args.posonlyargs), len(args.args), len(args.kwonlyargs), int(args.vararg is not None), int(args.kwarg is not None), len(args.defaults), len(args.kw_defaults), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Return): rows.append(('return', type(node.value).__name__ if node.value else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Yield): rows.append(('yield', type(node.value).__name__ if node.value else '', getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __sorn__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef): rows.append(('class', node.name, len(node.bases), len(node.keywords), len(node.decorator_list), len(node.body), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.With): rows.append(('with', len(node.items), len(node.body), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.AsyncWith): rows.append(('awith', len(node.items), len(node.body), getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __tav__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp)): rows.append((type(node).__name__, type(node.elt).__name__, len(node.generators), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.DictComp): rows.append(('DictComp', type(node.key).__name__, type(node.value).__name__, len(node.generators), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.comprehension): rows.append(('gen', type(node.target).__name__, type(node.iter).__name__, len(node.ifs), int(node.is_async)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __umber__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.AsyncFunctionDef, ast.AsyncFor, ast.AsyncWith, ast.Await)): rows.append((type(node).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in ('run','create_task','gather','wait_for','sleep','wait_closed'): rows.append(('call', node.func.attr, len(node.args), getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __vor__(tree, code, seed):
    keys = ('open','read','write','close','exists','isfile','isdir','join','remove','rename','replace','socket','connect','send','recv','request','get','post','urlopen','urlparse','wrap_socket','AsyncClient','Client','Session','HTTPConnectionPool','HTTPSConnectionPool','SSLContext')
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in keys: rows.append(('a', node.attr, type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Name) and node.id in keys: rows.append(('n', node.id, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.keyword) and node.arg in keys: rows.append(('k', node.arg, type(node.value).__name__))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __wool__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)): rows.append((type(node).__name__, len(node.elts), type(getattr(node, 'ctx', None)).__name__, tuple(type(one).__name__ for one in node.elts[:64]), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Dict): rows.append(('Dict', len(node.keys), tuple(type(one).__name__ if one else '' for one in node.keys[:64]), tuple(type(one).__name__ for one in node.values[:64]), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Starred): rows.append(('Starred', type(node.value).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __yul__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript): rows.append(('sub', type(node.value).__name__, type(node.slice).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Slice): rows.append(('slice', int(node.lower is not None), int(node.upper is not None), int(node.step is not None)))
        elif isinstance(node, ast.Delete): rows.append(('del', len(node.targets), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.AugAssign): rows.append(('aug', type(node.target).__name__, type(node.op).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __ziv__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp): rows.append(('bin', type(node.op).__name__, type(node.left).__name__, type(node.right).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.BoolOp): rows.append(('bool', type(node.op).__name__, len(node.values), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.UnaryOp): rows.append(('unary', type(node.op).__name__, type(node.operand).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Compare): rows.append(('cmp', type(node.left).__name__, tuple(type(one).__name__ for one in node.ops), len(node.comparators), getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __kro__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Match): rows.append(('match', type(node.subject).__name__, len(node.cases), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.match_case): rows.append(('case', type(node.pattern).__name__, type(node.guard).__name__ if node.guard else '', len(node.body)))
        elif type(node).__name__.startswith('Match'): rows.append((type(node).__name__, getattr(node, 'name', '') or '', getattr(node, 'rest', '') or ''))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __lum__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr): rows.append(('join', len(node.values), tuple(type(one).__name__ for one in node.values), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.FormattedValue): rows.append(('fmt', node.conversion, type(node.value).__name__, type(node.format_spec).__name__ if node.format_spec else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.NamedExpr): rows.append(('walrus', type(node.target).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __orz__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Global): rows.append(('global', tuple(node.names), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Nonlocal): rows.append(('nonlocal', tuple(node.names), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.arg): rows.append(('arg', node.arg, type(node.annotation).__name__ if node.annotation else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.alias): rows.append(('alias', node.name, node.asname or ''))
    mark = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __dusk__(tree, code, seed):
    rows = []
    hold = [(tree, 0)]
    while hold:
        node, deep = hold.pop()
        kids = list(ast.iter_child_nodes(node))
        rows.append((type(node).__name__, deep, len(kids), getattr(node, 'lineno', 0)))
        for one in reversed(kids): hold.append((one, deep + 1))
    wide = max((row[1] for row in rows), default=0)
    fog = __mix__(seed, (__hist__((row[0], row[1], row[2]) for row in rows), tuple(rows[:1024]), len(rows), wide))
    return (len(rows), wide, fog.hex())
def __peace__(tree, code, seed):
    rows = []
    for one in __drip__(code):
        raw = one.co_code
        rows.append((one.co_name, len(raw), one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount, one.co_nlocals, one.co_stacksize, one.co_flags, zlib.crc32(raw[:128]) & 0xffffffff, zlib.adler32(raw[-128:]) & 0xffffffff))
    shape = __shape__(tree)
    fog = __mix__(seed, (__hist__(rows), shape, tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __quill__(tree, code, seed):
    rows = []
    kind = type(code)
    for one in __drip__(code):
        for slot, val in enumerate(one.co_consts[:256]):
            if isinstance(val, kind): rows.append((one.co_name, slot, 'code', val.co_name, len(val.co_code), len(val.co_consts), len(val.co_names)))
            elif isinstance(val, (str, bytes, int, float, complex, type(None))): rows.append((one.co_name, slot, type(val).__name__, len(repr(val))))
            else: rows.append((one.co_name, slot, type(val).__name__, zlib.crc32(repr(val).encode('utf-8', 'replace')) & 0xffffffff))
    shape = __shape__(tree)
    fog = __mix__(seed, (__hist__(rows), shape, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __rust__(tree, code, seed):
    rows = []
    for one in __drip__(code):
        line = getattr(one, 'co_linetable', getattr(one, 'co_lnotab', b'')); exc = getattr(one, 'co_exceptiontable', b'')
        rows.append((one.co_name, one.co_firstlineno, len(line), len(exc), zlib.crc32(line) & 0xffffffff, zlib.adler32(exc) & 0xffffffff, line[:48], exc[:48]))
    shape = __shape__(tree)
    fog = __mix__(seed, (__hist__(rows), shape, tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __siv__(tree, code, seed):
    rows = []
    for one in __drip__(code):
        raw = one.co_code
        bag = []
        for slot in range(0, min(len(raw), 768) - 2, 3): bag.append((raw[slot], raw[slot + 1], raw[slot + 2]))
        rows.append((one.co_name, len(raw), __hist__(bag), tuple(bag[:96])))
    shape = __shape__(tree)
    fog = __mix__(seed, (__hist__(rows), shape, tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __tick__(tree, code, seed):
    rows = []
    for one in __drip__(code):
        names = tuple((slot, val, len(val), zlib.crc32(val.encode('utf-8', 'replace')) & 0xffffffff) for slot, val in enumerate(one.co_names[:256]))
        vars = tuple((slot, val, len(val), zlib.adler32(val.encode('utf-8', 'replace')) & 0xffffffff) for slot, val in enumerate(one.co_varnames[:256]))
        rows.append((one.co_name, names, vars, tuple(one.co_freevars), tuple(one.co_cellvars)))
    shape = __shape__(tree)
    fog = __mix__(seed, (__hist__(rows), shape, tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __uvo__(tree, code, seed):
    rows = []
    for one in __drip__(code):
        raw = __dump__(one)
        pack = __gasket__(raw)
        rows.append((one.co_name, len(raw), len(pack), pack[0], hashlib.sha256(raw[:1024]).hexdigest(), hashlib.sha1(pack[:1024]).hexdigest()))
    shape = __shape__(tree)
    fog = __mix__(seed, (__hist__(rows), shape, tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __vyn__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)): rows.append((type(node).__name__, getattr(node, 'lineno', 0), len(list(ast.iter_child_nodes(node)))))
        elif isinstance(node, (ast.Assert, ast.Pass, ast.Break, ast.Continue)): rows.append((type(node).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Expr): rows.append(('expr', type(node.value).__name__, getattr(node, 'lineno', 0)))
    mark = tuple((one.co_name, one.co_flags, one.co_stacksize) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), mark, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())

def __wok__(tree, code, seed):
    rows = []
    hold = [(tree, None, 0)]
    while hold:
        node, parent, deep = hold.pop()
        kids = list(ast.iter_child_nodes(node))
        rows.append((type(node).__name__, parent or '', deep, len(kids), getattr(node, 'lineno', 0), getattr(node, 'col_offset', 0)))
        for kid in reversed(kids):
            hold.append((kid, type(node).__name__, deep + 1))
    edge = tuple((rows[i][0], rows[i + 1][0], rows[i + 1][2] - rows[i][2]) for i in range(min(len(rows) - 1, 2048)))
    mark = tuple((one.co_name, len(one.co_code), one.co_stacksize) for one in __drip__(code)[:96])
    fog = __mix__(seed, (__hist__(rows), __hist__(edge), mark, len(rows)))
    return (len(rows), fog.hex())
def __xul__(tree, code, seed):
    rows = []
    stack = ['<module>']
    def walk(node):
        name = getattr(node, 'name', None)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            stack.append(name or type(node).__name__)
            rows.append(('scope', type(node).__name__, tuple(stack[-4:]), len(getattr(node, 'body', [])), getattr(node, 'lineno', 0)))
            for kid in ast.iter_child_nodes(node): walk(kid)
            stack.pop(); return
        if isinstance(node, ast.Name): rows.append(('name', tuple(stack[-3:]), node.id, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.arg): rows.append(('arg', tuple(stack[-3:]), node.arg, type(node.annotation).__name__ if node.annotation else ''))
        elif isinstance(node, (ast.Global, ast.Nonlocal)): rows.append((type(node).__name__, tuple(stack[-3:]), tuple(node.names)))
        for kid in ast.iter_child_nodes(node): walk(kid)
    walk(tree)
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1536]), len(rows), len(set(row[0] for row in rows))))
    return (len(rows), fog.hex())
def __yarn__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            val = node.value
            raw = repr(val).encode('utf-8', 'replace')
            bins = [0, 0, 0, 0]
            for byte in raw[:4096]: bins[(byte >> 6) & 3] += 1
            rows.append((type(val).__name__, len(raw), tuple(bins), zlib.crc32(raw[:512]) & 0xffffffff, getattr(node, 'lineno', 0)))
    codebag = []
    for one in __drip__(code): codebag.append((one.co_name, len(one.co_consts), __hist__(type(val).__name__ for val in one.co_consts)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), tuple(codebag[:256]), len(rows)))
    return (len(rows), fog.hex())
def __zok__(tree, code, seed):
    keys = ('trace','debug','profile','inspect','frame','ctypes','pythonapi','marshal','exec','eval','compile','open','socket','ssl','urllib','urllib3','httpx','aiohttp','requests','pystyle','proxy','thread','asyncio')
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and any(key in node.id.lower() for key in keys): rows.append(('n', node.id, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Attribute) and any(key in node.attr.lower() for key in keys): rows.append(('a', node.attr, type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str) and any(key in node.value.lower() for key in keys): rows.append(('s', len(node.value), zlib.crc32(node.value.encode('utf-8', 'replace')) & 0xffffffff, getattr(node, 'lineno', 0)))
    names = []
    for one in __drip__(code): names.extend(str(name).lower() for name in one.co_names)
    fog = __mix__(seed, (__hist__(rows), __hist__(names), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __pearl__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            rows.append(('try', len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody), tuple(type(one).__name__ for one in node.body[:8]), getattr(node, 'lineno', 0)))
            for at, handler in enumerate(node.handlers): rows.append(('handler', at, type(handler.type).__name__ if handler.type else '', handler.name or '', len(handler.body)))
        elif isinstance(node, ast.Raise): rows.append(('raise', type(node.exc).__name__ if node.exc else '', type(node.cause).__name__ if node.cause else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Assert): rows.append(('assert', type(node.test).__name__, type(node.msg).__name__ if node.msg else '', getattr(node, 'lineno', 0)))
    exc = []
    for one in __drip__(code): exc.append((one.co_name, len(getattr(one, 'co_exceptiontable', b'')), zlib.crc32(getattr(one, 'co_exceptiontable', b'')) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), tuple(exc[:256]), len(rows)))
    return (len(rows), fog.hex())
def __lime__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Await): rows.append(('await', type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.AsyncFunctionDef, ast.AsyncFor, ast.AsyncWith)): rows.append((type(node).__name__, getattr(node, 'name', ''), len(getattr(node, 'body', [])), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Call):
            head = node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id if isinstance(node.func, ast.Name) else type(node.func).__name__
            if head in ('run','gather','wait','wait_for','create_task','sleep','open_connection','start_server'): rows.append(('call', head, len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
    flags = tuple((one.co_name, one.co_flags, one.co_stacksize) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), flags, len(rows)))
    return (len(rows), fog.hex())
def __cedar__(tree, code, seed):
    rows = []
    for one in __drip__(code):
        raw = one.co_code
        pairs = []
        for at in range(0, min(len(raw), 1536) - 1, 2): pairs.append((raw[at], raw[at + 1]))
        jumps = sum(1 for byte in raw if byte in (93, 110, 111, 112, 114, 115, 140, 176))
        rows.append((one.co_name, len(raw), jumps, __hist__(pairs), tuple(pairs[:128])))
    shape = __shape__(tree)
    fog = __mix__(seed, (__hist__(rows), shape, tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __nuv__(tree, code, seed):
    rows = []
    for one in __drip__(code):
        pool = []
        for val in one.co_consts:
            raw = marshal.dumps(val) if type(val) in (str, bytes, int, float, complex, tuple, frozenset, type(None), bool) else repr(type(val)).encode()
            pool.append((type(val).__name__, len(raw), zlib.crc32(raw[:1024]) & 0xffffffff))
        rows.append((one.co_name, len(pool), tuple(pool[:128]), __hist__(row[0] for row in pool)))
    marks = tuple((type(node).__name__, getattr(node, 'lineno', 0)) for node in ast.walk(tree) if isinstance(node, (ast.Constant, ast.JoinedStr, ast.FormattedValue)))[:1024]
    fog = __mix__(seed, (__hist__(rows), marks, tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __oxa__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            head = node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id if isinstance(node.func, ast.Name) else type(node.func).__name__
            vals = tuple(type(arg).__name__ for arg in node.args[:16])
            kws = tuple((kw.arg or '*', type(kw.value).__name__) for kw in node.keywords[:16])
            rows.append((head, vals, kws, getattr(node, 'lineno', 0)))
    order = tuple(row[0] for row in rows[:2048])
    fog = __mix__(seed, (__hist__(rows), __hist__(order), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __piv__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign): rows.append(('assign', len(node.targets), tuple(type(one).__name__ for one in node.targets), type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.AnnAssign): rows.append(('ann', type(node.target).__name__, type(node.annotation).__name__, int(node.simple), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.NamedExpr): rows.append(('named', type(node.target).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Delete): rows.append(('del', len(node.targets), tuple(type(one).__name__ for one in node.targets), getattr(node, 'lineno', 0)))
    vars = tuple((one.co_name, one.co_nlocals, len(one.co_varnames), tuple(one.co_varnames[:64])) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), vars, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __qor__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import): rows.append(('import', tuple((one.name, one.asname or '') for one in node.names), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.ImportFrom): rows.append(('from', node.module or '', node.level, tuple((one.name, one.asname or '') for one in node.names), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == '__import__': rows.append(('dyn', len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
    names = []
    for one in __drip__(code): names.extend(name for name in one.co_names if isinstance(name, str) and ('import' in name or name in ('sys','os','ctypes','marshal')))
    fog = __mix__(seed, (__hist__(rows), __hist__(names), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __zinc__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef): rows.append(('class', node.name, tuple(type(one).__name__ for one in node.bases), len(node.keywords), len(node.body), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.FunctionDef): rows.append(('func', node.name, len(node.decorator_list), len(node.args.args), len(node.body), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.AsyncFunctionDef): rows.append(('afunc', node.name, len(node.decorator_list), len(node.args.args), len(node.body), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Lambda): rows.append(('lambda', len(node.args.args), type(node.body).__name__, getattr(node, 'lineno', 0)))
    quals = tuple((one.co_name, one.co_qualname, one.co_firstlineno) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), quals, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __topaz__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr): rows.append(('join', len(node.values), tuple(type(one).__name__ for one in node.values), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.FormattedValue): rows.append(('fmt', node.conversion, type(node.value).__name__, type(node.format_spec).__name__ if node.format_spec else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str) and ('{' in node.value or '}' in node.value): rows.append(('brace', len(node.value), node.value.count('{'), node.value.count('}'), getattr(node, 'lineno', 0)))
    consts = tuple((one.co_name, sum(1 for val in one.co_consts if isinstance(val, str))) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), consts, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __tov__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript): rows.append(('sub', type(node.value).__name__, type(node.slice).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Slice): rows.append(('slice', type(node.lower).__name__ if node.lower else '', type(node.upper).__name__ if node.upper else '', type(node.step).__name__ if node.step else ''))
        elif isinstance(node, ast.Starred): rows.append(('star', type(node.value).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    line = tuple((one.co_name, one.co_firstlineno, len(getattr(one, 'co_linetable', b''))) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), line, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __uzn__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Match): rows.append(('match', type(node.subject).__name__, len(node.cases), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.match_case): rows.append(('case', type(node.pattern).__name__, type(node.guard).__name__ if node.guard else '', len(node.body)))
        elif type(node).__name__.startswith('Match'): rows.append((type(node).__name__, getattr(node, 'name', '') or '', getattr(node, 'rest', '') or '', len(list(ast.iter_child_nodes(node)))))
    raw = __dump__(code)
    fog = __mix__(seed, (__hist__(rows), len(raw), hashlib.sha256(raw[:2048]).hexdigest(), tuple(rows[:512]), len(rows)))
    return (len(rows), fog.hex())
def __vok__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.With): rows.append(('with', len(node.items), len(node.body), tuple(type(one.context_expr).__name__ for one in node.items), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.AsyncWith): rows.append(('awith', len(node.items), len(node.body), tuple(type(one.context_expr).__name__ for one in node.items), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.withitem): rows.append(('item', type(node.context_expr).__name__, type(node.optional_vars).__name__ if node.optional_vars else ''))
    ops = tuple((one.co_name, one.co_code.count(143), one.co_code.count(53), one.co_code.count(54)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), ops, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __waz__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.BoolOp): rows.append(('bool', type(node.op).__name__, len(node.values), tuple(type(one).__name__ for one in node.values[:16]), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Compare): rows.append(('cmp', tuple(type(one).__name__ for one in node.ops), len(node.comparators), type(node.left).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.UnaryOp): rows.append(('unary', type(node.op).__name__, type(node.operand).__name__, getattr(node, 'lineno', 0)))
    nums = tuple((one.co_name, sum(1 for val in one.co_consts if isinstance(val, (int, float, complex)) and not isinstance(val, bool))) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), nums, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __xir__(tree, code, seed):
    rows = []
    for one in __drip__(code):
        raw = __dump__(one)
        a = zlib.crc32(raw) & 0xffffffff
        b = zlib.adler32(raw) & 0xffffffff
        c = hashlib.blake2s(raw[:4096], digest_size=16).hexdigest()
        rows.append((one.co_name, len(raw), a, b, c, len(one.co_consts), len(one.co_names), len(one.co_varnames)))
    depth = 0
    hold = [(tree, 0)]
    while hold:
        node, deep = hold.pop(); depth = max(depth, deep)
        for kid in ast.iter_child_nodes(node): hold.append((kid, deep + 1))
    fog = __mix__(seed, (__hist__(rows), depth, tuple(rows[:256]), len(rows)))
    return (len(rows), fog.hex())
def __yok__(tree, code, seed):
    rows = []
    last = None
    for node in ast.walk(tree):
        now = getattr(node, 'lineno', 0)
        col = getattr(node, 'col_offset', 0)
        if now:
            rows.append((type(node).__name__, now, col, 0 if last is None else now - last))
            last = now
    tables = tuple((one.co_name, one.co_firstlineno, len(getattr(one, 'co_linetable', b'')), zlib.crc32(getattr(one, 'co_linetable', b'')) & 0xffffffff) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tables, tuple(rows[:1536]), len(rows)))
    return (len(rows), fog.hex())
def __ruby__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        kids = list(ast.iter_child_nodes(node))
        if len(kids) > 2: rows.append((type(node).__name__, len(kids), tuple(type(one).__name__ for one in kids[:12]), getattr(node, 'lineno', 0)))
    raw = b''.join(one.co_code[:128] for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), hashlib.sha1(raw).hexdigest(), tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())

def __kao__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.If): rows.append(('if', type(node.test).__name__, tuple(type(one).__name__ for one in node.body[:6]), tuple(type(one).__name__ for one in node.orelse[:6]), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.IfExp): rows.append(('ifexp', type(node.test).__name__, type(node.body).__name__, type(node.orelse).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.Break, ast.Continue, ast.Pass)): rows.append((type(node).__name__, getattr(node, 'lineno', 0)))
    jumps = tuple((one.co_name, sum(1 for byte in one.co_code if byte in (110,111,112,114,115,140,176))) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), jumps, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __leo__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        dec = getattr(node, 'decorator_list', None)
        if dec is not None: rows.append(('deco', type(node).__name__, getattr(node, 'name', ''), len(dec), tuple(type(one).__name__ for one in dec[:16]), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ('property','staticmethod','classmethod'): rows.append(('builtin', node.func.id, getattr(node, 'lineno', 0)))
    qual = tuple((one.co_name, one.co_qualname.count('.'), one.co_flags) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), qual, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __mio__(tree, code, seed):
    rows = []
    keys = ('argv','stdin','stdout','stderr','environ','path','platform','version','modules','meta_path','settrace','gettrace')
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in keys: rows.append(('attr', node.attr, type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Name) and node.id in ('sys','os','platform','warnings'): rows.append(('name', node.id, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    pool = tuple((one.co_name, tuple(name for name in one.co_names if name in keys or name in ('sys','os','warnings'))[:32]) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), pool, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __neo__(tree, code, seed):
    rows = []
    keys = ('Structure','windll','kernel32','pythonapi','py_object','c_char_p','c_long','create_string_buffer','cast','byref')
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in keys: rows.append(('attr', node.attr, type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str) and any(key in node.value for key in keys): rows.append(('str', len(node.value), zlib.crc32(node.value.encode()) & 0xffffffff, getattr(node, 'lineno', 0)))
    raw = tuple((one.co_name, sum(1 for name in one.co_names if name in keys)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), raw, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __pio__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            gens = getattr(node, 'generators', [])
            rows.append((type(node).__name__, len(gens), tuple((type(gen.target).__name__, type(gen.iter).__name__, len(gen.ifs), int(gen.is_async)) for gen in gens[:8]), getattr(node, 'lineno', 0)))
    flags = tuple((one.co_name, one.co_flags, len(one.co_freevars), len(one.co_cellvars)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), flags, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __qio__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            raw = node.value.encode('utf-8', 'replace')
            wide = sum(1 for ch in node.value if ord(ch) > 127)
            rows.append((len(raw), wide, node.value.count('\u200d'), node.value.count('\u200c'), zlib.crc32(raw[:1024]) & 0xffffffff, getattr(node, 'lineno', 0)))
    consts = tuple((one.co_name, sum(1 for val in one.co_consts if isinstance(val, str) and any(ord(ch) > 127 for ch in val))) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), consts, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __rio__(tree, code, seed):
    rows = []
    keys = ('Thread','Event','Lock','Queue','Executor','Process','start','join','daemon','submit','result')
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in keys: rows.append(('attr', node.attr, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Call):
            head = node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id if isinstance(node.func, ast.Name) else ''
            if head in keys: rows.append(('call', head, len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
    pool = tuple((one.co_name, tuple(name for name in one.co_names if name in keys)[:32]) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), pool, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __sio__(tree, code, seed):
    rows = []
    keys = ('sha1','sha256','sha512','md5','blake2s','crc32','adler32','hexdigest','digest','compress','decompress','b64encode','b64decode')
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in keys: rows.append(('attr', node.attr, type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Name) and node.id in keys: rows.append(('name', node.id, getattr(node, 'lineno', 0)))
    raw = marshal.dumps(code)
    fog = __mix__(seed, (__hist__(rows), hashlib.sha512(raw[:4096]).hexdigest(), zlib.crc32(raw) & 0xffffffff, tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __tio__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp): rows.append(('bin', type(node.op).__name__, type(node.left).__name__, type(node.right).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.AugAssign): rows.append(('aug', type(node.op).__name__, type(node.target).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
    op = tuple((one.co_name, sum(one.co_code.count(byte) for byte in (45,46,47,48,49,50,51,52,122))) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), op, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __uio__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.keyword): rows.append((node.arg or '*', type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Call) and node.keywords: rows.append(('callkw', len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
    names = tuple((one.co_name, len(one.co_names), tuple(one.co_names[:32])) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), names, tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __vio__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Return): rows.append(('return', type(node.value).__name__ if node.value else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, (ast.Yield, ast.YieldFrom)): rows.append((type(node).__name__, type(node.value).__name__ if node.value else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Expr): rows.append(('expr', type(node.value).__name__, getattr(node, 'lineno', 0)))
    stack = tuple((one.co_name, one.co_stacksize, len(one.co_code)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), stack, tuple(rows[:1536]), len(rows)))
    return (len(rows), fog.hex())
def __wio__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute): rows.append((node.attr, type(node.ctx).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
    chain = []
    for one in __drip__(code):
        chain.append((one.co_name, tuple(name for name in one.co_names[:64]), tuple(one.co_varnames[:32])))
    fog = __mix__(seed, (__hist__(rows), tuple(chain[:256]), tuple(rows[:1536]), len(rows)))
    return (len(rows), fog.hex())

def __xio__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict): rows.append(('dict', len(node.keys), tuple(type(one).__name__ if one else '' for one in node.keys[:32]), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Set): rows.append(('set', len(node.elts), tuple(type(one).__name__ for one in node.elts[:32]), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, len(one.co_consts)) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __yio__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.List): rows.append(('list', len(node.elts), type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Tuple): rows.append(('tuple', len(node.elts), type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, one.co_code[:16]) for one in __drip__(code)[:128]), tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __zio__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.AnnAssign): rows.append(('ann', type(node.target).__name__, type(node.annotation).__name__, type(node.value).__name__ if node.value else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.arg) and node.annotation: rows.append(('arg', node.arg, type(node.annotation).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, one.co_flags) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __kra__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert): rows.append(('assert', type(node.test).__name__, type(node.msg).__name__ if node.msg else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Raise): rows.append(('raise', type(node.exc).__name__ if node.exc else '', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, len(one.co_exceptiontable)) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __lra__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.For): rows.append(('for', type(node.target).__name__, type(node.iter).__name__, len(node.body), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.While): rows.append(('while', type(node.test).__name__, len(node.body), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, one.co_stacksize) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __mra__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom): rows.append((node.module or '', node.level, len(node.names), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.alias): rows.append((node.name, node.asname or '', len(node.name)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, len(one.co_names)) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __nra__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.TryStar): rows.append(('trystar', len(node.body), len(node.handlers), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.ExceptHandler): rows.append(('except', type(node.type).__name__ if node.type else '', len(node.body), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, zlib.crc32(one.co_code) & 0xffffffff) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __pra__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.NamedExpr): rows.append((type(node.target).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Lambda): rows.append((len(node.args.args), type(node.body).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, len(one.co_freevars), len(one.co_cellvars)) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __qra__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef): rows.append((node.name, len(node.bases), len(node.keywords), tuple(type(one).__name__ for one in node.body[:16]), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.keyword): rows.append((node.arg or '*', type(node.value).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, one.co_qualname) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __rra__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Module): rows.append(('module', len(node.body), tuple(type(one).__name__ for one in node.body[:32])))
        elif isinstance(node, ast.Expr): rows.append(('expr', type(node.value).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), hashlib.blake2b(marshal.dumps(code)[:4096], digest_size=32).hexdigest(), tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __grave__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Delete): rows.append(('del', tuple(type(one).__name__ for one in node.targets[:16]), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Global): rows.append(('global', tuple(node.names[:32]), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Nonlocal): rows.append(('nonlocal', tuple(node.names[:32]), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, tuple(one.co_names[:24])) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __shiver__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Await): rows.append(('await', type(node.value).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.AsyncFor): rows.append(('asyncfor', type(node.target).__name__, type(node.iter).__name__, getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.AsyncWith): rows.append(('asyncwith', len(node.items), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, one.co_flags, one.co_stacksize) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __sable__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Slice): rows.append(('slice', type(node.lower).__name__ if node.lower else '', type(node.upper).__name__ if node.upper else '', type(node.step).__name__ if node.step else '', getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.Starred): rows.append(('star', type(node.value).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, len(one.co_consts), one.co_nlocals) for one in __drip__(code)[:128]), tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __mosaic__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.MatchClass): rows.append(('mclass', type(node.cls).__name__, len(node.patterns), len(node.kwd_patterns), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.MatchMapping): rows.append(('mmap', len(node.keys), len(node.patterns), bool(node.rest), getattr(node, 'lineno', 0)))
        elif isinstance(node, ast.MatchSequence): rows.append(('mseq', len(node.patterns), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, zlib.adler32(one.co_code) & 0xffffffff) for one in __drip__(code)[:128]), tuple(rows[:768]), len(rows)))
    return (len(rows), fog.hex())
def __lamb__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Lambda):
            args = node.args
            rows.append((len(args.posonlyargs), len(args.args), len(args.kwonlyargs), int(args.vararg is not None), int(args.kwarg is not None), len(args.defaults), len(args.kw_defaults), type(node.body).__name__, getattr(node, 'lineno', 0)))
            rows.extend(('name', one.arg, len(one.arg)) for one in args.posonlyargs + args.args + args.kwonlyargs)
            args.vararg and rows.append(('var', args.vararg.arg, len(args.vararg.arg)))
            args.kwarg and rows.append(('kw', args.kwarg.arg, len(args.kwarg.arg)))
    fog = __mix__(seed, (__hist__(rows), tuple((one.co_name, len(one.co_freevars), len(one.co_cellvars), one.co_argcount) for one in __drip__(code)[:256]), tuple(rows[:1024]), len(rows)))
    return (len(rows), fog.hex())
def __bee__(tree, code, seed):
    rows = []
    built = {'abs','all','any','ascii','bin','bool','bytearray','bytes','callable','chr','compile','dict','dir','divmod','enumerate','eval','exec','filter','float','format','frozenset','getattr','globals','hasattr','hash','hex','id','input','int','isinstance','issubclass','iter','len','list','locals','map','max','min','next','object','oct','open','ord','pow','print','range','repr','reversed','round','set','setattr','slice','sorted','str','sum','super','tuple','type','vars','zip'}
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            mark = 1 if node.id in built else 0
            rows.append(('name', node.id, mark, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Attribute):
            rows.append(('attr', node.attr, len(node.attr), getattr(node, 'lineno', 0)))
    top = []
    for one in __drip__(code)[:256]:
        top.append((one.co_name, tuple(name for name in one.co_names if name in built), len(one.co_names)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), tuple(top), len(rows)))
    return (len(rows), fog.hex())
def __camel__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            val = node.value
            kind = type(val).__name__
            if isinstance(val, str):
                rows.append(('str', len(val), zlib.crc32(val.encode('utf-8', 'replace')) & 0xffffffff, getattr(node, 'lineno', 0)))
            if isinstance(val, bytes):
                rows.append(('bytes', len(val), zlib.crc32(val) & 0xffffffff, getattr(node, 'lineno', 0)))
            if isinstance(val, int) and not isinstance(val, bool):
                rows.append(('int', val.bit_length(), val & 0xffff, getattr(node, 'lineno', 0)))
            if isinstance(val, float):
                rows.append(('float', repr(val), getattr(node, 'lineno', 0)))
            if isinstance(val, complex):
                rows.append(('complex', repr(val.real), repr(val.imag), getattr(node, 'lineno', 0)))
            if val is None or isinstance(val, bool):
                rows.append((kind, repr(val), getattr(node, 'lineno', 0)))
    raw = []
    for one in __drip__(code)[:256]:
        raw.append((one.co_name, tuple(type(item).__name__ for item in one.co_consts[:64]), len(one.co_consts)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), tuple(raw), len(rows)))
    return (len(rows), fog.hex())
def __warden__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = node.args
            deco = tuple(type(one).__name__ for one in node.decorator_list)
            rows.append(('fn', node.name, len(node.body), len(deco), len(args.args), len(args.kwonlyargs), int(args.vararg is not None), int(args.kwarg is not None), getattr(node, 'lineno', 0)))
            for arg in args.posonlyargs + args.args + args.kwonlyargs:
                rows.append(('arg', node.name, arg.arg, 1 if arg.annotation else 0))
        if isinstance(node, ast.ClassDef):
            rows.append(('cls', node.name, len(node.body), len(node.bases), len(node.decorator_list), getattr(node, 'lineno', 0)))
            for base in node.bases:
                rows.append(('base', node.name, type(base).__name__))
    raw = []
    for one in __drip__(code)[:256]:
        raw.append((one.co_name, one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount, one.co_nlocals, len(one.co_varnames)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), tuple(raw), len(rows)))
    return (len(rows), fog.hex())
def __allay__(tree, code, seed):
    rows = []
    stack = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                rows.append(('imp', alias.name, alias.asname or '', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.ImportFrom):
            rows.append(('from', node.module or '', node.level, len(node.names), getattr(node, 'lineno', 0)))
            for alias in node.names:
                rows.append(('alias', alias.name, alias.asname or ''))
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == '__import__':
                stack.append(('dyn', len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
            if isinstance(node.func, ast.Name) and node.func.id in ('getattr','setattr','delattr','hasattr'):
                stack.append(('reflect', node.func.id, len(node.args), getattr(node, 'lineno', 0)))
    raw = tuple((one.co_name, tuple(one.co_names[:32])) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows + stack), tuple((rows + stack)[:2048]), raw, len(rows), len(stack)))
    return (len(rows) + len(stack), fog.hex())
def __breeze__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            rows.append(('if', type(node.test).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.For):
            rows.append(('for', type(node.target).__name__, type(node.iter).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.While):
            rows.append(('while', type(node.test).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Try):
            rows.append(('try', len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.With):
            rows.append(('with', len(node.items), len(node.body), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Match):
            rows.append(('match', len(node.cases), type(node.subject).__name__, getattr(node, 'lineno', 0)))
    raw = tuple((one.co_name, len(one.co_exceptiontable), one.co_stacksize, one.co_flags) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), raw, len(rows)))
    return (len(rows), fog.hex())
def __sniffer__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.BoolOp):
            rows.append(('bool', type(node.op).__name__, len(node.values), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.BinOp):
            rows.append(('bin', type(node.op).__name__, type(node.left).__name__, type(node.right).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.UnaryOp):
            rows.append(('unary', type(node.op).__name__, type(node.operand).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Compare):
            rows.append(('cmp', tuple(type(op).__name__ for op in node.ops), len(node.comparators), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.IfExp):
            rows.append(('ifexp', type(node.test).__name__, type(node.body).__name__, type(node.orelse).__name__, getattr(node, 'lineno', 0)))
    ops = []
    for one in __drip__(code)[:256]:
        data = one.co_code
        ops.append((one.co_name, tuple(data[:96]), len(data)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), tuple(ops), len(rows)))
    return (len(rows), fog.hex())
def __strider__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ListComp):
            rows.append(('listcomp', len(node.generators), type(node.elt).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.SetComp):
            rows.append(('setcomp', len(node.generators), type(node.elt).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.DictComp):
            rows.append(('dictcomp', len(node.generators), type(node.key).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.GeneratorExp):
            rows.append(('gen', len(node.generators), type(node.elt).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.comprehension):
            rows.append(('comp', type(node.target).__name__, type(node.iter).__name__, len(node.ifs), node.is_async))
    raw = tuple((one.co_name, len(one.co_freevars), len(one.co_cellvars), len(one.co_consts)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), raw, len(rows)))
    return (len(rows), fog.hex())
def __hoglin__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr):
            rows.append(('join', len(node.values), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.FormattedValue):
            rows.append(('fmt', type(node.value).__name__, node.conversion, type(node.format_spec).__name__ if node.format_spec else '', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Subscript):
            rows.append(('sub', type(node.value).__name__, type(node.slice).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Slice):
            rows.append(('slice', int(node.lower is not None), int(node.upper is not None), int(node.step is not None)))
        if isinstance(node, ast.Starred):
            rows.append(('star', type(node.value).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), tuple((one.co_name, one.co_firstlineno) for one in __drip__(code)[:128]), len(rows)))
    return (len(rows), fog.hex())
def __panda__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            rows.append(('assign', len(node.targets), type(node.value).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.AnnAssign):
            rows.append(('annassign', type(node.target).__name__, type(node.annotation).__name__, int(node.value is not None), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.AugAssign):
            rows.append(('aug', type(node.target).__name__, type(node.op).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.NamedExpr):
            rows.append(('walrus', type(node.target).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, (ast.Global, ast.Nonlocal)):
            rows.append(('scope', type(node).__name__, tuple(node.names), getattr(node, 'lineno', 0)))
    raw = tuple((one.co_name, tuple(one.co_varnames[:48]), tuple(one.co_cellvars), tuple(one.co_freevars)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), raw, len(rows)))
    return (len(rows), fog.hex())
def __llama__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Return):
            rows.append(('ret', type(node.value).__name__ if node.value else '', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Yield):
            rows.append(('yield', type(node.value).__name__ if node.value else '', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.YieldFrom):
            rows.append(('yieldfrom', type(node.value).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Await):
            rows.append(('await', type(node.value).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Raise):
            rows.append(('raise', type(node.exc).__name__ if node.exc else '', type(node.cause).__name__ if node.cause else '', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Assert):
            rows.append(('assert', type(node.test).__name__, type(node.msg).__name__ if node.msg else '', getattr(node, 'lineno', 0)))
    raw = tuple((one.co_name, one.co_flags, len(one.co_code), one.co_stacksize) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), raw, len(rows)))
    return (len(rows), fog.hex())
def __ocelot__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Delete):
            rows.append(('del', len(node.targets), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Pass):
            rows.append(('pass', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Break):
            rows.append(('break', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Continue):
            rows.append(('continue', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Expr):
            rows.append(('expr', type(node.value).__name__, getattr(node, 'lineno', 0)))
    raw = []
    for one in __drip__(code)[:256]:
        raw.append((one.co_name, zlib.crc32(one.co_code) & 0xffffffff, len(one.co_code)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), tuple(raw), len(rows)))
    return (len(rows), fog.hex())
def __ravager__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            rows.append(('dict', len(node.keys), len(node.values), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.List):
            rows.append(('list', len(node.elts), type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Tuple):
            rows.append(('tuple', len(node.elts), type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Set):
            rows.append(('set', len(node.elts), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.keyword):
            rows.append(('kw', node.arg or '', type(node.value).__name__))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), tuple((one.co_name, len(one.co_consts)) for one in __drip__(code)[:128]), len(rows)))
    return (len(rows), fog.hex())
def __turtle__(tree, code, seed):
    rows = []
    prev = 0
    for node in ast.walk(tree):
        line = getattr(node, 'lineno', 0)
        end = getattr(node, 'end_lineno', 0)
        col = getattr(node, 'col_offset', 0)
        last = getattr(node, 'end_col_offset', 0)
        if line or end or col or last:
            rows.append((type(node).__name__, line, end, col, last, line - prev))
            prev = line or prev
    raw = tuple((one.co_name, one.co_firstlineno, len(one.co_linetable)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:4096]), raw, len(rows)))
    return (len(rows), fog.hex())
def __phantom__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler):
            rows.append(('except', type(node.type).__name__ if node.type else '', node.name or '', len(node.body), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.TryStar):
            rows.append(('trystar', len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.AsyncFor):
            rows.append(('asyncfor', type(node.target).__name__, type(node.iter).__name__, len(node.body), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.AsyncWith):
            rows.append(('asyncwith', len(node.items), len(node.body), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.AsyncFunctionDef):
            rows.append(('asyncfn', node.name, len(node.body), getattr(node, 'lineno', 0)))
    raw = tuple((one.co_name, one.co_flags, len(one.co_exceptiontable)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), raw, len(rows)))
    return (len(rows), fog.hex())
def __dolphin__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            kind = type(node.func).__name__
            name = ''
            if isinstance(node.func, ast.Name):
                name = node.func.id
            if isinstance(node.func, ast.Attribute):
                name = node.func.attr
            rows.append(('call', kind, name, len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
            for arg in node.args[:16]:
                rows.append(('argkind', name, type(arg).__name__))
    raw = tuple((one.co_name, tuple(one.co_names[:64]), len(one.co_names)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:4096]), raw, len(rows)))
    return (len(rows), fog.hex())
def __fox__(tree, code, seed):
    rows = []
    keys = ('token','password','secret','key','api','auth','cookie','session','bearer','webhook','license','private','credential','encrypt','decrypt','hash','salt','nonce','proxy','host','port','url')
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            low = node.id.lower()
            hit = tuple(word for word in keys if word in low)
            if hit:
                rows.append(('name', node.id, hit, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            low = node.value.lower()
            hit = tuple(word for word in keys if word in low)
            if hit:
                rows.append(('str', len(node.value), hit, getattr(node, 'lineno', 0)))
    raw = tuple((one.co_name, tuple(name for name in one.co_names if any(word in name.lower() for word in keys))) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), raw, len(rows)))
    return (len(rows), fog.hex())
def __goat__(tree, code, seed):
    rows = []
    mods = {'os','sys','subprocess','socket','requests','httpx','urllib','urllib3','ssl','pystyle','hashlib','hmac','base64','marshal','pickle','zlib','bz2','lzma','ctypes','inspect','dis','ast','traceback','threading','asyncio','time','random','secrets'}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split('.')[0]
                rows.append(('imp', root, 1 if root in mods else 0, alias.asname or ''))
        if isinstance(node, ast.ImportFrom):
            root = (node.module or '').split('.')[0]
            rows.append(('from', root, 1 if root in mods else 0, node.level, len(node.names)))
    raw = []
    for one in __drip__(code)[:128]:
        found = tuple(name for name in one.co_names if name.split('.')[0] in mods)
        raw.append((one.co_name, found, len(found)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), tuple(raw), len(rows)))
    return (len(rows), fog.hex())
def __parrot__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.pattern):
            rows.append(('pat', type(node).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.MatchClass):
            rows.append(('mcls', type(node.cls).__name__, len(node.patterns), len(node.kwd_attrs), len(node.kwd_patterns), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.MatchMapping):
            rows.append(('mmap', len(node.keys), len(node.patterns), int(node.rest is not None), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.MatchSequence):
            rows.append(('mseq', len(node.patterns), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.MatchOr):
            rows.append(('mor', len(node.patterns), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), tuple((one.co_name, len(one.co_consts)) for one in __drip__(code)[:128]), len(rows)))
    return (len(rows), fog.hex())
def __rabbit__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)):
            body = getattr(node, 'body', [])
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
                rows.append(('doc', type(node).__name__, getattr(node, 'name', '<module>'), len(body[0].value.value), getattr(body[0], 'lineno', 0)))
            rows.append(('body', type(node).__name__, getattr(node, 'name', '<module>'), len(body)))
    raw = tuple((one.co_name, one.co_consts[0] if one.co_consts and isinstance(one.co_consts[0], str) else '', len(one.co_consts)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), raw, len(rows)))
    return (len(rows), fog.hex())
def __salmon__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            rows.append(('attr', type(node.value).__name__, node.attr, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Subscript):
            rows.append(('sub', type(node.value).__name__, type(node.slice).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            rows.append(('meth', node.func.attr, len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
    raw = tuple((one.co_name, tuple(name for name in one.co_names if not name.startswith('__'))[:64]) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), raw, len(rows)))
    return (len(rows), fog.hex())
def __spider__(tree, code, seed):
    rows = []
    bag = {}
    for node in ast.walk(tree):
        name = type(node).__name__
        bag[name] = bag.get(name, 0) + 1
        line = getattr(node, 'lineno', 0)
        if line:
            rows.append((name, line & 255, bag[name] & 255))
    hist = tuple(sorted(bag.items()))
    raw = tuple((one.co_name, len(one.co_code), len(one.co_names), len(one.co_consts)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), hist, tuple(rows[:4096]), raw, len(rows)))
    return (len(rows), fog.hex())
def __squid__(tree, code, seed):
    rows = []
    for one in __drip__(code):
        data = one.co_code
        part = []
        at = 0
        while at < len(data):
            part.append(data[at])
            at += 2
        rows.append((one.co_name, len(data), zlib.crc32(bytes(part)) & 0xffffffff, sum(part) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows), __glow__(code), __bloom__(code)))
    return (len(rows), fog.hex())
def __wraith__(tree, code, seed):
    rows = []
    names = set()
    attrs = set()
    const = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            names.add(node.id)
        if isinstance(node, ast.Attribute):
            attrs.add(node.attr)
        if isinstance(node, ast.Constant):
            const += 1
    rows.append(('set', len(names), len(attrs), const))
    rows.extend(('name', one, len(one)) for one in sorted(names)[:512])
    rows.extend(('attr', one, len(one)) for one in sorted(attrs)[:512])
    raw = tuple((one.co_name, len(set(one.co_names)), len(set(one.co_varnames))) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows), raw, len(rows)))
    return (len(rows), fog.hex())
def __zombie__(tree, code, seed):
    rows = []
    order = []
    for node in ast.walk(tree):
        order.append(type(node).__name__)
        if len(order) >= 4096:
            break
    for slot, name in enumerate(order):
        left = order[slot - 1] if slot else ''
        right = order[slot + 1] if slot + 1 < len(order) else ''
        rows.append((left, name, right, slot & 255))
    raw = tuple((one.co_name, one.co_firstlineno, one.co_stacksize, one.co_flags) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows), raw, len(rows)))
    return (len(rows), fog.hex())
def __creeper__(tree, code, seed):
    rows = []
    for one in __drip__(code)[:256]:
        raw = __raw__(one)
        rows.append((one.co_name, len(raw), hashlib.sha256(raw[:4096]).hexdigest(), zlib.adler32(raw) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows), len(rows), __echo__(code), __magma__(code)))
    return (len(rows), fog.hex())
def __piglin__(tree, code, seed):
    rows = []
    bank = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            key = type(node.value).__name__
            bank[key] = bank.get(key, 0) + 1
        if isinstance(node, ast.Name):
            key = 'load' if isinstance(node.ctx, ast.Load) else 'store' if isinstance(node.ctx, ast.Store) else 'del'
            bank[key] = bank.get(key, 0) + 1
        if isinstance(node, ast.Call):
            bank['call'] = bank.get('call', 0) + 1
            rows.append(('call', len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
    rows.extend(('bank', one, bank[one]) for one in sorted(bank))
    raw = tuple((one.co_name, len(one.co_names), len(one.co_varnames), len(one.co_consts)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), raw, len(rows)))
    return (len(rows), fog.hex())
def __ghast__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names = []
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name):
                    names.append(sub.id)
            rows.append((type(node).__name__, node.name, len(names), len(set(names)), getattr(node, 'lineno', 0)))
            rows.extend(('seen', node.name, one, names.count(one)) for one in sorted(set(names))[:64])
    raw = tuple((one.co_name, tuple(one.co_names[:32]), tuple(one.co_varnames[:32])) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:4096]), raw, len(rows)))
    return (len(rows), fog.hex())
def __shulker__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            sig = []
            for arg in node.args[:12]:
                sig.append(type(arg).__name__)
            for kw in node.keywords[:12]:
                sig.append('kw:' + (kw.arg or '*') + ':' + type(kw.value).__name__)
            name = ''
            if isinstance(node.func, ast.Name):
                name = node.func.id
            if isinstance(node.func, ast.Attribute):
                name = node.func.attr
            rows.append((name, tuple(sig), getattr(node, 'lineno', 0)))
    raw = tuple((one.co_name, hashlib.sha1(one.co_code).hexdigest(), len(one.co_code)) for one in __drip__(code)[:128])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), raw, len(rows)))
    return (len(rows), fog.hex())
def __enderman__(tree, code, seed):
    rows = []
    depth = {}
    def __step__(node, level):
        name = type(node).__name__
        depth[name] = max(depth.get(name, 0), level)
        for child in ast.iter_child_nodes(node):
            __step__(child, level + 1)
    __step__(tree, 0)
    rows.extend((one, depth[one]) for one in sorted(depth))
    raw = tuple((one.co_name, one.co_stacksize, one.co_nlocals) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows), raw, len(rows)))
    return (len(rows), fog.hex())
def __villager__(tree, code, seed):
    rows = []
    scope = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            scope.append(getattr(node, 'name', ''))
        if isinstance(node, ast.Name):
            rows.append((tuple(scope[-4:]), node.id, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            scope = scope[:-1]
    raw = tuple((one.co_name, one.co_qualname, len(one.co_names), len(one.co_varnames)) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:4096]), raw, len(rows)))
    return (len(rows), fog.hex())
def __pillager__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        line = getattr(node, 'lineno', 0)
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            text = node.value
            rows.append(('s', len(text), sum(ord(ch) for ch in text[:256]) & 0xffffffff, len(set(text)), line))
        if isinstance(node, ast.Constant) and isinstance(node.value, bytes):
            raw = node.value
            rows.append(('b', len(raw), sum(raw[:256]) & 0xffffffff, len(set(raw)), line))
    raw = []
    for one in __drip__(code)[:256]:
        part = []
        for item in one.co_consts[:64]:
            if isinstance(item, (str, bytes)):
                part.append((type(item).__name__, len(item)))
        raw.append((one.co_name, tuple(part)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), tuple(raw), len(rows)))
    return (len(rows), fog.hex())
def __guardian__(tree, code, seed):
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Module):
            rows.append(('module', len(node.body), tuple(type(one).__name__ for one in node.body[:64])))
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            rows.append(('fnbody', node.name, len(node.body), tuple(type(one).__name__ for one in node.body[:64])))
        if isinstance(node, ast.ClassDef):
            rows.append(('clbody', node.name, len(node.body), tuple(type(one).__name__ for one in node.body[:64])))
        if isinstance(node, (ast.If, ast.For, ast.While, ast.With, ast.Try)):
            rows.append(('body', type(node).__name__, len(getattr(node, 'body', [])), len(getattr(node, 'orelse', [])), getattr(node, 'lineno', 0)))
    raw = tuple((one.co_name, len(one.co_consts), len(one.co_names), hashlib.blake2s(one.co_code, digest_size=16).hexdigest()) for one in __drip__(code)[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), raw, len(rows)))
    return (len(rows), fog.hex())
def __oak__(bag, seed):
    rows = []
    for slot, node in enumerate(bag['nodes'][:4096]):
        rows.append(('node', slot & 255, type(node).__name__, getattr(node, 'lineno', 0), getattr(node, 'col_offset', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), bag['wide']))
    return ('oak', len(rows), fog.hex())
def __spruce__(bag, seed):
    rows = []
    last = ''
    for node in bag['nodes'][:4096]:
        name = type(node).__name__
        rows.append((last, name))
        last = name
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('spruce', len(rows), fog.hex())
def __birch__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Name):
            rows.append((node.id, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:4096]), bag['wide']))
    return ('birch', len(rows), fog.hex())
def __jungle__(bag, seed):
    rows = []
    seen = {}
    for node in bag['nodes']:
        if isinstance(node, ast.Name):
            seen[node.id] = seen.get(node.id, 0) + 1
    rows.extend((name, seen[name], len(name)) for name in sorted(seen)[:1024])
    fog = __mix__(seed, (__hist__(rows), tuple(rows), len(seen)))
    return ('jungle', len(rows), fog.hex())
def __acacia__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Attribute):
            root = type(node.value).__name__
            rows.append((node.attr, root, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:4096]), len(rows)))
    return ('acacia', len(rows), fog.hex())
def __mangrove__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Call):
            kind = type(node.func).__name__
            name = ''
            if isinstance(node.func, ast.Name):
                name = node.func.id
            if isinstance(node.func, ast.Attribute):
                name = node.func.attr
            rows.append((kind, name, len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:4096]), len(rows)))
    return ('mangrove', len(rows), fog.hex())
def __cherry__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Constant):
            val = node.value
            kind = type(val).__name__
            size = len(val) if isinstance(val, (str, bytes, tuple, list, set, dict)) else 0
            rows.append((kind, size, repr(val)[:64], getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:4096]), len(rows)))
    return ('cherry', len(rows), fog.hex())
def __bamboo__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
            rows.append((type(node).__name__, len(node.elts), type(getattr(node,'ctx',None)).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Dict):
            rows.append(('Dict', len(node.keys), len(node.values), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('bamboo', len(rows), fog.hex())
def __cactus__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.BinOp):
            rows.append(('bin', type(node.op).__name__, type(node.left).__name__, type(node.right).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.UnaryOp):
            rows.append(('unary', type(node.op).__name__, type(node.operand).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('cactus', len(rows), fog.hex())
def __kelp__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.BoolOp):
            rows.append(('bool', type(node.op).__name__, len(node.values), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Compare):
            rows.append(('cmp', tuple(type(one).__name__ for one in node.ops), len(node.comparators), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('kelp', len(rows), fog.hex())
def __shell__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.If):
            rows.append(('if', type(node.test).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.IfExp):
            rows.append(('ifexp', type(node.test).__name__, type(node.body).__name__, type(node.orelse).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('coralx', len(rows), fog.hex())
def __seagrass__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.For):
            rows.append(('for', type(node.target).__name__, type(node.iter).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.AsyncFor):
            rows.append(('asyncfor', type(node.target).__name__, type(node.iter).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('seagrass', len(rows), fog.hex())
def __mycelium__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.While):
            rows.append(('while', type(node.test).__name__, len(node.body), len(node.orelse), getattr(node, 'lineno', 0)))
        if isinstance(node, (ast.Break, ast.Continue)):
            rows.append((type(node).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('mycelium', len(rows), fog.hex())
def __shroom__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Try):
            rows.append(('try', len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.TryStar):
            rows.append(('trystar', len(node.body), len(node.handlers), len(node.orelse), len(node.finalbody), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('shroom', len(rows), fog.hex())
def __azalea__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.ExceptHandler):
            rows.append((type(node.type).__name__ if node.type else '', node.name or '', len(node.body), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('azalea', len(rows), fog.hex())
def __dripstone__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.With, ast.AsyncWith)):
            rows.append((type(node).__name__, len(node.items), len(node.body), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.withitem):
            rows.append(('item', type(node.context_expr).__name__, type(node.optional_vars).__name__ if node.optional_vars else ''))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('dripstone', len(rows), fog.hex())
def __sculk__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            args = node.args
            rows.append((type(node).__name__, node.name, len(node.body), len(args.args), len(args.kwonlyargs), int(args.vararg is not None), int(args.kwarg is not None), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('sculkx', len(rows), fog.hex())
def __tufa__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.arg):
            rows.append((node.arg, int(node.annotation is not None), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('tuffx', len(rows), fog.hex())
def __calcite__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.ClassDef):
            rows.append((node.name, len(node.bases), len(node.keywords), len(node.body), len(node.decorator_list), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('calcite', len(rows), fog.hex())
def __amethyst__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Lambda):
            args = node.args
            rows.append((len(args.args), len(args.kwonlyargs), int(args.vararg is not None), int(args.kwarg is not None), type(node.body).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('amethyst', len(rows), fog.hex())
def __granite__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Assign):
            rows.append(('assign', len(node.targets), type(node.value).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.AnnAssign):
            rows.append(('ann', type(node.target).__name__, type(node.annotation).__name__, int(node.value is not None), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('granite', len(rows), fog.hex())
def __diorite__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.AugAssign):
            rows.append((type(node.target).__name__, type(node.op).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.NamedExpr):
            rows.append(('named', type(node.target).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('diorite', len(rows), fog.hex())
def __andesite__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Delete):
            rows.append(('del', len(node.targets), getattr(node, 'lineno', 0)))
        if isinstance(node, (ast.Global, ast.Nonlocal)):
            rows.append((type(node).__name__, tuple(node.names), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('andesite', len(rows), fog.hex())
def __crag__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Return):
            rows.append(('ret', type(node.value).__name__ if node.value else '', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Raise):
            rows.append(('raise', type(node.exc).__name__ if node.exc else '', type(node.cause).__name__ if node.cause else '', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('basaltx', len(rows), fog.hex())
def __blackstone__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.Yield, ast.YieldFrom, ast.Await)):
            rows.append((type(node).__name__, type(getattr(node, 'value', None)).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('blackstone', len(rows), fog.hex())
def __netherrack__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Import):
            for alias in node.names:
                rows.append(('imp', alias.name, alias.asname or '', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.ImportFrom):
            rows.append(('from', node.module or '', node.level, tuple((one.name, one.asname or '') for one in node.names), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('netherrack', len(rows), fog.hex())
def __glowstone__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Subscript):
            rows.append((type(node.value).__name__, type(node.slice).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Slice):
            rows.append(('slice', int(node.lower is not None), int(node.upper is not None), int(node.step is not None)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('glowstone', len(rows), fog.hex())
def __endstone__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.JoinedStr):
            rows.append(('join', len(node.values), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.FormattedValue):
            rows.append(('fmt', type(node.value).__name__, node.conversion, type(node.format_spec).__name__ if node.format_spec else '', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('endstone', len(rows), fog.hex())
def __purpur__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.ListComp):
            rows.append(('list', len(node.generators), type(node.elt).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.SetComp):
            rows.append(('set', len(node.generators), type(node.elt).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.DictComp):
            rows.append(('dict', len(node.generators), type(node.key).__name__, type(node.value).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.GeneratorExp):
            rows.append(('gen', len(node.generators), type(node.elt).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('purpur', len(rows), fog.hex())
def __prismarine__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.comprehension):
            rows.append((type(node.target).__name__, type(node.iter).__name__, len(node.ifs), node.is_async))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('prismarine', len(rows), fog.hex())
def __terracotta__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Match):
            rows.append(('match', type(node.subject).__name__, len(node.cases), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.match_case):
            rows.append(('case', type(node.pattern).__name__, int(node.guard is not None), len(node.body)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('terracotta', len(rows), fog.hex())
def __concrete__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.MatchMapping):
            rows.append(('map', len(node.keys), len(node.patterns), int(node.rest is not None), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.MatchClass):
            rows.append(('class', type(node.cls).__name__, len(node.patterns), len(node.kwd_attrs), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.MatchSequence):
            rows.append(('seq', len(node.patterns), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('concrete', len(rows), fog.hex())
def __lantern__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Assert):
            rows.append((type(node.test).__name__, type(node.msg).__name__ if node.msg else '', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Pass):
            rows.append(('pass', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('lantern', len(rows), fog.hex())
def __lamp__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount, one.co_nlocals))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('lamp', len(rows), fog.hex())
def __campfire__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, one.co_stacksize, one.co_flags, one.co_firstlineno, len(one.co_code)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('campfire', len(rows), fog.hex())
def __hammer__(bag, seed):
    rows = []
    for one in bag['codes']:
        raw = '|'.join(one.co_names).encode('utf-8', 'replace')
        rows.append((one.co_name, tuple((slot, len(name), zlib.crc32(name.encode('utf-8', 'replace')) & 0xffffffff) for slot, name in enumerate(one.co_names[:64])), len(one.co_names), zlib.adler32(raw) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('hammer', len(rows), fog.hex())
def __furnace__(bag, seed):
    rows = []
    for one in bag['codes']:
        vals = tuple((slot, name in one.co_names, len(name), sum(name.encode('utf-8', 'replace')) & 0xffff) for slot, name in enumerate(one.co_varnames[:64]))
        rows.append((one.co_name, vals, len(one.co_varnames), one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('furnace', len(rows), fog.hex())
def __hopper__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, tuple(type(item).__name__ for item in one.co_consts[:64]), len(one.co_consts)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('hopper', len(rows), fog.hex())
def __dropper__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, tuple(one.co_freevars), tuple(one.co_cellvars)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('dropper', len(rows), fog.hex())
def __observer__(bag, seed):
    rows = []
    for one in bag['codes']:
        raw = one.co_code
        rows.append((one.co_name, len(raw), zlib.crc32(raw) & 0xffffffff, zlib.adler32(raw) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('observer', len(rows), fog.hex())
def __piston__(bag, seed):
    rows = []
    for one in bag['codes']:
        raw = one.co_code
        rows.append((one.co_name, tuple(raw[:96]), tuple(raw[-32:] if raw else b'')))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return ('piston', len(rows), fog.hex())
def __rail__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, len(one.co_linetable), len(getattr(one, 'co_exceptiontable', b''))))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('rail', len(rows), fog.hex())
def __minecart__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, one.co_filename, one.co_qualname, one.co_firstlineno))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('minecart', len(rows), fog.hex())
def __bee2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            rows.append((getattr(node, 'name', ''), tuple(type(one).__name__ for one in node.decorator_list), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('bee2', len(rows), fog.hex())
def __camel2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.keyword):
            rows.append((node.arg or '*', type(node.value).__name__))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('camel2', len(rows), fog.hex())
def __warden2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.arguments):
            rows.append((len(node.posonlyargs), len(node.args), len(node.kwonlyargs), len(node.defaults), len(node.kw_defaults), int(node.vararg is not None), int(node.kwarg is not None)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('warden2', len(rows), fog.hex())
def __allay2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.arguments):
            rows.append(tuple(type(one).__name__ for one in node.defaults[:32]))
            rows.append(tuple(type(one).__name__ if one else '' for one in node.kw_defaults[:32]))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('allay2', len(rows), fog.hex())
def __breeze2__(bag, seed):
    rows = []
    last = 0
    for node in bag['nodes'][:4096]:
        line = getattr(node, 'lineno', 0)
        if line:
            rows.append((type(node).__name__, line - last, line & 255))
            last = line
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('breeze2', len(rows), fog.hex())
def __sniffer2__(bag, seed):
    rows = []
    for node in bag['nodes'][:4096]:
        start = getattr(node, 'col_offset', 0)
        end = getattr(node, 'end_col_offset', 0)
        if start or end:
            rows.append((type(node).__name__, start, end, end - start))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('sniffer2', len(rows), fog.hex())
def __strider2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Expr):
            rows.append((type(node.value).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('strider2', len(rows), fog.hex())
def __hoglin2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Starred):
            rows.append((type(node.value).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('hoglin2', len(rows), fog.hex())
def __panda2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.FormattedValue):
            rows.append((type(node.value).__name__, node.conversion, type(node.format_spec).__name__ if node.format_spec else '', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('panda2', len(rows), fog.hex())
def __llama2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            text = node.value
            rows.append((len(text), text.count('\n'), text.count('{'), text.count('%'), zlib.crc32(text.encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('llama2', len(rows), fog.hex())
def __ocelot2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and not isinstance(node.value, bool):
            val = node.value
            rows.append((val.bit_length(), val & 255, (val >> 8) & 255, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('ocelot2', len(rows), fog.hex())
def __ravager2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            rows.append((repr(node.value), math.isfinite(node.value), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Constant) and isinstance(node.value, complex):
            rows.append((repr(node.value.real), repr(node.value.imag), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('ravager2', len(rows), fog.hex())
def __turtle2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Constant) and isinstance(node.value, bytes):
            raw = node.value
            rows.append((len(raw), raw[:8], raw[-8:], zlib.crc32(raw) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('turtle2', len(rows), fog.hex())
def __phantom2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            rows.append((node.value.id, node.attr, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('phantom2', len(rows), fog.hex())
def __dolphin2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            rows.append((type(node.func.value).__name__, node.func.attr, len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('dolphin2', len(rows), fog.hex())
def __fox2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            rows.append((node.func.id, len(node.args), len(node.keywords), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('fox2', len(rows), fog.hex())
def __goat2__(bag, seed):
    rows = []
    built = {'len','range','print','open','str','int','float','dict','list','set','tuple','sum','min','max','getattr','setattr','hasattr','__import__'}
    for node in bag['nodes']:
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in built:
            rows.append((node.func.id, len(node.args), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('goat2', len(rows), fog.hex())
def __parrot2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Import):
            rows.extend((alias.name.split('.')[0], alias.name.count('.'), alias.asname or '') for alias in node.names)
        if isinstance(node, ast.ImportFrom):
            rows.append((node.module or '', node.level, len(node.names)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('parrot2', len(rows), fog.hex())
def __rabbit2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)):
            body = getattr(node, 'body', [])
            has = body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str)
            rows.append((type(node).__name__, getattr(node, 'name', ''), int(bool(has)), len(body)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('rabbit2', len(rows), fog.hex())
def __salmon2__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.arg, ast.AnnAssign)):
            rows.append((type(node).__name__, int(getattr(node, 'returns', None) is not None), int(getattr(node, 'annotation', None) is not None), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('salmon2', len(rows), fog.hex())
def __spider2__(bag, seed):
    rows = []
    stack = []
    for node in bag['nodes']:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            stack.append(node.name)
            rows.append((tuple(stack[-6:]), len(getattr(node, 'body', [])), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Return):
            rows.append((tuple(stack[-6:]), 'return', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('spider2', len(rows), fog.hex())
def __squid2__(bag, seed):
    rows = []
    rows.extend(bag.get('shape', ()))
    fog = __mix__(seed, (__hist__(rows), tuple(rows), len(rows)))
    return ('squid2', len(rows), fog.hex())
def __vex2__(bag, seed):
    rows = []
    for one in bag['codes']:
        raw = one.co_code
        rows.append((one.co_name, sum(raw) & 0xffffffff, max(raw) if raw else 0, min(raw) if raw else 0))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('vex2', len(rows), fog.hex())
def __zombie2__(bag, seed):
    rows = []
    for one in bag['codes']:
        raw = one.co_code
        rows.append((one.co_name, tuple(raw[::2][:64]), tuple(raw[1::2][:64])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return ('zombie2', len(rows), fog.hex())
def __creeper2__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, __glow__(one), __bloom__(one), len(one.co_code), zlib.crc32(one.co_code[:2048]) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('creeper2', len(rows), fog.hex())
def __piglin2__(bag, seed):
    rows = [(one.co_name, __echo__(one), __magma__(one), tuple(type(val).__name__ for val in one.co_consts[:32])) for one in bag['codes']]
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return ('piglin2', len(rows), fog.hex())
def __ghast2__(bag, seed):
    rows = []
    at = 0
    while at < len(bag['codes']):
        one = bag['codes'][at]; rows.append((one.co_name, __soul__(one), __wisp__(one), at, len(__dump__(one))))
        at += 1
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return ('ghast2', len(rows), fog.hex())
def __shulker2__(bag, seed):
    rows = []
    for one in bag['codes']:
        raw = __raw__(one)
        rows.append((one.co_name, len(raw), hashlib.blake2s(raw[:4096], digest_size=16).hexdigest()))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('shulker2', len(rows), fog.hex())
def __ender2__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, len(one.co_names), len(set(one.co_names)), len(one.co_varnames), len(set(one.co_varnames))))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('ender2', len(rows), fog.hex())
def __slime2__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, tuple(sorted(set(type(item).__name__ for item in one.co_consts)))[:32]))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('slime2', len(rows), fog.hex())
def __magma2__(bag, seed):
    rows = []
    for one in bag['codes']:
        nums = [item for item in one.co_consts if isinstance(item, int) and not isinstance(item, bool)]
        rows.append((one.co_name, len(nums), sum(val & 0xffff for val in nums[:128]) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('magma2', len(rows), fog.hex())
def __blaze2__(bag, seed):
    rows = []
    for one in bag['codes']:
        txt = [item for item in one.co_consts if isinstance(item, str)]
        rows.append((one.co_name, len(txt), sum(len(item) for item in txt[:128]) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('blaze2', len(rows), fog.hex())
def __stray2__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, tuple(name for name in one.co_names if name.startswith('__'))[:64]))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('stray2', len(rows), fog.hex())
def __husk2__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, tuple(name for name in one.co_varnames if len(name) <= 2)[:64]))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('husk2', len(rows), fog.hex())
def __drowned2__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, getattr(one, 'co_positions', lambda: ())().__class__.__name__, len(one.co_linetable)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('drowned2', len(rows), fog.hex())
def __watch__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, one.co_flags & 0xff, (one.co_flags >> 8) & 0xff, one.co_stacksize))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('wardenx', len(rows), fog.hex())
def __sprite__(bag, seed):
    rows = []
    for node in bag['nodes'][:4096]:
        rows.append((type(node).__name__, int(hasattr(node, 'body')), int(hasattr(node, 'value')), int(hasattr(node, 'target')), int(hasattr(node, 'name'))))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('allayx', len(rows), fog.hex())
def __axolotl__(bag, seed):
    rows = []
    level = []
    for node in bag['nodes']:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            level.append(getattr(node, 'name', ''))
            rows.append(('push', tuple(level[-8:]), getattr(node, 'lineno', 0)))
        if isinstance(node, (ast.Return, ast.Raise, ast.Yield, ast.Await)):
            rows.append(('act', tuple(level[-8:]), type(node).__name__, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('axolotl', len(rows), fog.hex())
def __armadillo__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Call):
            pos = tuple(type(one).__name__ for one in node.args[:16])
            key = tuple((one.arg or '*', type(one.value).__name__) for one in node.keywords[:16])
            rows.append((type(node.func).__name__, pos, key, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('armadillo', len(rows), fog.hex())
def __badger__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Constant):
            val = node.value
            if isinstance(val, str):
                rows.append(('str', len(val), len(set(val)), sum(ord(ch) for ch in val[:128]) & 0xffffffff))
            if isinstance(val, bytes):
                rows.append(('bytes', len(val), len(set(val)), sum(val[:128]) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('badger', len(rows), fog.hex())
def __bogged__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.MatchAs):
            rows.append(('as', node.name or '', type(node.pattern).__name__ if node.pattern else '', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.MatchStar):
            rows.append(('star', node.name or '', getattr(node, 'lineno', 0)))
        if isinstance(node, ast.MatchOr):
            rows.append(('or', len(node.patterns), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('bogged', len(rows), fog.hex())
def __breezez__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            for comp in node.generators:
                rows.append((type(node).__name__, type(comp.target).__name__, type(comp.iter).__name__, len(comp.ifs), comp.is_async, getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('breezez', len(rows), fog.hex())
def __cat__(bag, seed):
    rows = []
    side = getattr(ast, 'ExtSlice', None)
    for node in bag['nodes']:
        if isinstance(node, ast.Subscript):
            rows.append((type(node.value).__name__, type(node.slice).__name__, type(node.ctx).__name__, getattr(node, 'lineno', 0)))
        if side is not None and isinstance(node, side):
            rows.append(('ext', len(node.dims)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('catx', len(rows), fog.hex())
def __donkey__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.ImportFrom):
            rows.append((node.module or '', node.level, tuple(alias.name for alias in node.names), tuple(alias.asname or '' for alias in node.names)))
        if isinstance(node, ast.Import):
            rows.append(('', 0, tuple(alias.name for alias in node.names), tuple(alias.asname or '' for alias in node.names)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('donkey', len(rows), fog.hex())
def __frog__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Assign):
            rows.append((tuple(type(one).__name__ for one in node.targets[:16]), type(node.value).__name__, getattr(node, 'lineno', 0)))
        if isinstance(node, ast.Delete):
            rows.append((tuple(type(one).__name__ for one in node.targets[:16]), '', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('frog', len(rows), fog.hex())
def __horse__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.For, ast.AsyncFor)):
            rows.append((type(node.target).__name__, type(node.iter).__name__, tuple(type(one).__name__ for one in node.body[:16]), tuple(type(one).__name__ for one in node.orelse[:16]), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('horse', len(rows), fog.hex())
def __metal__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.Try):
            rows.append((tuple(type(one).__name__ for one in node.body[:16]), tuple(type(one.type).__name__ if one.type else '' for one in node.handlers[:16]), tuple(type(one).__name__ for one in node.finalbody[:16]), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('metal', len(rows), fog.hex())
def __mooshroom__(bag, seed):
    rows = []
    for one in bag['codes']:
        size = len(one.co_code)
        head = one.co_code[:16]
        tail = one.co_code[-16:] if one.co_code else b''
        rows.append((one.co_name, size, head, tail, hashlib.sha1(one.co_code).hexdigest()))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return ('mooshroom', len(rows), fog.hex())
def __mule__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, tuple((name, len(name)) for name in one.co_names[:64]), tuple((name, len(name)) for name in one.co_varnames[:64])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return ('mule', len(rows), fog.hex())
def __polar__(bag, seed):
    rows = []
    for one in bag['codes']:
        vals = []
        for item in one.co_consts[:128]:
            vals.append((type(item).__name__, len(item) if isinstance(item, (str, bytes, tuple)) else 0))
        rows.append((one.co_name, tuple(vals)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return ('polar', len(rows), fog.hex())
def __snow__(bag, seed):
    rows = []
    for node in bag['nodes'][:4096]:
        line = getattr(node, 'lineno', 0)
        end = getattr(node, 'end_lineno', 0)
        rows.append((type(node).__name__, line, end, end - line if end and line else 0))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('snow', len(rows), fog.hex())
def __wolf__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.ClassDef):
            rows.append((node.name, tuple(type(one).__name__ for one in node.bases), tuple(key.arg or '' for key in node.keywords), tuple(type(one).__name__ for one in node.body[:32])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('wolfx', len(rows), fog.hex())
def __zoglin__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.FunctionDef):
            rows.append((node.name, 'sync', tuple(type(one).__name__ for one in node.body[:32]), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.AsyncFunctionDef):
            rows.append((node.name, 'async', tuple(type(one).__name__ for one in node.body[:32]), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('zoglin', len(rows), fog.hex())
def __brute__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.If, ast.While)):
            rows.append((type(node).__name__, type(node.test).__name__, tuple(type(one).__name__ for one in node.body[:16]), tuple(type(one).__name__ for one in node.orelse[:16]), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('piglinx', len(rows), fog.hex())
def __silver__(bag, seed):
    rows = []
    for one in bag['codes']:
        raw = one.co_exceptiontable
        rows.append((one.co_name, len(raw), zlib.crc32(raw) & 0xffffffff if raw else 0, tuple(raw[:32])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return ('silver', len(rows), fog.hex())
def __copper__(bag, seed):
    rows = []
    for node in bag['nodes']:
        body = getattr(node, 'body', None)
        if isinstance(body, list):
            rows.append((type(node).__name__, getattr(node, 'name', ''), tuple(type(one).__name__ for one in body[:32]), len(body), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('copper', len(rows), fog.hex())
def __wax__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.ExceptHandler):
            rows.append((node.name or '', type(node.type).__name__ if node.type else '', tuple(type(one).__name__ for one in node.body[:32]), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('wax', len(rows), fog.hex())
def __glint__(bag, seed):
    rows = []
    for node in bag['nodes']:
        ann = getattr(node, 'annotation', None)
        ret = getattr(node, 'returns', None)
        if ann is not None or ret is not None:
            rows.append((type(node).__name__, type(ann).__name__ if ann else '', type(ret).__name__ if ret else '', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('glint', len(rows), fog.hex())
def __echoes__(bag, seed):
    rows = []
    depth = [0]
    for node in bag['nodes']:
        if isinstance(node, ast.Call):
            depth[0] += 1
            rows.append((depth[0] & 255, type(node.func).__name__, len(node.args), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:2048]), len(rows)))
    return ('echoes', len(rows), fog.hex())
def __golem__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.ClassDef):
            funcs = []
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    funcs.append((item.name, len(item.args.args), len(item.body)))
            rows.append((node.name, tuple(funcs[:64]), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('golem', len(rows), fog.hex())
def __ravine__(bag, seed):
    rows = []
    for one in bag['codes']:
        rows.append((one.co_name, one.co_flags & 3, one.co_flags & 12, one.co_flags & 240, one.co_flags >> 8))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('ravine', len(rows), fog.hex())
def __geode__(bag, seed):
    rows = []
    for one in bag['codes']:
        raw = __vine__(one.co_consts[:128])
        rows.append((one.co_name, len(raw), hashlib.sha256(raw).hexdigest(), zlib.crc32(raw) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), len(rows)))
    return ('geode', len(rows), fog.hex())
def __spire__(bag, seed):
    rows = []
    for one in bag['codes']:
        raw = one.co_code
        parts = []
        at = 0
        while at < len(raw):
            part = raw[at:at + 16]
            parts.append((len(part), sum(part) & 0xffff, part[:1], part[-1:]))
            at += 16
        rows.append((one.co_name, tuple(parts[:64])))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:128]), len(rows)))
    return ('spire', len(rows), fog.hex())
def __agate__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            args = getattr(node, 'args', None)
            if args is None:
                continue
            names = []
            for one in list(args.posonlyargs) + list(args.args) + list(args.kwonlyargs):
                names.append(one.arg)
            if args.vararg:
                names.append(args.vararg.arg)
            if args.kwarg:
                names.append(args.kwarg.arg)
            loads = []
            for part in ast.walk(node):
                if isinstance(part, ast.Name) and isinstance(part.ctx, ast.Load):
                    loads.append(part.id)
            rows.append((getattr(node, 'name', '<lambda>'), tuple(sorted(set(names) & set(loads))), len(names), len(loads), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('agate', len(rows), fog.hex())
def __jade__(bag, seed):
    rows = []
    roots = (ast.If, ast.For, ast.AsyncFor, ast.While, ast.Try, ast.With, ast.AsyncWith, ast.Match)
    for node in bag['nodes']:
        if isinstance(node, roots):
            body = getattr(node, 'body', [])
            other = getattr(node, 'orelse', [])
            final = getattr(node, 'finalbody', [])
            cases = getattr(node, 'cases', [])
            chain = []
            for part in body[:16]:
                chain.append(type(part).__name__)
            for part in other[:16]:
                chain.append('else:' + type(part).__name__)
            for part in final[:16]:
                chain.append('final:' + type(part).__name__)
            for part in cases[:16]:
                chain.append('case:' + type(part.pattern).__name__)
            rows.append((type(node).__name__, tuple(chain), len(body), len(other), len(final), len(cases), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('jade', len(rows), fog.hex())
def __quartz__(bag, seed):
    rows = []
    for node in bag['nodes']:
        if isinstance(node, ast.JoinedStr):
            parts = []
            for one in node.values:
                if isinstance(one, ast.Constant):
                    parts.append(('const', len(str(one.value))))
                if isinstance(one, ast.FormattedValue):
                    spec = one.format_spec
                    parts.append(('fmt', one.conversion, type(one.value).__name__, type(spec).__name__ if spec is not None else ''))
            rows.append((tuple(parts), getattr(node, 'lineno', 0)))
        if isinstance(node, ast.FormattedValue):
            rows.append(('one', type(node.value).__name__, node.conversion, type(node.format_spec).__name__ if node.format_spec is not None else '', getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('quartz', len(rows), fog.hex())
def __mica__(bag, seed):
    rows = []
    kinds = (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
    for node in bag['nodes']:
        if isinstance(node, kinds):
            gens = []
            for gen in node.generators:
                tests = []
                for test in gen.ifs:
                    tests.append(type(test).__name__)
                gens.append((type(gen.target).__name__, type(gen.iter).__name__, gen.is_async, tuple(tests), len(gen.ifs)))
            elt = getattr(node, 'elt', None)
            key = getattr(node, 'key', None)
            val = getattr(node, 'value', None)
            rows.append((type(node).__name__, type(elt).__name__ if elt is not None else '', type(key).__name__ if key is not None else '', type(val).__name__ if val is not None else '', tuple(gens), getattr(node, 'lineno', 0)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('mica', len(rows), fog.hex())
def __lexi__(text):
    rows = []
    tok = __import__('tokenize')
    io = __import__('io')
    try:
        for one in tok.generate_tokens(io.StringIO(text).readline):
            rows.append((one.type, one.string, one.start, one.end, one.line))
    except tok.TokenError as err:
        rows.append((-1, repr(err), (0, 0), (0, 0), ''))
    return tuple(rows)
def __linen__(text, lex, path, seed):
    rows = []
    lines = text.splitlines(True)
    vals = []
    for slot, line in enumerate(lines):
        vals.append(len(line))
        rows.append((slot & 255, len(line), int(line.endswith('\n')), int(line.endswith('\r\n')), zlib.crc32(line.encode('utf-8', 'replace')) & 0xffffffff))
    wide = (min(vals) if vals else 0, max(vals) if vals else 0, sum(vals) if vals else 0, len(vals))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), tuple(rows[-128:]), wide))
    return ('linen', len(rows), fog.hex())
def __gap__(text, lex, path, seed):
    rows = []
    space = tab = cr = lf = form = vert = 0
    for ch in text:
        if ch == ' ': space += 1
        elif ch == '\t': tab += 1
        elif ch == '\r': cr += 1
        elif ch == '\n': lf += 1
        elif ch == '\f': form += 1
        elif ch == '\v': vert += 1
    for line in text.splitlines():
        lead = len(line) - len(line.lstrip(' \t'))
        rows.append((lead, line[:lead], len(line), len(line.rstrip(' \t'))))
    fog = __mix__(seed, ((space, tab, cr, lf, form, vert), __hist__(rows), tuple(rows[:512])))
    return ('gap', len(rows), fog.hex())
def __dent__(text, lex, path, seed):
    rows = []
    stack = [0]
    turns = []
    for line in text.splitlines():
        if not line.strip():
            continue
        lead = len(line) - len(line.lstrip(' '))
        hard = len(line) - len(line.lstrip('\t'))
        mix = lead + hard * 8
        if mix > stack[-1]:
            stack.append(mix); turns.append(('in', mix, len(stack)))
        while mix < stack[-1] and len(stack) > 1:
            turns.append(('out', stack.pop(), len(stack)))
        rows.append((mix, hard, len(line), line.lstrip()[:12]))
    fog = __mix__(seed, (__hist__(rows), tuple(turns[:512]), tuple(rows[:512]), len(stack)))
    return ('dent', len(rows), fog.hex())
def __track__(text, lex, path, seed):
    rows = []
    hits = []
    for slot, line in enumerate(text.splitlines(True)):
        tail = len(line.rstrip('\r\n')) - len(line.rstrip(' \t\r\n'))
        semi = line.rstrip().endswith(';')
        if tail or semi:
            hits.append((slot, tail, int(semi), len(line)))
        rows.append((tail, int(semi), len(line), line.count(';')))
    fog = __mix__(seed, (__hist__(rows), tuple(hits[:512]), len(hits)))
    return ('track', len(hits), fog.hex())
def __letter__(text, lex, path, seed):
    rows = []
    uni = __import__('unicodedata')
    cats = {}
    wide = [0, 0, 0, 0, 0]
    for ch in text:
        cat = uni.category(ch)
        cats[cat] = cats.get(cat, 0) + 1
        code = ord(ch)
        if code < 128: wide[0] += 1
        elif code < 2048: wide[1] += 1
        elif code < 65536: wide[2] += 1
        elif code < 1114112: wide[3] += 1
        if ch.isidentifier(): wide[4] += 1
    for key in sorted(cats):
        rows.append((key, cats[key]))
    fog = __mix__(seed, (tuple(rows), tuple(wide), len(text)))
    return ('glyphs', len(rows), fog.hex())
def __word__(text, lex, path, seed):
    rows = []
    words = []
    name = getattr(__import__('token'), 'NAME')
    for typ, val, start, end, line in lex:
        if typ == name:
            words.append(val)
    bits = [0] * 64
    ngram = {}
    for word in words[:4096]:
        low = word.lower()
        raw = word.encode('utf-8', 'replace')
        mark = int.from_bytes(hashlib.blake2s(raw, digest_size=8).digest(), 'little')
        for bit in range(64):
            bits[bit] += 1 if (mark >> bit) & 1 else -1
        for slot in range(max(0, len(low) - 2)):
            tri = low[slot:slot + 3]
            ngram[tri] = ngram.get(tri, 0) + 1
        rows.append((len(word), int(word == low), int(word.isupper()), int(any(ord(ch) > 127 for ch in word)), word.count('_'), zlib.crc32(raw) & 0xffffffff))
    face = sum((1 << bit) for bit, val in enumerate(bits) if val >= 0)
    gram = tuple(sorted(ngram.items(), key=lambda row: (-row[1], row[0]))[:256])
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(set(words)), len(words), face, gram))
    return ('word', len(words), fog.hex())
def __key__(text, lex, path, seed):
    rows = []
    key = set(__import__('keyword').kwlist)
    name = getattr(__import__('token'), 'NAME')
    flow = []
    for typ, val, start, end, line in lex:
        if typ == name and val in key:
            flow.append((val, start[0], start[1]))
    for val, row, col in flow[:2048]:
        rows.append((val, row & 255, col, len(val)))
    fog = __mix__(seed, (__hist__(val for val, _, _ in flow), tuple(rows), len(flow)))
    return ('key', len(flow), fog.hex())
def __digit__(text, lex, path, seed):
    rows = []
    num = getattr(__import__('token'), 'NUMBER')
    for typ, val, start, end, line in lex:
        if typ != num:
            continue
        low = val.lower()
        rows.append((len(val), int('x' in low), int('b' in low), int('o' in low), int('e' in low), int('_' in low), int('j' in low), start[0] & 255, zlib.crc32(val.encode()) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('numx', len(rows), fog.hex())
def __string__(text, lex, path, seed):
    rows = []
    st = getattr(__import__('token'), 'STRING')
    for typ, val, start, end, line in lex:
        if typ != st:
            continue
        low = val[:8].lower()
        raw = val.encode('utf-8', 'replace')
        hist = [0] * 8
        for byte in raw[:4096]:
            hist[byte >> 5] += 1
        ent = 0
        if raw:
            tab = {}
            for byte in raw[:4096]:
                tab[byte] = tab.get(byte, 0) + 1
            for valx in tab.values():
                ent += valx * valx
        rows.append((len(val), int("'''" in val[:6] or '"""' in val[:6]), int('r' in low), int('b' in low), int('f' in low), val[:3], val[-3:], tuple(hist), ent, zlib.crc32(raw) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows), __hist__(row[7] for row in rows)))
    return ('string', len(rows), fog.hex())
def __head__(text, lex, path, seed):
    rows = []
    st = getattr(__import__('token'), 'STRING')
    for typ, val, start, end, line in lex:
        if typ != st:
            continue
        pre = []
        for ch in val[:8]:
            if ch in 'rRuUbBfF':
                pre.append(ch.lower())
            elif ch in '"\'':
                break
        rows.append((''.join(pre), len(val), start[0] & 255))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('head', len(rows), fog.hex())
def __slash__(text, lex, path, seed):
    rows = []
    st = getattr(__import__('token'), 'STRING')
    for typ, val, start, end, line in lex:
        if typ != st:
            continue
        esc = val.count('\\')
        rows.append((esc, val.count('\\n'), val.count('\\x'), val.count('\\u'), val.count('\\U'), val.count('\\N'), len(val)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('slash', len(rows), fog.hex())
def __mold__(text, lex, path, seed):
    rows = []
    st = getattr(__import__('token'), 'STRING')
    for typ, val, start, end, line in lex:
        low = val[:8].lower()
        if typ == st and 'f' in low:
            dep = top = 0
            for ch in val:
                if ch == '{':
                    dep += 1
                    top = max(top, dep)
                elif ch == '}' and dep:
                    dep -= 1
            rows.append((len(val), val.count('{'), val.count('}'), val.count('!'), val.count(':'), top, dep, start[0] & 255))
    scan = []
    for slot, line in enumerate(text.splitlines()):
        if 'f"' in line or "f'" in line or 'F"' in line or "F'" in line:
            scan.append((slot, line.count('{'), line.count('}'), line.count('='), line.count('!'), len(line)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:256]), tuple(scan[:256]), len(scan), __hist__(row[5] for row in rows)))
    return ('mold', len(rows) + len(scan), fog.hex())
def __brace__(text, lex, path, seed):
    rows = []
    open = {'(': 0, '[': 0, '{': 0}
    close = {')': 0, ']': 0, '}': 0}
    for ch in text:
        if ch in open: open[ch] += 1
        elif ch in close: close[ch] += 1
    rows.extend((key, open[key]) for key in sorted(open))
    rows.extend((key, close[key]) for key in sorted(close))
    fog = __mix__(seed, (tuple(rows), len(text), zlib.crc32(text.encode('utf-8', 'replace')) & 0xffffffff))
    return ('bracez', len(rows), fog.hex())
def __paren__(text, lex, path, seed):
    rows = []
    dep = 0
    top = 0
    hist = {}
    for ch in text:
        if ch in '([{':
            dep += 1
            top = max(top, dep)
        elif ch in ')]}' and dep:
            dep -= 1
        hist[dep] = hist.get(dep, 0) + 1
    for key in sorted(hist)[:256]:
        rows.append((key, hist[key]))
    fog = __mix__(seed, (tuple(rows), top, dep, len(text)))
    return ('paren', len(rows), fog.hex())
def __sign__(text, lex, path, seed):
    rows = []
    op = getattr(__import__('token'), 'OP')
    vals = {}
    for typ, val, start, end, line in lex:
        if typ == op:
            vals[val] = vals.get(val, 0) + 1
    for key in sorted(vals):
        rows.append((key, vals[key]))
    fog = __mix__(seed, (tuple(rows), len(rows)))
    return ('sign', len(rows), fog.hex())
def __point__(text, lex, path, seed):
    rows = []
    vals = [one[1] for one in lex]
    for slot in range(1, len(vals) - 1):
        if vals[slot] == '.' and vals[slot - 1].isidentifier() and vals[slot + 1].isidentifier():
            rows.append((vals[slot - 1][-16:], vals[slot + 1][:16], slot & 1023))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('point', len(rows), fog.hex())
def __summon__(text, lex, path, seed):
    rows = []
    vals = [(one[0], one[1], one[2]) for one in lex if one[1].strip()]
    name = getattr(__import__('token'), 'NAME')
    for slot in range(len(vals) - 1):
        if vals[slot][0] == name and vals[slot + 1][1] == '(':
            rows.append((vals[slot][1], vals[slot][2][0] & 255, vals[slot][2][1]))
    fog = __mix__(seed, (__hist__(row[0] for row in rows), tuple(rows[:1024]), len(rows)))
    return ('summon', len(rows), fog.hex())
def __bring__(text, lex, path, seed):
    rows = []
    lines = text.splitlines()
    for slot, line in enumerate(lines):
        cut = line.strip()
        if cut.startswith('import ') or cut.startswith('from '):
            rows.append((slot & 255, len(cut), cut.count(','), cut.count('.'), zlib.crc32(cut.encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('bring', len(rows), fog.hex())
def __path__(text, lex, path, seed):
    rows = []
    base = os.path.basename(path)
    root = os.path.dirname(path)
    parts = [part for part in root.replace('\\', '/').split('/') if part]
    for slot, part in enumerate(parts[-16:]):
        rows.append((slot, len(part), zlib.crc32(part.encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, (base, len(base), tuple(rows), len(text)))
    return ('path', len(rows), fog.hex())
def __shebang__(text, lex, path, seed):
    first = text.splitlines()[0] if text.splitlines() else ''
    hit = first.startswith('#!')
    row = (int(hit), len(first), first[:64], zlib.crc32(first.encode('utf-8', 'replace')) & 0xffffffff)
    fog = __mix__(seed, row)
    return ('shebang', int(hit), fog.hex())
def __coding__(text, lex, path, seed):
    rows = []
    for slot, line in enumerate(text.splitlines()[:2]):
        low = line.lower()
        hit = 'coding' in low or 'encoding' in low
        rows.append((slot, int(hit), len(line), zlib.crc32(line.encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, tuple(rows))
    return ('coding', len(rows), fog.hex())
def __blank__(text, lex, path, seed):
    rows = []
    run = 0
    for line in text.splitlines():
        if line.strip():
            if run:
                rows.append(run)
                run = 0
        else:
            run += 1
    if run:
        rows.append(run)
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('blank', len(rows), fog.hex())
def __chunk__(text, lex, path, seed):
    rows = []
    lines = text.splitlines()
    at = 0
    while at < len(lines):
        part = lines[at:at + 16]
        vals = [len(line) for line in part]
        rows.append((at // 16, sum(vals), max(vals) if vals else 0, min(vals) if vals else 0, zlib.adler32('\n'.join(part).encode('utf-8', 'replace')) & 0xffffffff))
        at += 16
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('chunk', len(rows), fog.hex())
def __cover__(text, lex, path, seed):
    rows = []
    for slot, line in enumerate(text.splitlines()):
        cut = line.rstrip()
        rows.append((int(cut.endswith('\\')), int(line.startswith((' ', '\t'))), cut.count(','), cut.count('(') + cut.count('[') + cut.count('{'), len(cut)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('cover', len(rows), fog.hex())
def __style__(text, lex, path, seed):
    rows = []
    name = getattr(__import__('token'), 'NAME')
    for typ, val, start, end, line in lex:
        if typ != name:
            continue
        low = val.lower()
        snake = '_' in val
        camel = any(ch.isupper() for ch in val[1:])
        rows.append((len(val), int(snake), int(camel), int(val == low), int(val[:1].isupper())))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('style', len(rows), fog.hex())
def __noise__(text, lex, path, seed):
    rows = []
    chars = '{}[]();:,.+-*/%@&|^~=<>'
    for ch in chars:
        rows.append((ch, text.count(ch)))
    fog = __mix__(seed, (tuple(rows), len(text)))
    return ('noise', len(rows), fog.hex())
def __ratio__(text, lex, path, seed):
    total = len(text) or 1
    line = len(text.splitlines()) or 1
    alpha = sum(1 for ch in text if ch.isalpha())
    digit = sum(1 for ch in text if ch.isdigit())
    space = sum(1 for ch in text if ch.isspace())
    punct = total - alpha - digit - space
    row = (total, line, alpha * 1000 // total, digit * 1000 // total, space * 1000 // total, punct * 1000 // total)
    fog = __mix__(seed, row)
    return ('ratio', total, fog.hex())
def __duet__(text, lex, path, seed):
    rows = []
    seen = {}
    for slot in range(max(0, len(text) - 1)):
        pair = text[slot:slot + 2]
        seen[pair] = seen.get(pair, 0) + 1
    tri = {}
    for slot in range(max(0, len(text) - 2)):
        one = text[slot:slot + 3]
        tri[one] = tri.get(one, 0) + 1
    for key, val in sorted(seen.items(), key=lambda row: (-row[1], row[0]))[:512]:
        rows.append((key, val))
    top = tuple(sorted(tri.items(), key=lambda row: (-row[1], row[0]))[:256])
    fog = __mix__(seed, (tuple(rows), top, len(seen), len(tri), len(text)))
    return ('duet', len(rows) + len(top), fog.hex())
def __current__(text, lex, path, seed):
    rows = []
    keys = {'if', 'elif', 'else', 'for', 'while', 'try', 'except', 'finally', 'with', 'match', 'case', 'return', 'yield', 'raise', 'assert'}
    name = getattr(__import__('token'), 'NAME')
    for typ, val, start, end, line in lex:
        if typ == name and val in keys:
            rows.append((val, start[0] & 255, start[1]))
    fog = __mix__(seed, (__hist__(row[0] for row in rows), tuple(rows[:1024]), len(rows)))
    return ('flowtxt', len(rows), fog.hex())
def __brine__(text, lex, path, seed):
    raw = text.encode('utf-8', 'replace')
    cuts = []
    for step in (1, 3, 5, 7, 11):
        bag = bytearray()
        for slot, byte in enumerate(raw[:65536]):
            bag.append((byte + step + slot) & 255)
        cuts.append((step, len(bag), zlib.crc32(bytes(bag)) & 0xffffffff, hashlib.sha1(bytes(bag[:4096])).hexdigest()))
    fog = __mix__(seed, tuple(cuts))
    return ('saltxt', len(raw), fog.hex())
def __scan__(text, lex, path, seed):
    rows = []
    keys = ('exec', 'eval', 'compile', 'open', '__import__', 'getattr', 'setattr', 'globals', 'locals', 'vars', 'input', 'print', 'len', 'list', 'bytearray', 'socket', 'subprocess', 'requests', 'requests.sessions', 'requests.api', 'httpx', 'aiohttp', 'urllib', 'urllib3', 'ssl', 'pystyle', 'pickle', 'marshal', 'base64', 'zlib', 'bz2', 'lzma', 'ctypes', 'threading', 'asyncio', 'password', 'token', 'secret', 'cookie', 'session', 'apikey', 'webhook', 'bearer', 'credential', 'license')
    low = text.lower()
    for key in keys:
        count = low.count(key)
        if count:
            rows.append((key, count, low.find(key), low.rfind(key)))
    fog = __mix__(seed, (tuple(rows), __hist__(row[0] for row in rows), len(low)))
    return ('scan', len(rows), fog.hex())
def __moss__(text, lex, path, seed):
    rows = []
    last = ''
    for slot, line in enumerate(text.splitlines()):
        cut = line.strip()
        if cut:
            rows.append((slot & 255, len(cut), zlib.crc32((last + cut).encode('utf-8', 'replace')) & 0xffffffff))
            last = cut[-32:]
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), tuple(rows[-256:])))
    return ('mossy', len(rows), fog.hex())
def __reed__(text, lex, path, seed):
    rows = []
    vals = text.splitlines()
    for slot in range(0, len(vals), 8):
        part = vals[slot:slot + 8]
        tall = ''.join(line[:1] for line in part)
        deep = ''.join(line[-1:] for line in part if line)
        rows.append((slot // 8, len(part), zlib.crc32(tall.encode('utf-8', 'replace')) & 0xffffffff, zlib.adler32(deep.encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('reedx', len(rows), fog.hex())
def __weave__(text, lex, path, seed):
    rows = []
    name = getattr(__import__('token'), 'NAME')
    op = getattr(__import__('token'), 'OP')
    last = None
    for typ, val, start, end, line in lex:
        if typ in (name, op):
            if last is not None:
                rows.append((last[0], val, start[0] - last[1][0], start[1]))
            last = (val, start)
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('loomx', len(rows), fog.hex())
def __flax__(text, lex, path, seed):
    rows = []
    vals = []
    for typ, val, start, end, line in lex:
        vals.append((typ, len(val), start[0], start[1], end[0], end[1]))
    for slot in range(0, len(vals), 32):
        part = vals[slot:slot + 32]
        rows.append((slot // 32, len(part), __hist__(one[0] for one in part), sum(one[1] for one in part)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(vals)))
    return ('flax', len(rows), fog.hex())
def __fiber__(text, lex, path, seed):
    rows = []
    for line in text.splitlines():
        if not line:
            continue
        rows.append((len(line), line[:1], line[-1:], line.count(' '), line.count('\t'), zlib.crc32(line[:80].encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('grainx', len(rows), fog.hex())
def __badge__(text, lex, path, seed):
    rows = []
    cur = hashlib.sha256(seed).digest()
    for line in text.splitlines()[:4096]:
        raw = line.encode('utf-8', 'replace')
        cur = hashlib.sha256(cur + len(raw).to_bytes(4, 'little') + raw[:256]).digest()
        rows.append((cur[:4], len(raw), raw[:1], raw[-1:]))
    fog = __mix__(seed, (cur, tuple(rows[:256]), len(rows)))
    return ('stampx', len(rows), fog.hex())
def __crease__(text, lex, path, seed):
    rows = []
    lines = text.splitlines()
    for slot, line in enumerate(lines):
        left = line[:len(line) // 2]
        right = line[len(line) // 2:]
        rows.append((slot & 255, zlib.crc32(left.encode('utf-8', 'replace')) & 0xffffffff, zlib.adler32(right.encode('utf-8', 'replace')) & 0xffffffff, len(left), len(right)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('foldx', len(rows), fog.hex())
def __quote__(text, lex, path, seed):
    rows = []
    for line in text.splitlines():
        rows.append((line.count("'"), line.count('"'), line.count("'''"), line.count('"""'), line.count('`'), len(line)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('quotex', len(rows), fog.hex())
def __stripe__(text, lex, path, seed):
    rows = []
    roll = hashlib.sha256(seed + b'stripe').digest()
    for slot, line in enumerate(text.splitlines()):
        raw = line.encode('utf-8', 'replace')
        roll = hashlib.sha256(roll + raw[:256] + len(raw).to_bytes(4, 'little')).digest()
        rows.append((slot & 1023, hashlib.blake2s(raw, digest_size=8).hexdigest(), roll[:6], len(raw)))
    fog = __mix__(seed, (__hist__(row[1] for row in rows), tuple(rows[:512]), tuple(rows[-128:]), roll))
    return ('linehash', len(rows), fog.hex())
def __space__(text, lex, path, seed):
    rows = []
    for line in text.splitlines():
        runs = []
        cur = 0
        for ch in line:
            if ch == ' ':
                cur += 1
            elif cur:
                runs.append(cur); cur = 0
        if cur:
            runs.append(cur)
        rows.append((len(runs), max(runs) if runs else 0, sum(runs), len(line)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('space', len(rows), fog.hex())
def __meter__(text, lex, path, seed):
    rows = []
    jump = []
    last = (0, 0)
    for typ, val, start, end, line in lex:
        jump.append((start[0] - last[0], start[1] - last[1]))
        rows.append((typ, end[0] - start[0], end[1] - start[1], len(val), start[0] & 255))
        last = end
    fog = __mix__(seed, (__hist__(rows), __hist__(jump), tuple(rows[:2048]), len(rows)))
    return ('meter', len(rows), fog.hex())
def __route__(text, lex, path, seed):
    rows = []
    vals = [one[1] for one in lex if one[1].strip()]
    for slot in range(max(0, len(vals) - 2)):
        tri = vals[slot:slot + 3]
        raw = ''.join(tri).encode('utf-8', 'replace')
        rows.append((slot & 1023, len(raw), zlib.crc32(raw) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('route', len(rows), fog.hex())
def __matter__(text, lex, path, seed):
    rows = []
    take = {getattr(__import__('token'), 'STRING'), getattr(__import__('token'), 'NUMBER')}
    for typ, val, start, end, line in lex:
        if typ in take:
            raw = val.encode('utf-8', 'replace')
            rows.append((typ, len(raw), raw[:8], raw[-8:], zlib.crc32(raw) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('matter', len(rows), fog.hex())
def __bare__(text, lex, path, seed):
    rows = []
    bag = []
    for line in text.splitlines():
        cut = line.strip()
        if cut and not cut.startswith('#'):
            bag.append(cut)
    for slot, cut in enumerate(bag[:4096]):
        rows.append((slot & 255, len(cut), cut[:16], cut[-16:], zlib.adler32(cut.encode('utf-8', 'replace')) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(bag)))
    return ('bare', len(bag), fog.hex())
def __rind__(text, lex, path, seed):
    rows = []
    vals = text.splitlines()
    for slot, line in enumerate(vals):
        raw = line[::-1].encode('utf-8', 'replace')
        rows.append((slot & 255, len(raw), zlib.crc32(raw[:128]) & 0xffffffff, zlib.adler32(raw[-128:]) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('rind', len(rows), fog.hex())
def __stamp__(text, lex, path, seed):
    rows = []
    last = 0
    for slot, ch in enumerate(text[:131072]):
        cur = (last + ord(ch) + slot) & 0xffffffff
        if slot % 64 == 0:
            rows.append((slot // 64, cur, ord(ch), last))
        last = ((cur << 3) | (cur >> 29)) & 0xffffffff
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), last, len(text)))
    return ('stamp', len(rows), fog.hex())
def __wave__(text, lex, path, seed):
    rows = []
    vals = [len(line) for line in text.splitlines()]
    for slot in range(1, len(vals)):
        rows.append((slot & 255, vals[slot - 1], vals[slot], vals[slot] - vals[slot - 1]))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(vals)))
    return ('wave', len(rows), fog.hex())
def __cord__(text, lex, path, seed):
    rows = []
    name = getattr(__import__('token'), 'NAME')
    vals = [one for one in lex if one[1].strip()]
    at = 0
    while at < len(vals):
        typ, val, start, end, line = vals[at]
        if typ != name:
            at += 1; continue
        deep = call = dot = 0; raw = [val]; cur = at + 1
        while cur + 1 < len(vals) and vals[cur][1] in ('.', '('):
            if vals[cur][1] == '.' and vals[cur + 1][0] == name:
                dot += 1; raw.append(vals[cur + 1][1]); cur += 2; continue
            if vals[cur][1] == '(':
                call += 1; deep += 1; cur += 1; break
        if dot or call:
            buf = '.'.join(raw).encode('utf-8', 'replace')
            rows.append((len(raw), dot, call, deep, start[0] & 255, zlib.crc32(buf) & 0xffffffff))
        at = max(cur, at + 1)
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(rows)))
    return ('cord', len(rows), fog.hex())
def __shade__(text, lex, path, seed):
    rows = []
    com = getattr(__import__('tokenize'), 'COMMENT')
    for typ, val, start, end, line in lex:
        if typ != com:
            continue
        low = val.lower()
        raw = val.encode('utf-8', 'replace')
        rows.append((len(val), int('type:' in low), int('noqa' in low), int('todo' in low or 'fixme' in low), start[0] & 255, zlib.adler32(raw) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('shade', len(rows), fog.hex())
def __frost__(text, lex, path, seed):
    rows = []
    name = getattr(__import__('token'), 'NAME')
    bag = {}
    for typ, val, start, end, line in lex:
        if typ == name:
            dat = bag.setdefault(val, [0, start[0], start[0], start[1], 0])
            dat[0] += 1; dat[2] = start[0]; dat[3] = min(dat[3], start[1]); dat[4] = max(dat[4], end[1])
    for val, dat in sorted(bag.items(), key=lambda row: (-row[1][0], row[0]))[:2048]:
        raw = val.encode('utf-8', 'replace')
        rows.append((dat[0], dat[2] - dat[1], dat[3], dat[4], len(val), zlib.crc32(raw) & 0xffffffff))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(bag)))
    return ('frost', len(rows), fog.hex())
def __lens__(text, lex, path, seed):
    rows = []
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}
    for typ, val, start, end, line in lex:
        if val in '([{':
            stack.append((val, start))
        elif val in pair:
            ok = int(bool(stack) and stack[-1][0] == pair[val])
            old = stack.pop()[1] if ok else start
            rows.append((ok, val, start[0] - old[0], start[1] - old[1], len(stack)))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:1024]), len(stack), len(rows)))
    return ('lens', len(rows), fog.hex())
def __ink__(text, lex, path, seed):
    rows = []
    uni = __import__('unicodedata')
    name = getattr(__import__('token'), 'NAME')
    for typ, val, start, end, line in lex:
        raw = val.encode('utf-8', 'replace')
        wide = sum(1 for ch in val if ord(ch) > 127)
        if not wide:
            continue
        cats = {}
        for ch in val:
            cat = uni.category(ch)
            cats[cat] = cats.get(cat, 0) + 1
        norm = uni.normalize('NFKC', val)
        rows.append((typ, int(typ == name), len(val), wide, int(norm != val), tuple(sorted(cats.items())[:8]), zlib.crc32(raw) & 0xffffffff, start[0] & 255))
    fog = __mix__(seed, (__hist__(row[0] for row in rows), __hist__(row[5] for row in rows), tuple(rows[:512]), len(rows)))
    return ('ink', len(rows), fog.hex())
def __accent__(text, lex, path, seed):
    rows = []
    name = getattr(__import__('token'), 'NAME')
    vals = [one for one in lex if one[1].strip()]
    for slot, one in enumerate(vals):
        typ, val, start, end, line = one
        if typ == name and val == 'lambda':
            depth = 0
            args = comma = call = 0
            cur = slot + 1
            while cur < len(vals):
                curval = vals[cur][1]
                if curval == ':' and depth == 0:
                    break
                if curval in '([{':
                    depth += 1
                elif curval in ')]}' and depth:
                    depth -= 1
                elif curval == ',':
                    comma += 1
                elif vals[cur][0] == name:
                    args += 1
                cur += 1
            if cur + 1 < len(vals) and vals[cur + 1][1] == '(':
                call = 1
            rows.append((args, comma, call, cur - slot, start[0] & 255, start[1]))
    fog = __mix__(seed, (__hist__(rows), tuple(rows[:512]), len(rows)))
    return ('accent', len(rows), fog.hex())
def __tone__(text, lex, path, seed):
    rows = []
    uni = __import__('unicodedata')
    name = getattr(__import__('token'), 'NAME')
    for typ, val, start, end, line in lex:
        if typ != name:
            continue
        norm = uni.normalize('NFKC', val)
        wide = tuple((ord(ch), uni.category(ch), int(uni.combining(ch) > 0)) for ch in val if ord(ch) > 127)
        if wide or norm != val:
            rows.append((len(val), len(norm), zlib.crc32(val.encode('utf-8', 'replace')) & 0xffffffff, zlib.crc32(norm.encode('utf-8', 'replace')) & 0xffffffff, tuple(wide[:16]), start[0] & 1023, start[1] & 255))
    fog = __mix__(seed, (__hist__(row[0] for row in rows), __hist__(row[1] for row in rows), tuple(rows[:384]), len(rows)))
    return ('tone', len(rows), fog.hex())
def __arc__(text, lex, path, seed):
    rows = []
    name = getattr(__import__('token'), 'NAME')
    vals = [one for one in lex if one[1].strip()]
    for slot, one in enumerate(vals):
        typ, val, start, end, line = one
        if typ != name or val != 'lambda':
            continue
        depth = span = call = bind = 0
        cur = slot + 1
        while cur < len(vals):
            curval = vals[cur][1]
            if curval in '([{':
                depth += 1
            elif curval in ')]}' and depth:
                depth -= 1
            elif curval == ':' and depth == 0:
                span = cur - slot
                break
            elif vals[cur][0] == name:
                bind += 1
            cur += 1
        pos = cur + 1
        while pos < len(vals) and vals[pos][1] in (')', ']', '}'):
            pos += 1
        if pos < len(vals) and vals[pos][1] == '(':
            call = 1
        rows.append((bind, depth, span, call, start[0] & 1023, start[1] & 255))
    fog = __mix__(seed, (__hist__(row[0] for row in rows), __hist__(row[3] for row in rows), tuple(rows[:384]), len(rows)))
    return ('arc', len(rows), fog.hex())
def __scroll__(raw, path, seed):
    if isinstance(raw, (bytes, bytearray)):
        raw = bytes(raw); step = max(1, len(raw) // 4096)
        rows = []
        rows.append(('size', len(raw), zlib.crc32(raw) & 0xffffffff, zlib.adler32(raw) & 0xffffffff, hashlib.sha256(raw).hexdigest(), hashlib.sha1(raw).hexdigest()))
        rows.append(('edge', raw[:128], raw[-128:], tuple(raw[::step][:4096])))
        rows.append(('hist', __hist__(raw), __hist__(raw[::step])))
        rows.append(('win', tuple((slot, zlib.crc32(raw[slot:slot + 512]) & 0xffffffff, hashlib.blake2b(raw[slot:slot + 512], digest_size=16).hexdigest()) for slot in range(0, len(raw), max(512, len(raw) // 64)))))
        fog = __mix__(seed, (tuple(rows), os.path.basename(path)))
        return (len(rows), fog.hex())
    text = raw.decode('utf-8', 'replace') if isinstance(raw, (bytes, bytearray)) else str(raw)
    lex = __lexi__(text)
    seq = ((b'linen', __linen__), (b'gap', __gap__), (b'dent', __dent__), (b'track', __track__), (b'letter', __letter__), (b'word', __word__), (b'key', __key__), (b'digit', __digit__), (b'string', __string__), (b'head', __head__), (b'slash', __slash__), (b'mold', __mold__), (b'brace', __brace__), (b'paren', __paren__), (b'sign', __sign__), (b'point', __point__), (b'summon', __summon__), (b'bring', __bring__), (b'path', __path__), (b'shebang', __shebang__), (b'coding', __coding__), (b'blank', __blank__), (b'chunk', __chunk__), (b'cover', __cover__), (b'style', __style__), (b'noise', __noise__), (b'ratio', __ratio__), (b'duet', __duet__), (b'current', __current__), (b'brine', __brine__), (b'scan', __scan__), (b'moss', __moss__), (b'reed', __reed__), (b'weave', __weave__), (b'flax', __flax__), (b'fiber', __fiber__), (b'badge', __badge__), (b'crease', __crease__), (b'quote', __quote__), (b'stripe', __stripe__), (b'space', __space__), (b'meter', __meter__), (b'route', __route__), (b'matter', __matter__), (b'bare', __bare__), (b'rind', __rind__), (b'stamp', __stamp__), (b'wave', __wave__), (b'cord', __cord__), (b'shade', __shade__), (b'frost', __frost__), (b'lens', __lens__), (b'ink', __ink__), (b'accent', __accent__), (b'tone', __tone__), (b'arc', __arc__))
    rows = [fn(text, lex, path, seed + tag) for tag, fn in seq]
    fog = __mix__(seed, (tuple(rows), len(text), len(lex), os.path.basename(path)))
    return (len(rows), fog.hex())
def __ore__(tree, code, seed):
    full = tuple(ast.walk(tree)); codes = __drip__(code); wide = (len(full), len(codes))
    nodes = full; shape = __hist__(type(node).__name__ for node in full)
    bag = {'nodes': nodes, 'codes': codes, 'wide': wide, 'shape': shape}
    seq = ((b'oak', __oak__), (b'spruce', __spruce__), (b'birch', __birch__), (b'jungle', __jungle__), (b'acacia', __acacia__), (b'mangrove', __mangrove__), (b'cherry', __cherry__), (b'bamboo', __bamboo__), (b'cactus', __cactus__), (b'kelp', __kelp__), (b'shell', __shell__), (b'seagrass', __seagrass__), (b'mycelium', __mycelium__), (b'shroom', __shroom__), (b'azalea', __azalea__), (b'dripstone', __dripstone__), (b'sculk', __sculk__), (b'tufa', __tufa__), (b'calcite', __calcite__), (b'amethyst', __amethyst__), (b'granite', __granite__), (b'diorite', __diorite__), (b'andesite', __andesite__), (b'crag', __crag__), (b'blackstone', __blackstone__), (b'netherrack', __netherrack__), (b'glowstone', __glowstone__), (b'endstone', __endstone__), (b'purpur', __purpur__), (b'prismarine', __prismarine__), (b'terracotta', __terracotta__), (b'concrete', __concrete__), (b'lantern', __lantern__), (b'lamp', __lamp__), (b'campfire', __campfire__), (b'hammer', __hammer__), (b'furnace', __furnace__), (b'hopper', __hopper__), (b'dropper', __dropper__), (b'observer', __observer__), (b'piston', __piston__), (b'rail', __rail__), (b'minecart', __minecart__), (b'bee2', __bee2__), (b'camel2', __camel2__), (b'warden2', __warden2__), (b'allay2', __allay2__), (b'breeze2', __breeze2__), (b'sniffer2', __sniffer2__), (b'strider2', __strider2__), (b'hoglin2', __hoglin2__), (b'panda2', __panda2__), (b'llama2', __llama2__), (b'ocelot2', __ocelot2__), (b'ravager2', __ravager2__), (b'turtle2', __turtle2__), (b'phantom2', __phantom2__), (b'dolphin2', __dolphin2__), (b'fox2', __fox2__), (b'goat2', __goat2__), (b'parrot2', __parrot2__), (b'rabbit2', __rabbit2__), (b'salmon2', __salmon2__), (b'spider2', __spider2__), (b'squid2', __squid2__), (b'vex2', __vex2__), (b'zombie2', __zombie2__), (b'creeper2', __creeper2__), (b'piglin2', __piglin2__), (b'ghast2', __ghast2__), (b'shulker2', __shulker2__), (b'ender2', __ender2__), (b'slime2', __slime2__), (b'magma2', __magma2__), (b'blaze2', __blaze2__), (b'stray2', __stray2__), (b'husk2', __husk2__), (b'drowned2', __drowned2__), (b'watch', __watch__), (b'sprite', __sprite__), (b'axolotl', __axolotl__), (b'armadillo', __armadillo__), (b'badger', __badger__), (b'bogged', __bogged__), (b'breezez', __breezez__), (b'cat', __cat__), (b'donkey', __donkey__), (b'frog', __frog__), (b'horse', __horse__), (b'metal', __metal__), (b'mooshroom', __mooshroom__), (b'mule', __mule__), (b'polar', __polar__), (b'snow', __snow__), (b'wolf', __wolf__), (b'zoglin', __zoglin__), (b'brute', __brute__), (b'silver', __silver__), (b'copper', __copper__), (b'wax', __wax__), (b'glint', __glint__), (b'echoes', __echoes__), (b'golem', __golem__), (b'ravine', __ravine__), (b'geode', __geode__), (b'spire', __spire__), (b'agate', __agate__), (b'jade', __jade__), (b'quartz', __quartz__), (b'mica', __mica__))
    rows = [fn(bag, seed + tag) for tag, fn in seq]
    fog = __mix__(seed, (tuple(rows), wide, len(nodes), shape, __hist__(rows)))
    return (len(rows), wide, len(nodes), fog.hex())
def __chart__(tree, code, stem, path, seed):
    old = ast.walk
    cache = {}
    def roam(row):
        key = id(row)
        if key not in cache: cache[key] = tuple(old(row))
        return iter(cache[key])
    ast.walk = roam
    try:
        flow = ((tree, ((b'shape', __shapeid__), (b'literal', __literal__), (b'label', __label__), (b'flow', __flow__), (b'call', __call__), (b'scope', __scope__), (b'module', __module__), (b'set', __set__), (b'sub', __sub__), (b'bin', __bin__), (b'cmp', __cmp__), (b'form', __form__), (b'trap', __trap__), (b'pat', __pat__), (b'ret', __ret__), (b'loop', __loop__), (b'comp', __comp__), (b'ann', __ann__), (b'ref', __ref__), (b'depth', __depth__), (b'tile', __tile__), (b'context', __context__), (b'discard', __discard__), (b'wth', __wth__), (b'body', __body__), (b'glyph', __glyph__), (b'alph', __alph__), (b'span', __span__), (b'gram', __gram__))), (tree, ((b'tok', __tok__), (b'atom', __atom__), (b'num', __num__), (b'txt', __txt__), (b'bop', __bop__), (b'cmpr', __cmpr__), (b'dial', __dial__), (b'asgn', __asgn__), (b'river', __river__), (b'catch', __catch__), (b'mask', __mask__), (b'coil', __coil__), (b'fmt', __fmt__), (b'match', __match__), (b'imp', __imp__), (b'func', __func__), (b'arg', __arg__), (b'clan', __clan__), (b'deco', __deco__), (b'anno', __anno__))), (tree, ((b'out', __out__), (b'slice', __slice__), (b'seq', __seq__), (b'paper', __paper__), (b'lineage', __lineage__), (b'tree', __tree__), (b'leaf', __leaf__), (b'edge', __edge__), (b'order', __order__), (b'nom', __nom__), (b'attr', __attr__), (b'kwd', __kwd__), (b'place', __place__), (b'sym', __sym__), (b'api', __api__), (b'lit', __lit__), (b'blend', __blend__), (b'block', __block__), (b'expr', __expr__), (b'stmt', __stmt__), (b'hash', __hash__), (b'trace', __trace__), (b'flat', __flat__), (b'rill', __rill__), (b'tor', __tor__), (b'dell', __dell__), (b'fell', __fell__), (b'crux', __crux__), (b'vane', __vane__), (b'pinion', __pinion__), (b'ochre', __ochre__), (b'prong', __prong__), (b'gauze', __gauze__), (b'pylon', __pylon__), (b'keel', __keel__), (b'mast', __mast__), (b'wheel', __wheel__), (b'level', __level__), (b'wrap', __wrap__), (b'source', __source__), (b'middle', __middle__), (b'tail', __tail__), (b'field', __field__), (b'wide', __wide__), (b'den', __den__))), (code, ((b'op', __op__), (b'constant', __constant__), (b'line', __line__), (b'free', __free__), (b'window', __window__), (b'vmap', __vmap__), (b'pool', __pool__), (b'ord', __ord__), (b'sig', __sig__), (b'fvn', __fvn__), (b'rivet', __rivet__), (b'hinge', __hinge__), (b'nickel', __nickel__), (b'tin', __tin__), (b'rope', __rope__), (b'sail', __sail__), (b'anchor', __anchor__), (b'ctor', __ctor__), (b'made', __made__), (b'byte', __byte__), (b'blob', __blob__), (b'opcode', __opcode__), (b'quad', __quad__), (b'const', __const__), (b'nam', __nam__), (b'var', __var__), (b'cell', __cell__), (b'tab', __tab__), (b'except', __except__), (b'coord', __coord__), (b'fname', __fname__), (b'argv', __argv__), (b'flag', __flag__), (b'mar', __mar__), (b'slot', __slot__), (b'ordr', __ordr__), (b'pack', __pack__), (b'dig', __dig__), (b'pond', __pond__), (b'stk', __stk__))), (code, ((b'qual', __qual__), (b'size', __size__), (b'rng', __rng__), (b'duo', __duo__), (b'tri', __tri__), (b'oct', __oct__), (b'cnt', __cnt__), (b'dep', __dep__), (b'kind', __kind__), (b'pak', __pak__), (b'trail', __trail__), (b'split', __split__), (b'xor', __xor__), (b'sum', __sum__), (b'layout', __layout__), (b'mesh', __mesh__), (b'gate', __gate__), (b'fold', __fold__))), (tree, ((b'crestcall', __crestcall__), (b'crestattr', __crestattr__), (b'crestimp', __crestimp__), (b'creststr', __creststr__), (b'crestbytes', __crestbytes__), (b'crestnum', __crestnum__), (b'crestseq', __crestseq__), (b'crestbranch', __crestbranch__), (b'cresttry', __cresttry__), (b'crestfunc', __crestfunc__), (b'crestclass', __crestclass__), (b'crestcomp', __crestcomp__), (b'crestpat', __crestpat__), (b'crestfmt', __crestfmt__), (b'crestscope', __crestscope__), (b'crestname', __crestname__), (b'crestop', __crestop__), (b'crestline', __crestline__), (b'crestapi', __crestapi__))), (tree, ((b'crestio', __crestio__), (b'crestnet', __crestnet__), (b'cresttime', __cresttime__), (b'cresterr', __cresterr__), (b'crestasync', __crestasync__), (b'crestui', __crestui__), (b'crestpack', __crestpack__))), (code, ((b'crestcode', __crestcode__), (b'crestconst', __crestconst__), (b'crestpool', __crestpool__), (b'cresttable', __cresttable__), (b'crestmar', __crestmar__))))
        rows = []
        for arg, seq in flow:
            rows.extend(fn(arg, seed + tag) for tag, fn in seq)
        dual = (((b'vex', __vex__), (b'zod', __zod__), (b'kiv', __kiv__), (b'mav', __mav__), (b'night', __night__), (b'pyr', __pyr__), (b'qel', __qel__), (b'rice', __rice__), (b'sorn', __sorn__), (b'tav', __tav__), (b'umber', __umber__), (b'vor', __vor__), (b'wool', __wool__), (b'yul', __yul__), (b'ziv', __ziv__), (b'kro', __kro__), (b'lum', __lum__), (b'orz', __orz__), (b'dusk', __dusk__), (b'peace', __peace__), (b'quill', __quill__), (b'rust', __rust__), (b'siv', __siv__), (b'tick', __tick__), (b'uvo', __uvo__), (b'vyn', __vyn__)), ((b'wok', __wok__), (b'xul', __xul__), (b'yarn', __yarn__), (b'zok', __zok__), (b'pearl', __pearl__), (b'lime', __lime__), (b'cedar', __cedar__), (b'nuv', __nuv__), (b'oxa', __oxa__), (b'piv', __piv__), (b'qor', __qor__), (b'zinc', __zinc__), (b'topaz', __topaz__), (b'tov', __tov__), (b'uzn', __uzn__), (b'vok', __vok__), (b'waz', __waz__), (b'xir', __xir__), (b'yok', __yok__), (b'ruby', __ruby__)), ((b'kao', __kao__), (b'leo', __leo__), (b'mio', __mio__), (b'neo', __neo__), (b'pio', __pio__), (b'qio', __qio__), (b'rio', __rio__), (b'sio', __sio__), (b'tio', __tio__), (b'uio', __uio__), (b'vio', __vio__), (b'wio', __wio__)), ((b'xio', __xio__), (b'yio', __yio__), (b'zio', __zio__), (b'kra', __kra__), (b'lra', __lra__), (b'mra', __mra__), (b'nra', __nra__), (b'pra', __pra__), (b'qra', __qra__), (b'rra', __rra__)), ((b'grave', __grave__), (b'shiver', __shiver__), (b'sable', __sable__), (b'mosaic', __mosaic__), (b'lamb', __lamb__)), ((b'bee', __bee__), (b'camel', __camel__), (b'warden', __warden__), (b'allay', __allay__), (b'breeze', __breeze__), (b'sniffer', __sniffer__), (b'strider', __strider__), (b'hoglin', __hoglin__), (b'panda', __panda__), (b'llama', __llama__), (b'ocelot', __ocelot__), (b'ravager', __ravager__), (b'turtle', __turtle__), (b'phantom', __phantom__), (b'dolphin', __dolphin__), (b'fox', __fox__), (b'goat', __goat__), (b'parrot', __parrot__), (b'rabbit', __rabbit__), (b'salmon', __salmon__), (b'spider', __spider__), (b'wraith', __wraith__), (b'zombie', __zombie__), (b'creeper', __creeper__)), ((b'piglin', __piglin__), (b'ghast', __ghast__), (b'shulker', __shulker__), (b'enderman', __enderman__), (b'villager', __villager__), (b'pillager', __pillager__), (b'guardian', __guardian__)), ((b'squid', __squid__),))
        for seq in dual:
            rows.extend(fn(tree, code, seed + tag) for tag, fn in seq)
        rows.append(__ore__(tree, code, seed + b'ore')); rows.append(__scroll__(stem, path, seed + b'scroll')); rows.extend((__salt__(tree, code, seed + b'salt').hex(), __ring__(tree, code, seed + b'ring')))
        mark = (os.path.basename(path), len(stem), hashlib.sha256(stem).hexdigest(), zlib.crc32(stem) & 0xffffffff, zlib.adler32(stem) & 0xffffffff)
        core = __vine__((tuple(rows), mark)); fog = hashlib.sha512(core).digest(); salt = __mist__(seed + b'atlas' + fog, 64)
        return hashlib.blake2b(fog + salt + core[:4096], digest_size=64).digest()
    finally:
        ast.walk = old
def __pare__(tree):
    lim=4096;num=10**18
    def __ok__(v): return (v is None or v is Ellipsis or isinstance(v,(bool,int,float,complex,str,bytes,tuple,frozenset))) and not (isinstance(v,int) and abs(v)>num) and not (isinstance(v,(str,bytes)) and len(v)>lim) and not (isinstance(v,(tuple,frozenset)) and (len(v)>256 or any(not __ok__(x) for x in v)))
    def __val__(n):
        if isinstance(n,ast.Constant): return True,n.value
        if isinstance(n,(ast.Tuple,ast.List,ast.Set)):
            bag=[]
            for x in n.elts:
                ok,v=__val__(x)
                if not ok: return False,None
                bag.append(v)
            if len(bag)>256: return False,None
            if isinstance(n,ast.Tuple): return True,tuple(bag)
            if isinstance(n,ast.List): return True,bag
            try: return True,set(bag)
            except: return False,None
        if isinstance(n,ast.Dict):
            bag={}
            for k,x in zip(n.keys,n.values):
                if k is None: return False,None
                ko,kv=__val__(k);xo,xv=__val__(x)
                if not ko or not xo: return False,None
                try: bag[kv]=xv
                except: return False,None
            return len(bag)<=256,bag
        return False,None
    def __mk__(v,n):
        if not __ok__(v): return n
        return ast.copy_location(ast.Constant(v),n)
    def __ev__(fn,*v):
        try:
            out=fn(*v)
            if __ok__(out) or isinstance(out,(list,set,dict)): return True,out
        except: pass
        return False,None
    def __say__(n):
        if isinstance(n,ast.Constant) and isinstance(n.value,str): return True,n.value
        if not isinstance(n,ast.JoinedStr): return False,None
        bag=[]
        for x in n.values:
            if isinstance(x,ast.Constant) and isinstance(x.value,str): bag.append(x.value)
            elif isinstance(x,ast.FormattedValue):
                ok,v=__val__(x.value);so,s=__say__(x.format_spec) if x.format_spec else (True,'')
                if not ok or not so: return False,None
                try:
                    v=str(v) if x.conversion==115 else repr(v) if x.conversion==114 else ascii(v) if x.conversion==97 else v
                    if x.conversion not in (-1,97,114,115): return False,None
                    bag.append(format(v,s))
                except: return False,None
            else: return False,None
        out=''.join(bag);return (len(out)<=lim),out
    def __sim__(n):
        if isinstance(n,ast.Name) and n.id=='__debug__': return True,False
        ok,v=__val__(n)
        if ok and __ok__(v): return True,v
        return __say__(n) if isinstance(n,ast.JoinedStr) else (False,None)
    def __raw__(n):
        if isinstance(n,ast.Name) and n.id=='__debug__': return True,False
        ok,v=__val__(n)
        if ok: return True,v
        return __say__(n) if isinstance(n,ast.JoinedStr) else (False,None)
    def __pure__(n):
        return isinstance(n,ast.Name) and n.id=='__debug__' or isinstance(n,ast.Constant) or isinstance(n,(ast.Tuple,ast.List,ast.Set)) and all(__pure__(x) for x in n.elts) or isinstance(n,ast.Dict) and all(k is not None and __pure__(k) and __pure__(v) for k,v in zip(n.keys,n.values)) or isinstance(n,ast.UnaryOp) and __pure__(n.operand) or isinstance(n,ast.BinOp) and __pure__(n.left) and __pure__(n.right) or isinstance(n,ast.BoolOp) and all(__pure__(x) for x in n.values) or isinstance(n,ast.Compare) and __pure__(n.left) and all(__pure__(x) for x in n.comparators) or isinstance(n,ast.IfExp) and __pure__(n.test) and __pure__(n.body) and __pure__(n.orelse) or isinstance(n,ast.JoinedStr) and all(__pure__(x) for x in n.values) or isinstance(n,ast.FormattedValue) and __pure__(n.value) and (n.format_spec is None or __pure__(n.format_spec)) or isinstance(n,ast.Subscript) and __pure__(n.value) and __pure__(n.slice) or isinstance(n,ast.Slice) and (n.lower is None or __pure__(n.lower)) and (n.upper is None or __pure__(n.upper)) and (n.step is None or __pure__(n.step))
    def __drop__(x,first):
        return isinstance(x,(ast.Pass,ast.Assert)) or isinstance(x,ast.Expr) and (isinstance(x.value,ast.Constant) or __pure__(x.value))
    def __same__(a,b):
        try: return ast.dump(a,include_attributes=False)==ast.dump(b,include_attributes=False)
        except: return False
    def __lift__(v,n):
        made=__node__(v,n)
        if made is not None: return made
        return __mk__(v,n) if __ok__(v) else n
    def __keyn__(n):
        if isinstance(n,ast.Name): return {n.id}
        if isinstance(n,(ast.Tuple,ast.List)):
            bag=set()
            for x in n.elts: bag.update(__keyn__(x))
            return bag
        if isinstance(n,ast.Starred): return __keyn__(n.value)
        if isinstance(n,ast.Attribute): return set()
        if isinstance(n,ast.Subscript): return set()
        return set()
    def __readn__(n):
        bag=set()
        for x in ast.walk(n):
            if isinstance(x,ast.Name) and isinstance(x.ctx,ast.Load): bag.add(x.id)
            elif isinstance(x,ast.AugAssign): bag.update(__keyn__(x.target))
        return bag
    def __litok__(v):
        return v is None or v is Ellipsis or isinstance(v,(bool,int,float,complex,str,bytes,tuple)) and __ok__(v)
    def __clone__(v,n):
        return ast.copy_location(ast.Constant(v),n)
    def __swap__(n,tab):
        if isinstance(n,ast.Name) and isinstance(n.ctx,ast.Load) and n.id in tab: return __clone__(tab[n.id],n)
        for f,v in ast.iter_fields(n):
            if isinstance(v,list):
                bag=[]
                for x in v:
                    bag.append(__swap__(x,tab) if isinstance(x,ast.AST) else x)
                setattr(n,f,bag)
            elif isinstance(v,ast.AST): setattr(n,f,__swap__(v,tab))
        return n
    def __cutn__(tab,names):
        for x in names:
            if x in tab: del tab[x]
    def __storen__(n):
        bag=set()
        def go(x,root=False):
            if not root and isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef,ast.Lambda)): return
            if isinstance(x,ast.Name) and isinstance(x.ctx,(ast.Store,ast.Del)): bag.add(x.id)
            elif isinstance(x,ast.arg): bag.add(x.arg)
            elif isinstance(x,ast.ExceptHandler) and x.name: bag.add(x.name)
            for y in ast.iter_child_nodes(x): go(y)
        go(n,True);return bag
    def __bindn__(tab,x):
        if isinstance(x,ast.Assign):
            for t in x.targets: __cutn__(tab,__keyn__(t))
            if len(x.targets)==1 and isinstance(x.targets[0],ast.Name):
                ok,v=__raw__(x.value)
                if ok and __litok__(v): tab[x.targets[0].id]=v
        elif isinstance(x,ast.AnnAssign):
            __cutn__(tab,__keyn__(x.target))
            if isinstance(x.target,ast.Name) and x.value is not None:
                ok,v=__raw__(x.value)
                if ok and __litok__(v): tab[x.target.id]=v
        elif isinstance(x,ast.AugAssign): __cutn__(tab,__keyn__(x.target))
        elif isinstance(x,(ast.For,ast.AsyncFor,ast.While,ast.If,ast.With,ast.AsyncWith,ast.Try,ast.Match)): __cutn__(tab,__storen__(x))
        elif isinstance(x,ast.With):
            for y in x.items:
                if y.optional_vars is not None: __cutn__(tab,__keyn__(y.optional_vars))
        elif isinstance(x,ast.Import):
            for y in x.names: __cutn__(tab,{y.asname or y.name.split('.')[0]})
        elif isinstance(x,ast.ImportFrom):
            for y in x.names: __cutn__(tab,{y.asname or y.name})
        elif isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): __cutn__(tab,{x.name})
        elif isinstance(x,ast.Delete):
            for y in x.targets: __cutn__(tab,__keyn__(y))
    def __hard__(x):
        return isinstance(x,(ast.Global,ast.Nonlocal,ast.Try,ast.Raise,ast.Match,ast.AsyncFor,ast.AsyncWith))
    def __lane__(rows):
        if len(rows)>12: return rows
        tab={};bag=[]
        for x in rows:
            if __hard__(x):
                tab.clear();bag.append(x);continue
            if not isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
                x=__swap__(x,tab)
            bag.append(x);__bindn__(tab,x)
            if isinstance(x,(ast.Return,ast.Raise,ast.Break,ast.Continue)): tab.clear()
        return bag
    def __uses__(rows):
        bag={}
        for x in rows:
            for y in __readn__(x): bag[y]=bag.get(y,0)+1
        return bag
    def __dead__(rows):
        if len(rows)>12: return rows
        cnt=__uses__(rows)
        out=[]
        for x in rows:
            if isinstance(x,ast.Assign) and len(x.targets)==1 and isinstance(x.targets[0],ast.Name):
                ok,v=__raw__(x.value)
                if ok and __litok__(v) and cnt.get(x.targets[0].id,0)==0: continue
            if isinstance(x,ast.AnnAssign) and isinstance(x.target,ast.Name) and x.value is not None:
                ok,v=__raw__(x.value)
                if ok and __litok__(v) and cnt.get(x.target.id,0)==0: continue
            out.append(x)
        return out
    def __isn__(n,v):
        ok,x=__raw__(n)
        return ok and x==v
    def __z__(n): return __isn__(n,0)
    def __o__(n): return __isn__(n,1)
    def __mone__(n): return __isn__(n,-1)
    def __empn__(n):
        got=__tally__(n)
        return got==0 if got is not None else False
    def __copyloc__(x,n):
        return ast.copy_location(x,n)
    def __alg__(n):
        if isinstance(n.op,ast.Mod) and isinstance(n.left,ast.Constant) and isinstance(n.left.value,(str,bytes)):
            ok,v=__raw__(n.right)
            if ok:
                done,out=__ev__(lambda a,b:a%b,n.left.value,v)
                if done: return __done__(out,n)
        if isinstance(n.op,ast.Add):
            if __z__(n.right) and __pure__(n.left): return n.left
            if __z__(n.left) and __pure__(n.right): return n.right
            if __empn__(n.right) and __pure__(n.left): return n.left
            if __empn__(n.left) and __pure__(n.right): return n.right
        if isinstance(n.op,ast.Sub):
            if __z__(n.right) and __pure__(n.left): return n.left
            if __z__(n.left) and __pure__(n.right): return __copyloc__(ast.UnaryOp(op=ast.USub(),operand=n.right),n)
        if isinstance(n.op,ast.Mult):
            if __o__(n.right) and __pure__(n.left): return n.left
            if __o__(n.left) and __pure__(n.right): return n.right
            if __mone__(n.right) and __pure__(n.left): return ast.copy_location(ast.UnaryOp(op=ast.USub(),operand=n.left),n)
            if __mone__(n.left) and __pure__(n.right): return ast.copy_location(ast.UnaryOp(op=ast.USub(),operand=n.right),n)
            if (__z__(n.right) and __pure__(n.left)) or (__z__(n.left) and __pure__(n.right)): return __mk__(0,n)
        if isinstance(n.op,ast.Div) and __o__(n.right) and __pure__(n.left): return n.left
        if isinstance(n.op,ast.FloorDiv) and __o__(n.right) and __pure__(n.left): return n.left
        if isinstance(n.op,ast.Pow):
            if __o__(n.right) and __pure__(n.left): return n.left
            if __z__(n.right) and __pure__(n.left): return __mk__(1,n)
            if __o__(n.left) and __pure__(n.right): return __mk__(1,n)
        if isinstance(n.op,(ast.BitOr,ast.BitXor)) and __z__(n.right) and __pure__(n.left): return n.left
        if isinstance(n.op,(ast.BitOr,ast.BitXor)) and __z__(n.left) and __pure__(n.right): return n.right
        if isinstance(n.op,ast.BitAnd) and __z__(n.right) and __pure__(n.left): return __mk__(0,n)
        if isinstance(n.op,ast.BitAnd) and __z__(n.left) and __pure__(n.right): return __mk__(0,n)
        if isinstance(n.op,(ast.LShift,ast.RShift)) and __z__(n.right) and __pure__(n.left): return n.left
        return n
    def __boolop__(n):
        if isinstance(n.op,ast.And):
            vals=[]
            for x in n.values:
                ok,v=__truthy__(x)
                if ok and v: continue
                if ok and not v and __pure__(x): return x
                vals.append(x)
            return vals[0] if len(vals)==1 else ast.copy_location(ast.BoolOp(op=n.op,values=vals),n) if vals else __mk__(True,n)
        if isinstance(n.op,ast.Or):
            vals=[]
            for x in n.values:
                ok,v=__truthy__(x)
                if ok and not v: continue
                if ok and v and __pure__(x): return x
                vals.append(x)
            return vals[0] if len(vals)==1 else ast.copy_location(ast.BoolOp(op=n.op,values=vals),n) if vals else __mk__(False,n)
        return n
    def __tern__(n):
        if __same__(n.body,n.orelse) and __pure__(n.test): return n.body
        val=__bexp__(n.test,n.body,n.orelse,n)
        if val is not None: return val
        if __isn__(n.body,True) and __isn__(n.orelse,False): return ast.copy_location(ast.Call(func=ast.Name(id='bool',ctx=ast.Load()),args=[n.test],keywords=[]),n)
        if __isn__(n.body,False) and __isn__(n.orelse,True): return ast.copy_location(ast.UnaryOp(op=ast.Not(),operand=n.test),n)
        return n
    def __judge__(n):
        if len(n.ops)==1 and __same__(n.left,n.comparators[0]) and __pure__(n.left):
            if isinstance(n.ops[0],(ast.Eq,ast.LtE,ast.GtE,ast.Is)): return __mk__(True,n)
            if isinstance(n.ops[0],(ast.NotEq,ast.Lt,ast.Gt,ast.IsNot)): return __mk__(False,n)
        return n
    def __deny__(n):
        if isinstance(n,ast.Compare) and len(n.ops)==1:
            tab={ast.Eq:ast.NotEq,ast.NotEq:ast.Eq,ast.Lt:ast.GtE,ast.LtE:ast.Gt,ast.Gt:ast.LtE,ast.GtE:ast.Lt,ast.Is:ast.IsNot,ast.IsNot:ast.Is,ast.In:ast.NotIn,ast.NotIn:ast.In}
            kind=tab.get(type(n.ops[0]))
            if kind is not None: return ast.copy_location(ast.Compare(left=n.left,ops=[kind()],comparators=n.comparators),n)
        return None
    def __argn__(a):
        bag=[]
        for x in a.posonlyargs: bag.append(x.arg)
        for x in a.args: bag.append(x.arg)
        return bag
    def __simplea__(a):
        return not a.vararg and not a.kwarg and not a.kwonlyargs and not a.kw_defaults and not a.defaults
    def __lambok__(node):
        for x in ast.walk(node):
            if isinstance(x,(ast.Lambda,ast.NamedExpr,ast.Yield,ast.YieldFrom,ast.Await)): return False
        return True
    def __lam__(n,args):
        if not isinstance(n.func,ast.Lambda): return None
        lam=n.func
        if not __simplea__(lam.args): return None
        names=__argn__(lam.args)
        if len(names)!=len(args): return None
        if len(set(names))!=len(names): return None
        if not __lambok__(lam.body): return None
        tab={}
        for k,v in zip(names,args):
            if not __litok__(v): return None
            tab[k]=v
        return ast.copy_location(__swap__(lam.body,tab),n)
    def __noun__(n):
        if isinstance(n,ast.Call) and not n.keywords and isinstance(n.func,ast.Name) and n.func.id=='type' and len(n.args)==1:
            ok,v=__raw__(n.args[0])
            if ok: return True,type(v)
        return False,None
    def __typeattr__(n,attr):
        ok,t=__noun__(n)
        if ok and attr=='__name__': return True,t.__name__
        if ok and attr=='__qualname__': return True,t.__qualname__
        if ok and attr=='__module__': return True,t.__module__
        return False,None
    def __typec__(tree):
        for x in ast.walk(tree):
            if isinstance(x,ast.Module):
                x.type_ignores=[]
            if isinstance(x,ast.FunctionDef):
                x.type_comment=None
            if isinstance(x,ast.AsyncFunctionDef):
                x.type_comment=None
            if isinstance(x,ast.Assign):
                x.type_comment=None
            if isinstance(x,ast.For):
                x.type_comment=None
            if isinstance(x,ast.AsyncFor):
                x.type_comment=None
            if isinstance(x,ast.With):
                x.type_comment=None
            if isinstance(x,ast.AsyncWith):
                x.type_comment=None
            if isinstance(x,ast.arg) and hasattr(x,'type_comment'):
                x.type_comment=None
            if isinstance(x,ast.arguments):
                if hasattr(x,'posonlyargs'):
                    for y in x.posonlyargs:
                        if hasattr(y,'type_comment'): y.type_comment=None
                for y in x.args:
                    if hasattr(y,'type_comment'): y.type_comment=None
                for y in x.kwonlyargs:
                    if hasattr(y,'type_comment'): y.type_comment=None
                if x.vararg is not None and hasattr(x.vararg,'type_comment'):
                    x.vararg.type_comment=None
                if x.kwarg is not None and hasattr(x.kwarg,'type_comment'):
                    x.kwarg.type_comment=None
        return tree
    def __argu__(args,t):
        return len(args)==1 and isinstance(args[0],t) or len(args)==2 and isinstance(args[0],t) and isinstance(args[1],int)
    def __sets__(obj,name,args):
        if name in ('isdisjoint','issubset','issuperset') and len(args)==1 and isinstance(args[0],(set,frozenset,tuple,list)): return __ev__(getattr(obj,name),args[0])
        if name in ('union','intersection','difference','symmetric_difference') and len(args)<=8 and all(isinstance(x,(set,frozenset,tuple,list)) for x in args):
            try: return True,getattr(obj,name)(*args)
            except: return False,None
        if name=='copy' and not args: return True,obj.copy()
        return __ev__(obj.__contains__,args[0]) if name=='__contains__' and len(args)==1 else (False,None)
    def __dicts__(obj,name,args):
        if name=='get' and 1<=len(args)<=2: return __ev__(obj.get,*args)
        if name=='copy' and not args: return True,obj.copy()
        if name=='__contains__' and len(args)==1: return __ev__(obj.__contains__,args[0])
        return __ev__(lambda d,m:tuple(getattr(d,m)()),obj,name) if name in ('keys','values','items') and not args else (False,None)
    def __lists__(obj,name,args):
        if name=='copy' and not args: return True,obj.copy()
        if name=='count' and len(args)==1: return __ev__(obj.count,args[0])
        if name=='index' and 1<=len(args)<=3: return __ev__(obj.index,*args)
        return __ev__(obj.__contains__,args[0]) if name=='__contains__' and len(args)==1 else (False,None)
    def __tup__(obj,name,args):
        if name=='count' and len(args)==1: return __ev__(obj.count,args[0])
        if name=='index' and 1<=len(args)<=3: return __ev__(obj.index,*args)
        return False,None
    def __octet__(obj,name,args):
        if name=='capitalize' and not args: return __ev__(obj.capitalize)
        if name=='title' and not args: return __ev__(obj.title)
        if name=='swapcase' and not args: return __ev__(obj.swapcase)
        if name=='expandtabs' and len(args)<=1 and (not args or isinstance(args[0],int)): return __ev__(obj.expandtabs,*args)
        if name=='translate' and 1<=len(args)<=2 and isinstance(args[0],(bytes,bytearray)) and (len(args)==1 or isinstance(args[1],bytes)): return __ev__(obj.translate,*args)
        return __ev__(getattr(obj,name)) if name in ('lower','upper','strip','lstrip','rstrip') and not args else __ev__(obj.replace,*args) if name=='replace' and 2<=len(args)<=3 and all(isinstance(x,bytes) for x in args[:2]) and (len(args)==2 or isinstance(args[2],int)) else __ev__(getattr(obj,name),*args) if name in ('startswith','endswith') and 1<=len(args)<=3 and isinstance(args[0],(bytes,tuple)) and all(isinstance(x,int) for x in args[1:]) else __ev__(obj.hex,*args) if name=='hex' and (not args or __argu__(args,str)) else (False,None)
    def __text__(obj,name,args):
        if name=='format' and len(args)<=16: return __ev__(obj.format,*args)
        if name=='format_map' and len(args)==1 and isinstance(args[0],dict): return __ev__(obj.format_map,args[0])
        if name=='maketrans' and 1<=len(args)<=3 and all(isinstance(x,(str,dict)) for x in args): return __ev__(str.maketrans,*args)
        return __ev__(getattr(obj,name)) if name in ('lower','upper','casefold','capitalize','title','swapcase','strip','lstrip','rstrip') and not args else __ev__(obj.replace,*args) if name=='replace' and 2<=len(args)<=3 and all(isinstance(x,str) for x in args[:2]) and (len(args)==2 or isinstance(args[2],int)) else __ev__(getattr(obj,name),*args) if name in ('startswith','endswith') and 1<=len(args)<=3 and __pref__(args[0],str) and all(isinstance(x,int) for x in args[1:]) else (False,None)
    def __kwarg__(node):
        bag={}
        for x in node.keywords:
            if x.arg is None: return False,None
            ok,v=__raw__(x.value)
            if not ok: return False,None
            bag[x.arg]=v
        return True,bag
    def __safek__(name,args,kw):
        if name=='sorted' and len(args)==1 and set(kw)<= {'reverse'} and isinstance(args[0],(tuple,list,frozenset,str,bytes,dict)) and len(args[0])<=256 and all(isinstance(x,(int,float,str,bytes)) for x in args[0]) and (not kw or isinstance(kw.get('reverse'),bool)):
            try: return True,sorted(args[0],**kw)
            except: return False,None
        if name=='round' and len(args)==1 and set(kw)<= {'ndigits'} and isinstance(args[0],(int,float)) and (not kw or isinstance(kw.get('ndigits'),int)): return __ev__(round,args[0],**kw)
        if name=='format' and len(args)==1 and set(kw)<= {'format_spec'} and isinstance(kw.get('format_spec',''),str): return __ev__(format,args[0],**kw)
        if name=='int' and len(args)==1 and set(kw)<= {'base'} and isinstance(args[0],(str,bytes)) and isinstance(kw.get('base'),int): return __ev__(int,args[0],**kw)
        if name=='bytes' and len(args)==1 and set(kw)<= {'encoding','errors'} and isinstance(args[0],str) and isinstance(kw.get('encoding'),str) and (not 'errors' in kw or isinstance(kw.get('errors'),str)): return __ev__(bytes,args[0],**kw)
        if name=='dict' and not args and all(isinstance(k,str) and __ok__(v) for k,v in kw.items()): return True,dict(kw)
        if name=='complex' and not args and set(kw)<= {'real','imag'} and all(isinstance(x,(int,float,complex,str)) for x in kw.values()): return __ev__(complex,**kw)
        if name=='pow' and 2<=len(args)<=3 and set(kw)<= {'mod'} and all(isinstance(x,int) for x in args) and all(isinstance(x,int) for x in kw.values()) and abs(args[1])<=32: return __ev__(pow,*args,**kw)
        return False,None
    def __methk__(obj,name,args,kw):
        if isinstance(obj,str):
            if name=='format' and len(args)<=16 and all(__ok__(x) for x in args) and all(isinstance(k,str) and __ok__(v) for k,v in kw.items()):
                try: return True,obj.format(*args,**kw)
                except: return False,None
            if name in ('split','rsplit') and not args and set(kw)<= {'sep','maxsplit'} and (not 'sep' in kw or isinstance(kw.get('sep'),str) or kw.get('sep') is None) and (not 'maxsplit' in kw or isinstance(kw.get('maxsplit'),int)): return __ev__(getattr(obj,name),**kw)
            if name=='splitlines' and not args and set(kw)<= {'keepends'} and (not kw or isinstance(kw.get('keepends'),bool)): return __ev__(obj.splitlines,**kw)
            if name=='replace' and not args and {'old','new'}<=set(kw) and set(kw)<= {'old','new','count'} and isinstance(kw.get('old'),str) and isinstance(kw.get('new'),str) and (not 'count' in kw or isinstance(kw.get('count'),int)): return __ev__(obj.replace,**kw)
            if name=='encode' and not args and set(kw)<= {'encoding','errors'} and (not 'encoding' in kw or isinstance(kw.get('encoding'),str)) and (not 'errors' in kw or isinstance(kw.get('errors'),str)): return __ev__(obj.encode,**kw)
            if name in ('center','ljust','rjust') and len(args)==1 and set(kw)<= {'fillchar'} and isinstance(args[0],int) and (not kw or isinstance(kw.get('fillchar'),str)): return __ev__(getattr(obj,name),*args,**kw)
            if name in ('startswith','endswith') and not args and {'prefix'}<=set(kw) and set(kw)<= {'prefix','start','end'} and __pref__(kw.get('prefix'),str) and all(isinstance(v,int) for k,v in kw.items() if k!='prefix'): return __ev__(getattr(obj,name),**kw)
            if name in ('find','rfind','index','rindex','count') and not args and {'sub'}<=set(kw) and set(kw)<= {'sub','start','end'} and isinstance(kw.get('sub'),str) and all(isinstance(v,int) for k,v in kw.items() if k!='sub'): return __ev__(getattr(obj,name),**kw)
        if isinstance(obj,bytes):
            if name in ('split','rsplit') and not args and set(kw)<= {'sep','maxsplit'} and (not 'sep' in kw or isinstance(kw.get('sep'),bytes) or kw.get('sep') is None) and (not 'maxsplit' in kw or isinstance(kw.get('maxsplit'),int)): return __ev__(getattr(obj,name),**kw)
            if name=='splitlines' and not args and set(kw)<= {'keepends'} and (not kw or isinstance(kw.get('keepends'),bool)): return __ev__(obj.splitlines,**kw)
            if name=='replace' and not args and {'old','new'}<=set(kw) and set(kw)<= {'old','new','count'} and isinstance(kw.get('old'),bytes) and isinstance(kw.get('new'),bytes) and (not 'count' in kw or isinstance(kw.get('count'),int)): return __ev__(obj.replace,**kw)
            if name=='decode' and not args and set(kw)<= {'encoding','errors'} and (not 'encoding' in kw or isinstance(kw.get('encoding'),str)) and (not 'errors' in kw or isinstance(kw.get('errors'),str)): return __ev__(obj.decode,**kw)
            if name in ('center','ljust','rjust') and len(args)==1 and set(kw)<= {'fillbyte'} and isinstance(args[0],int) and (not kw or isinstance(kw.get('fillbyte'),bytes)): return __ev__(getattr(obj,name),*args,**kw)
            if name=='hex' and not args and set(kw)<= {'sep','bytes_per_sep'} and (not 'sep' in kw or isinstance(kw.get('sep'),str)) and (not 'bytes_per_sep' in kw or isinstance(kw.get('bytes_per_sep'),int)): return __ev__(obj.hex,**kw)
            if name in ('startswith','endswith') and not args and {'prefix'}<=set(kw) and set(kw)<= {'prefix','start','end'} and __pref__(kw.get('prefix'),bytes) and all(isinstance(v,int) for k,v in kw.items() if k!='prefix'): return __ev__(getattr(obj,name),**kw)
            if name in ('find','rfind','index','rindex','count') and not args and {'sub'}<=set(kw) and set(kw)<= {'sub','start','end'} and isinstance(kw.get('sub'),bytes) and all(isinstance(v,int) for k,v in kw.items() if k!='sub'): return __ev__(getattr(obj,name),**kw)
        if isinstance(obj,int):
            if name=='to_bytes' and not args and {'length','byteorder'}<=set(kw) and set(kw)<= {'length','byteorder','signed'} and isinstance(kw.get('length'),int) and 0<=kw.get('length')<=lim and isinstance(kw.get('byteorder'),str) and (not 'signed' in kw or isinstance(kw.get('signed'),bool)): return __ev__(obj.to_bytes,**kw)
        if isinstance(obj,dict) and name=='get' and len(args)==1 and set(kw)<= {'default'}: return __ev__(obj.get,*args,**kw)
        return False,None
    def __modk__(head,tail,args,kw):
        if head=='math' and tail=='isclose' and 2<=len(args)<=3 and set(kw)<= {'rel_tol','abs_tol'} and __numok__(args) and all(isinstance(x,(int,float)) for x in kw.values()): return __ev__(math.isclose,*args,**kw)
        if head=='base64' and tail in ('b64decode','b32decode','b16decode') and 1<=len(args)<=2 and set(kw)<= {'casefold','map01','altchars','validate'} and isinstance(args[0],(bytes,str)): return __ev__(getattr(base64,tail),*args,**kw)
        if head=='zlib' and tail=='compress' and len(args)==1 and set(kw)<= {'level'} and isinstance(args[0],bytes) and len(args[0])<=lim and (not kw or isinstance(kw.get('level'),int)): return __ev__(zlib.compress,*args,**kw)
        if head=='json' and tail=='dumps' and len(args)==1 and set(kw)<= {'skipkeys','ensure_ascii','check_circular','allow_nan','indent','separators','sort_keys'} and isinstance(args[0],(dict,list,tuple,str,int,float,bool,type(None))) and all(isinstance(v,(bool,int,str,tuple,type(None))) for v in kw.values()):
            try: return True,json.dumps(*args,**kw)
            except: return False,None
        done,out=__packk__(head,tail,args,kw)
        if done: return True,out
        if head=='dict' and tail=='fromkeys' and len(args)==1 and set(kw)<= {'value'} and isinstance(args[0],(tuple,list,frozenset,str,bytes,dict)) and len(args[0])<=128: return __ev__(dict.fromkeys,*args,**kw)
        if head=='unicodedata' and tail=='name' and len(args)==1 and set(kw)<= {'default'} and isinstance(args[0],str) and len(args[0])==1: return __ev__(unicodedata.name,*args,**kw)
        return False,None
    def __flip__(n): return ast.UnaryOp(op=ast.Not(),operand=n)
    def __bval__(n):
        if isinstance(n,ast.Constant) and isinstance(n.value,bool): return True,n.value
        return False,None
    def __bexp__(test,left,right,node):
        lo,lv=__bval__(left);ro,rv=__bval__(right)
        if not lo or not ro: return None
        if lv==rv: return None
        val=ast.Call(func=ast.Name(id='bool',ctx=ast.Load()),args=[test],keywords=[]) if lv and not rv else __flip__(test)
        return ast.copy_location(val,node)
    def __tuck__(x,y=None):
        if isinstance(x,ast.If) and len(x.body)==1 and isinstance(x.body[0],ast.Return):
            if len(x.orelse)==1 and isinstance(x.orelse[0],ast.Return):
                val=__bexp__(x.test,x.body[0].value or ast.Constant(None),x.orelse[0].value or ast.Constant(None),x) or ast.IfExp(test=x.test,body=x.body[0].value or ast.Constant(None),orelse=x.orelse[0].value or ast.Constant(None))
                return ast.copy_location(ast.Return(value=val),x)
            if y is not None and not x.orelse and isinstance(y,ast.Return):
                val=__bexp__(x.test,x.body[0].value or ast.Constant(None),y.value or ast.Constant(None),x) or ast.IfExp(test=x.test,body=x.body[0].value or ast.Constant(None),orelse=y.value or ast.Constant(None))
                return ast.copy_location(ast.Return(value=val),x)
        if isinstance(x,ast.If) and len(x.body)==1 and isinstance(x.body[0],ast.Assign):
            left=x.body[0]
            if len(x.orelse)==1 and isinstance(x.orelse[0],ast.Assign) and len(left.targets)==1 and len(x.orelse[0].targets)==1 and __same__(left.targets[0],x.orelse[0].targets[0]):
                val=__bexp__(x.test,left.value,x.orelse[0].value,x) or ast.IfExp(test=x.test,body=left.value,orelse=x.orelse[0].value)
                return ast.copy_location(ast.Assign(targets=left.targets,value=val),x)
            if y is not None and not x.orelse and isinstance(y,ast.Assign) and len(left.targets)==1 and len(y.targets)==1 and __same__(left.targets[0],y.targets[0]):
                val=__bexp__(x.test,left.value,y.value,x) or ast.IfExp(test=x.test,body=left.value,orelse=y.value)
                return ast.copy_location(ast.Assign(targets=left.targets,value=val),x)
        if isinstance(x,ast.If) and len(x.body)==1 and isinstance(x.body[0],ast.Expr):
            left=x.body[0]
            if len(x.orelse)==1 and isinstance(x.orelse[0],ast.Expr) and isinstance(left.value,ast.Call) and isinstance(x.orelse[0].value,ast.Call) and __same__(left.value.func,x.orelse[0].value.func) and not left.value.keywords and not x.orelse[0].value.keywords and len(left.value.args)==1 and len(x.orelse[0].value.args)==1: return ast.copy_location(ast.Expr(value=ast.Call(func=left.value.func,args=[ast.IfExp(test=x.test,body=left.value.args[0],orelse=x.orelse[0].value.args[0])],keywords=[])),x)
        return None
    def __bod__(rows):
        bag=[];first=True;stop=False
        at=0
        while at<len(rows):
            x=rows[at];nxt=rows[at+1] if at+1<len(rows) else None
            pair=nxt is not None and isinstance(x,ast.If) and not x.orelse and ((len(x.body)==1 and isinstance(x.body[0],ast.Return) and isinstance(nxt,ast.Return)) or (len(x.body)==1 and isinstance(x.body[0],ast.Assign) and isinstance(nxt,ast.Assign) and len(x.body[0].targets)==1 and len(nxt.targets)==1 and __same__(x.body[0].targets[0],nxt.targets[0])))
            got=__tuck__(x,nxt)
            if got is not None: x=got;at+=2 if pair else 1
            else: at+=1
            if stop: continue
            if __drop__(x,first) and len(rows)>1: first=False;continue
            bag.append(x);first=False;stop=isinstance(x,(ast.Return,ast.Raise,ast.Break,ast.Continue))
        return __dead__(__lane__(bag)) or [ast.Pass()]
    def __tru__(n):
        ok,v=__raw__(n)
        if ok:
            try: return True,bool(v)
            except: pass
        return False,None
    def __safe__(name,args):
        if not args and name in ('list','tuple','dict','set','frozenset','str','bytes','int','float','complex','bool'): return True,{'list':[],'tuple':(),'dict':{},'set':set(),'frozenset':frozenset(),'str':'','bytes':b'','int':0,'float':0.0,'complex':0j,'bool':False}[name]
        if name=='len' and len(args)==1: return __ev__(len,args[0])
        if name=='bool' and len(args)==1: return __ev__(bool,args[0])
        if name=='str' and len(args)==1: return __ev__(str,args[0])
        if name=='repr' and len(args)==1: return __ev__(repr,args[0])
        if name=='ascii' and len(args)==1: return __ev__(ascii,args[0])
        if name=='callable' and len(args)==1: return __ev__(callable,args[0])
        if name=='hash' and len(args)==1 and isinstance(args[0],(int,float,complex)): return __ev__(hash,args[0])
        if name=='bin' and len(args)==1 and isinstance(args[0],int): return __ev__(bin,args[0])
        if name=='oct' and len(args)==1 and isinstance(args[0],int): return __ev__(oct,args[0])
        if name=='hex' and len(args)==1 and isinstance(args[0],int): return __ev__(hex,args[0])
        if name=='format' and 1<=len(args)<=2 and (len(args)==1 or isinstance(args[1],str)): return __ev__(format,*args)
        if name=='ord' and len(args)==1 and isinstance(args[0],str) and len(args[0])==1: return __ev__(ord,args[0])
        if name=='chr' and len(args)==1 and isinstance(args[0],int) and 0<=args[0]<=0x10ffff: return __ev__(chr,args[0])
        if name=='int' and (len(args)==1 and isinstance(args[0],(int,float,str,bytes)) or len(args)==2 and isinstance(args[0],(str,bytes)) and isinstance(args[1],int)): return __ev__(int,*args)
        if name=='float' and len(args)==1 and isinstance(args[0],(int,float,str,bytes)): return __ev__(float,args[0])
        if name=='complex' and 1<=len(args)<=2 and all(isinstance(x,(int,float,complex,str)) for x in args): return __ev__(complex,*args)
        if name=='bytes' and 2<=len(args)<=3 and isinstance(args[0],str) and isinstance(args[1],str) and (len(args)==2 or isinstance(args[2],str)): return __ev__(bytes,*args)
        if name=='abs' and len(args)==1 and isinstance(args[0],(int,float,complex)): return __ev__(abs,args[0])
        if name=='round' and 1<=len(args)<=2 and isinstance(args[0],(int,float)) and (len(args)==1 or isinstance(args[1],int)): return __ev__(round,*args)
        if name=='divmod' and len(args)==2 and all(isinstance(x,(int,float)) for x in args): return __ev__(divmod,*args)
        if name=='pow' and 2<=len(args)<=3 and all(isinstance(x,int) for x in args) and abs(args[1])<=32: return __ev__(pow,*args)
        if name=='sum' and 1<=len(args)<=2 and isinstance(args[0],(tuple,list,set,frozenset)) and all(isinstance(x,(int,float,complex)) for x in args[0]) and len(args[0])<=256 and (len(args)==1 or isinstance(args[1],(int,float,complex))): return __ev__(sum,*args)
        if name=='all' and len(args)==1 and isinstance(args[0],(tuple,list,set,frozenset,dict)) and len(args[0])<=256: return __ev__(all,args[0])
        if name=='any' and len(args)==1 and isinstance(args[0],(tuple,list,set,frozenset,dict)) and len(args[0])<=256: return __ev__(any,args[0])
        if name=='min' and len(args)==1 and isinstance(args[0],(tuple,list,set,frozenset)) and 0<len(args[0])<=256 and all(isinstance(x,(int,float,str,bytes)) for x in args[0]): return __ev__(min,args[0])
        if name=='max' and len(args)==1 and isinstance(args[0],(tuple,list,set,frozenset)) and 0<len(args[0])<=256 and all(isinstance(x,(int,float,str,bytes)) for x in args[0]): return __ev__(max,args[0])
        if name=='min' and 1<len(args)<=16 and all(isinstance(x,(int,float,str,bytes)) for x in args): return __ev__(min,*args)
        if name=='max' and 1<len(args)<=16 and all(isinstance(x,(int,float,str,bytes)) for x in args): return __ev__(max,*args)
        if name=='sorted' and len(args)==1 and isinstance(args[0],(tuple,list,set,frozenset,str,bytes)) and len(args[0])<=256 and all(isinstance(x,(int,float,str,bytes)) for x in args[0]):
            try: return True,sorted(args[0])
            except: return False,None
        if name=='list' and len(args)==1 and isinstance(args[0],(tuple,set,frozenset,str,bytes,dict)) and len(args[0])<=256: return True,list(args[0])
        if name=='dict' and len(args)==1 and isinstance(args[0],(tuple,list,set,frozenset)) and len(args[0])<=128:
            try: return True,dict(args[0])
            except: return False,None
        if name in ('tuple','reversed','enumerate') and len(args)==1 and isinstance(args[0],(tuple,list,set,frozenset,str,bytes,dict)) and len(args[0])<=256 and (name=='tuple' or not isinstance(args[0],(set,frozenset,dict))): return __ev__(tuple if name=='tuple' else (lambda x:tuple(reversed(x))) if name=='reversed' else (lambda x:tuple(enumerate(x))),args[0])
        if name in ('frozenset','set') and len(args)==1 and isinstance(args[0],(tuple,list,set,frozenset,str,bytes,dict)) and len(args[0])<=256:
            try: return True,(frozenset if name=='frozenset' else set)(args[0])
            except: return False,None
        if name=='bytes' and len(args)==1 and isinstance(args[0],(tuple,list,set,frozenset)) and len(args[0])<=lim and all(isinstance(x,int) and 0<=x<=255 for x in args[0]): return __ev__(bytes,args[0])
        if name=='getattr' and 2<=len(args)<=3 and isinstance(args[1],str) and not args[1].startswith('__'): return __ev__(getattr,*args)
        if name=='hasattr' and len(args)==2 and isinstance(args[1],str) and not args[1].startswith('__'): return __ev__(hasattr,*args)
        return False,None
    def __klass__(n):
        tab={'bool':bool,'int':int,'float':float,'complex':complex,'str':str,'bytes':bytes,'tuple':tuple,'list':list,'set':set,'frozenset':frozenset,'dict':dict,'type':type,'object':object}
        if isinstance(n,ast.Name) and n.id in tab: return True,tab[n.id]
        if isinstance(n,ast.Tuple):
            bag=[]
            for x in n.elts:
                ok,v=__klass__(x)
                if not ok: return False,None
                bag.append(v)
            return True,tuple(bag)
        return False,None
    def __isa__(n,args):
        if isinstance(n.func,ast.Name) and n.func.id=='isinstance' and len(n.args)==2:
            ok,obj=__raw__(n.args[0]);ko,kind=__klass__(n.args[1])
            if ok and ko: return __ev__(isinstance,obj,kind)
        if isinstance(n.func,ast.Name) and n.func.id=='issubclass' and len(n.args)==2:
            ko,kind=__klass__(n.args[0]);lo,base=__klass__(n.args[1])
            if ko and lo: return __ev__(issubclass,kind,base)
        return False,None
    def __jag__(n):
        if not isinstance(n,ast.Call) or n.keywords or not isinstance(n.func,ast.Name) or n.func.id!='range' or not 1<=len(n.args)<=3: return False,None
        args=[]
        for x in n.args:
            ok,v=__raw__(x)
            if not ok or not isinstance(v,int): return False,None
            args.append(v)
        done,out=__ev__(lambda *a:tuple(range(*a)),*args)
        return (done,out) if done and len(out)<=512 else (False,None)
    def __fn__(n):
        tab={'str':str,'repr':repr,'ascii':ascii,'bool':bool,'int':int,'float':float,'complex':complex,'bytes':bytes,'abs':abs,'chr':chr,'ord':ord,'hex':hex,'oct':oct,'bin':bin,'len':len,'sum':sum,'round':round,'tuple':tuple,'list':list,'set':set,'frozenset':frozenset,'divmod':divmod,'pow':lambda a,b,*c:pow(a,b,*c) if isinstance(b,int) and abs(b)<=32 and (not c or isinstance(c[0],int)) else (_ for _ in ()).throw(ValueError)}
        if isinstance(n,ast.Name) and n.id in tab: return True,tab[n.id]
        return False,None
    def __stream__(x,kind):
        if not isinstance(x,ast.Call) or x.keywords: return False,None
        if isinstance(x.func,ast.Name) and x.func.id=='map' and 2<=len(x.args)<=8:
            ok,fn=__fn__(x.args[0]);vals=[]
            if ok:
                for row in x.args[1:]:
                    ko,val=__raw__(row)
                    if not ko:
                        ko,val=__jag__(row)
                    if not ko or not isinstance(val,(tuple,list,frozenset,str,bytes,dict)) or len(val)>256: return False,None
                    vals.append(val)
                return __ev__(lambda f,a,k:k(map(f,*a)),fn,vals,kind)
        if isinstance(x.func,ast.Name) and x.func.id=='filter' and len(x.args)==2:
            ko,val=__raw__(x.args[1])
            if not ko:
                ko,val=__jag__(x.args[1])
            if ko and isinstance(val,(tuple,list,frozenset,str,bytes,dict)) and len(val)<=256:
                if isinstance(x.args[0],ast.Constant) and x.args[0].value is None: return __ev__(lambda a,k:k(filter(None,a)),val,kind)
                ok,fn=__fn__(x.args[0])
                if ok: return __ev__(lambda f,a,k:k(filter(f,a)),fn,val,kind)
        if isinstance(x.func,ast.Attribute) and not x.args and x.func.attr in ('keys','values','items'):
            ok,val=__raw__(x.func.value)
            if ok and isinstance(val,dict) and len(val)<=128: return __ev__(lambda d,m,k:k(getattr(d,m)()),val,x.func.attr,kind)
        return False,None
    def __born__(n,args):
        if isinstance(n.func,ast.Name) and n.func.id=='tuple' and len(n.args)==1:
            done,out=__jag__(n.args[0])
            if done: return True,out
            x=n.args[0]
            done,out=__stream__(x,tuple)
            if done: return True,out
            if isinstance(x,ast.Call) and not x.keywords and isinstance(x.func,ast.Name) and x.func.id in ('reversed','sorted','enumerate') and 1<=len(x.args)<=2 and (x.func.id=='enumerate' or len(x.args)==1):
                ok,v=__raw__(x.args[0])
                if ok and isinstance(v,(tuple,list,frozenset,str,bytes,dict)) and len(v)<=512 and (x.func.id!='reversed' or not isinstance(v,(set,frozenset))) and (len(x.args)==1 or isinstance(x.args[1],ast.Constant) and isinstance(x.args[1].value,int)): return __ev__(lambda f,a,*b:tuple(f(a,*b)), {'reversed':reversed,'sorted':sorted,'enumerate':enumerate}[x.func.id], v, *( [x.args[1].value] if len(x.args)>1 else [] ))
            if isinstance(x,ast.Call) and (not x.keywords or set(y.arg for y in x.keywords if y.arg)<= {'strict'}) and isinstance(x.func,ast.Name) and x.func.id=='zip' and 1<=len(x.args)<=8:
                vals=[]
                ko,kw=__kwarg__(x) if x.keywords else (True,{})
                if not ko or any(not isinstance(v,bool) for v in kw.values()): return False,None
                for row in x.args:
                    ok,v=__raw__(row)
                    if not ok or not isinstance(v,(tuple,list,frozenset,str,bytes,dict)) or len(v)>512: return False,None
                    vals.append(v)
                return __ev__(lambda a,k:tuple(zip(*a,**k)),vals,kw)
        if isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name):
            head=n.func.value.id;tail=n.func.attr
            if head=='str' and tail=='maketrans' and 1<=len(args)<=3 and all(isinstance(x,(str,dict)) for x in args): return __ev__(str.maketrans,*args)
            if head=='dict' and tail=='fromkeys' and 1<=len(n.args)<=2:
                done,out=__jag__(n.args[0])
                if not done: done,out=__stream__(n.args[0],tuple)
                if done and len(out)<=128:
                    if len(n.args)==1: return __ev__(dict.fromkeys,out)
                    ok,v=__raw__(n.args[1])
                    if ok: return __ev__(dict.fromkeys,out,v)
            if head=='dict' and tail=='fromkeys' and 1<=len(args)<=2 and isinstance(args[0],(tuple,list,frozenset,str,bytes,dict)) and len(args[0])<=128: return __ev__(dict.fromkeys,*args)
            if head=='bytes' and tail=='fromhex' and len(args)==1 and isinstance(args[0],str): return __ev__(bytes.fromhex,args[0])
            if head=='int' and tail=='from_bytes' and 2<=len(args)<=3 and isinstance(args[0],(bytes,bytearray)) and isinstance(args[1],str) and (len(args)==2 or isinstance(args[2],bool)): return __ev__(int.from_bytes,*args)
            if head=='float' and tail=='fromhex' and len(args)==1 and isinstance(args[0],str): return __ev__(float.fromhex,args[0])
        return False,None
    def __node__(v,n):
        if isinstance(v,list) and len(v)<=256 and all(__ok__(x) for x in v): return ast.copy_location(ast.List(elts=[ast.Constant(x) for x in v],ctx=ast.Load()),n)
        if isinstance(v,set) and len(v)<=256 and all(__ok__(x) for x in v):
            try:
                for x in v: hash(x)
                return ast.copy_location(ast.Set(elts=[ast.Constant(x) for x in v]),n)
            except: return None
        if isinstance(v,dict) and len(v)<=128 and all(__ok__(k) and __ok__(x) for k,x in v.items()): return ast.copy_location(ast.Dict(keys=[ast.Constant(k) for k in v],values=[ast.Constant(x) for x in v.values()]),n)
        return None
    def __done__(v,n):
        return __lift__(v,n)
    def __morph__(n,args):
        if not isinstance(n.func,ast.Name): return None
        name=n.func.id
        if len(n.args)==1:
            x=n.args[0];ok,val=__raw__(x)
            if name=='list':
                if ok and isinstance(val,(tuple,list,frozenset,str,bytes,dict)) and len(val)<=256: return __node__(list(val),n)
                done,out=__jag__(n.args[0])
                if done: return __node__(list(out),n)
                done,out=__stream__(x,list)
                if done: return __node__(out,n)
                if isinstance(x,ast.Call) and not x.keywords and isinstance(x.func,ast.Name) and x.func.id in ('reversed','sorted','enumerate') and 1<=len(x.args)<=2 and (x.func.id=='enumerate' or len(x.args)==1):
                    ok,v=__raw__(x.args[0])
                    if ok and isinstance(v,(tuple,list,frozenset,str,bytes,dict)) and len(v)<=256 and (x.func.id!='reversed' or not isinstance(v,(set,frozenset))) and (len(x.args)==1 or isinstance(x.args[1],ast.Constant) and isinstance(x.args[1].value,int)):
                        done,out=__ev__(lambda f,a,*b:list(f(a,*b)),{'reversed':reversed,'sorted':sorted,'enumerate':enumerate}[x.func.id],v,*( [x.args[1].value] if len(x.args)>1 else [] ))
                        if done: return __node__(out,n)
                if isinstance(x,ast.Call) and (not x.keywords or set(y.arg for y in x.keywords if y.arg)<= {'strict'}) and isinstance(x.func,ast.Name) and x.func.id=='zip' and 1<=len(x.args)<=8:
                    vals=[]
                    ko,kw=__kwarg__(x) if x.keywords else (True,{})
                    if not ko or any(not isinstance(v,bool) for v in kw.values()): return None
                    for row in x.args:
                        ok,v=__raw__(row)
                        if not ok or not isinstance(v,(tuple,list,frozenset,str,bytes,dict)) or len(v)>256: return None
                        vals.append(v)
                    done,out=__ev__(lambda a,k:list(zip(*a,**k)),vals,kw)
                    if done: return __node__(out,n)
            if name=='set':
                if ok and isinstance(val,(tuple,list,frozenset,str,bytes,dict)) and len(val)<=256: return __node__(set(val),n)
                done,out=__jag__(n.args[0])
                if done: return __node__(set(out),n)
                done,out=__stream__(x,set)
                if done: return __node__(out,n)
                if isinstance(x,ast.Call) and not x.keywords and isinstance(x.func,ast.Name) and x.func.id in ('reversed','sorted') and len(x.args)==1:
                    ok,v=__raw__(x.args[0])
                    if ok and isinstance(v,(tuple,list,frozenset,str,bytes,dict)) and len(v)<=256 and (x.func.id!='reversed' or not isinstance(v,(set,frozenset))):
                        done,out=__ev__(lambda f,a:set(f(a)),{'reversed':reversed,'sorted':sorted}[x.func.id],v)
                        if done: return __node__(out,n)
            if ok and name=='dict' and isinstance(val,(tuple,list,frozenset,set)) and len(val)<=128:
                try: return __node__(dict(val),n)
                except: return None
        if name=='dict' and len(n.args)==1:
            x=n.args[0]
            if isinstance(x,ast.Call) and not x.keywords and isinstance(x.func,ast.Name) and x.func.id=='zip' and len(x.args)==2:
                ok,a=__raw__(x.args[0]);ko,b=__raw__(x.args[1])
                if ok and ko and isinstance(a,(tuple,list,frozenset,str,bytes,dict)) and isinstance(b,(tuple,list,frozenset,str,bytes,dict)) and len(a)<=128 and len(b)<=128:
                    try: return __node__(dict(zip(a,b)),n)
                    except: return None
        return None
    def __empty__(n):
        done,out=__jag__(n)
        if done: return len(out)==0
        ok,val=__raw__(n)
        if ok and isinstance(val,(tuple,list,set,frozenset,dict,str,bytes)): return len(val)==0
        return False
    def __voids__(n):
        if isinstance(n,ast.ListComp): return ast.copy_location(ast.List(elts=[],ctx=ast.Load()),n)
        if isinstance(n,ast.SetComp): return ast.copy_location(ast.Set(elts=[]),n)
        if isinstance(n,ast.DictComp): return ast.copy_location(ast.Dict(keys=[],values=[]),n)
        return n
    def __cgen__(n):
        if not isinstance(n,(ast.ListComp,ast.SetComp,ast.DictComp)) or len(n.generators)!=1: return None
        gen=n.generators[0]
        if gen.is_async or not isinstance(gen.target,ast.Name): return None
        done,seq=__jag__(gen.iter)
        if not done: done,seq=__stream__(gen.iter,tuple)
        if not done: done,seq=__raw__(gen.iter)
        if not done or not isinstance(seq,(tuple,list,frozenset,str,bytes,dict)) or len(seq)>128: return None
        bag=[];keys=[];vals=[]
        for val in seq:
            tab={gen.target.id:val};keep=True
            for row in gen.ifs:
                node=__go__(__swap__(copy.deepcopy(row),tab));ok,hit=__truthy__(node)
                if not ok: return None
                if not hit: keep=False;break
            if not keep: continue
            if isinstance(n,ast.DictComp):
                ko,k=__raw__(__go__(__swap__(copy.deepcopy(n.key),tab)));vo,v=__raw__(__go__(__swap__(copy.deepcopy(n.value),tab)))
                if not ko or not vo: return None
                keys.append(k);vals.append(v)
            else:
                ok,out=__raw__(__go__(__swap__(copy.deepcopy(n.elt),tab)))
                if not ok: return None
                bag.append(out)
        return __node__(dict(zip(keys,vals)),n) if isinstance(n,ast.DictComp) else __node__(set(bag),n) if isinstance(n,ast.SetComp) else __node__(bag,n)
    def __tally__(n):
        if isinstance(n,ast.List): return len(n.elts)
        if isinstance(n,ast.Tuple): return len(n.elts)
        if isinstance(n,ast.Set): return len(n.elts)
        if isinstance(n,ast.Dict): return len(n.keys)
        done,out=__jag__(n)
        if done: return len(out)
        ok,val=__raw__(n)
        return len(val) if ok and isinstance(val,(tuple,list,set,frozenset,dict,str,bytes)) else None
    def __slc__(n):
        if isinstance(n,ast.Slice):
            ao,a=(True,None) if n.lower is None else __raw__(n.lower);bo,b=(True,None) if n.upper is None else __raw__(n.upper);co,c=(True,None) if n.step is None else __raw__(n.step)
            if ao and bo and co: return __ev__(slice,a,b,c)
        if isinstance(n,ast.Call) and not n.keywords and isinstance(n.func,ast.Name) and n.func.id=='slice' and 1<=len(n.args)<=3:
            args=[]
            for x in n.args:
                ok,v=__raw__(x)
                if not ok or not (v is None or isinstance(v,int)): return False,None
                args.append(v)
            return __ev__(slice,*args)
        return False,None
    def __truthy__(n):
        got=__tally__(n)
        if got is not None: return True,bool(got)
        return __tru__(n)
    def __pref__(x,t):
        return isinstance(x,t) or isinstance(x,tuple) and all(isinstance(y,t) for y in x)
    def __spread__(args,t):
        return all(isinstance(x,t) for x in args) or len(args)>1 and isinstance(args[0],t) and all(isinstance(x,int) for x in args[1:])
    def __meth__(obj,name,args):
        if isinstance(obj,str):
            done,out=__text__(obj,name,args)
            if done: return True,out
            if name in ('lower','upper','casefold','capitalize','title','swapcase','strip','lstrip','rstrip') and not args: return __ev__(getattr(obj,name))
            if name in ('strip','lstrip','rstrip') and len(args)==1 and isinstance(args[0],str): return __ev__(getattr(obj,name),args[0])
            if name in ('isalpha','isalnum','isascii','isdecimal','isdigit','isidentifier','islower','isnumeric','isprintable','isspace','istitle','isupper') and not args: return __ev__(getattr(obj,name))
            if name in ('removeprefix','removesuffix') and len(args)==1 and isinstance(args[0],str): return __ev__(getattr(obj,name),*args)
            if name=='replace' and 2<=len(args)<=3 and isinstance(args[0],str) and isinstance(args[1],str) and (len(args)==2 or isinstance(args[2],int)): return __ev__(obj.replace,*args)
            if name in ('find','rfind','count','index','rindex') and 1<=len(args)<=3 and __spread__(args,str): return __ev__(getattr(obj,name),*args)
            if name in ('startswith','endswith') and 1<=len(args)<=3 and __pref__(args[0],str) and all(isinstance(x,int) for x in args[1:]): return __ev__(getattr(obj,name),*args)
            if name in ('center','ljust','rjust') and 1<=len(args)<=2 and isinstance(args[0],int) and (len(args)==1 or isinstance(args[1],str)): return __ev__(getattr(obj,name),*args)
            if name=='zfill' and len(args)==1 and isinstance(args[0],int): return __ev__(obj.zfill,args[0])
            if name in ('partition','rpartition') and len(args)==1 and isinstance(args[0],str): return __ev__(getattr(obj,name),args[0])
            if name=='expandtabs' and len(args)<=1 and (not args or isinstance(args[0],int)): return __ev__(obj.expandtabs,*args)
            if name=='translate' and len(args)==1 and isinstance(args[0],dict): return __ev__(obj.translate,args[0])
            if name=='join' and len(args)==1 and isinstance(args[0],(tuple,list,frozenset)) and all(isinstance(x,str) for x in args[0]): return __ev__(obj.join,args[0])
            if name in ('split','rsplit') and len(args)<=2 and all(isinstance(x,(str,int)) for x in args) and (len(args)<2 or isinstance(args[1],int)): return __ev__(getattr(obj,name),*args)
            if name=='splitlines' and len(args)<=1 and (not args or isinstance(args[0],bool)): return __ev__(obj.splitlines,*args)
            if name=='encode' and len(args)<=2 and all(isinstance(x,str) for x in args): return __ev__(obj.encode,*args)
        if isinstance(obj,bytes):
            done,out=__octet__(obj,name,args)
            if done: return True,out
            if name in ('lower','upper','strip','lstrip','rstrip') and not args: return __ev__(getattr(obj,name))
            if name in ('strip','lstrip','rstrip') and len(args)==1 and isinstance(args[0],bytes): return __ev__(getattr(obj,name),args[0])
            if name in ('isalnum','isalpha','isascii','isdigit','islower','isspace','istitle','isupper') and not args: return __ev__(getattr(obj,name))
            if name in ('removeprefix','removesuffix') and len(args)==1 and isinstance(args[0],bytes): return __ev__(getattr(obj,name),*args)
            if name=='replace' and 2<=len(args)<=3 and isinstance(args[0],bytes) and isinstance(args[1],bytes) and (len(args)==2 or isinstance(args[2],int)): return __ev__(obj.replace,*args)
            if name in ('find','rfind','count','index','rindex') and 1<=len(args)<=3 and __spread__(args,bytes): return __ev__(getattr(obj,name),*args)
            if name in ('startswith','endswith') and 1<=len(args)<=3 and __pref__(args[0],bytes) and all(isinstance(x,int) for x in args[1:]): return __ev__(getattr(obj,name),*args)
            if name in ('center','ljust','rjust') and 1<=len(args)<=2 and isinstance(args[0],int) and (len(args)==1 or isinstance(args[1],bytes)): return __ev__(getattr(obj,name),*args)
            if name=='zfill' and len(args)==1 and isinstance(args[0],int): return __ev__(obj.zfill,args[0])
            if name in ('partition','rpartition') and len(args)==1 and isinstance(args[0],bytes): return __ev__(getattr(obj,name),args[0])
            if name=='hex' and (not args or len(args)==2 and isinstance(args[0],str) and isinstance(args[1],int)): return __ev__(obj.hex,*args)
            if name=='join' and len(args)==1 and isinstance(args[0],(tuple,list,frozenset)) and all(isinstance(x,bytes) for x in args[0]): return __ev__(obj.join,args[0])
            if name in ('split','rsplit') and len(args)<=2 and all(isinstance(x,(bytes,int)) for x in args) and (len(args)<2 or isinstance(args[1],int)): return __ev__(getattr(obj,name),*args)
            if name=='splitlines' and len(args)<=1 and (not args or isinstance(args[0],bool)): return __ev__(obj.splitlines,*args)
            if name=='decode' and len(args)<=2 and all(isinstance(x,str) for x in args): return __ev__(obj.decode,*args)
        if isinstance(obj,tuple): return __tup__(obj,name,args)
        if isinstance(obj,list): return __lists__(obj,name,args)
        if isinstance(obj,dict): return __dicts__(obj,name,args)
        if isinstance(obj,(set,frozenset)): return __sets__(obj,name,args)
        if isinstance(obj,int):
            if name in ('bit_length','bit_count') and not args: return __ev__(getattr(obj,name))
            if name=='to_bytes' and 1<=len(args)<=3 and isinstance(args[0],int) and 0<=args[0]<=lim and (len(args)<2 or isinstance(args[1],str)) and (len(args)<3 or isinstance(args[2],bool)): return __ev__(obj.to_bytes,*args)
            if name=='as_integer_ratio' and not args: return __ev__(obj.as_integer_ratio)
        if isinstance(obj,float):
            if name in ('hex','is_integer','as_integer_ratio') and not args: return __ev__(getattr(obj,name))
        return False,None
    def __prop__(obj,name):
        if isinstance(obj,(int,float,complex)) and name in ('real','imag'): return __ev__(lambda x,y:getattr(x,y),obj,name)
        if isinstance(obj,int) and name in ('numerator','denominator'): return __ev__(lambda x,y:getattr(x,y),obj,name)
        if isinstance(obj,(int,float,complex)) and name=='conjugate': return __ev__(obj.conjugate)
        return False,None
    def __modv__(head,tail):
        if head=='math' and tail in ('pi','e','tau','inf','nan'): return __ev__(lambda x:getattr(math,x),tail)
        if head=='base64' and tail in ('MAXBINSIZE','MAXLINESIZE'): return __ev__(lambda x:getattr(base64,x),tail)
        if head=='zlib' and tail in ('MAX_WBITS','DEFLATED','DEF_MEM_LEVEL','Z_DEFAULT_COMPRESSION','Z_BEST_COMPRESSION','Z_BEST_SPEED','Z_NO_COMPRESSION'): return __ev__(lambda x:getattr(zlib,x),tail)
        if head=='bz2' and tail in ('__doc__','__name__'): return __ev__(lambda x:getattr(bz2,x),tail)
        if head=='lzma' and tail in ('CHECK_NONE','CHECK_CRC32','CHECK_CRC64','CHECK_SHA256'): return __ev__(lambda x:getattr(lzma,x),tail)
        if head=='lzma' and tail in ('FILTER_LZMA1','FILTER_LZMA2','FILTER_DELTA','FILTER_X86','FILTER_POWERPC'): return __ev__(lambda x:getattr(lzma,x),tail)
        if head=='lzma' and tail in ('FILTER_ARM','FILTER_ARMTHUMB','FILTER_IA64','FILTER_SPARC'): return __ev__(lambda x:getattr(lzma,x),tail)
        if head=='lzma' and tail in ('FORMAT_XZ','FORMAT_ALONE','FORMAT_RAW','FORMAT_AUTO'): return __ev__(lambda x:getattr(lzma,x),tail)
        if head=='lzma' and tail in ('MF_HC3','MF_HC4','MF_BT2','MF_BT3','MF_BT4'): return __ev__(lambda x:getattr(lzma,x),tail)
        if head=='lzma' and tail in ('MODE_FAST','MODE_NORMAL','PRESET_EXTREME'): return __ev__(lambda x:getattr(lzma,x),tail)
        if head=='lzma' and tail in ('FILTER_ARM64','FILTER_RISCV'): return __ev__(lambda x:getattr(lzma,x),tail)
        if head=='lzma' and tail in ('CHECK_ID_MAX','CHECK_UNKNOWN'): return __ev__(lambda x:getattr(lzma,x),tail)
        if head=='zlib' and tail in ('Z_FILTERED','Z_HUFFMAN_ONLY','Z_RLE','Z_FIXED','Z_DEFAULT_STRATEGY'): return __ev__(lambda x:getattr(zlib,x),tail)
        if head=='zlib' and tail in ('Z_NO_FLUSH','Z_SYNC_FLUSH','Z_FULL_FLUSH','Z_FINISH','Z_BLOCK'): return __ev__(lambda x:getattr(zlib,x),tail)
        if head=='hashlib' and tail in ('algorithms_guaranteed',): return __ev__(lambda:tuple(sorted(hashlib.algorithms_guaranteed)))
        if head=='hashlib' and tail in ('algorithms_available',): return __ev__(lambda:tuple(sorted(hashlib.algorithms_available)))
        return False,None
    def __numok__(args):
        return all(isinstance(x,(int,float)) and math.isfinite(x) for x in args)
    def __maths__(tail,args):
        one={'acos','asin','atan','ceil','cos','cosh','degrees','erf','erfc','exp','expm1','fabs','floor','gamma','isfinite','isinf','isnan','lgamma','log1p','radians','sin','sinh','sqrt','tan','tanh','trunc','ulp'}
        two={'atan2','copysign','dist','fmod','hypot','isclose','ldexp','log','nextafter','pow','remainder'}
        if tail in one and len(args)==1 and isinstance(args[0],(int,float)): return __ev__(getattr(math,tail),*args)
        if tail in two and 2<=len(args)<=3 and __numok__(args): return __ev__(getattr(math,tail),*args)
        if tail in ('comb','perm') and 1<=len(args)<=2 and all(isinstance(x,int) and 0<=x<=2048 for x in args): return __ev__(getattr(math,tail),*args)
        if tail in ('factorial','isqrt') and len(args)==1 and isinstance(args[0],int) and 0<=args[0]<=4096: return __ev__(getattr(math,tail),*args)
        if tail in ('gcd','lcm') and len(args)<=16 and all(isinstance(x,int) for x in args): return __ev__(getattr(math,tail),*args)
        if tail=='prod' and 1<=len(args)<=2 and isinstance(args[0],(tuple,list,frozenset)) and len(args[0])<=256 and all(isinstance(x,(int,float,complex)) for x in args[0]) and (len(args)==1 or isinstance(args[1],(int,float,complex))): return __ev__(math.prod,*args)
        if tail=='fsum' and len(args)==1 and isinstance(args[0],(tuple,list,frozenset)) and len(args[0])<=256 and all(isinstance(x,(int,float)) for x in args[0]): return __ev__(math.fsum,args[0])
        return False,None
    def __b64__(tail,args):
        if tail in ('b16encode','b32encode','b64encode','urlsafe_b64encode') and len(args)==1 and isinstance(args[0],bytes): return __ev__(getattr(base64,tail),args[0])
        if tail in ('b16decode','b32decode','b64decode','urlsafe_b64decode') and 1<=len(args)<=2 and isinstance(args[0],(bytes,str)) and (len(args)==1 or isinstance(args[1],bool)): return __ev__(getattr(base64,tail),*args)
        if tail in ('standard_b64encode','encodebytes') and len(args)==1 and isinstance(args[0],bytes): return __ev__(getattr(base64,tail),args[0])
        if tail in ('standard_b64decode','decodebytes') and len(args)==1 and isinstance(args[0],(bytes,str)): return __ev__(getattr(base64,tail),args[0])
        if tail in ('b32hexencode','b32hexdecode') and 1<=len(args)<=2 and isinstance(args[0],(bytes,str)) and (len(args)==1 or isinstance(args[1],bool)): return __ev__(getattr(base64,tail),*args)
        if tail in ('a85encode','b85encode') and 1<=len(args)<=4 and isinstance(args[0],bytes): return __ev__(getattr(base64,tail),*args)
        if tail in ('a85decode','b85decode') and 1<=len(args)<=5 and isinstance(args[0],(bytes,str)): return __ev__(getattr(base64,tail),*args)
        return False,None
    def __zlib__(tail,args):
        if tail in ('crc32','adler32') and 1<=len(args)<=2 and isinstance(args[0],bytes) and (len(args)==1 or isinstance(args[1],int)): return __ev__(getattr(zlib,tail),*args)
        if tail=='compress' and 1<=len(args)<=2 and isinstance(args[0],bytes) and len(args[0])<=lim and (len(args)==1 or isinstance(args[1],int)): return __ev__(zlib.compress,*args)
        if tail=='decompress' and 1<=len(args)<=3 and isinstance(args[0],bytes) and len(args[0])<=lim and all(isinstance(x,int) for x in args[1:]): return __ev__(zlib.decompress,*args)
        return False,None
    def __bz__(tail,args):
        if tail=='compress' and 1<=len(args)<=2 and isinstance(args[0],bytes) and len(args[0])<=lim and (len(args)==1 or isinstance(args[1],int)): return __ev__(bz2.compress,*args)
        if tail=='decompress' and len(args)==1 and isinstance(args[0],bytes) and len(args[0])<=lim: return __ev__(bz2.decompress,args[0])
        return False,None
    def __lz__(tail,args):
        if tail=='compress' and 1<=len(args)<=3 and isinstance(args[0],bytes) and len(args[0])<=lim: return __ev__(lzma.compress,*args)
        if tail=='decompress' and 1<=len(args)<=4 and isinstance(args[0],bytes) and len(args[0])<=lim: return __ev__(lzma.decompress,*args)
        if tail=='is_check_supported' and len(args)==1 and isinstance(args[0],int): return __ev__(lzma.is_check_supported,args[0])
        return False,None
    def __hashnew__(name,args):
        tab={'md5':hashlib.md5,'sha1':hashlib.sha1,'sha224':hashlib.sha224,'sha256':hashlib.sha256,'sha384':hashlib.sha384,'sha512':hashlib.sha512,'blake2b':hashlib.blake2b,'blake2s':hashlib.blake2s}
        if name in tab and len(args)<=1 and (not args or isinstance(args[0],bytes)): return True,tab[name](*args)
        if name=='new' and 1<=len(args)<=2 and isinstance(args[0],str) and (len(args)==1 or isinstance(args[1],bytes)): return __ev__(hashlib.new,*args)
        return False,None
    def __hashc__(n):
        if not isinstance(n.func,ast.Attribute) or not isinstance(n.func.value,ast.Call) or n.args or n.keywords: return False,None
        call=n.func.value
        if call.keywords or not isinstance(call.func,ast.Attribute) or not isinstance(call.func.value,ast.Name) or call.func.value.id!='hashlib': return False,None
        args=[]
        for x in call.args:
            ok,v=__raw__(x)
            if not ok: return False,None
            args.append(v)
        ok,obj=__hashnew__(call.func.attr,args)
        if not ok: return False,None
        if n.func.attr in ('digest','hexdigest'): return __ev__(getattr(obj,n.func.attr))
        return False,None
    def __packk__(head,tail,args,kw):
        if head=='bz2' and tail=='compress' and len(args)==1 and set(kw)<= {'compresslevel'} and isinstance(args[0],bytes) and len(args[0])<=lim and (not kw or isinstance(kw.get('compresslevel'),int)): return __ev__(bz2.compress,*args,**kw)
        if head=='lzma' and tail=='compress' and len(args)==1 and set(kw)<= {'format','check','preset'} and isinstance(args[0],bytes) and len(args[0])<=lim and all(isinstance(x,int) for x in kw.values()): return __ev__(lzma.compress,*args,**kw)
        if head=='lzma' and tail=='decompress' and len(args)==1 and set(kw)<= {'format','memlimit','filters'} and isinstance(args[0],bytes) and len(args[0])<=lim and all(x is None or isinstance(x,int) for x in kw.values()): return __ev__(lzma.decompress,*args,**kw)
        return False,None
    def __uni__(tail,args):
        if tail=='normalize' and len(args)==2 and isinstance(args[0],str) and isinstance(args[1],str): return __ev__(unicodedata.normalize,*args)
        if tail in ('category','bidirectional','combining','east_asian_width','mirrored','decomposition','name') and 1<=len(args)<=2 and isinstance(args[0],str) and len(args[0])==1: return __ev__(getattr(unicodedata,tail),*args)
        if tail=='lookup' and len(args)==1 and isinstance(args[0],str): return __ev__(unicodedata.lookup,args[0])
        if tail=='decimal' and 1<=len(args)<=2 and isinstance(args[0],str) and len(args[0])==1: return __ev__(unicodedata.decimal,*args)
        if tail=='digit' and 1<=len(args)<=2 and isinstance(args[0],str) and len(args[0])==1: return __ev__(unicodedata.digit,*args)
        if tail=='numeric' and 1<=len(args)<=2 and isinstance(args[0],str) and len(args[0])==1: return __ev__(unicodedata.numeric,*args)
        if tail=='is_normalized' and len(args)==2 and isinstance(args[0],str) and isinstance(args[1],str): return __ev__(unicodedata.is_normalized,*args)
        return False,None
    def __json__(tail,args):
        if tail=='dumps' and len(args)==1 and isinstance(args[0],(dict,list,tuple,str,int,float,bool,type(None))): return __ev__(json.dumps,args[0])
        if tail=='loads' and len(args)==1 and isinstance(args[0],(str,bytes,bytearray)) and len(args[0])<=lim: return __ev__(json.loads,args[0])
        return False,None
    def __modu__(head,tail,args):
        if head=='math': return __maths__(tail,args)
        if head=='base64': return __b64__(tail,args)
        if head=='zlib': return __zlib__(tail,args)
        if head=='bz2': return __bz__(tail,args)
        if head=='lzma': return __lz__(tail,args)
        if head=='unicodedata': return __uni__(tail,args)
        if head=='json': return __json__(tail,args)
        if head=='hashlib': return __hashnew__(tail,args)
        return False,None
    def __patv__(p):
        if isinstance(p,ast.MatchValue): return __raw__(p.value)
        if isinstance(p,ast.MatchSingleton): return True,p.value
        if isinstance(p,ast.MatchSequence):
            bag=[]
            for x in p.patterns:
                ok,v=__patv__(x)
                if not ok: return False,None
                bag.append(v)
            return True,tuple(bag)
        return False,None
    def __hitp__(val,p):
        if isinstance(p,ast.MatchAs) and p.name is None and p.pattern is None: return True
        if isinstance(p,ast.MatchOr): return any(__hitp__(val,x) for x in p.patterns)
        ok,got=__patv__(p)
        if ok:
            try: return val==got
            except: return False
        return False
    def __cap__(p):
        if isinstance(p,ast.MatchAs): return p.name is not None or p.pattern is not None and __cap__(p.pattern)
        if isinstance(p,ast.MatchStar): return True
        if isinstance(p,ast.MatchMapping): return bool(p.rest) or any(__cap__(x) for x in p.patterns)
        if isinstance(p,ast.MatchClass): return True
        if isinstance(p,ast.MatchSequence): return any(__cap__(x) for x in p.patterns)
        if isinstance(p,ast.MatchOr): return any(__cap__(x) for x in p.patterns)
        return False
    def __mcase__(n):
        ok,val=__raw__(n.subject)
        if not ok: return None
        for x in n.cases:
            if __cap__(x.pattern): return None
            if __hitp__(val,x.pattern):
                if x.guard is None: return x.body
                go,gv=__truthy__(x.guard)
                if go and gv: return x.body
                if not go: return None
        return []
    bmap={ast.Add:lambda a,b:a+b,ast.Sub:lambda a,b:a-b,ast.Mult:lambda a,b:a*b,ast.Div:lambda a,b:a/b,ast.FloorDiv:lambda a,b:a//b,ast.Mod:lambda a,b:a%b,ast.BitOr:lambda a,b:a|b,ast.BitXor:lambda a,b:a^b,ast.BitAnd:lambda a,b:a&b,ast.LShift:lambda a,b:a<<b if isinstance(b,int) and 0<=b<=64 else (_ for _ in ()).throw(ValueError),ast.RShift:lambda a,b:a>>b if isinstance(b,int) and 0<=b<=64 else (_ for _ in ()).throw(ValueError),ast.Pow:lambda a,b:a**b if not isinstance(b,int) or abs(b)<=32 else (_ for _ in ()).throw(ValueError)}
    umap={ast.UAdd:lambda a:+a,ast.USub:lambda a:-a,ast.Invert:lambda a:~a,ast.Not:lambda a:not a};cmap={ast.Eq:lambda a,b:a==b,ast.NotEq:lambda a,b:a!=b,ast.Lt:lambda a,b:a<b,ast.LtE:lambda a,b:a<=b,ast.Gt:lambda a,b:a>b,ast.GtE:lambda a,b:a>=b,ast.In:lambda a,b:a in b,ast.NotIn:lambda a,b:a not in b,ast.Is:lambda a,b:a is b,ast.IsNot:lambda a,b:a is not b}
    def __go__(n):
        if n is None: return None
        for f,v in ast.iter_fields(n):
            if isinstance(v,list):
                bag=[]
                for x in v:
                    y=__go__(x) if isinstance(x,ast.AST) else x
                    if y is None: continue
                    bag.extend(y) if isinstance(y,list) else bag.append(y)
                setattr(n,f,bag)
            elif isinstance(v,ast.AST):
                y=__go__(v)
                if y is None:
                    try: delattr(n,f)
                    except: pass
                else: setattr(n,f,y)
        if isinstance(n,(ast.Module,ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): n.body=__bod__(n.body);return n
        if isinstance(n,ast.ExceptHandler): n.body=__bod__(n.body);return n
        if hasattr(ast,'match_case') and isinstance(n,ast.match_case): n.body=__bod__(n.body);return n
        if isinstance(n,(ast.Assert,)): return None
        if isinstance(n,ast.If):
            ok,v=__tru__(n.test)
            if ok: return n.body if v else n.orelse
            n.body=__bod__(n.body);n.orelse=__bod__(n.orelse) if n.orelse else []
            if len(n.body)==1 and isinstance(n.body[0],ast.Pass) and n.orelse: n.test=__flip__(n.test);n.body=n.orelse;n.orelse=[];return n
            if len(n.orelse)==1 and isinstance(n.orelse[0],ast.Pass): n.orelse=[];return n
            if len(n.body)==1 and isinstance(n.body[0],ast.Pass) and not n.orelse and __pure__(n.test): return None
            if n.orelse and len(n.body)==len(n.orelse) and all(__same__(a,b) for a,b in zip(n.body,n.orelse)) and __pure__(n.test): return n.body
            return n
        if isinstance(n,ast.While):
            ok,v=__tru__(n.test)
            if ok and not v: return n.orelse
            n.body=__bod__(n.body);n.orelse=__bod__(n.orelse) if n.orelse else [];return n
        if isinstance(n,ast.For):
            if __empty__(n.iter): return n.orelse
            n.body=__bod__(n.body);n.orelse=__bod__(n.orelse) if n.orelse else [];return n
        if isinstance(n,ast.AsyncFor): n.body=__bod__(n.body);n.orelse=__bod__(n.orelse) if n.orelse else [];return n
        if isinstance(n,(ast.With,ast.AsyncWith)): n.body=__bod__(n.body);return n
        if isinstance(n,ast.Try):
            n.body=__bod__(n.body);n.orelse=__bod__(n.orelse) if n.orelse else [];n.finalbody=__bod__(n.finalbody) if n.finalbody else []
            for x in n.handlers: x.body=__bod__(x.body)
            return n
        if isinstance(n,ast.Match):
            got=__mcase__(n)
            if got is not None: return got
            for x in n.cases: x.body=__bod__(x.body)
            return n
        if isinstance(n,ast.IfExp):
            ok,v=__truthy__(n.test);return n.body if ok and v else n.orelse if ok else __tern__(n)
        if isinstance(n,(ast.ListComp,ast.SetComp,ast.DictComp)):
            made=__cgen__(n)
            if made is not None: return made
            pure=all(__pure__(g.iter) for g in n.generators)
            for g in n.generators:
                keep=[]
                for x in g.ifs:
                    ok,v=__truthy__(x)
                    if ok and not v:
                        if pure: return __voids__(n)
                        keep.append(x)
                    if not ok: keep.append(x)
                g.ifs=keep
            if n.generators and __empty__(n.generators[0].iter): return __voids__(n)
        if isinstance(n,ast.UnaryOp):
            if isinstance(n.op,ast.Not) and isinstance(n.operand,ast.UnaryOp) and isinstance(n.operand.op,ast.Not): return ast.copy_location(ast.Call(func=ast.Name(id='bool',ctx=ast.Load()),args=[n.operand.operand],keywords=[]),n)
            if isinstance(n.op,ast.Not):
                got=__deny__(n.operand)
                if got is not None: return got
            ok,v=__sim__(n.operand);fn=umap.get(type(n.op));done,out=__ev__(fn,v) if ok and fn else (False,None);return __mk__(out,n) if done else n
        if isinstance(n,ast.BinOp):
            lo,l=__sim__(n.left);ro,r=__sim__(n.right);fn=bmap.get(type(n.op));done,out=__ev__(fn,l,r) if lo and ro and fn else (False,None);return __mk__(out,n) if done else __alg__(n)
        if isinstance(n,ast.BoolOp):
            got=__boolop__(n)
            if got is not n: return got
            vals=[]
            for x in n.values:
                ok,v=__raw__(x)
                if not ok: return n
                vals.append(v)
            if isinstance(n.op,ast.And):
                out=vals[-1] if vals else True
                for x in vals:
                    if not x: out=x;break
                return __mk__(out,n)
            if isinstance(n.op,ast.Or):
                out=vals[-1] if vals else False
                for x in vals:
                    if x: out=x;break
                return __mk__(out,n)
        if isinstance(n,ast.Compare):
            got=__judge__(n)
            if got is not n: return got
            ok,cur=__raw__(n.left)
            if not ok: return n
            for op,x in zip(n.ops,n.comparators):
                ro,r=__raw__(x);fn=cmap.get(type(op));done,out=__ev__(fn,cur,r) if ro and fn else (False,None)
                if not done: return n
                if not out: return __mk__(False,n)
                cur=r
            return __mk__(True,n)
        if isinstance(n,ast.JoinedStr):
            ok,v=__say__(n);return __mk__(v,n) if ok else n
        if isinstance(n,ast.FormattedValue):
            ok,v=__say__(ast.JoinedStr(values=[n]));return __mk__(v,n) if ok else n
        if isinstance(n,ast.Name) and isinstance(n.ctx,ast.Load) and n.id=='__debug__': return ast.copy_location(ast.Constant(False),n)
        if isinstance(n,ast.Attribute) and isinstance(n.ctx,ast.Load):
            done,out=__typeattr__(n.value,n.attr)
            if done: return __done__(out,n)
            if isinstance(n.value,ast.Name):
                done,out=__modv__(n.value.id,n.attr)
                if done: return __done__(out,n)
            ok,obj=__raw__(n.value)
            if ok:
                done,out=__prop__(obj,n.attr)
                return __mk__(out,n) if done else n
        if isinstance(n,ast.Subscript):
            lo,l=__raw__(n.value);ro,r=__raw__(n.slice)
            if lo and ro:
                done,out=__ev__(lambda a,b:a[b],l,r)
                if done: return __done__(out,n)
            so,s=__slc__(n.slice)
            if lo and so:
                done,out=__ev__(lambda x,y:x[y],l,s)
                if done: return __done__(out,n)
        if isinstance(n,ast.Call) and not n.keywords:
            if isinstance(n.func,ast.Attribute) and n.func.attr=='join' and len(n.args)==1:
                ok,obj=__raw__(n.func.value)
                if ok and isinstance(obj,(str,bytes)):
                    done,out=__stream__(n.args[0],list)
                    if done and isinstance(out,list) and all(isinstance(x,type(obj)) for x in out): return __done__(obj.join(out),n)
            if isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=='dict' and n.func.attr=='fromkeys':
                done,out=__born__(n,[])
                if done: return __done__(out,n)
            if isinstance(n.func,ast.Name) and n.func.id in ('len','bool') and len(n.args)==1:
                got=__tally__(n.args[0])
                if got is not None: return __mk__(got if n.func.id=='len' else bool(got),n)
            if isinstance(n.func,ast.Name) and len(n.args)==1:
                done,out=__jag__(n.args[0])
                if done:
                    done,out=__safe__(n.func.id,[out])
                    if done: return __done__(out,n)
                done,out=__stream__(n.args[0],tuple)
                if done:
                    done,out=__safe__(n.func.id,[out])
                    if done: return __done__(out,n)
            if isinstance(n.func,ast.Name) and n.func.id in ('list','set','dict','tuple') and len(n.args)==1:
                cast=__morph__(n,[])
                if cast is not None: return cast
                done,out=__born__(n,[])
                if done: return __done__(out,n)
            args=[]
            for x in n.args:
                ok,v=__raw__(x)
                if not ok: return n
                args.append(v)
            got=__lam__(n,args)
            if got is not None: return got
            cast=__morph__(n,args)
            if cast is not None: return cast
            done,out=__isa__(n,args)
            if done: return __done__(out,n)
            done,out=__born__(n,args)
            if done: return __done__(out,n)
            if isinstance(n.func,ast.Name):
                done,out=__safe__(n.func.id,args)
                return __done__(out,n) if done else n
            if isinstance(n.func,ast.Attribute):
                if isinstance(n.func.value,ast.Name):
                    done,out=__modu__(n.func.value.id,n.func.attr,args)
                    if done: return __done__(out,n)
                done,out=__hashc__(n)
                if done: return __done__(out,n)
                ok,obj=__raw__(n.func.value)
                if ok:
                    done,out=__meth__(obj,n.func.attr,args)
                    return __done__(out,n) if done else n
        if isinstance(n,ast.Call) and n.keywords:
            args=[]
            for x in n.args:
                ok,v=__raw__(x)
                if not ok: return n
                args.append(v)
            ko,kw=__kwarg__(n)
            if not ko: return n
            if isinstance(n.func,ast.Name):
                done,out=__safek__(n.func.id,args,kw)
                return __done__(out,n) if done else n
            if isinstance(n.func,ast.Attribute):
                if isinstance(n.func.value,ast.Name):
                    done,out=__modk__(n.func.value.id,n.func.attr,args,kw)
                    if done: return __done__(out,n)
                ok,obj=__raw__(n.func.value)
                if ok:
                    done,out=__methk__(obj,n.func.attr,args,kw)
                    return __done__(out,n) if done else n
        return n
    tree=__typec__(__go__(tree));ast.fix_missing_locations(tree);return tree
def __vein__(code):
    tree = ast.parse(code)
    tree = __pare__(tree)
    seed = hashlib.sha256(code.encode('utf-8')).digest()
    plain = []
    seen = {}
    dust = {'__import__','abs','all','any','ascii','aiter','anext','bin','breakpoint','callable','chr','classmethod','compile','delattr','dir','divmod','eval','exec','format','getattr','globals','hasattr','hash','hex','id','input','isinstance','issubclass','iter','len','locals','max','memoryview','min','next','oct','open','ord','pow','print','property','repr','round','setattr','slice','sorted','staticmethod','sum','vars','bool','bytearray','bytes','complex','dict','enumerate','filter','float','frozenset','int','list','map','object','range','reversed','set','str','super','tuple','type','zip','Ellipsis','NotImplemented'}
    dust.update({'BaseException','BaseExceptionGroup','Exception','ExceptionGroup','ArithmeticError','BufferError','LookupError','AssertionError','AttributeError','EOFError','FloatingPointError','GeneratorExit','ImportError','ModuleNotFoundError','IndexError','KeyError','KeyboardInterrupt','MemoryError','NameError','NotImplementedError','OSError','OverflowError','RecursionError','ReferenceError','RuntimeError','StopAsyncIteration','StopIteration','SyntaxError','IndentationError','TabError','SystemError','SystemExit','TypeError','UnboundLocalError','UnicodeError','UnicodeEncodeError','UnicodeDecodeError','UnicodeTranslateError','ValueError','ZeroDivisionError','BlockingIOError','ChildProcessError','ConnectionError','BrokenPipeError','ConnectionAbortedError','ConnectionRefusedError','ConnectionResetError','FileExistsError','FileNotFoundError','InterruptedError','IsADirectoryError','NotADirectoryError','PermissionError','ProcessLookupError','TimeoutError','Warning','UserWarning','DeprecationWarning','PendingDeprecationWarning','SyntaxWarning','RuntimeWarning','FutureWarning','ImportWarning','UnicodeWarning','BytesWarning','ResourceWarning'})
    ward = {'__name__','__file__','__package__','__spec__','__loader__','__builtins__','__doc__','__annotations__','__cached__','__path__','__slots__','__class__'}
    def __gather__(root):
        seen = set()
        bind = set()
        frost = set()
        for node in ast.walk(root):
            if isinstance(node, ast.Name):
                seen.add(node.id)
                if isinstance(node.ctx, (ast.Store, ast.Del)):
                    bind.add(node.id)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                seen.add(node.name)
                bind.add(node.name)
            elif isinstance(node, ast.arg):
                seen.add(node.arg)
                bind.add(node.arg)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.asname or alias.name.split('.')[0]
                    seen.add(name); bind.add(name); frost.add(name)
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == '*':
                        continue
                    name = alias.asname or alias.name
                    seen.add(name); bind.add(name); frost.add(name)
            elif isinstance(node, ast.ExceptHandler) and node.name:
                seen.add(node.name)
                bind.add(node.name)
        return seen, bind, frost
    used, bind, frost = __gather__(tree)
    mint = [0]
    gear = {}
    room = [0]
    wall = [0]
    lock = []
    def __token__(name):
        if not isinstance(name, str) or not name:
            return False
        if name in dust or name in ward or name in frost:
            return False
        if name.startswith('__') and name.endswith('__'):
            return False
        if not name.isidentifier() or __import__('keyword').iskeyword(name):
            return False
        return True
    def __pick__(name):
        if name not in gear:
            fog = name.encode('utf-8', 'ignore') or b'x'
            gear[name] = __mint__(used, seed + fog + len(gear).to_bytes(4, 'little'), mint); used.add(gear[name])
        return gear[name]
    def __lock__(args):
        bag = set()
        for one in args.posonlyargs + args.args + args.kwonlyargs:
            one.arg and bag.add(one.arg)
        args.vararg and args.vararg.arg and bag.add(args.vararg.arg)
        args.kwarg and args.kwarg.arg and bag.add(args.kwarg.arg)
        return bag
    def __held__(name):
        for row in reversed(lock):
            if name in row:
                return True
        return False
    blob, keep, load, proof, tint, rune, dawn, dusk, kiln, loom, reef, wave, mire, sootf, brimf, crustf, ashf, flaref, cask, spinef, huskf, barkf, pearlf, mazef, cordf, pathf, lockf, rayf, beadf, combf, silkf, knotf, amberf, glazef, sentryf, veilf, nockf, snagf, wardf, chafff, opbox, biobox, bookf, evalf, boolf, strf, typef, intf, bytesf, varsf, callf, listf, mapf, impf, bytef, lenf, inputf, joinf, hexf, globf = [__mint__(used, seed, mint) for slot in range(60)]
    tick = [0]
    gate = [0]
    lam = [0]
    bend = 257 + int.from_bytes(seed[8:12], 'little')
    mask = int.from_bytes(seed[12:16], 'little') | 1
    crisp = 1009 + int.from_bytes(seed[16:20], 'little')
    wide = 0x110000 + int.from_bytes(hashlib.blake2b(seed + b'wide', digest_size=12).digest(), 'little')
    def __pval__(node):
        if isinstance(node, ast.Attribute):
            node.value = __pval__(node.value)
            return node
        if isinstance(node, ast.Name):
            if not __held__(node.id) and __token__(node.id):
                node.id = __pick__(node.id)
            return node
        return node
    def __patt__(node):
        if isinstance(node, ast.MatchValue):
            node.value = __pval__(node.value)
            return node
        if isinstance(node, ast.MatchSingleton):
            return node
        if isinstance(node, ast.MatchStar):
            if node.name and __token__(node.name):
                node.name = __pick__(node.name)
            return node
        if isinstance(node, ast.MatchAs):
            if node.pattern is not None:
                node.pattern = __patt__(node.pattern)
            if node.name and __token__(node.name):
                node.name = __pick__(node.name)
            return node
        if isinstance(node, ast.MatchMapping):
            node.patterns = [__patt__(one) for one in node.patterns]
            if node.rest and __token__(node.rest):
                node.rest = __pick__(node.rest)
            return node
        if isinstance(node, ast.MatchClass):
            node.cls = __pval__(node.cls)
            node.patterns = [__patt__(one) for one in node.patterns]
            node.kwd_patterns = [__patt__(one) for one in node.kwd_patterns]
            return node
        if isinstance(node, ast.MatchSequence):
            node.patterns = [__patt__(one) for one in node.patterns]
            return node
        if isinstance(node, ast.MatchOr):
            node.patterns = [__patt__(one) for one in node.patterns]
            return node
        return node
    def __cast__(node, kind, skip):
        for field, value in ast.iter_fields(node):
            if field in skip:
                continue
            if field == 'pattern' and isinstance(value, ast.AST):
                setattr(node, field, __patt__(value) if kind == 'shape' else value)
                continue
            if isinstance(value, list):
                bag = []
                for item in value:
                    if isinstance(item, ast.AST):
                        item = __shape__(item) if kind == 'shape' else __gem__(item)
                        if item is None:
                            continue
                        if isinstance(item, list):
                            bag.extend(item)
                        else:
                            bag.append(item)
                    else:
                        bag.append(item)
                setattr(node, field, bag)
            elif isinstance(value, ast.AST):
                item = __shape__(value) if kind == 'shape' else __gem__(value)
                if item is None:
                    try:
                        delattr(node, field)
                    except:
                        pass
                else:
                    setattr(node, field, item)
        return node
    def __seam__():
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        glass = __mint__(used, seed, mint)
        tick[0] += 1
        left = __spark__(seed + b'seam' + tick[0].to_bytes(4, 'little'), 10**6, 10**9)
        right = __spark__(seed + b'seam2' + tick[0].to_bytes(4, 'little'), 10**6, 10**9)
        while left == right:
            right = __spark__(seed + b'seam3' + tick[0].to_bytes(4, 'little') + right.to_bytes(4, 'little'), 10**6, 10**9)
        third = __spark__(seed + b'seam4' + tick[0].to_bytes(4, 'little'), 10**6, 10**9)
        body1 = [ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(left)), ast.Pass()]
        body2 = [ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Constant(right)), ast.Pass()]
        body3 = [ast.Assign(targets=[ast.Name(id=glass, ctx=ast.Store())], value=ast.Constant(third)), ast.Pass()]
        test1 = ast.Compare(left=ast.Constant(left), ops=[ast.Eq()], comparators=[ast.Constant(right)])
        test2 = ast.Compare(left=ast.Constant(right), ops=[ast.Lt()], comparators=[ast.Constant(0)])
        return ast.If(test=test1, body=body1, orelse=[ast.If(test=test2, body=body2, orelse=body3)])
    def __ledge__(body):
        if not body:
            return body
        tick[0] += 1
        trap = __mint__(used, seed, mint)
        flag = __mint__(used, seed, mint)
        err = __mint__(used, seed, mint)
        rock = __spark__(seed + b'ledge' + tick[0].to_bytes(4, 'little'), 1, 999)
        init = ast.Assign(targets=[ast.Name(id=flag, ctx=ast.Store())], value=ast.Constant(rock))
        bump = ast.AugAssign(target=ast.Name(id=flag, ctx=ast.Store()), op=ast.Add(), value=ast.Constant(1))
        raiser = ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[ast.Name(id=flag, ctx=ast.Load())], keywords=[]))
        real = []
        junk = []
        for slot, one in enumerate(body):
            cond = ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=err, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(rock + 1)])
            real.append(ast.If(test=cond, body=[one], orelse=[]))
            tick[0] += 1
            fake = __spark__(seed + b'ledgejunk' + tick[0].to_bytes(4, 'little'), 10**5, 10**8)
            jcond = ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=err, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(fake)])
            junk.append(ast.If(test=jcond, body=[ast.Assign(targets=[ast.Name(id=trap, ctx=ast.Store())], value=ast.Constant(fake))], orelse=[]))
        handler = ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name=err, body=real + junk)
        wrap = ast.Try(body=[bump, raiser], handlers=[handler], orelse=[], finalbody=[])
        return [init, wrap]
    def __vault__(tag):
        tick[0] += 1
        left = __spark__(seed + b'vaulta' + tag + tick[0].to_bytes(4, 'little'), 10**6, 10**9)
        right = __spark__(seed + b'vaultb' + tag + tick[0].to_bytes(4, 'little'), 10**6, 10**9)
        return left, right, left ^ right
    def __crash__():
        return ast.Subscript(value=ast.Tuple(elts=[], ctx=ast.Load()), slice=ast.Constant(0), ctx=ast.Load())
    def __guard__(left, right, mark):
        return ast.Compare(left=ast.BinOp(left=ast.Name(id=left, ctx=ast.Load()), op=ast.BitXor(), right=ast.Name(id=right, ctx=ast.Load())), ops=[ast.Eq()], comparators=[ast.Name(id=mark, ctx=ast.Load())])
    def __lambda__(body, args, vals, tag, vararg=None, kwarg=None, keys=None):
        left, right, mark = __mint__(used, seed, mint), __mint__(used, seed, mint), __mint__(used, seed, mint)
        a, b, c = __vault__(tag)
        rows = [ast.arg(arg=one) for one in args]
        rows.extend((ast.arg(arg=left), ast.arg(arg=right), ast.arg(arg=mark)))
        lock = [ast.Constant(a), ast.Constant(b), ast.Constant(c)]
        call = lock + list(vals) if (vararg or kwarg) and not args else list(vals) + lock
        body = ast.IfExp(test=__guard__(left, right, mark), body=body, orelse=__crash__())
        return ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=rows, vararg=ast.arg(arg=vararg) if vararg else None, kwonlyargs=[], kw_defaults=[], kwarg=ast.arg(arg=kwarg) if kwarg else None, defaults=[]), body=body), args=call, keywords=keys or [])
    def __rim__(node, raw):
        return ast.Subscript(value=ast.Tuple(elts=[node], ctx=ast.Load()), slice=ast.BinOp(left=ast.Constant(raw), op=ast.BitXor(), right=ast.Constant(raw)), ctx=ast.Load())
    def __carry__(node, tag):
        name = __mint__(used, seed, mint)
        return __lambda__(ast.Name(id=name, ctx=ast.Load()), [name], [node], tag)
    def __gorge__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        rock = __spark__(seed + b'gorge' + tick[0].to_bytes(4, 'little'), 10**4, 10**7)
        nest = __carry__(ast.Constant(rock), b'gorge')
        for _ in range(__spark__(seed + b'gorgedepth' + tick[0].to_bytes(4, 'little'), 2, 5)):
            nest = __carry__(nest, b'gorgeloop')
        return ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=nest)
    def __ridge__(body):
        if not body:
            return body
        tick[0] += 1
        pick = __spark__(seed + b'ridge' + tick[0].to_bytes(4, 'little'), 0, len(body) - 1)
        node = body[pick]
        if isinstance(node, (ast.Global, ast.Nonlocal, ast.Import, ast.ImportFrom, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            return body
        flag = __mint__(used, seed, mint)
        init = ast.Assign(targets=[ast.Name(id=flag, ctx=ast.Store())], value=ast.Constant(True))
        test = ast.Name(id=flag, ctx=ast.Load())
        flip = ast.Assign(targets=[ast.Name(id=flag, ctx=ast.Store())], value=ast.Constant(False))
        loop = ast.While(test=test, body=[node, flip, ast.Break()], orelse=[])
        body[pick] = loop
        body.insert(pick, init)
        return body
    def __mesa__(node):
        if not isinstance(node, ast.Call) or not node.keywords:
            return node
        bag = []
        for kw in node.keywords:
            if kw.arg is not None:
                bag.append(ast.keyword(arg=None, value=ast.Dict(keys=[ast.Constant(kw.arg)], values=[kw.value])))
            else:
                bag.append(kw)
        node.keywords = bag
        return node
    def __knoll__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        rock = __spark__(seed + b'knoll' + tick[0].to_bytes(4, 'little'), 10**5, 10**8)
        utext = ''.join(chr(__spark__(seed + b'knollu' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x4e00, 0x9fff)) for s in range(6))
        return ast.For(target=ast.Name(id=slag, ctx=ast.Store()), iter=ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[ast.Constant(0)], keywords=[]), body=[ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Constant(utext)), ast.Expr(value=ast.Constant(rock))], orelse=[])
    def __dale__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        rock = __spark__(seed + b'dale' + tick[0].to_bytes(4, 'little'), 10**6, 10**9)
        utext = ''.join(chr(__spark__(seed + b'daleu' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x3041, 0x30fa)) for s in range(10))
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assert(test=ast.Constant(False), msg=ast.Constant(utext)), ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(rock))], orelse=[])
    def __scree__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        rock = __spark__(seed + b'scree' + tick[0].to_bytes(4, 'little'), 10**4, 10**7)
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(rock)), ast.AugAssign(target=ast.Name(id=slag, ctx=ast.Store()), op=ast.Add(), value=ast.Constant(0)), ast.AugAssign(target=ast.Name(id=slag, ctx=ast.Store()), op=ast.Mult(), value=ast.Constant(1))], orelse=[])
    def __cliff__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        glass = __mint__(used, seed, mint)
        utext = ''.join(chr(__spark__(seed + b'cliffu' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0xac00, 0xd7a3)) for s in range(5))
        rock = __spark__(seed + b'cliff' + tick[0].to_bytes(4, 'little'), 10**5, 10**8)
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.ClassDef(name=slag, bases=[], keywords=[], body=[ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Constant(utext)), ast.Assign(targets=[ast.Name(id=glass, ctx=ast.Store())], value=ast.Constant(rock))], decorator_list=[])], orelse=[])
    def __reef__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        utext = ''.join(chr(__spark__(seed + b'reefu' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x0400, 0x04ff)) for s in range(7))
        return ast.While(test=ast.Constant(False), body=[ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(utext)), ast.Expr(value=ast.Call(func=ast.Name(id='len', ctx=ast.Load()), args=[ast.Name(id=slag, ctx=ast.Load())], keywords=[]))], orelse=[])
    def __dune__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        rock = __spark__(seed + b'dune' + tick[0].to_bytes(4, 'little'), 10**6, 10**9)
        utext = ''.join(chr(__spark__(seed + b'duneu' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x1200, 0x137f)) for s in range(8))
        inner = ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(utext))
        outer = ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Constant(rock))
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Try(body=[inner], handlers=[], orelse=[], finalbody=[outer])], orelse=[])
    def __fjord__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        moss = __mint__(used, seed, mint)
        left = ''.join(chr(__spark__(seed + b'fjordl' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x1780, 0x17ff)) for s in range(7))
        right = ''.join(chr(__spark__(seed + b'fjordr' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0xa500, 0xa63f)) for s in range(7))
        body = [ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(left)), ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Constant(right))]
        hand = ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name=moss, body=[ast.Expr(value=ast.Call(func=ast.Name(id='str', ctx=ast.Load()), args=[ast.Name(id=moss, ctx=ast.Load())], keywords=[]))])
        return ast.If(test=ast.Constant(False), body=[ast.Try(body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[ast.Constant(left)], keywords=[]), cause=None)], handlers=[hand], orelse=body, finalbody=[])], orelse=[])
    def __karst__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        gem = __spark__(seed + b'karst' + tick[0].to_bytes(4, 'little'), 10**6, 10**9)
        ash = ''.join(chr(__spark__(seed + b'karstu' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x1e00, 0x1eff)) for s in range(9))
        call = ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=slag)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=ast.IfExp(test=ast.Compare(left=ast.Name(id=slag, ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(gem)]), body=ast.Constant(ash), orelse=ast.Constant(gem))), args=[ast.Constant(gem + 1)], keywords=[])
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=call)], orelse=[])
    def __moraine__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        raw = tuple(__spark__(seed + b'moraine' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 1000, 9999) for s in range(4))
        seq = ast.Tuple(elts=[ast.Constant(one) for one in raw], ctx=ast.Load())
        body = [ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Call(func=ast.Name(id='sum', ctx=ast.Load()), args=[ast.Name(id=slag, ctx=ast.Load())], keywords=[]))]
        return ast.If(test=ast.Constant(False), body=[ast.For(target=ast.Name(id=slag, ctx=ast.Store()), iter=ast.Tuple(elts=[seq], ctx=ast.Load()), body=body, orelse=[ast.Pass()])], orelse=[])
    def __talus__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        raw = ''.join(chr(__spark__(seed + b'talus' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0xaa00, 0xaa5f)) for s in range(8))
        test = ast.BoolOp(op=ast.And(), values=[ast.Compare(left=ast.Constant(1), ops=[ast.Eq()], comparators=[ast.Constant(2)]), ast.Call(func=ast.Name(id='all', ctx=ast.Load()), args=[ast.List(elts=[ast.Constant(False), ast.Constant(True)], ctx=ast.Load())], keywords=[])])
        return ast.If(test=test, body=[ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(raw)), ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Call(func=ast.Name(id='len', ctx=ast.Load()), args=[ast.Name(id=slag, ctx=ast.Load())], keywords=[]))], orelse=[])
    def __cairn__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        utext = ''.join(chr(__spark__(seed + b'cairnu' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x0e00, 0x0e7f)) for s in range(6))
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(utext)), ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Call(func=ast.Name(id='type', ctx=ast.Load()), args=[ast.Constant(None)], keywords=[]))], orelse=[])
    def __delta__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        left = ''.join(chr(__spark__(seed + b'deltal' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x4e00, 0x9fff)) for s in range(4))
        right = ''.join(chr(__spark__(seed + b'deltar' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x3041, 0x30fa)) for s in range(4))
        case = ast.match_case(pattern=ast.MatchSequence(patterns=[ast.MatchAs(name=None)]), guard=None, body=[ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(__spark__(seed + b'deltav' + tick[0].to_bytes(4, 'little'), 10**5, 10**8)))])
        last = ast.match_case(pattern=ast.MatchAs(name=None), guard=None, body=[ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Constant(left))])
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Match(subject=ast.List(elts=[ast.Constant(right)], ctx=ast.Load()), cases=[case, last])], orelse=[])
    def __cinder__():
        tick[0] += 1
        bag = []
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        glass = __mint__(used, seed, mint)
        rock = __spark__(seed + b'junk' + tick[0].to_bytes(4, 'little'), 10**7, 10**9)
        text = ['obsidian', 'glass', 'ash', 'vein'][__spark__(seed + b'text' + tick[0].to_bytes(4, 'little'), 0, 3)]
        bag.append(ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(rock)), ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Constant(text)), ast.Assign(targets=[ast.Name(id=glass, ctx=ast.Store())], value=ast.Tuple(elts=[ast.Name(id=slag, ctx=ast.Load()), ast.Name(id=coal, ctx=ast.Load())], ctx=ast.Load())), ast.Expr(value=ast.Call(func=ast.Name(id='str', ctx=ast.Load()), args=[ast.Name(id=glass, ctx=ast.Load())], keywords=[]))], orelse=[ast.Pass()]))
        bag.append(__seam__())
        bag.append(__gorge__())
        slag2 = __mint__(used, seed, mint)
        coal2 = __mint__(used, seed, mint)
        rock2 = __spark__(seed + b'ujunk' + tick[0].to_bytes(4, 'little'), 0x4e00, 0x9fff)
        utext = ''.join(chr(__spark__(seed + b'uchar' + tick[0].to_bytes(4, 'little') + slot.to_bytes(2, 'little'), 0x4e00, 0x9fff)) for slot in range(8))
        bag.append(ast.If(test=ast.Compare(left=ast.Constant(rock2), ops=[ast.Lt()], comparators=[ast.Constant(0)]), body=[ast.Assign(targets=[ast.Name(id=slag2, ctx=ast.Store())], value=ast.Constant(utext)), ast.Assign(targets=[ast.Name(id=coal2, ctx=ast.Store())], value=ast.Name(id=slag2, ctx=ast.Load())), ast.Expr(value=ast.Call(func=ast.Name(id='len', ctx=ast.Load()), args=[ast.Name(id=coal2, ctx=ast.Load())], keywords=[]))], orelse=[ast.Pass()]))
        bag.append(__knoll__())
        bag.append(__dale__())
        bag.append(__scree__())
        bag.append(__cliff__())
        bag.append(__reef__())
        bag.append(__dune__())
        bag.append(__fjord__())
        bag.append(__karst__())
        bag.append(__moraine__())
        bag.append(__talus__())
        bag.append(__cairn__())
        bag.append(__delta__())
        if ((seed[26] + tick[0]) & 1) == 0:
            slag6 = __mint__(used, seed, mint); coal6 = __mint__(used, seed, mint); glass6 = __mint__(used, seed, mint)
            grit6 = ''.join(chr(__spark__(seed + b'antiu' + tick[0].to_bytes(4, 'little') + slot.to_bytes(2, 'little'), 0xac00, 0xd7a3)) for slot in range(6))
            mist6 = ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=slag6)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=ast.Call(func=ast.Attribute(value=ast.Constant(''), attr='join', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='map', ctx=ast.Load()), args=[ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=coal6)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=ast.Call(func=ast.Attribute(value=ast.Constant('{}'), attr='format', ctx=ast.Load()), args=[ast.BinOp(left=ast.Name(id=coal6, ctx=ast.Load()), op=ast.BitXor(), right=ast.Constant(64))], keywords=[])), ast.Name(id=slag6, ctx=ast.Load())], keywords=[])], keywords=[])), args=[ast.Tuple(elts=[ast.Constant(ord(one) ^ 64) for one in grit6], ctx=ast.Load())], keywords=[])
            bag.append(ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=glass6, ctx=ast.Store())], value=mist6)], orelse=[]))
        else:
            slag7 = __mint__(used, seed, mint); coal7 = __mint__(used, seed, mint)
            gem7 = ''.join(chr(__spark__(seed + b'chain' + tick[0].to_bytes(4, 'little') + slot.to_bytes(2, 'little'), 0x0400, 0x04ff)) for slot in range(5))
            mist7 = ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=slag7)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=ast.Name(id=slag7, ctx=ast.Load()))
            chain7 = ast.Call(func=mist7, args=[ast.Call(func=mist7, args=[ast.Call(func=mist7, args=[ast.Constant(gem7)], keywords=[])], keywords=[])], keywords=[])
            bag.append(ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=coal7, ctx=ast.Store())], value=chain7)], orelse=[]))
        tick[0] += 1
        rubbles = __rubble__(seed + tick[0].to_bytes(4, 'little'), 3)
        pebbles = __pebble__(seed + tick[0].to_bytes(4, 'little'), 2, 6)
        cobbled = __cobble__(rubbles[0], seed + tick[0].to_bytes(4, 'little'), 2)
        slag3 = __mint__(used, seed, mint)
        coal3 = __mint__(used, seed, mint)
        bag.append(ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Tuple(elts=[ast.Name(id=slag3, ctx=ast.Store()), ast.Name(id=coal3, ctx=ast.Store())], ctx=ast.Store())], value=ast.Tuple(elts=[ast.Constant(rubbles[1]), ast.Constant(pebbles[0])], ctx=ast.Load()))], orelse=[]))
        slag4 = __mint__(used, seed, mint)
        bag.append(ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Try(body=[ast.Assign(targets=[ast.Name(id=slag4, ctx=ast.Store())], value=ast.Constant(rubbles[2]))], handlers=[ast.ExceptHandler(type=None, name=None, body=[ast.Pass()])], orelse=[], finalbody=[])], orelse=[]))
        names = __basalt__(seed + tick[0].to_bytes(4, 'little'), 2, used)
        kiln = __kiln__(seed + tick[0].to_bytes(4, 'little'), 2, 3)
        batch = __batch__([names[0], names[1]], seed)
        bag.append(ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=names[0], ctx=ast.Store())], value=ast.Constant(str(kiln))), ast.Assign(targets=[ast.Name(id=names[1], ctx=ast.Store())], value=ast.Constant(str(batch)))], orelse=[]))
        slag5 = __mint__(used, seed, mint)
        bag.append(ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.If(test=ast.Constant(False), body=[ast.Assign(targets=[ast.Name(id=slag5, ctx=ast.Store())], value=ast.Constant(cobbled))], orelse=[ast.Assign(targets=[ast.Name(id=slag5, ctx=ast.Store())], value=ast.Constant(pebbles[1]))])], orelse=[]))
        return bag
    def __smoke__(body):
        bag = []
        done = 0
        for one in body:
            if done < 4 and not isinstance(one, (ast.Global, ast.Nonlocal, ast.Break, ast.Continue, ast.Import, ast.ImportFrom, ast.Assign, ast.AnnAssign, ast.AugAssign, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                tag = __mint__(used, seed, mint)
                flag = __mint__(used, seed, mint)
                flip = ast.Assign(targets=[ast.Name(id=flag, ctx=ast.Store())], value=ast.Constant(False))
                work = ast.Try(body=[one], handlers=[], orelse=[], finalbody=[flip])
                work = ast.While(test=ast.Name(id=flag, ctx=ast.Load()), body=[work, ast.Break()], orelse=[])
                work = ast.Try(body=[ast.Expr(value=ast.Call(func=ast.Name(id='bool', ctx=ast.Load()), args=[ast.Constant(True)], keywords=[]))], handlers=[ast.ExceptHandler(type=ast.Name(id='Exception', ctx=ast.Load()), name=None, body=[ast.Pass()])], orelse=[work], finalbody=[ast.Expr(value=ast.Constant(None))])
                work = ast.Try(body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[ast.Constant(done)], keywords=[]), cause=None)], handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name=tag, body=[work])], orelse=[], finalbody=[])
                work = ast.Try(body=[ast.Expr(value=ast.Call(func=ast.Name(id='type', ctx=ast.Load()), args=[ast.Constant(None)], keywords=[]))], handlers=[], orelse=[], finalbody=[work])
                work = ast.Try(body=[ast.Expr(value=ast.BinOp(left=ast.Constant(1), op=ast.Mod(), right=ast.Constant(1)))], handlers=[ast.ExceptHandler(type=None, name=None, body=[ast.Pass()])], orelse=[work], finalbody=[])
                work = ast.Try(body=[ast.Expr(value=ast.BinOp(left=ast.Constant(1), op=ast.Div(), right=ast.Constant(0)))], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()), name=None, body=[work])], orelse=[], finalbody=[])
                bag.append(ast.Assign(targets=[ast.Name(id=flag, ctx=ast.Store())], value=ast.Constant(True)))
                bag.append(work)
                done += 1
            else:
                bag.append(one)
        return bag
    def __gloom__(node):
        if node is None:
            return node
        for one in ast.walk(node):
            if isinstance(one, (ast.Await, ast.Yield, ast.YieldFrom)):
                return node
        lam[0] += 1
        if lam[0] & 1:
            return node
        node = __carry__(node, b'gloom')
        return node
    def __anvil__(op):
        if isinstance(op, ast.Add):
            return ast.Add()
        if isinstance(op, ast.Sub):
            return ast.Sub()
        if isinstance(op, ast.Mult):
            return ast.Mult()
        if isinstance(op, ast.Div):
            return ast.Div()
        if isinstance(op, ast.FloorDiv):
            return ast.FloorDiv()
        if isinstance(op, ast.Mod):
            return ast.Mod()
        if isinstance(op, ast.Pow):
            return ast.Pow()
        if isinstance(op, ast.LShift):
            return ast.LShift()
        if isinstance(op, ast.RShift):
            return ast.RShift()
        if isinstance(op, ast.BitOr):
            return ast.BitOr()
        if isinstance(op, ast.BitXor):
            return ast.BitXor()
        if isinstance(op, ast.BitAnd):
            return ast.BitAnd()
        if isinstance(op, ast.MatMult):
            return ast.MatMult()
        return None
    def __latch__(node):
        vals = list(node.values)
        if not vals:
            return ast.Constant(True)
        out = vals[0]
        if isinstance(node.op, ast.And):
            for one in vals[1:]:
                name = __mint__(used, seed + b'and' + len(vals).to_bytes(2, 'little'), mint)
                out = __lambda__(ast.IfExp(test=ast.Name(id=name, ctx=ast.Load()), body=one, orelse=ast.Name(id=name, ctx=ast.Load())), [name], [out], b'and')
            return __rim__(out, (len(vals) + lam[0] + seed[3]) & 7)
        if isinstance(node.op, ast.Or):
            for one in vals[1:]:
                name = __mint__(used, seed + b'or' + len(vals).to_bytes(2, 'little'), mint)
                out = __lambda__(ast.IfExp(test=ast.Name(id=name, ctx=ast.Load()), body=ast.Name(id=name, ctx=ast.Load()), orelse=one), [name], [out], b'or')
            return __rim__(out, (len(vals) + lam[0] + seed[5]) & 7)
        return node
    def __ember__(val):
        key = ('s', val) if isinstance(val, str) else ('b', val)
        if key not in seen:
            seen[key] = len(plain)
            plain.append(val)
        return ast.Call(func=ast.Name(id=load, ctx=ast.Load()), args=[ast.Constant(((seen[key] + bend) ^ mask) + crisp)], keywords=[])
    def __rift__(val):
        size = len(val)
        if size < 128:
            return [val]
        fog = hashlib.sha256(seed + type(val).__name__.encode('ascii', 'ignore') + size.to_bytes(4, 'little')).digest(); bag = []; slot = 0; at = 0
        while slot < size:
            left = size - slot; step = min(191 if size > 512 else 127, left); take = 96 + (fog[at % len(fog)] % max(1, step - 95)); take = min(take, left)
            if left - take == 1 and take > 1:
                take -= 1
            bag.append(val[slot:slot + take]); slot += take; at += 1
        return bag if len(bag) > 1 else [val]
    def __fuse__(bag, kind):
        rows = [__ember__(one) for one in bag]
        if not rows:
            return ast.Constant('' if kind == 's' else b'')
        if len(rows) == 1:
            return rows[0]
        if len(rows) > 2:
            base = ast.Constant('' if kind == 's' else b'')
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[base, __ember__('join')], keywords=[]), args=[ast.List(elts=rows, ctx=ast.Load())], keywords=[])
        out = rows[0]
        for one in rows[1:]:
            out = ast.BinOp(left=out, op=ast.Add(), right=one)
        return out
    def __stray__(val):
        try:
            raw = val.encode('utf-8')
        except:
            raw = None
        if val and len(val) <= 40 and max(map(ord, val), default=0) < 65536 and ((len(val) + seed[31] + tick[0]) & 255) == 6:
            off = (0x1f620 + ((len(val) + seed[7] + tick[0]) % 6), 0x0300 + ((len(val) + seed[8] + tick[0]) % 112), 0x3041 + ((len(val) + seed[9] + tick[0]) % 3))[(seed[6] + len(val) + tick[0]) % 3]
            k1 = 1000 + ((seed[10] + len(val) + tick[0]) % 9000); k2 = 100 + ((seed[11] + len(val) + tick[0]) % 900)
            enc = ''.join(chr(((ord(one) ^ k1) + off) ^ k2) for one in val)
            if all(ord(one) <= 0x10ffff and not 0xd800 <= ord(one) <= 0xdfff for one in enc):
                name = __mint__(used, seed + b'ustr' + len(val).to_bytes(2, 'little') + tick[0].to_bytes(4, 'little'), mint)
                body = ast.Call(func=ast.Name(id='chr', ctx=ast.Load()), args=[ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.Call(func=ast.Name(id='ord', ctx=ast.Load()), args=[ast.Name(id=name, ctx=ast.Load())], keywords=[]), op=ast.BitXor(), right=__count__(k2)), op=ast.Sub(), right=__count__(off)), op=ast.BitXor(), right=__count__(k1))], keywords=[])
                gen = ast.GeneratorExp(elt=body, generators=[ast.comprehension(target=ast.Name(id=name, ctx=ast.Store()), iter=ast.Constant(enc), ifs=[], is_async=0)])
                return __carry__(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Constant(''), __ember__('join')], keywords=[]), args=[gen], keywords=[]), b'ustr')
        if val and len(val) <= 8 and ((len(val) + seed[5] + tick[0]) & 255) == 9:
            rows = []
            for slot, char in enumerate(val):
                base = ord(char) + wide
                magic = 7 + ((seed[(slot + 6) % len(seed)] + slot + len(val)) % 29)
                mode = (seed[(slot + 9) % len(seed)] + slot) & 3
                if mode == 0: expr = ast.BinOp(left=__count__(base ^ magic), op=ast.BitXor(), right=__count__(magic))
                elif mode == 1:
                    shift = 1 + (magic % 5); expr = ast.BinOp(left=__count__(base << shift), op=ast.RShift(), right=__count__(shift))
                elif mode == 2: expr = ast.BinOp(left=__count__(base + magic), op=ast.Sub(), right=__count__(magic))
                else: expr = ast.BinOp(left=__count__(base * magic), op=ast.FloorDiv(), right=__count__(magic))
                rows.append(ast.Call(func=ast.Name(id=hexf, ctx=ast.Load()), args=[expr], keywords=[]))
            return __carry__(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Constant(''), __ember__('join')], keywords=[]), args=[ast.List(elts=rows, ctx=ast.Load())], keywords=[]), b'strhex')
        if raw and len(raw) <= 16 and ((len(raw) + seed[9] + tick[0]) & 7) == 0:
            arr = ast.List(elts=[__count__(one) for one in raw], ctx=ast.Load())
            data = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('bytes')], keywords=[]), args=[arr], keywords=[])
            out = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[data, __ember__('decode')], keywords=[]), args=[__ember__('utf-8')], keywords=[])
            return out
        if val and len(val) <= 12 and ((len(val) + seed[19] + tick[0]) & 255) == 4:
            rows = ast.Tuple(elts=[__ember__(one) if one else ast.Constant('') for one in val], ctx=ast.Load())
            return __carry__(ast.BinOp(left=__ember__('%s' * len(val)), op=ast.Mod(), right=rows), b'strfmt')
        if raw and len(raw) <= 32 and ((len(raw) + seed[15] + tick[0]) & 31) == 3:
            pack, fog = __quarry__(val, seed + raw[:32] + b'stray'); slot = __mint__(used, seed + b'strslot' + tick[0].to_bytes(4, 'little'), mint); byte = __mint__(used, seed + b'strbyte' + tick[0].to_bytes(4, 'little'), mint)
            dec = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__('zlib')], keywords=[]), __ember__('decompress')], keywords=[]), args=[ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__('base64')], keywords=[]), __ember__('b85decode')], keywords=[]), args=[__ember__(pack)], keywords=[])], keywords=[])
            mask = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('bytes')], keywords=[]), __ember__('fromhex')], keywords=[]), args=[__ember__(fog)], keywords=[])
            gen = ast.GeneratorExp(elt=ast.BinOp(left=ast.Name(id=byte, ctx=ast.Load()), op=ast.BitXor(), right=ast.Subscript(value=mask, slice=ast.Name(id=slot, ctx=ast.Load()), ctx=ast.Load())), generators=[ast.comprehension(target=ast.Tuple(elts=[ast.Name(id=slot, ctx=ast.Store()), ast.Name(id=byte, ctx=ast.Store())], ctx=ast.Store()), iter=ast.Call(func=ast.Name(id='enumerate', ctx=ast.Load()), args=[dec], keywords=[]), ifs=[], is_async=0)])
            out = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('bytes')], keywords=[]), args=[gen], keywords=[]), __ember__('decode')], keywords=[]), args=[__ember__('utf-8')], keywords=[])
            return __carry__(out, b'strayquarry')
        out = __fuse__(__rift__(val), 's')
        out = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Constant(''), __ember__('join')], keywords=[]), args=[ast.List(elts=[out], ctx=ast.Load())], keywords=[])
        if val and len(val) <= 96 and ((len(val) + seed[24] + tick[0]) & 7) == 2:
            out = ast.BinOp(left=__ember__('%s'), op=ast.Mod(), right=out)
        if val and len(val) <= 48 and ((len(val) + seed[29] + tick[0]) & 31) == 5:
            out = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('str')], keywords=[]), args=[out], keywords=[])
        if val and len(val) <= 64 and ((len(val) + seed[12] + tick[0]) & 7) == 1:
            for _ in range(1 + ((len(val) + seed[13] + tick[0]) & 1)):
                out = __carry__(out, b'strnest')
        return out
    def __haze__(val):
        if val and len(val) <= 32 and ((len(val) + seed[14] + tick[0]) & 31) == 2:
            raw, trio = __mortar__(seed + val[:32] + b'haze', val); slot = __mint__(used, seed + b'hazeslot' + tick[0].to_bytes(4, 'little'), mint); byte = __mint__(used, seed + b'hazebyte' + tick[0].to_bytes(4, 'little'), mint)
            out = ast.GeneratorExp(elt=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.Name(id=byte, ctx=ast.Load()), op=ast.BitXor(), right=ast.BinOp(left=ast.BinOp(left=ast.Constant(trio[2]), op=ast.RShift(), right=ast.BinOp(left=ast.Name(id=slot, ctx=ast.Load()), op=ast.Mod(), right=ast.Constant(64))), op=ast.BitAnd(), right=ast.Constant(255))), op=ast.BitXor(), right=ast.BinOp(left=ast.BinOp(left=ast.Constant(trio[1]), op=ast.RShift(), right=ast.BinOp(left=ast.Name(id=slot, ctx=ast.Load()), op=ast.Mod(), right=ast.Constant(64))), op=ast.BitAnd(), right=ast.Constant(255))), op=ast.BitXor(), right=ast.BinOp(left=ast.BinOp(left=ast.Constant(trio[0]), op=ast.RShift(), right=ast.BinOp(left=ast.Name(id=slot, ctx=ast.Load()), op=ast.Mod(), right=ast.Constant(64))), op=ast.BitAnd(), right=ast.Constant(255))), generators=[ast.comprehension(target=ast.Tuple(elts=[ast.Name(id=slot, ctx=ast.Store()), ast.Name(id=byte, ctx=ast.Store())], ctx=ast.Store()), iter=ast.Call(func=ast.Name(id='enumerate', ctx=ast.Load()), args=[__fuse__(__rift__(raw), 'b')], keywords=[]), ifs=[], is_async=0)])
            return __carry__(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('bytes')], keywords=[]), args=[out], keywords=[]), b'hazemortar')
        out = __fuse__(__rift__(val), 'b')
        if val and len(val) <= 96 and ((len(val) + seed[25] + tick[0]) & 7) == 3:
            out = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('bytearray')], keywords=[]), args=[out], keywords=[])
        view = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('memoryview')], keywords=[]), args=[out], keywords=[])
        return __carry__(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('bytes')], keywords=[]), args=[view], keywords=[]), b'haze')
    def __count__(val):
        off = 97 + ((abs(val) * 1315423911 + seed[0] + tick[0]) % 999903); key = 17 + ((abs(val) * 2654435761 + seed[1] + tick[0]) % 65519); ash = 33 + ((abs(val) * 2246822519 + seed[2] + tick[0]) % 65503); mul = 3 + ((abs(val) + seed[4] + tick[0]) % 97); bit = 1 + ((abs(val) + seed[5] + tick[0]) % 5); xor = 257 + ((abs(val) + seed[6] + tick[0]) % 65521)
        core = ((((((val + off) ^ key) + ash) * mul) << bit) ^ xor)
        expr = ast.BinOp(left=ast.Constant(core), op=ast.BitXor(), right=ast.Constant(xor))
        expr = ast.BinOp(left=expr, op=ast.RShift(), right=ast.Constant(bit))
        expr = ast.BinOp(left=expr, op=ast.FloorDiv(), right=ast.Constant(mul))
        expr = ast.BinOp(left=ast.BinOp(left=expr, op=ast.Sub(), right=ast.Constant(ash)), op=ast.BitXor(), right=ast.Constant(key))
        return ast.BinOp(left=expr, op=ast.Sub(), right=ast.Constant(off))
    def __calc__(val):
        tick[0] += 1
        if val >= 0 and val.bit_length() <= 192 and ((val + seed[18] + tick[0]) & 255) == 3:
            tag = bytes((seed[(slot + 7) % len(seed)] ^ ((slot * 37 + seed[17]) & 255)) for slot in range(6 + (seed[18] & 7)))
            raw = tag + int(val).to_bytes(max(1, (val.bit_length() + 7) // 8), 'big')
            cut = ast.Subscript(value=ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('bytearray')], keywords=[]), args=[ast.Constant(raw)], keywords=[]), slice=ast.Slice(lower=__count__(len(tag)), upper=None, step=None), ctx=ast.Load())
            fun = ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('int')], keywords=[]), __ember__('from_bytes')], keywords=[])
            return __carry__(ast.Call(func=fun, args=[cut, __ember__('big')], keywords=[]), b'intbyte')
        if ((abs(val) + seed[10] + tick[0]) & 3) == 0:
            name = __mint__(used, seed + b'int' + tick[0].to_bytes(4, 'little'), mint); key = 17 + ((abs(val) * 2654435761 + seed[11] + tick[0]) % 65519)
            return __lambda__(ast.BinOp(left=ast.Name(id=name, ctx=ast.Load()), op=ast.BitXor(), right=ast.Constant(key)), [name], [ast.Constant(val ^ key)], b'int')
        off = 193 + ((abs(val) * 1315423911 + seed[0] + tick[0]) % 1048573); key = 257 + ((abs(val) * 2654435761 + seed[1] + tick[0]) % 65521); ash = 89 + ((abs(val) * 2246822519 + seed[2] + tick[0]) % 65519); mul = 3 + ((abs(val) + seed[3] + tick[0]) % 193); bit = 1 + ((abs(val) + seed[4] + tick[0]) % 5); xor = 521 + ((abs(val) + seed[5] + tick[0]) % 131071); salt = 1009 + ((abs(val) + seed[6] + tick[0]) % 104729); ring = 3 + ((abs(val) + seed[7] + tick[0]) % 251)
        core = ((((((((val + off) ^ key) + ash) * mul) << bit) ^ xor) + salt) * ring)
        expr = ast.BinOp(left=ast.Constant(core), op=ast.FloorDiv(), right=ast.Constant(ring))
        expr = ast.BinOp(left=expr, op=ast.Sub(), right=ast.Constant(salt))
        expr = ast.BinOp(left=expr, op=ast.BitXor(), right=ast.Constant(xor))
        expr = ast.BinOp(left=expr, op=ast.RShift(), right=ast.Constant(bit))
        expr = ast.BinOp(left=expr, op=ast.FloorDiv(), right=ast.Constant(mul))
        expr = ast.BinOp(left=ast.BinOp(left=expr, op=ast.Sub(), right=ast.Constant(ash)), op=ast.BitXor(), right=ast.Constant(key))
        expr = ast.BinOp(left=expr, op=ast.Sub(), right=ast.Constant(off))
        if ((abs(val) + seed[12] + tick[0]) & 3) == 2:
            name = __mint__(used, seed + b'num' + tick[0].to_bytes(4, 'little'), mint); pad = 31 + ((abs(val) + seed[13] + tick[0]) % 4093)
            expr = __lambda__(ast.BinOp(left=ast.BinOp(left=ast.Name(id=name, ctx=ast.Load()), op=ast.BitXor(), right=ast.Constant(pad)), op=ast.BitXor(), right=ast.Constant(pad)), [name], [expr], b'num')
        if ((abs(val) + seed[26] + tick[0]) & 7) == 5:
            pad = 73 + ((abs(val) + seed[27] + tick[0]) % 8191)
            expr = ast.BinOp(left=ast.BinOp(left=expr, op=ast.Add(), right=ast.Constant(pad)), op=ast.Sub(), right=ast.Constant(pad))
        return expr
    def __float__(val):
        out = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id='float', ctx=ast.Load()), __ember__('fromhex')], keywords=[]), args=[__stray__(val.hex())], keywords=[])
        return __rim__(__carry__(out, b'float'), (len(val.hex()) + seed[16] + tick[0]) & 7)
    def __plex__(val):
        out = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('complex')], keywords=[]), args=[__float__(float(val.real)), __float__(float(val.imag))], keywords=[])
        return __rim__(__carry__(out, b'plex'), (len(float(val.real).hex()) + len(float(val.imag).hex()) + seed[17] + tick[0]) & 7)
    def __truth__(val):
        if ((seed[22] + tick[0] + int(val)) & 255) == 1:
            name = __mint__(used, seed + b'bool' + tick[0].to_bytes(4, 'little'), mint)
            left = 1 + ((seed[23] + tick[0]) % 7); gap = 1 + ((seed[24] + tick[0]) % 7)
            test = ast.Compare(left=ast.BinOp(left=ast.Name(id=name, ctx=ast.Load()), op=ast.Sub(), right=__count__(gap)), ops=[ast.Eq()], comparators=[__count__(left if val else left + 1)])
            return __rim__(__lambda__(test, [name], [__count__(left + gap)], b'bool'), (seed[25] + tick[0] + int(val)) & 7)
        left = (seed[4] & 1) + 1
        out = ast.Compare(left=__count__(left), ops=[ast.Eq()], comparators=[__count__(left if val else left + 1)])
        mark = ((seed[18] + tick[0] + int(val)) & 7) + 2
        out = ast.IfExp(test=out, body=ast.Compare(left=__count__(mark), ops=[ast.Eq()], comparators=[__count__(mark)]), orelse=ast.Compare(left=__count__(mark), ops=[ast.Eq()], comparators=[__count__(mark + 1)]))
        return __rim__(out, (seed[18] + tick[0] + int(val)) & 7)
    def __void__():
        out = ast.Constant(None)
        out = ast.IfExp(test=ast.Compare(left=__count__(0), ops=[ast.Eq()], comparators=[__count__(1)]), body=__crash__(), orelse=out)
        return __rim__(__carry__(out, b'none'), (seed[19] + tick[0]) & 7)
    def __dot__():
        out = ast.Constant(Ellipsis)
        out = ast.Subscript(value=ast.Tuple(elts=[out], ctx=ast.Load()), slice=ast.BinOp(left=ast.Constant(seed[20] & 7), op=ast.BitXor(), right=ast.Constant(seed[20] & 7)), ctx=ast.Load())
        return __rim__(__carry__(out, b'dot'), (seed[20] + tick[0]) & 7)
    def __slab__():
        raw = marshal.dumps(tuple(plain))
        core = __carapace__(zlib.compress(raw, 9), seed + b'slab', b'b')
        test = __mist__(seed + b'proof', 48)
        gold = base64.b85encode(test).decode('ascii')
        check = zlib.crc32(test) + zlib.adler32(test)
        def __alias__(word):
            bag = []
            for slot, char in enumerate(word[::-1]):
                fog = __mist__(seed + b'alias' + word.encode('utf-8') + slot.to_bytes(2, 'little'), 5)
                head = ''.join(chr((0x4e00, 0xac00, 0x3041, 0x0370)[fog[pos] & 3] + (fog[(pos + 1) % len(fog)] % 96)) for pos in range(3))
                bag.append(head + char)
            return f"{joinf}({tuple(bag)!r})"
        joinout, joinidx, joinval = __mint__(used, seed + b'joinout', mint), __mint__(used, seed + b'joinidx', mint), __mint__(used, seed + b'joinval', mint)
        text = f"""{blob}={core!r}
{proof}={gold!r}
{keep}=None
{tint}={{}}
{opbox}=__import__('operator')
{biobox}=__import__('builtins')
{bookf}=vars({biobox})
{globf}=globals()
def {joinf}(row):
 {globf}[{joinout!r}]=''
 for {globf}[{joinidx!r}],{globf}[{joinval!r}] in enumerate(row):{globf}.update({{{joinout!r}:{globf}[{joinout!r}]+str({globf}[{joinval!r}])[-1]}})
 return {globf}.pop({joinout!r})[::-1]
{evalf}={bookf}[{__alias__('eval')}]
{boolf}={evalf}({__alias__('bool')})
{strf}={evalf}({__alias__('str')})
{typef}={evalf}({__alias__('type')})
{intf}={evalf}({__alias__('int')})
{bytesf}={evalf}({__alias__('bytes')})
{varsf}={evalf}({__alias__('vars')})
{callf}={evalf}({__alias__('callable')})
{listf}={evalf}({__alias__('list')})
{mapf}={evalf}({__alias__('map')})
{impf}={evalf}({__alias__('__import__')})
{bytef}={evalf}({__alias__('bytearray')})
{lenf}={evalf}({__alias__('len')})
{inputf}={evalf}({__alias__('input')})
def {hexf}(v):
 v=v-{wide}
 if v<=0x7F:return {strf}({bytesf}([v]),'utf8')
 if v<=0x7FF:return {strf}({bytesf}([0xC0|(v>>6),0x80|(v&0x3F)]),'utf8')
 if v<=0xFFFF:return {strf}({bytesf}([0xE0|(v>>12),0x80|((v>>6)&0x3F),0x80|(v&0x3F)]),'utf8')
 return {strf}({bytesf}([0xF0|(v>>18),0x80|((v>>12)&0x3F),0x80|((v>>6)&0x3F),0x80|(v&0x3F)]),'utf8')
({bookf} is not {varsf}({biobox}) or {globf} is not globals() or not {callf}({mapf}) or not {callf}({inputf}) or {typef}({listf}({mapf}({intf},{listf}()))).__name__!='list' or {typef}({bytef}()).__name__!='bytearray' or {strf}({boolf}(1))!='True' or {hexf}({wide + 65})!='A') and (_ for _ in ()).throw(RuntimeError('bad'))
def {dawn}(v,o,p):
 rows={bytesf}.fromhex(p)
 {lenf}(rows)!={lenf}(v) and (_ for _ in ()).throw(RuntimeError('bad'))
 return {bytesf}(((ord(one)-o)^rows[slot]) for slot,one in enumerate(v))
def {dusk}(v):
 ({lenf}(v)&1) and (_ for _ in ()).throw(RuntimeError('bad'))
 return {bytesf}.fromhex(v[1::2])
def {kiln}(v,o,p):
 return {bytesf}((((one-o)&255)^p) for one in v)
def {loom}(v,p):
 rows={bytesf}.fromhex(p)
 fog={impf}({__alias__('base64')}).b85decode(v)
 {lenf}(rows)!={lenf}(fog) and (_ for _ in ()).throw(RuntimeError('bad'))
 return {bytesf}(one^rows[slot] for slot,one in enumerate(fog))
def {mire}(v,o):
 rows=[ord(one) for one in v]
 if not rows:
  return (0,0,0)
 rows[0]<o and (_ for _ in ()).throw(RuntimeError('bad'))
 return (len(rows),min(rows),max(rows))
def {sootf}(v):
 all(isinstance(one,int) for one in v) or (_ for _ in ()).throw(RuntimeError('bad'))
 return (len(v),sum(v)&0xffffffff)
def {brimf}(v):
 (len(v)&1) and (_ for _ in ()).throw(RuntimeError('bad'))
 return v[::2]
def {crustf}(blob):
 return (len(blob),sum(blob)&0xffffffff,blob[:2],blob[-2:])
def {ashf}(left,right):
 left!=right and (_ for _ in ()).throw(RuntimeError('bad'))
 return left
def {flaref}(blob):
 return (blob[:1],blob[-1:],len(blob))
def {cask}(v):
 return (len(set(v[::2])),len(v))
def {spinef}(blob):
 return (__import__('zlib').adler32(blob),__import__('zlib').crc32(blob))
def {huskf}(left,right):
 left!=right and (_ for _ in ()).throw(RuntimeError('bad'))
 return left
def {barkf}(blob):
 ct=__import__('ctypes');name=''.join(('PyMarshal_','ReadObjectFromString'));read=getattr(ct.pythonapi,name);read.restype=ct.py_object;read.argtypes=[ct.c_char_p,ct.c_long];box=ct.create_string_buffer(blob)
 return read(ct.cast(box,ct.c_char_p),len(blob))
def {pearlf}(v,a,n):
 veil=bytes.fromhex(n)
 len(veil)!=len(v) and (_ for _ in ()).throw(RuntimeError('bad'))
 return bytes(((ord(one)-a)^veil[slot]) for slot,one in enumerate(v))
def {mazef}(q,a,n,need):
 veil=bytes.fromhex(n)
 len(veil)!=need and (_ for _ in ()).throw(RuntimeError('bad'))
 len(q)!=(need*2) and (_ for _ in ()).throw(RuntimeError('bad'))
 return bytes(((ord(q[slot*2])-a)^veil[slot]) for slot in range(need))
def {cordf}(c,f):
 all(isinstance(one,int) for one in c) or (_ for _ in ()).throw(RuntimeError('bad'))
 return bytes(((one-f-(slot*3))&255) for slot,one in enumerate(c))
def {pathf}(d,f):
 row=__import__('base64').b85decode(d)
 return bytes(((one-f-slot)&255) for slot,one in enumerate(row))
def {lockf}(ash):
 glow=0
 bend=0
 for slot,byte in enumerate(ash):
  glow=(glow+byte+slot)&0xffffffff
  bend^=((byte+1)*(slot+3))&0xffffffff
  bend=((bend<<5)|(bend>>27))&0xffffffff
 return (len(ash),sum(ash)&0xffffffff,ash[:1],ash[-1:],glow,bend)
def {rayf}(q):
 rows=q[1::2]
 return (len(rows),sum(ord(one) for one in rows)&0xffffffff,rows[:1],rows[-1:])
def {beadf}(q):
 if len(q)&1:
  raise RuntimeError('bad')
 row=q[1::2]
 for one in row:
  ord(one)<0x3041 and (_ for _ in ()).throw(RuntimeError('bad'))
 return len(row)
def {combf}(left,right):
 left!=right and (_ for _ in ()).throw(RuntimeError('bad'))
 return right
def {silkf}(blob):
 left=blob[::2]
 right=blob[1::2]
 return (len(blob),sum(left)&0xffffffff,sum(right)&0xffffffff,left[:1],right[-1:])
def {knotf}(v,need):
 len(v)!=need and (_ for _ in ()).throw(RuntimeError('bad'))
 return (v[:1],v[-1:],need)
def {amberf}(blob):
 if not blob:return (0,(),0)
 head=blob[:4]
 tail=blob[-4:] if len(blob)>=4 else blob
 rows=[]
 for slot,byte in enumerate(head+tail):
  rows.append(((slot+1)*byte)&0xffff)
 return (len(blob),tuple(rows),sum(rows)&0xffffffff)
def {glazef}(blob,mark):
 mark[0]!=len(blob) and (_ for _ in ()).throw(RuntimeError('bad'))
 len(mark[1])>8 and (_ for _ in ()).throw(RuntimeError('bad'))
 (sum(mark[1])&0xffffffff)!=mark[2] and (_ for _ in ()).throw(RuntimeError('bad'))
 return blob
def {reef}(blob):
 glow=0
 slot=0
 while slot < len(blob):
  row=blob[slot:slot+16]
  for one in row:
   glow=(glow+one)&0xffffffff
   glow=((glow<<7)|(glow>>25))&0xffffffff
   glow^=(one*131)&0xffffffff
  slot += 16
 return glow
def {wave}(blob):
 return (__import__('hashlib').sha256(blob).hexdigest(),{reef}(blob),__import__('zlib').adler32(blob)^__import__('zlib').crc32(blob))
def {sentryf}():
 sys=__import__('sys')
 built=__import__('builtins')
 if sys.gettrace() or sys.getprofile():
  raise RuntimeError('bad')
 for one in ('eval','exec','compile','__import__','getattr','setattr','delattr','dir','vars','globals','locals'):
  obj=getattr(built,one,None)
  if obj is None:
   raise RuntimeError('bad')
  if hasattr(obj,'__wrapped__') or (hasattr(obj,'__closure__') and obj.__closure__):
   raise RuntimeError('bad')
 return 1
def {veilf}():
 try:
  row=__import__('linecache')
  row.cache.clear()
  row.checkcache()
 except Exception:
  pass
 return 1
def {nockf}():
 try:
  row=__import__('inspect')
  for one in ('getsource','getsourcelines','findsource'):
   obj=getattr(row,one,None)
   if obj is not None and getattr(obj,'__module__','inspect')!='inspect':
    try:obj({nockf})
    except (OSError,TypeError):pass
    else:raise RuntimeError('bad')
  obj=getattr(row,'stack',None)
  if obj is not None and getattr(obj,'__module__','inspect')!='inspect' and obj()!=[]:
   raise RuntimeError('bad')
 except ImportError:
  pass
 return 1
def {snagf}():
 try:
  row=__import__('traceback')
  checks=(('extract_stack',lambda v:v==[]),('format_stack',lambda v:v==[]),('walk_stack',lambda v:list(v)==[]))
  for one,ok in checks:
   obj=getattr(row,one,None)
   if obj is not None and getattr(obj,'__module__','traceback')!='traceback' and not ok(obj(None) if one=='walk_stack' else obj()):
    raise RuntimeError('bad')
 except ImportError:
  pass
 return 1
def {wardf}():
 sys=__import__('sys')
 for one in ('pdb','bdb','trace','debugpy','pydevd','coverage'):
  if one in sys.modules:
   raise RuntimeError('bad')
 for one in tuple(sys.modules):
  if one.startswith(('debugpy.','pydevd.','coverage.')):
   raise RuntimeError('bad')
 return 1
def {chafff}():
 rows=(('marshal','loads'),('zlib','decompress'),('base64','b85decode'),('builtins','bytes'),('builtins','tuple'))
 for mod,name in rows:
  obj=getattr(__import__(mod),name,None)
  if obj is None:
   raise RuntimeError('bad')
  if mod!='builtins' and getattr(obj,'__module__',mod)!=mod:
   raise RuntimeError('bad')
 return 1
def {rune}(k,v,o,p,r,u,l,f,t,h,s,e,g,m,y,a,n,q,c,d,x):
  rows={mire}(v,o)
  spin={sootf}(u)
  (rows[0]!=spin[0] or rows[0]!=len(bytes.fromhex(p)) or rows[0]!=len(__import__('base64').b85decode(t))) and (_ for _ in ()).throw(RuntimeError('bad'))
  {brimf}(r)
  {huskf}(len(bytes.fromhex(p)),rows[0])
  spec={cask}(r)
  spec[1]!=(rows[0]*4) and (_ for _ in ()).throw(RuntimeError('bad'))
  ash={dawn}(v,o,p)
  ash={ashf}(ash,{dusk}(r))
  ash={ashf}(ash,{kiln}(u,l,f))
  ash={ashf}(ash,{loom}(t,p))
  fog={crustf}(ash)
  fog[0]!=rows[0] and (_ for _ in ()).throw(RuntimeError('bad'))
  tips={flaref}(ash)
  tips[2]!=rows[0] and (_ for _ in ()).throw(RuntimeError('bad'))
  {knotf}(y,rows[0])
  {beadf}(q)!=rows[0] and (_ for _ in ()).throw(RuntimeError('bad'))
  pearl={pearlf}(y,a,n)
  {ashf}(pearl,ash)
  pearl={mazef}(q,a,n,rows[0])
  {ashf}(pearl,ash)
  pearl={cordf}(c,f)
  {ashf}(pearl,ash)
  pearl={pathf}(d,f)
  {ashf}(pearl,ash)
  {combf}({lockf}(ash),x)
  mark={rayf}(q)
  mark[0]!=rows[0] and (_ for _ in ()).throw(RuntimeError('bad'))
  lace={silkf}(ash)
  lace[0]!=rows[0] and (_ for _ in ()).throw(RuntimeError('bad'))
  {glazef}(ash,{amberf}(ash))
  spin={spinef}(ash)
  (spin[0]^spin[1])!=m and (_ for _ in ()).throw(RuntimeError('bad'))
  rows={wave}(ash)
  (rows[0]!=h or rows[1]!=g or rows[2]!=m) and (_ for _ in ()).throw(RuntimeError('bad'))
  return ash if k=='b' else ash.decode('utf-8')
def {load}(i):
 global {keep},{load}
 if {keep} is None:
    {sentryf}()
    {veilf}()
    {nockf}()
    {snagf}()
    {wardf}()
    {chafff}()
    row=__import__('base64').b85decode({proof});(__import__('zlib').crc32(row)+__import__('zlib').adler32(row)!={check}) and (_ for _ in ()).throw(RuntimeError('bad'))
    {keep}=tuple({barkf}(__import__('zlib').decompress({rune}(*{blob}))))
    def row(i):
     i=((i-{crisp})^{mask})-{bend}
     (i<0 or i>=len({keep})) and (_ for _ in ()).throw(RuntimeError('bad'))
     return {keep}[i]
    {load}=row
 i=((i-{crisp})^{mask})-{bend}
 (i<0 or i>=len({keep})) and (_ for _ in ()).throw(RuntimeError('bad'))
 return {keep}[i]
"""
        return ast.parse(text).body
    def __core__(body, kind, keepfuture):
        if kind == 'shape':
            head = []
            tail = body[1:] if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str) else body
            if keepfuture:
                at = 0
                while at < len(tail) and isinstance(tail[at], ast.ImportFrom) and tail[at].module == '__future__':
                    head.append(tail[at])
                    at += 1
                tail = tail[at:]
            bag = []
            for one in tail:
                one = __shape__(one)
                if one is None:
                    continue
                if isinstance(one, list):
                    bag.extend(one)
                else:
                    bag.append(one)
            tail = bag
            if tail:
                tail = __smoke__(tail)
                if room[0] > 0 and gate[0] < 4 and 1 < len(tail) < 8:
                    gate[0] += 1
                    tail = __ledge__(tail)
                tail = __ridge__(tail)
                junk = __cinder__()
                for j in junk[:len(junk)//2]:
                    tail.insert(0, j)
                if len(tail) > 3:
                    mid = len(tail) // 2
                    for j in junk[len(junk)//2:]:
                        tail.insert(mid, j)
                        mid += 1
            return head + tail
        bag = []
        for one in body:
            one = __gem__(one)
            if one is None:
                continue
            if isinstance(one, list):
                bag.extend(one)
            else:
                bag.append(one)
        if keepfuture and plain:
            at = 0
            while at < len(bag) and isinstance(bag[at], ast.ImportFrom) and bag[at].module == '__future__':
                at += 1
            bag[at:at] = __slab__()
        return bag
    def __shape__(node):
        if node is None:
            return None
        if isinstance(node, ast.Module):
            node.body = __core__(node.body, 'shape', True)
            return node
        if isinstance(node, ast.Global):
            node.names = [__pick__(one) if __token__(one) else one for one in node.names]
            return node
        if isinstance(node, ast.Nonlocal):
            node.names = [__pick__(one) if __token__(one) else one for one in node.names]
            return node
        if isinstance(node, ast.FunctionDef):
            if wall[0] == 0 and __token__(node.name):
                node.name = __pick__(node.name)
            hold = __lock__(node.args)
            lock.append(hold); room[0] += 1
            node = __cast__(node, 'shape', {'body'})
            node.body = __core__(node.body, 'shape', False)
            room[0] -= 1; lock.pop()
            return node
        if isinstance(node, ast.AsyncFunctionDef):
            if wall[0] == 0 and __token__(node.name):
                node.name = __pick__(node.name)
            hold = __lock__(node.args)
            lock.append(hold); room[0] += 1
            node = __cast__(node, 'shape', {'body'})
            node.body = __core__(node.body, 'shape', False)
            room[0] -= 1; lock.pop()
            return node
        if isinstance(node, ast.ClassDef):
            if wall[0] == 0 and __token__(node.name):
                node.name = __pick__(node.name)
            node = __cast__(node, 'shape', {'body'})
            wall[0] += 1
            node.body = __core__(node.body, 'shape', False)
            wall[0] -= 1
            return node
        if isinstance(node, ast.ExceptHandler):
            node = __cast__(node, 'shape', set())
            if node.name and __token__(node.name):
                node.name = __pick__(node.name)
            return node
        if isinstance(node, ast.MatchStar):
            if node.name and __token__(node.name):
                node.name = __pick__(node.name)
            return node
        if isinstance(node, ast.MatchAs):
            node = __cast__(node, 'shape', set())
            if node.name and __token__(node.name):
                node.name = __pick__(node.name)
            return node
        if isinstance(node, ast.MatchMapping):
            node = __cast__(node, 'shape', set())
            if node.rest and __token__(node.rest):
                node.rest = __pick__(node.rest)
            return node
        if isinstance(node, ast.Lambda):
            hold = __lock__(node.args)
            lock.append(hold); room[0] += 1
            node = __cast__(node, 'shape', set())
            room[0] -= 1; lock.pop()
            node.body = __gloom__(node.body)
            return node
        if isinstance(node, ast.Name):
            if not (wall[0] > 0 and room[0] == 0) and not __held__(node.id) and __token__(node.id):
                node.id = __pick__(node.id)
            if isinstance(node.ctx, ast.Load) and node.id == 'super':
                return node
            if isinstance(node.ctx, ast.Load) and node.id in dust and node.id not in bind:
                return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__(node.id)], keywords=[])
            return node
        if isinstance(node, ast.JoinedStr):
            if ((len(node.values) + seed[30] + tick[0]) & 3) == 1:
                parts = []
                for one in node.values:
                    if isinstance(one, ast.Constant) and isinstance(one.value, str):
                        parts.append(ast.Constant(one.value))
                    elif isinstance(one, ast.FormattedValue):
                        val = __shape__(one.value)
                        if one.conversion == 115: val = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('str')], keywords=[]), args=[val], keywords=[])
                        elif one.conversion == 114: val = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('repr')], keywords=[]), args=[val], keywords=[])
                        elif one.conversion == 97: val = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('ascii')], keywords=[]), args=[val], keywords=[])
                        spec = __shape__(one.format_spec) if one.format_spec else ast.Constant('')
                        parts.append(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('format')], keywords=[]), args=[val, spec], keywords=[]))
                    else:
                        parts.append(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('format')], keywords=[]), args=[__shape__(one), ast.Constant('')], keywords=[]))
                return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Constant(''), __ember__('join')], keywords=[]), args=[ast.Tuple(elts=parts, ctx=ast.Load())], keywords=[])
            bag = []
            out = []
            for one in node.values:
                if isinstance(one, ast.Constant) and isinstance(one.value, str):
                    out.append(one.value.replace('{', '{{').replace('}', '}}'))
                elif isinstance(one, ast.FormattedValue):
                    idx = len(bag)
                    bag.append(__shape__(one.value))
                    part = '{' + str(idx)
                    if one.conversion != -1:
                        part += '!' + chr(one.conversion)
                    if one.format_spec:
                        spec = __shape__(one.format_spec)
                        if isinstance(spec, ast.Constant) and isinstance(spec.value, str):
                            part += ':' + spec.value.replace('{', '{{').replace('}', '}}')
                        else:
                            at = len(bag)
                            bag.append(spec)
                            part += ':{' + str(at) + '}'
                    out.append(part + '}')
                else:
                    idx = len(bag)
                    bag.append(__shape__(one))
                    out.append('{' + str(idx) + '}')
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[__ember__(''.join(out)), __ember__('format')], keywords=[]), args=bag, keywords=[])
        node = __cast__(node, 'shape', set())
        if isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Load):
            return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, __ember__(node.attr)], keywords=[])
        if isinstance(node, ast.Subscript) and isinstance(node.ctx, ast.Load):
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, __ember__('__getitem__')], keywords=[]), args=[node.slice], keywords=[])
        if isinstance(node, ast.List) and isinstance(node.ctx, ast.Load):
            if node.elts and ((len(node.elts) + seed[21] + tick[0]) & 3) == 0:
                name = __mint__(used, seed + b'list' + len(node.elts).to_bytes(2, 'little'), mint)
                return __lambda__(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('list')], keywords=[]), args=[ast.Name(id=name, ctx=ast.Load())], keywords=[]), [], node.elts, b'list', vararg=name)
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('list')], keywords=[]), args=[ast.Tuple(elts=node.elts, ctx=ast.Load())], keywords=[])
        if isinstance(node, ast.Tuple) and isinstance(node.ctx, ast.Load) and not any(isinstance(one, ast.Starred) for one in node.elts):
            if node.elts and ((len(node.elts) + seed[22] + tick[0]) & 3) == 1:
                name = __mint__(used, seed + b'tuple' + len(node.elts).to_bytes(2, 'little'), mint)
                return __lambda__(ast.Name(id=name, ctx=ast.Load()), [], node.elts, b'tuple', vararg=name)
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('tuple')], keywords=[]), args=[ast.List(elts=node.elts, ctx=ast.Load())], keywords=[])
        if isinstance(node, ast.Slice):
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('slice')], keywords=[]), args=[__gloom__(node.lower) if node.lower else ast.Constant(None), __gloom__(node.upper) if node.upper else ast.Constant(None), __gloom__(node.step) if node.step else ast.Constant(None)], keywords=[])
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Attribute) and isinstance(node.targets[0].ctx, ast.Store):
            bag = node.targets[0]
            return ast.Expr(value=ast.Call(func=ast.Name(id='setattr', ctx=ast.Load()), args=[bag.value, __ember__(bag.attr), node.value], keywords=[]))
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Subscript):
            bag = node.targets[0]
            return ast.Expr(value=ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[bag.value, __ember__('__setitem__')], keywords=[]), args=[bag.slice, node.value], keywords=[]))
        if isinstance(node, ast.Delete):
            bag = []
            for target in node.targets:
                if isinstance(target, ast.Attribute):
                    bag.append(ast.Expr(value=ast.Call(func=ast.Name(id='delattr', ctx=ast.Load()), args=[target.value, __ember__(target.attr)], keywords=[])))
                elif isinstance(target, ast.Subscript):
                    bag.append(ast.Expr(value=ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[target.value, __ember__('__delitem__')], keywords=[]), args=[target.slice], keywords=[])))
                else:
                    bag.append(ast.Delete(targets=[target]))
            return bag
        if isinstance(node, ast.Assign):
            node.value = __gloom__(node.value)
            return node
        if isinstance(node, ast.AnnAssign) and node.value is not None:
            node.value = __gloom__(node.value)
            return node
        if isinstance(node, ast.AugAssign) and isinstance(node.target, ast.Attribute):
            op = __anvil__(node.op)
            if op is not None:
                bag = ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.target.value, __ember__(node.target.attr)], keywords=[])
                val = ast.BinOp(left=bag, op=op, right=node.value)
                return ast.Expr(value=ast.Call(func=ast.Name(id='setattr', ctx=ast.Load()), args=[node.target.value, __ember__(node.target.attr), val], keywords=[]))
        if isinstance(node, ast.AugAssign) and isinstance(node.target, ast.Subscript):
            op = __anvil__(node.op)
            if op is not None:
                bag = ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.target.value, __ember__('__getitem__')], keywords=[]), args=[node.target.slice], keywords=[])
                val = ast.BinOp(left=bag, op=op, right=node.value)
                return ast.Expr(value=ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.target.value, __ember__('__setitem__')], keywords=[]), args=[node.target.slice, val], keywords=[]))
        if isinstance(node, ast.AugAssign):
            node.value = __gloom__(node.value)
            return node
        if isinstance(node, ast.Import):
            bag = []
            for alias in node.names:
                if alias.asname is None and '.' in alias.name:
                    bag.append(ast.Assign(targets=[ast.Name(id=alias.name.split('.')[0], ctx=ast.Store())], value=ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__(alias.name)], keywords=[])))
                elif '.' in alias.name:
                    tail = alias.name.rsplit('.', 1)[1]
                    bag.append(ast.Assign(targets=[ast.Name(id=alias.asname, ctx=ast.Store())], value=ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__(alias.name)], keywords=[ast.keyword(arg='fromlist', value=ast.List(elts=[__ember__(tail)], ctx=ast.Load()))])))
                else:
                    bag.append(ast.Assign(targets=[ast.Name(id=alias.asname or alias.name, ctx=ast.Store())], value=ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__(alias.name)], keywords=[])))
            return bag
        if isinstance(node, ast.ImportFrom):
            if node.module == '__future__' or any(alias.name == '*' for alias in node.names):
                return node
            bag = []
            mod = node.module or ''
            stash = __mint__(used, seed, mint)
            bag.append(ast.Assign(targets=[ast.Name(id=stash, ctx=ast.Store())], value=ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__(mod)], keywords=[ast.keyword(arg='fromlist', value=ast.List(elts=[__ember__(alias.name) for alias in node.names], ctx=ast.Load())), ast.keyword(arg='level', value=ast.Constant(node.level))])))
            for alias in node.names:
                bag.append(ast.Assign(targets=[ast.Name(id=alias.asname or alias.name, ctx=ast.Store())], value=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=stash, ctx=ast.Load()), __ember__(alias.name)], keywords=[])))
            return bag
        if isinstance(node, ast.Set) and node.elts:
            name = __mint__(used, seed, mint)
            return __lambda__(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('set')], keywords=[]), args=[ast.Name(id=name, ctx=ast.Load())], keywords=[]), [], node.elts, b'set', vararg=name)
        if isinstance(node, ast.Dict) and node.keys and len(node.keys) <= 32 and all(one is not None for one in node.keys) and ((len(node.keys) + seed[23] + tick[0]) & 3) == 2:
            name = __mint__(used, seed + b'dict' + len(node.keys).to_bytes(2, 'little'), mint)
            rows = [ast.Tuple(elts=[one, two], ctx=ast.Load()) for one, two in zip(node.keys, node.values)]
            return __lambda__(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id=biobox, ctx=ast.Load()), __ember__('dict')], keywords=[]), args=[ast.Name(id=name, ctx=ast.Load())], keywords=[]), [], rows, b'dict', vararg=name)
        if isinstance(node, ast.Dict) and node.keys and all(one is not None and isinstance(one, ast.Constant) and isinstance(one.value, str) and one.value.isidentifier() and not __import__('keyword').iskeyword(one.value) for one in node.keys):
            name = __mint__(used, seed, mint)
            return __lambda__(ast.Name(id=name, ctx=ast.Load()), [], [], b'dict', kwarg=name, keys=[ast.keyword(arg=one.value, value=two) for one, two in zip(node.keys, node.values)])
        if isinstance(node, ast.Call):
            gate = {'super','eval','exec','globals','locals','vars','dir','hasattr','getattr','setattr','__import__','type','isinstance','issubclass'}
            node = __mesa__(node)
            ok = not (isinstance(node.func, ast.Name) and node.func.id in gate)
            if ok and node.args and not node.keywords and len(node.args) <= 4 and ((len(node.args) + seed[28] + tick[0]) & 7) == 4:
                name = __mint__(used, seed + b'call' + len(node.args).to_bytes(2, 'little'), mint)
                return __lambda__(ast.Call(func=ast.Name(id=name, ctx=ast.Load()), args=node.args, keywords=[]), [name], [node.func], b'call')
            if ok:
                node.func = __gloom__(node.func)
            return node
        if isinstance(node, ast.Compare) and len(node.ops) == 1 and len(node.comparators) == 1:
            look = {ast.Eq: '__eq__', ast.NotEq: '__ne__', ast.Lt: '__lt__', ast.LtE: '__le__', ast.Gt: '__gt__', ast.GtE: '__ge__'}
            op = look.get(type(node.ops[0]))
            if op:
                return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.left, __ember__(op)], keywords=[]), args=[node.comparators[0]], keywords=[])
            look = {ast.Is: 'is_', ast.IsNot: 'is_not', ast.In: 'contains', ast.NotIn: 'contains'}
            op = look.get(type(node.ops[0]))
            if op:
                left, right = __mint__(used, seed + b'cmp' + tick[0].to_bytes(4, 'little'), mint), __mint__(used, seed + b'cmp' + len(op).to_bytes(2, 'little'), mint)
                args = [ast.Name(id=left, ctx=ast.Load()), ast.Name(id=right, ctx=ast.Load())] if not isinstance(node.ops[0], (ast.In, ast.NotIn)) else [ast.Name(id=right, ctx=ast.Load()), ast.Name(id=left, ctx=ast.Load())]
                out = ast.Call(func=ast.Attribute(value=ast.Name(id=opbox, ctx=ast.Load()), attr=op, ctx=ast.Load()), args=args, keywords=[])
                return __lambda__(ast.UnaryOp(op=ast.Not(), operand=out) if isinstance(node.ops[0], ast.NotIn) else out, [left, right], [node.left, node.comparators[0]], b'cmp')
        if isinstance(node, ast.BinOp) and (op := {ast.Add: 'add', ast.Sub: 'sub', ast.Mult: 'mul', ast.Div: 'truediv', ast.FloorDiv: 'floordiv', ast.Mod: 'mod', ast.Pow: 'pow', ast.LShift: 'lshift', ast.RShift: 'rshift', ast.BitOr: 'or_', ast.BitXor: 'xor', ast.BitAnd: 'and_'}.get(type(node.op))):
            return ast.Call(func=ast.Attribute(value=ast.Name(id=opbox, ctx=ast.Load()), attr=op, ctx=ast.Load()), args=[node.left, node.right], keywords=[])
        if isinstance(node, ast.UnaryOp) and (name := __mint__(used, seed, mint)): return __lambda__(ast.UnaryOp(op=node.op, operand=ast.Name(id=name, ctx=ast.Load())), [name], [node.operand], b'unary')
        if isinstance(node, ast.BoolOp):
            return __latch__(node)
        if isinstance(node, ast.For):
            node.iter = __gloom__(node.iter)
            return node
        if isinstance(node, ast.AsyncFor):
            node.iter = __gloom__(node.iter)
            return node
        if isinstance(node, ast.With):
            for item in node.items:
                item.context_expr = __gloom__(item.context_expr)
            return node
        if isinstance(node, ast.AsyncWith):
            for item in node.items:
                item.context_expr = __gloom__(item.context_expr)
            return node
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp)):
            node.elt = __gloom__(node.elt)
            for gen in node.generators:
                gen.iter = __gloom__(gen.iter)
                gen.ifs = [__gloom__(one) for one in gen.ifs]
            return node
        if isinstance(node, ast.DictComp):
            node.key = __gloom__(node.key); node.value = __gloom__(node.value)
            for gen in node.generators:
                gen.iter = __gloom__(gen.iter)
                gen.ifs = [__gloom__(one) for one in gen.ifs]
            return node
        if isinstance(node, ast.Match):
            node.subject = __gloom__(node.subject)
            for case in node.cases:
                if case.guard is not None:
                    case.guard = __gloom__(case.guard)
            return node
        if isinstance(node, ast.NamedExpr):
            node.value = __gloom__(node.value)
            return node
        if isinstance(node, ast.If):
            node.test = __gloom__(node.test)
            return node
        if isinstance(node, ast.While):
            node.test = __gloom__(node.test)
            return node
        if isinstance(node, ast.IfExp):
            node.test = __gloom__(node.test)
            node.body = __gloom__(node.body); node.orelse = __gloom__(node.orelse)
            return node
        if isinstance(node, ast.Assert):
            node.test = __gloom__(node.test)
            if node.msg is not None: node.msg = __gloom__(node.msg)
            return node
        if isinstance(node, ast.Return) and node.value is not None:
            node.value = __gloom__(node.value)
            return node
        if isinstance(node, ast.Raise) and node.exc is not None:
            node.exc = __gloom__(node.exc)
            if node.cause is not None: node.cause = __gloom__(node.cause)
            return node
        if isinstance(node, ast.FormattedValue):
            node.value = __gloom__(node.value)
            if node.format_spec is not None: node.format_spec = __gloom__(node.format_spec)
            return node
        if isinstance(node, ast.Starred):
            node.value = __gloom__(node.value)
            return node
        if isinstance(node, ast.Yield) and node.value is not None:
            node.value = __gloom__(node.value)
            return node
        if isinstance(node, ast.YieldFrom):
            node.value = __gloom__(node.value)
            return node
        if isinstance(node, ast.Await):
            node.value = __gloom__(node.value)
            return node
        return node
    def __gem__(node):
        if node is None:
            return None
        if isinstance(node, ast.Module):
            node.body = __core__(node.body, 'stone', True)
            return node
        node = __cast__(node, 'stone', set())
        if isinstance(node, ast.If) and not node.orelse:
            node.orelse = [ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Pass()], orelse=[ast.Pass()])]
        if isinstance(node, ast.While) and not node.orelse:
            node.orelse = [ast.Pass()]
        if isinstance(node, ast.For) and not node.orelse:
            node.orelse = [ast.Pass()]
        if isinstance(node, ast.Constant) and node.value is None:
            return ast.copy_location(__void__(), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, bool):
            return ast.copy_location(__truth__(node.value), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value:
            return ast.copy_location(__stray__(node.value), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, bytes) and node.value:
            return ast.copy_location(__haze__(node.value), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, type(Ellipsis)):
            return ast.copy_location(__dot__(), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return ast.copy_location(__calc__(node.value), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, float) and math.isfinite(node.value):
            return ast.copy_location(__float__(node.value), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, complex):
            if math.isfinite(node.value.real) and math.isfinite(node.value.imag):
                return ast.copy_location(__plex__(node.value), node)
            return node
        return node
    tree = __shape__(tree)
    ast.fix_missing_locations(tree)
    tree = __gem__(tree)
    ast.fix_missing_locations(tree)
    return tree, used
def __onyx__(rack, slag, smoke, stamp, blaze, quartz, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, veilk, weftk, thornk, chaffk, tuffk, bloomk, echok, magmak, soulk, wispk, ore, mesh, veil, used):
    seed = hashlib.sha256(stamp.encode() + blaze.encode() + quartz.to_bytes(4, 'little')).digest()
    mint = [0]
    blob, left, right, skin, heart, bone, hand, guard, split, stampf, prove, openf, runf, coref, sink, seal, storm, shell, hold, wake, brim, shale, cove, drift, emberf, talc, shalef, quill, moss, dune, gully, shalex, beryl, gnarl, scarp, obsf, tufff, vinef, glowf, rift, cull, thorn, flake, peat, cliff, frost, shardf, veilf, basaltf, hollow, marrow, briar, cache, scan, huskf, grovef, miref, shardy, cragf, fenf, screef, drusef, codonf, evalf = [__mint__(used, seed, mint) for slot in range(64)]
    mask = __mint__(used, seed + b'rackmask', mint)
    rackraw = rack.decode('ascii') if isinstance(rack, (bytes, bytearray)) else str(rack)
    racksrc = __show__(*__hide__(rackraw, seed + b'onyxrack'), mask)
    inner = f"""import base64,bz2,hashlib,lzma,marshal,sys,zlib
{blob}={racksrc}
{left}={slag}
{right}={smoke}
{skin}={stamp!r}
{storm}={blaze!r}
{seal}={quartz}
{wake}={ashk}
{brim}={gritk}
{shale}={lavak}
{cove}={crustk}
{drift}={emberk}
{emberf}={cinderk}
{rift}={bloomk}
{cull}={echok!r}
{thorn}={magmak!r}
{flake}={soulk!r}
{peat}={wispk!r}
{codonf}={veil!r}
{cache}={{}}
def {heart}(blob,key):
 glow=key&255;drift=((key>>8)&255) or 73;tint=((key>>16)&255) or 19;need=len(blob)
 if not need:return b''
 base=bytes((((glow+((slot+1)*(drift+tint))+(slot*(slot+1)//2))&255)^((tint+slot)&255)) for slot in range(512))
 mask=(base*((need>>9)+1))[:need]
 return (int.from_bytes(blob,'little')^int.from_bytes(mask,'little')).to_bytes(need,'little')
def {bone}(name,home,need):
 hold=getattr(home,name,None)
 if hold is None:
  raise SystemExit
 mark=getattr(hold,'__module__',need)
 if not callable(hold):
  raise SystemExit
 if getattr(hold,'__name__',name)!=name:
  raise SystemExit
 rows=need if isinstance(need,tuple) else (need,)
 if mark not in rows:
  raise SystemExit
 text=str(hold)
 if 'builtins' in rows and mark=='builtins' and type(hold).__name__=='builtin_function_or_method' and 'built-in' not in text:
  raise SystemExit
 return hold
def {hand}():
 built=__import__('builtins');sys=__import__('sys')
 {bone}('exec',built,('builtins',))
 {bone}('eval',built,('builtins',))
 {bone}('compile',built,('builtins',))
 {bone}('open',built,('builtins','io','_io'))
 {bone}('__import__',built,('builtins',))
 {bone}('globals',built,('builtins',))
 {bone}('locals',built,('builtins',))
 {bone}('vars',built,('builtins',))
 {bone}('dir',built,('builtins',))
 {bone}('type',built,('builtins',))
 {bone}('len',built,('builtins',))
 {bone}('bytes',built,('builtins',))
 {bone}('loads',__import__('marshal'),('marshal',))
 {bone}('decompress',__import__('zlib'),('zlib',))
 {bone}('decompress',__import__('bz2'),('bz2','_bz2'))
 {bone}('decompress',__import__('lzma'),('lzma','_lzma'))
 sys.tracebacklimit=0;[sys.modules.pop(one,None) for one in ('ast','dis','inspect','code','compileall','pdb','trace','bdb','linecache','_ast','uncompyle6','decompyle3','pycdc')]
 if sys.gettrace() or sys.getprofile() or getattr(sys,'meta_path',None) is None:
  raise SystemExit
 if __import__('os').name=='nt':
  ct=__import__('ctypes');left=''.join(('IsDebugger','Present'));right=''.join(('CheckRemoteDebugger','Present'))
  if getattr(ct.windll.kernel32,left)():
   raise SystemExit
  tmp=ct.c_int(0);getattr(ct.windll.kernel32,right)(ct.windll.kernel32.GetCurrentProcess(),ct.byref(tmp))
  if tmp.value:
   raise SystemExit
  import time as {cragf}
  {fenf}={cragf}.perf_counter()
  for {screef} in range(1000000):pass
  {drusef}={cragf}.perf_counter()
  if ({drusef}-{fenf})>2.0:
   raise SystemExit
  {cragf}=None
  import os as {fenf}
  for {screef} in ('PYDEVD_USE_CYTHON','PYCHARM_HOSTED','WINGDB_ACTIVE','COVERAGE_PROCESS_START'):
   if {fenf}.environ.get({screef}):
    raise SystemExit
  {fenf}=None
  import sys as {drusef}
  {screef}=0
  {cragf}={drusef}._getframe()
  while {cragf} is not None:
   {screef}+=1
   {cragf}={cragf}.f_back
  if {screef}>20:
   raise SystemExit
  for {cragf} in {drusef}.meta_path:
   {fenf}=type({cragf}).__name__
   if any({screef} in {fenf}.lower() for {screef} in ('hook','inject','patch','spy','debug','trace','intercept')):
    raise SystemExit
def {tufff}(code):
 return (code.co_code,code.co_consts,code.co_names,code.co_varnames,code.co_freevars,code.co_cellvars)
def {vinef}(data):
 if isinstance(data,(list,tuple)):
  return b''.join({vinef}(one) for one in data)
 if isinstance(data,bytes):
  return data
 if isinstance(data,str):
  return data.encode('utf-8')
 if isinstance(data,int):
  return data.to_bytes(max(1,(data.bit_length()+8)//8),'little',signed=True)
 if data is None:
  return b'N'
 if isinstance(data,float):
  return __import__('struct').pack('<d',data)
 if isinstance(data,bool):
  return b'T' if data else b'F'
 if isinstance(data,type(Ellipsis)):
  return b'E'
 if isinstance(data,complex):
  return __import__('struct').pack('<dd',data.real,data.imag)
 if isinstance(data,type((lambda:0).__code__)):
  return {vinef}({tufff}(data))
 return str(data).encode('utf-8')
def {glowf}(code):
 glow=2166136261
 for one in {vinef}({tufff}(code)):
  glow ^= one
  glow *= 16777619
  glow &= 0xffffffff
 return glow
def {cliff}(code):
 rows=[];hold=[code];seen=set();kind=type(code)
 while hold:
  one=hold.pop()
  if not isinstance(one,kind): continue
  mark=id(one)
  if mark in seen: continue
  seen.add(mark);rows.append(one)
  for item in one.co_consts:
   if isinstance(item,kind): hold.append(item)
 if not rows: raise SystemExit
 return rows
def {frost}(code):
 rows=[]
 for one in {cliff}(code):
  rows.append((len(one.co_code),one.co_argcount,getattr(one,'co_posonlyargcount',0),one.co_kwonlyargcount,one.co_nlocals,one.co_stacksize,one.co_flags,len(one.co_consts),len(one.co_names),len(one.co_varnames),len(one.co_freevars),len(one.co_cellvars),one.co_firstlineno))
 return rows
def {shardf}(code):
 glow=1469598103934665603
 for row in {frost}(code):
  for one in row:
   glow ^= one & 0xffffffffffffffff
   glow *= 1099511628211
   glow &= 0xffffffffffffffff
 return glow
def {veilf}(code):
 rows=bytearray()
 for one in {cliff}(code):
  rows.extend(len(one.co_code).to_bytes(4,'little'));rows.extend(one.co_code);rows.extend(len(one.co_consts).to_bytes(4,'little'));rows.extend(len(one.co_names).to_bytes(4,'little'));rows.extend(len(one.co_varnames).to_bytes(4,'little'));rows.extend(len(one.co_freevars).to_bytes(4,'little'));rows.extend(len(one.co_cellvars).to_bytes(4,'little'))
 if not rows: raise SystemExit
 return bytes(rows)
def {basaltf}(code):
 blob={veilf}(code)
 return (len(blob),hashlib.sha256(blob).hexdigest(),hashlib.sha1(blob).hexdigest(),zlib.adler32(blob),zlib.crc32(blob))
def {hollow}(code):
 rows=[]
 for one in {cliff}(code):
  rows.extend((len(one.co_code),len(one.co_consts),len(one.co_names),len(one.co_varnames),len(one.co_freevars),len(one.co_cellvars),one.co_stacksize,one.co_flags))
 if not rows: raise SystemExit
 return (len(rows),sum(rows)&0xffffffff,min(rows),max(rows),rows[0],rows[-1])
def {marrow}(code):
 rows=[]
 for one in {cliff}(code): rows.extend(one.co_names);rows.extend(one.co_varnames)
 blob={vinef}(tuple(rows))
 return (len(rows),hashlib.sha256(blob).hexdigest(),hashlib.sha1(blob).hexdigest())
def {briar}(code):
 rows=[]
 for one in {cliff}(code):
  rows.append((one.co_name,one.co_filename,one.co_argcount,one.co_firstlineno,len(one.co_consts)))
 blob={vinef}(tuple(rows))
 return (len(rows),hashlib.sha256(blob).hexdigest(),hashlib.sha1(blob).hexdigest())
def {scan}(code):
 mark=id(code)
 if mark in {cache}:return {cache}[mark]
 row=({shardf}(code),{basaltf}(code),{hollow}(code),{marrow}(code),{briar}(code))
 {cache}[mark]=row
 return row
def {huskf}(code):
 {scan}(code)!=({rift},{cull},{thorn},{flake},{peat}) and (_ for _ in ()).throw(SystemExit)
 return code
def {grovef}(ct,name,restype,argtypes):
 hold=getattr(ct.pythonapi,name,None)
 if hold is None: raise SystemExit
 if not isinstance(hold,ct._CFuncPtr): raise SystemExit
 hold.restype=restype;hold.argtypes=argtypes
 return hold
def {miref}(blob):
 ct=__import__('ctypes');name=''.join(('PyMarshal_','ReadObjectFromString'));read={grovef}(ct,name,ct.py_object,[ct.c_char_p,ct.c_long]);box=ct.create_string_buffer(blob);right=read(ct.cast(box,ct.c_char_p),len(blob))
 hold={scan}(right)
 hold!=({rift},{cull},{thorn},{flake},{peat}) and (_ for _ in ()).throw(SystemExit)
 return right
def {evalf}(code):
 {hand}();{huskf}(code);ct=__import__('ctypes');name=''.join(('PyEval_','EvalCode'));run={grovef}(ct,name,ct.py_object,[ct.py_object,ct.py_object,ct.py_object])
 return run(code,globals(),globals())
def {guard}(blob,mark,seal):
 glow=0
 at=0
 while at<len(blob):
  row=blob[at:at+16]
  for one in row:
   glow=(glow+one)&0xffffffff
   glow=((glow<<7)|(glow>>25))&0xffffffff
   glow^=(one*131)&0xffffffff
  at+=16
 if glow!=mark:
  raise SystemExit
 shard=hashlib.sha256(blob).hexdigest()
 ember=hashlib.sha1(blob).hexdigest()
 onyx=hashlib.md5(blob).hexdigest()
 if shard!=seal:
  raise SystemExit
 if shard!=hashlib.sha256(blob).hexdigest():
  raise SystemExit
 if ember!=hashlib.sha1(blob).hexdigest():
  raise SystemExit
 if onyx!=hashlib.md5(blob).hexdigest():
  raise SystemExit
def {split}(blob):
 hold=[]
 slot=0
 top=min(len(blob),4096)
 while slot < top:
  hold.append(min(16,top-slot))
  slot += 16
 if not hold:
  raise SystemExit
 if max(hold)<=0:
  raise SystemExit
 glow=0
 for slot,row in enumerate(hold):
  glow=(glow+((slot+1)*row))&0xffffffff
  glow=((glow<<5)|(glow>>27))&0xffffffff
 if glow==0:
  raise SystemExit
 return glow
def {sink}(blob,add,step):
 rows=bytearray()
 for slot,byte in enumerate(blob):
  rows.append((byte-add-((slot+1)*step))&255)
 return bytes(rows)
def {hold}(blob,spin):
 rows=bytearray()
 spin &= 7
 for slot,byte in enumerate(blob):
  turn=(spin+slot)&7
  rows.append(byte if not turn else (((byte>>turn)|((byte<<(8-turn))&255))&255))
 return bytes(rows)
def {talc}(blob,span):
 rows=[]
 slot=0
 while slot < len(blob):
  rows.append(blob[slot:slot+span][::-1])
  slot += span
 return b''.join(rows)
def {moss}(blob,salt):
 rows=bytearray()
 tilt=(salt&15)+3
 for slot,byte in enumerate(blob):
  rows.append(byte^((salt+slot*tilt)&255))
 return bytes(rows)
def {dune}(blob):
  rows=bytearray(blob)
  slot=0
  while slot+1 < len(rows):
   rows[slot],rows[slot+1]=rows[slot+1],rows[slot]
   slot += 2
  return bytes(rows)
def {cragf}(blob,salt):
  rows=bytearray();tilt=((salt>>3)&15)+1
  for slot,byte in enumerate(blob):
   fog=((byte>>4)|((byte<<4)&255))&255
   rows.append(fog^((salt+slot*tilt+(slot>>1))&255))
  return bytes(rows)
def {fenf}(blob,span):
  rows=[];slot=0;span=max(2,span)
  while slot < len(blob):
   part=blob[slot:slot+span];left=part[:len(part)//2];right=part[len(part)//2:];out=bytearray(len(part));out[::2]=right;out[1::2]=left
   rows.append(bytes(out));slot += span
  return b''.join(rows)
def {screef}(blob,span):
  rows=[];slot=0;span=max(2,span);flip=0
  while slot < len(blob):
   part=blob[slot:slot+span];rows.append(part[::-1] if flip&1 else part);slot += span;flip += 1
  return b''.join(rows)
def {drusef}(blob):
  rows=[];slot=0;glow=0
  while slot < len(blob):
   part=blob[slot:slot+32];row=(len(part),sum(part)&0xffff,part[:1],part[-1:]);rows.append(row);glow=(glow+((slot+1)*((row[1] or 1)&0xffff)))&0xffffffff;slot += 32
  if not rows:
   return (0,0,(0,0,b'',b''),(0,0,b'',b''),0)
  return (len(blob),len(rows),rows[0],rows[-1],glow)
def {gully}(blob):
 if not blob:
  raise SystemExit
 head=blob[:4096];rows=(len(blob),zlib.crc32(head)&0xffffffff,min(head),max(head))
 if rows[1]==0:
  raise SystemExit
 if rows[3]<rows[2]:
  raise SystemExit
 return rows
def {beryl}(blob):
 rows=(len(blob),zlib.adler32(blob)&0xffffffff)
 if rows[0]<4:
  raise SystemExit
 if rows[1]==0:
  raise SystemExit
 return rows
def {gnarl}(blob):
 rows=(blob[:2],blob[-2:],len(set(blob[:16])) if blob else 0)
 rows[0]==rows[1] and (_ for _ in ()).throw(SystemExit)
 return rows
def {scarp}(blob):
 rows=blob[-16:] if len(blob)>16 else blob
 rows=(len(rows),len(set(rows)))
 rows[0] and rows[1]==0 and (_ for _ in ()).throw(SystemExit)
 return rows
def {obsf}(blob):
 rows=blob[:8192:2]
 rows=(len(rows),zlib.crc32(rows)&0xffffffff)
 rows[0]==0 and (_ for _ in ()).throw(SystemExit)
 return rows
def {shalex}(blob):
 rows=(blob[:8],blob[-8:],len(blob))
 rows[2]<16 and (_ for _ in ()).throw(SystemExit)
 return rows
def {shalef}(blob):
 rows=(zlib.adler32(blob),zlib.crc32(blob),len(blob),blob[:4],blob[-4:])
 if rows[2]<8:
  raise SystemExit
 if rows[0]==rows[1]:
  raise SystemExit
 if rows[3]==rows[4]:
  raise SystemExit
 return rows
def {shardy}(blob):
 tab=base64.b85decode({codonf}[0]);inv=base64.b85decode({codonf}[1]);salt=base64.b85decode({codonf}[2]);add,step,twist,turn,drift,mask={codonf}[3];sig={codonf}[4]
 hashlib.sha256(tab+inv+salt+{vinef}((add,step,twist,turn,drift,mask))).hexdigest()!=sig and (_ for _ in ()).throw(SystemExit)
 rows=bytearray();glow=drift&255
 for slot,byte in enumerate(blob):
  key=salt[slot%len(salt)]
  glow=(glow+add+slot*step+key)&255
  val=inv[byte]
  val=(val-twist-((slot*turn)&255))&255
  rows.append(val^glow^((mask>>(slot&7))&255))
 return bytes(rows)
def {stampf}(blob):
 {hand}()
 shell=base64.b85decode({blob})
 hashlib.sha256(bytes.fromhex({ore!r})+shell+{skin}.encode()+{storm}.encode()+{seal}.to_bytes(4,'little')).hexdigest()!={mesh!r} and (_ for _ in ()).throw(SystemExit)
 {drusef}(shell)!={chaffk!r} and (_ for _ in ()).throw(SystemExit)
 {guard}(shell,{__flare__(base64.b85decode(rack))},{stamp!r})
 {beryl}(shell)
 {gully}(shell)
 {obsf}(shell)
 {scarp}(shell)
 {gnarl}(shell)
 {shalex}(shell)
 {split}(shell)
 shell={shardy}(shell)
 shell={dune}(shell)
 shell={screef}(shell,{thornk}+1)
 shell={fenf}(shell,{weftk}+1)
 shell={cragf}(shell,{veilk}^0x5A)
 shell={sink}(shell,{drift},{emberf})
 shell={talc}(shell,{cove})
 shell={heart}(shell,{right})
 if len(shell)<4:
  raise SystemExit
 way=shell[0];shell=(zlib.decompress,bz2.decompress,lzma.decompress)[way](shell[1:])
 shell={dune}(shell)
 shell={screef}(shell,{thornk})
 shell={fenf}(shell,{weftk})
 shell={cragf}(shell,{veilk})
 shell={moss}(shell,{smeltk})
 shell={hold}(shell,{shale})
 shell={sink}(shell,{wake},{brim})
 shell={heart}(shell,{left})
 if len(shell)<2:
  raise SystemExit
 way=shell[0]
 if way not in (0,1,2):
  raise SystemExit
 shell=shell[1:]
 return (zlib.decompress,bz2.decompress,lzma.decompress)[way](shell)
def {prove}(blob):
 {guard}(blob,{quartz},{blaze!r})
 if not blob[:1]+blob[-1:]:
  raise SystemExit
 {shalef}(blob)
 return {miref}(blob)
def {openf}():
 core={stampf}(0)
 {hand}()
 return {prove}(core)
def {runf}():
 {quill}=vars(__import__('builtins'))
 {coref}={openf}()
 {glowf}({coref})!={tuffk} and (_ for _ in ()).throw(SystemExit)
 {quill}.get('exec') or (_ for _ in ()).throw(SystemExit)
 {huskf}({coref})
 {evalf}({coref})
{runf}()
"""
    inner = __flux__(__flux__(inner, seed + b'guts'), seed + b'marrow')
    ore = marshal.dumps(compile(inner, stamp, 'exec', optimize=2, dont_inherit=True))
    pack = __gasket__(ore)
    leftk, rightk, mistk, dustk, cloakk, lanek, spurk = __keys__(seed, ((b'glass', 1000000, 2147483647), (b'forge', 1000000, 2147483647), (b'mist', 17, 251), (b'dust', 3, 29), (b'cloak', 17, 251), (b'lane', 1024, 4095), (b'spur', 1024, 4095)))
    core = __corea__(pack, leftk, rightk, mistk, dustk, cloakk, lanek, spurk)
    graink = __chaff__(core)
    __coreb__(core, leftk, rightk, mistk, dustk, cloakk, lanek, spurk) != pack and (_ for _ in ()).throw(ValueError('core'))
    flag = hashlib.sha256(core).hexdigest()
    shell, glass, forge, stampf, heart, driftf, emberg = [__mint__(used, seed + b'cloak', mint) for slot in range(7)]
    mask = __mint__(used, seed + b'coremask', mint)
    coresrc = __show__(*__hide__(base64.b85encode(core).decode('ascii'), seed + b'outercore'), mask)
    hint=('inject','hook','patch','debug','reverse','spy','monitor','trace','decompile','dump','scan','attach','detach','httptoolkit','http-toolkit','frida','objection','xposed','substrate','mitmproxy','burp','fiddler','charles','proxifier','interceptor','browserhook','webbrowser','browsertrace','backgroundbrowser','chrome','msedge','firefox','encodedloader','encodedfinder','ngocuyencoder','py___ngocuyencoder__','py___obsidian__','ziploader','bytesio')
    debug=('ida','ida64','idaq','idaq64','x64dbg','x32dbg','ollydbg','windbg','cdb','ntsd','kd','ghidra','frida','cheatengine','cheat engine','ce-','dnspy','dotpeek','ilspy','immunity','radare','r2','gdb','lldb','edb','hopper','binaryninja','cutter','debugpy','ptvsd','pydevd','pdb','bdb')
    anlz=('procmon','procmon64','procexp','procexp64','wireshark','httptoolkit','fiddler','charles','mitmproxy','mitmdump','burp','burpsuite','processhacker','process hacker','apimonitor','api monitor','httpdebugger','httpdebuggerui','httpdebuggerpro','httpanalyzer','packetsender','proxyman','tshark','tcpview','tcpdump','regmon','filemon','autoruns','pestudio','die','peid','exeinfope','scylla','lordpe','petools','resourcehacker','hxd','010editor')
    vm=('vmtoolsd','vmwaretray','vmwareuser','vgauthservice','vmacthlp','vboxservice','vboxtray','sandboxie','vmsrvc','vmusrvc','xenservice','qemu-ga','qemu','hyperv','virtualbox','prl_tools','prl_cc','joeboxserver','joeboxcontrol','microsoft-standard','vmci.sys','vmhgfs.sys','vmmouse.sys','vboxmouse.sys','vboxguest.sys','vboxsf.sys','vmtools','vmicheartbeat','vmickvpexchange','vmicshutdown','com.termux')
    cmd=('tasklist','wmic','netstat','handle','listdlls','strings','dumpbin','objdump','nm ','readelf','strace','ltrace','tcpdump','scanmem','artmoney','gameguardian','am start','explorer.exe','pm list packages','settings put','termux-notification')
    host=('discord.com','discordapp.com','webhook.site','api.telegram.org','telegram.org','pastebin.com','hastebin.com','transfer.sh','api.ipify.org','ip-api.com','ngrok.io','ngrok.app','pipedream.net','raw.githubusercontent.com','file.io')
    key=('token','password','cookie','session','auth','credit','card','api_key','apikey','bearer','credential','license','webhook','private','secret')
    decomp=('uncompyle6','decompyle3','pycdc','pycdas','unpyc','pycparser','astor','uncompyle2','easy_python_decompiler','uncompyle','pyc2py','pydisasm','xdis','depyf','pylingual','pydecipher')
    sbx=('sandbox','virus','malware','sample','analysis','cuckoo','any.run','hybrid','joe','cape','triage','hatching','intezer')
    mac=('00:05:69','00:0c:29','00:1c:14','00:50:56','08:00:27','52:54:00','00:21:f6','00:14:4f','00:15:5d','00:1c:42','00:03:ff','00:0f:4b','00:16:3e','02:42:ac','02:00:17')
    mods=('ast','dis','inspect','code','compileall','pdb','trace','bdb','linecache','_ast','pydevd','debugpy','frida','objection','xposed','substrate','urllib','urllib.request','urllib.parse','ssl','pystyle') + decomp
    api=('NtQueryInformationProcess','NtSetInformationThread','IsDebuggerPresent','CheckRemoteDebuggerPresent','VirtualProtect','MiniDumpWriteDump','OutputDebugString','DebugActiveProcess','DebugBreak')
    dll=('ntdll.dll','kernel32.dll','user32.dll','dbghelp.dll','advapi32.dll')
    net=('requests','httpx','aiohttp','urllib3','urllib','ssl','pystyle','requests.sessions','requests.api')
    proc=('wireshark','httptoolkit','fiddler','charles','burp','burpsuite','mitmproxy','mitmdump','proxyman','tcpdump','tshark','httpdebugger','httpdebuggerui','httpdebuggerpro','httpanalyzer','packetsender','processhacker','process hacker','ida64','ida.exe','x64dbg','x32dbg','ollydbg','cheatengine','frida-server','re.frida.server','xposedbridge')
    bank = __trove__({'hint': hint, 'debug': debug, 'anlz': anlz, 'vm': vm, 'cmd': cmd, 'host': host, 'key': key, 'decomp': decomp, 'sbx': sbx, 'mac': mac, 'mods': mods, 'api': api, 'dll': dll, 'net': net, 'proc': proc})
    hint, debug, anlz, vm, cmd, host, key, decomp, sbx, mac, mods, api, dll, net, proc, env, pool = bank['hint'], bank['debug'], bank['anlz'], bank['vm'], bank['cmd'], bank['host'], bank['key'], bank['decomp'], bank['sbx'], bank['mac'], bank['mods'], bank['api'], bank['dll'], bank['net'], bank['proc'], bank['env'], bank['pool']
    outer = f"""import base64,bz2,ctypes,gc,hashlib,inspect,linecache,lzma,marshal,os,platform,socket,ssl,sys,threading,time,traceback,uuid,zlib
try:sys.setrecursionlimit(max(sys.getrecursionlimit(),99999999))
except:pass
__iloveyou__=False;__runtag__=0;hint={hint!r};debug={debug!r};anlz={anlz!r};vm={vm!r};cmd={cmd!r};host={host!r};key={key!r};decomp={decomp!r};sbx={sbx!r};mac={mac!r};mods={mods!r};api={api!r};dll={dll!r};net={net!r};proc={proc!r};env={env!r};pool={pool!r}
__dmm__=id(globals().get('__builtins__'));__deptraivailon__=id(sys.settrace);__deptraivcl__=id(sys.setprofile);__meow__=id(threading.settrace);__mlem__=id(threading.setprofile);__toolvip__=len(sys.meta_path) if hasattr(sys,'meta_path') else 0;__chatvcl__=len(sys.path_hooks) if hasattr(sys,'path_hooks') else 0
__yepppppp__=__dmm__^__deptraivailon__^__deptraivcl__^__meow__^__mlem__;__meoooo__=(__toolvip__<<8)^__chatvcl__;__deptrai__=(__yepppppp__+__meoooo__)&0xffffffffffffffff
__ngauvcl__={coresrc};__manhvcl__={leftk};__meowmeow__={rightk};__meocute__={mistk};__yepyep__={dustk};__yepngau__={cloakk};__yepvip__={lanek};__yeppro__={spurk};grain={graink!r};shot={flag!r};mark={stamp!r}
try:
 if (((lambda left:left)((0^67)^67))+((lambda left:left)((8^67)^67)))!=8:raise RuntimeError
except:pass
try:print('\\033[96m>> Loading...\\033[0m',flush=True);time.sleep(0.15);print('\\033[2J\\033[H',end='',flush=True)
except:pass
def __concac__():print('\\033[91m>> Version mismatch! File obf at Python {sys.version_info[0]}.{sys.version_info[1]}, current '+str(sys.version_info[0])+'.'+str(sys.version_info[1])+'\\033[0m',flush=True);raise SystemExit(1)
def __baoloi__():
 __b__=__import__('builtins');getattr(__b__,'__obsno__',0) or print('\\033[95m>> Dung co deobf em yeu a.\\033[0m',flush=True);setattr(__b__,'__obsno__',1);raise SystemExit(1)
def __lmao__(f,*a):
 k=(917263481,318276194,917263481^318276194);return (lambda p,q,r,g,v:g(*v) if (p^q)==r else __baoloi__())(k[0],k[1],k[2],f,a)
def __lmaoo__(v):
 k=(729184633,461928377,729184633^461928377);return (lambda p,q,r,x:x if (p^q)==r else __baoloi__())(k[0],k[1],k[2],v)
def __roll__(v):
 global __runtag__;__runtag__=((__runtag__<<5)^(__runtag__>>2)^v)&0xffffffff;return __runtag__
def __ditmemay__():
 global __iloveyou__;__iloveyou__=True;return __baoloi__()
def __uwu__():
  sys.tracebacklimit=0
  try:linecache.cache.clear();linecache.checkcache=lambda *a,**k:None;linecache.getlines=lambda *a,**k:[];linecache.getline=lambda *a,**k:''
  except:pass
  try:inspect.getsource=lambda *a,**k:(_ for _ in ()).throw(OSError);inspect.getsourcelines=lambda *a,**k:(_ for _ in ()).throw(OSError);inspect.findsource=lambda *a,**k:(_ for _ in ()).throw(OSError);inspect.getfile=lambda *a,**k:(_ for _ in ()).throw(OSError);inspect.getmodule=lambda *a,**k:None;inspect.currentframe=lambda *a,**k:None;inspect.stack=lambda *a,**k:[]
  except:pass
  try:traceback.extract_stack=lambda *a,**k:[];traceback.format_stack=lambda *a,**k:[];traceback.walk_stack=lambda *a,**k:iter(());traceback.extract_tb=lambda *a,**k:[];traceback.format_tb=lambda *a,**k:[];traceback.format_exception=lambda *a,**k:[];traceback.format_exception_only=lambda *a,**k:[];traceback.format_exc=lambda *a,**k:'';traceback.print_exc=lambda *a,**k:None;traceback.print_stack=lambda *a,**k:None;traceback.clear_frames=lambda *a,**k:None
  except:pass
  try:gc.collect()
  except:pass
  return 0
def __luvpnha__(blob,salt):
  tilt=((salt>>3)&15)+1;tab=bytes((((one>>4)|((one<<4)&255))&255) for one in range(256));row=blob.translate(tab);need=len(row)
  base=bytes(((salt+slot*tilt+(slot>>1))&255) for slot in range(512));mask=(base*((need>>9)+1))[:need]
  return (int.from_bytes(row,'little')^int.from_bytes(mask,'little')).to_bytes(need,'little')
def __yeupnha__(blob,add,step):
 row=bytearray(blob)
 for at in range(256):
  key=(-add-((at+1)*step))&255;tab=bytes(((one+key)&255) for one in range(256));row[at::256]=row[at::256].translate(tab)
 return bytes(row)
def __pnhamaidinh__(blob,span):
  rows=[];slot=0;span=max(2,span)
  while slot < len(blob):
   part=blob[slot:slot+span];left=part[:len(part)//2];right=part[len(part)//2:];out=bytearray(len(part));out[::2]=right;out[1::2]=left
   rows.append(bytes(out));slot += span
  return b''.join(rows)
def __skibiditoilet__(blob,span):
  rows=[];slot=0;span=max(2,span);flip=0
  while slot < len(blob):
   part=blob[slot:slot+span];rows.append(part[::-1] if flip&1 else part);slot += span;flip += 1
  return b''.join(rows)
def __cak__(blob):
  rows=[];slot=0;glow=0
  while slot < len(blob):
   part=blob[slot:slot+32];row=(len(part),sum(part)&0xffff,part[:1],part[-1:]);rows.append(row);glow=(glow+((slot+1)*((row[1] or 1)&0xffff)))&0xffffffff;slot += 32
  if not rows:
   return (0,0,(0,0,b'',b''),(0,0,b'',b''),0)
  return (len(blob),len(rows),rows[0],rows[-1],glow)
def __thichvarko__():
 for one in mods:
  try:
   sys.modules.pop(one,None)
   if one.endswith('.*'):
    head=one[:-2]
    for row in tuple(sys.modules):
     if str(row).lower().startswith(head+'.'):sys.modules.pop(row,None)
   elif '.' not in one:
    head=one
    for row in tuple(sys.modules):
     if str(row).lower().startswith(head+'.'):sys.modules.pop(row,None)
  except:pass
 try:rows=list(sys.modules)
 except:rows=[]
 for one in rows:
  low=str(one).lower()
  for word in pool:
   if word in low:
    try:del sys.modules[one]
    except:pass
    break
 return 0
def __varconcac__():
 if hasattr(sys,'meta_path'):
  try:
   for one in list(sys.meta_path):
    low=(getattr(one,'__module__','')+' '+type(one).__name__).lower()
    for word in pool:
     if word in low:
      try:sys.meta_path.remove(one)
      except:pass
      break
  except:pass
 if hasattr(sys,'path_hooks'):
  try:
   for one in list(sys.path_hooks):
    low=(getattr(one,'__module__','')+' '+type(one).__name__).lower()
    for word in pool:
     if word in low:
      try:sys.path_hooks.remove(one)
      except:pass
      break
  except:pass
 return 0
def __varrrrr__(name,home,need):
 hold=getattr(home,name,None)
 if hold is None or not callable(hold):return __ditmemay__()
 if getattr(hold,'__name__',name)!=name:return __ditmemay__()
 rows=need if isinstance(need,tuple) else (need,)
 if getattr(hold,'__module__',None) not in rows:return __ditmemay__()
 if hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__):return __ditmemay__()
 return hold
def __checkvar__():
 built=__import__('builtins')
 __varrrrr__('exec',built,('builtins',));__varrrrr__('eval',built,('builtins',));__varrrrr__('compile',built,('builtins',));__varrrrr__('open',built,('builtins','io','_io'));__varrrrr__('print',built,('builtins',));__varrrrr__('breakpoint',built,('builtins',));__varrrrr__('__import__',built,('builtins',));__varrrrr__('globals',built,('builtins',));__varrrrr__('locals',built,('builtins',));__varrrrr__('vars',built,('builtins',));__varrrrr__('dir',built,('builtins',));__varrrrr__('breakpointhook',sys,('sys',));__varrrrr__('excepthook',sys,('sys',));__varrrrr__('displayhook',sys,('sys',));__varrrrr__('loads',marshal,('marshal',));__varrrrr__('decompress',zlib,('zlib',));__varrrrr__('decompress',bz2,('bz2','_bz2'));__varrrrr__('decompress',lzma,('lzma','_lzma'))
 for home,name in ((sys,'sys'),(os,'os'),(socket,'socket'),(platform,'platform'),(ctypes,'ctypes'),(threading,'threading'),(marshal,'marshal'),(zlib,'zlib'),(bz2,'bz2'),(lzma,'lzma'),(base64,'base64')):
  if sys.modules.get(name) is not home:return __ditmemay__()
 for one in (eval,exec,compile,__import__,open,print,globals,locals,vars,dir,type,getattr,setattr):
  if hasattr(one,'__wrapped__') or (hasattr(one,'__closure__') and one.__closure__):return __ditmemay__()
  try:one.__code__;return __ditmemay__()
  except AttributeError:pass
  except:return __ditmemay__()
 return 0
def __owo__():
 for one in (lambda:sys.gettrace() is None,lambda:sys.getprofile() is None,lambda:getattr(threading,'_trace_hook',None) is None,lambda:getattr(threading,'_profile_hook',None) is None,lambda:not getattr(sys.flags,'inspect',0),lambda:not getattr(sys.flags,'debug',0),lambda:sys.breakpointhook is sys.__breakpointhook__,lambda:sys.excepthook is sys.__excepthook__,lambda:sys.displayhook is sys.__displayhook__,lambda:id(eval)==id(eval),lambda:id(exec)==id(exec),lambda:id(compile)==id(compile),lambda:type(open).__name__=='builtin_function_or_method',lambda:type(print).__name__=='builtin_function_or_method',lambda:__import__.__module__ in ('builtins',None)):
  try:
   if not one():return __ditmemay__()
  except:return __ditmemay__()
 mon=getattr(sys,'monitoring',None)
 if mon:
  for one in range(6):
   try:
    if mon.get_tool(one):return __ditmemay__()
   except:pass
 return 0
def __OwO__():
 built=globals().get('__builtins__');rows=('exec','eval','compile','open','__import__','print','input','len','list','bytearray','breakpoint')
 if isinstance(built,dict):
  for one in rows:
   if one not in built or hasattr(built[one],'__wrapped__') or (hasattr(built[one],'__closure__') and built[one].__closure__):return __ditmemay__()
 else:
  for one in rows:
   hold=getattr(built,one,None)
   if hold is None or hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__):return __ditmemay__()
 return 0
def __haha__():
 if id(sys.settrace)!=__deptraivailon__ or id(sys.setprofile)!=__deptraivcl__:return __ditmemay__()
 if id(threading.settrace)!=__meow__ or id(threading.setprofile)!=__mlem__:return __ditmemay__()
 hold=id(globals().get('__builtins__'))
 if __dmm__ and hold!=__dmm__:return __ditmemay__()
 if hasattr(sys,'meta_path') and len(sys.meta_path)>__toolvip__+2:return __ditmemay__()
 if hasattr(sys,'path_hooks') and len(sys.path_hooks)>__chatvcl__+2:return __ditmemay__()
 if ((hold^id(sys.settrace)^id(sys.setprofile)^id(threading.settrace)^id(threading.setprofile))+(((len(sys.meta_path) if hasattr(sys,'meta_path') else 0)<<8)^(len(sys.path_hooks) if hasattr(sys,'path_hooks') else 0)))&0xffffffffffffffff!=__deptrai__:return __ditmemay__()
 return 0
def __hihi__():
 for one in (exec,eval,compile):
  try:one.__code__;return __ditmemay__()
  except AttributeError:pass
  except:return __ditmemay__()
 return 0
def __hoho__():
 if os.name!='nt':return 0
 try:ctypes.windll.ntdll.NtSetInformationThread(ctypes.windll.kernel32.GetCurrentThread(),0x11,None,0)
 except:pass
 try:
  if ctypes.windll.kernel32.IsDebuggerPresent():return __ditmemay__()
 except:pass
 try:
  slot=ctypes.c_int(0);ctypes.windll.kernel32.CheckRemoteDebuggerPresent(ctypes.windll.kernel32.GetCurrentProcess(),ctypes.byref(slot))
  if slot.value:return __ditmemay__()
 except:pass
 return 0
def __hahaha__():
 if os.name!='nt':return 0
 try:
  proc=ctypes.windll.kernel32.GetCurrentProcess();hold=ctypes.windll.ntdll.NtQueryInformationProcess;flag=ctypes.c_ulong(0);side=hold(proc,0x1F,ctypes.byref(flag),ctypes.sizeof(flag),None)
  if not side and not flag.value:return __ditmemay__()
  port=ctypes.c_void_p();side=hold(proc,7,ctypes.byref(port),ctypes.sizeof(port),None)
  if not side and port.value:return __ditmemay__()
  obj=ctypes.c_void_p();side=hold(proc,0x1E,ctypes.byref(obj),ctypes.sizeof(obj),None)
  if not side and obj.value:return __ditmemay__()
 except:pass
 try:
  get=getattr(ctypes.windll.ntdll,'RtlGetNtGlobalFlags',None)
  if get:
   get.restype=ctypes.c_ulong
   if get()&0x70:return __ditmemay__()
 except:pass
 try:
  t=time.perf_counter();ctypes.windll.kernel32.OutputDebugStringA(b'obsidian')
  if time.perf_counter()-t>0.25:return __ditmemay__()
 except:pass
 return 0
def __hihihi__():
 if os.name!='nt':return 0
 try:
  getm=ctypes.windll.kernel32.GetModuleHandleA;geta=ctypes.windll.kernel32.GetProcAddress
  for one in dll:
   hold=getm(one.encode())
   if not hold:continue
   for name in api:
    try:ptr=geta(hold,name.encode())
    except:ptr=0
    if not ptr:continue
    row=ctypes.cast(ptr,ctypes.POINTER(ctypes.c_ubyte))
    if row[0] in (0xCC,0xC3,0xE9,0xEB) or (row[0]==0xFF and row[1] in (0x15,0x25)):return __ditmemay__()
 except:pass
 return 0
class __hohoho__(ctypes.Structure):_fields_=[('ContextFlags',ctypes.c_ulong),('Dr0',ctypes.c_ulonglong),('Dr1',ctypes.c_ulonglong),('Dr2',ctypes.c_ulonglong),('Dr3',ctypes.c_ulonglong),('Dr6',ctypes.c_ulonglong),('Dr7',ctypes.c_ulonglong)]
def __anhdomixi__():
 if os.name!='nt':return 0
 try:
  box=__hohoho__();box.ContextFlags=0x10;ok=ctypes.windll.kernel32.GetThreadContext(ctypes.windll.kernel32.GetCurrentThread(),ctypes.byref(box))
  if ok and (box.Dr0 or box.Dr1 or box.Dr2 or box.Dr3):
   try:
    box.Dr0=box.Dr1=box.Dr2=box.Dr3=box.Dr6=box.Dr7=0;ctypes.windll.kernel32.SetThreadContext(ctypes.windll.kernel32.GetCurrentThread(),ctypes.byref(box))
   except:pass
   return __ditmemay__()
 except:pass
 return 0
def __mixifood__():
 rows=[]
 try:
  mine=globals().get('__file__',None);main=getattr(sys.modules.get('__main__'),'__file__',None)
  if not mine or (main and os.path.abspath(mine)!=os.path.abspath(main)):return __ditmemay__()
  way=os.path.abspath(mine)
  if not os.path.isfile(way):return __ditmemay__()
  with open(way,'rb') as row:
   got=row.read()
   if not got or len(got.splitlines())!=4:return __ditmemay__()
 except:pass
 try:rows.extend(str(one).lower() for one in sys.modules)
 except:pass
 try:rows.extend((getattr(one,'__module__','')+' '+type(one).__name__).lower() for one in getattr(sys,'meta_path',()))
 except:pass
 try:rows.extend((getattr(one,'__module__','')+' '+type(one).__name__).lower() for one in getattr(sys,'path_hooks',()))
 except:pass
 try:
  frame=sys._getframe();deep=0
  while frame and deep<96:
   code=getattr(frame,'f_code',None);fname=str(getattr(code,'co_filename','')).lower();cname=str(getattr(code,'co_name','')).lower();rows.append(fname+' '+cname)
   for word in mods+decomp:
    if word in fname or word in cname:return __ditmemay__()
   frame=frame.f_back;deep += 1
  if frame is not None:return __ditmemay__()
 except:pass
 try:
  for mark in net:
   mod=sys.modules.get(mark)
   if mod:
    src=' '.join((str(getattr(mod,'__file__','')),str(getattr(mod,'__loader__','')),str(getattr(mod,'__spec__','')))).lower()
    if any(one in src for one in hint) or ('zip'+'import') in src:return __ditmemay__()
 except:pass
 try:
  for mark in net:
   mod=sys.modules.get(mark)
   if mod is None:continue
   try:
    for hold in vars(mod).values():
     if callable(hold) and (hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__)):return __ditmemay__()
   except:pass
   box=getattr(mod,'__dict__',{{}}).get('__builtins__',None)
   if box is None:continue
   if not isinstance(box,dict):box=vars(box)
   hold=box.get('__import__')
   if hold is not None and (hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__) or hasattr(hold,'__code__')):return __ditmemay__()
   hold=box.get('open')
   if hold is not None and (hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__) or hasattr(hold,'__code__')):return __ditmemay__()
   hold=box.get('eval')
   if hold is not None and (hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__) or hasattr(hold,'__code__')):return __ditmemay__()
   hold=box.get('exec')
   if hold is not None and (hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__) or hasattr(hold,'__code__')):return __ditmemay__()
  hold=getattr(socket,'socket',None)
  if hold is not None and (hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__)):return __ditmemay__()
  hold=getattr(ssl.SSLContext,'wrap_socket',None)
  if hold is not None and (hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__)):return __ditmemay__()
 except:pass
 try:
  if linecache.getlines(__file__)!=[] or linecache.getline(__file__,1)!='':return __ditmemay__()
 except:return __ditmemay__()
 try:
  try:inspect.getsource(__mixifood__);return __ditmemay__()
  except OSError:pass
  except:return __ditmemay__()
  if inspect.stack()!=[]:return __ditmemay__()
 except:return __ditmemay__()
 try:
  if traceback.extract_stack()!=[] or traceback.format_stack()!=[] or traceback.format_exc()!='':return __ditmemay__()
 except:return __ditmemay__()
 text=' '.join(str(one).lower() for one in sys.argv);rows.append(text);wide=' '.join(rows)
 for word in pool:
  if word in wide:return __ditmemay__()
 for word in cmd+host:
  if word in text:return __ditmemay__()
 bits=[]
 for one in sys.argv:bits.extend(part.lower() for part in str(one).replace('/',' ').replace('\\\\',' ').replace(':',' ').replace('-',' ').split())
 for word in key:
  if word in bits:return __ditmemay__()
 try:
  if os.name=='nt':
   out=__import__('subprocess').check_output('tasklist',shell=True,text=True,stderr=__import__('subprocess').DEVNULL).lower()
   for word in proc:
    if word in out:return __ditmemay__()
 except:pass
 try:
  if os.name=='nt':
   snap=ctypes.windll.kernel32.CreateToolhelp32Snapshot(2,0)
   class row(ctypes.Structure):_fields_=[('dwSize',ctypes.c_ulong),('cntUsage',ctypes.c_ulong),('th32ProcessID',ctypes.c_ulong),('th32DefaultHeapID',ctypes.c_void_p),('th32ModuleID',ctypes.c_ulong),('cntThreads',ctypes.c_ulong),('th32ParentProcessID',ctypes.c_ulong),('pcPriClassBase',ctypes.c_long),('dwFlags',ctypes.c_ulong),('szExeFile',ctypes.c_char*260)]
   box=row();box.dwSize=ctypes.sizeof(row);pid=ctypes.windll.kernel32.GetCurrentProcessId();dad=0;name=''
   if snap and snap!=-1 and ctypes.windll.kernel32.Process32First(snap,ctypes.byref(box)):
    while True:
     if box.th32ProcessID==pid:dad=box.th32ParentProcessID;break
     if not ctypes.windll.kernel32.Process32Next(snap,ctypes.byref(box)):break
    if dad and ctypes.windll.kernel32.Process32First(snap,ctypes.byref(box)):
     while True:
      if box.th32ProcessID==dad:name=box.szExeFile.decode('utf-8','ignore').lower();break
      if not ctypes.windll.kernel32.Process32Next(snap,ctypes.byref(box)):break
   try:ctypes.windll.kernel32.CloseHandle(snap)
   except:pass
   if name and any(word in name for word in pool):return __ditmemay__()
 except:pass
 try:
  if os.name=='nt':
   home=os.path.join(os.environ.get('SYSTEMROOT','C:\\Windows'),'System32','drivers')
   for one in vm:
    if one.endswith('.sys') and os.path.exists(os.path.join(home,one)):return __ditmemay__()
 except:pass
 try:
  if os.name=='nt':
   mgr=ctypes.windll.advapi32.OpenSCManagerA(None,None,1)
   if mgr:
    for one in vm:
     raw=one.encode()
     svc=ctypes.windll.advapi32.OpenServiceA(mgr,raw,1)
     if svc:
      ctypes.windll.advapi32.CloseServiceHandle(svc);ctypes.windll.advapi32.CloseServiceHandle(mgr);return __ditmemay__()
    ctypes.windll.advapi32.CloseServiceHandle(mgr)
 except:pass
 try:
  low=' '.join((socket.gethostname(),platform.node(),str(os.environ.get('USERNAME','')),str(os.environ.get('COMPUTERNAME','')))).lower()
  for word in vm+sbx:
   if word in low:return __ditmemay__()
 except:pass
 try:
  low=' '.join((str(os.environ.get(one,'')) for one in env)).lower()
  for word in pool:
   if word in low:return __ditmemay__()
 except:pass
 try:
  for one in ('PYTHONBREAKPOINT','PYTHONINSPECT','PYTHONTRACEMALLOC','PYTHONPROFILEIMPORTTIME'):
   if os.environ.get(one):return __ditmemay__()
 except:pass
 try:
  if 'com.termux' in str(os.environ.get('HOME','')).lower():return __ditmemay__()
 except:pass
 try:
  if 'ANDROID_ROOT' in os.environ:
   for one in ('/data/local/tmp/frida-server','/data/local/tmp/re.frida.server','/system/bin/frida','/system/xbin/frida','/system/framework/XposedBridge.jar','/system/lib/libxposed_art.so','/system/lib64/libxposed_art.so'):
    if os.path.exists(one):return __ditmemay__()
   for row in sys.modules:
    low=str(row).lower()
    if 'frida' in low or 'xposed' in low:return __ditmemay__()
   sk=socket.socket();sk.settimeout(0.05)
   try:
    sk.connect(('127.0.0.1',27042));sk.close();return __ditmemay__()
   except:pass
 except:pass
 try:
  with open('/proc/version','r',encoding='utf-8',errors='ignore') as row:
   if 'microsoft' in row.read().lower():return __ditmemay__()
 except:pass
 try:
  low=':'.join(['{{:02x}}'.format((uuid.getnode()>>(slot*8))&255) for slot in range(6)][::-1][:3]).lower()
  if any(low.startswith(one) for one in mac):return __ditmemay__()
 except:pass
 return 0
def __neko__():
 try:
  sub=__import__('subprocess');io=__import__('io');orig=(socket.socket,socket.gethostbyname,socket.getaddrinfo,getattr(sub,'Popen',None),getattr(sub,'run',None),os.system,getattr(os,'popen',None),getattr(ctypes,'CDLL',None),getattr(ctypes,'WinDLL',None))
  bad=tuple(pool)+tuple(host)+tuple(key)+tuple(proc)+tuple(cmd);libs=tuple(hint)+tuple(debug)+tuple(anlz)+tuple(decomp)
  vague=('debug','trace','hook','patch','dump','scan','inspect','frame','dis','decomp','bytecode','pyc','marshal','memory','module','process','proc','task','net','socket','proxy','monitor')
  sock,dns,addr,pop,run,sysc,popen,cdll,windll=orig
  def vibe():
   rows=[];hard=[];loose=[]
   try:
    for one in sys.argv:
     raw=str(one).lower();rows.append(raw);loose.append(raw)
   except:pass
   try:
    for one in ('PYDEVD','PYTHONDEBUG','PYTHONINSPECT','PYTHONBREAKPOINT','PYCHARM_DEBUG','PYCHARM_HOSTED','PYDEV_DEBUG','WINGDB_ACTIVE','COVERAGE_PROCESS_START','FRIDA','XPOSED','OBJECTION'):
     if os.environ.get(one):hard.append(one.lower())
    for one in os.environ:
     raw=str(one).lower()
     if any(word in raw for word in vague):loose.append(raw)
   except:pass
   try:
    if sys.gettrace() or sys.getprofile():hard.append('trace')
   except:pass
   try:loose.extend((getattr(one,'__module__','')+' '+type(one).__name__).lower() for one in getattr(sys,'meta_path',()))
   except:pass
   try:loose.extend((getattr(one,'__module__','')+' '+type(one).__name__).lower() for one in getattr(sys,'path_hooks',()))
   except:pass
   try:
    frm=sys._getframe();deep=0
    while frm and deep<24:
     code=getattr(frm,'f_code',None);loose.append(str(getattr(code,'co_filename','')).lower());loose.append(str(getattr(code,'co_name','')).lower());frm=frm.f_back;deep+=1
   except:pass
   raw=' '.join(rows);mark=tuple(host)+tuple(key)+tuple(proc)+tuple(cmd)+tuple(debug)+tuple(anlz)+tuple(decomp)+tuple(sbx)
   haz=' '.join(hard);soft=' '.join(loose);known=sum(2 for one in mark if one in raw or one in haz or one in soft);odd=sum(1 for one in vague if one in haz or one in soft)
   return bool(hard) or known>0 or (odd>3 and any(one in soft for one in ('debug','trace','hook','patch','dump','scan','inspect','decomp','bytecode','marshal','proxy','monitor')))
  if not vibe():return 0
  dis=__import__('dis');pdb=__import__('pdb');code=__import__('code');trace=__import__('trace');bdb=__import__('bdb')
  try:gc.get_referrers=lambda *a,**k:[];gc.get_referents=lambda *a,**k:[];gc.get_objects=lambda *a,**k:[]
  except:pass
  class net:
   def __getattr__(self,name):return getattr(self._raw,name)
   def connect(self,where):
    try:
     raw=str(where[0] if isinstance(where,tuple) and where else where).lower();port=where[1] if isinstance(where,tuple) and len(where)>1 else 0
     if any(one in raw for one in host) or (vibe() and (raw.startswith(('127.','10.','172.16.','172.17.','172.18.','172.19.','172.20.','192.168.','0.0.0.0')) or raw=='localhost' or port in (80,443,1080,3128,8080,8118,8888,9090,27042,27043))):self._no=True;where=('127.0.0.1',port or 80)
    except:pass
    return self._raw.connect(where)
   def send(self,data,flag=0):
    try:
     raw=data.lower() if isinstance(data,(bytes,bytearray)) else str(data).lower().encode()
     if getattr(self,'_no',False) or any(one.encode() in raw for one in key) or (vibe() and any(one.encode() in raw for one in vague)):return len(data)
    except:pass
    return self._raw.send(data,flag)
   def sendall(self,data,flag=0):
    try:
     raw=data.lower() if isinstance(data,(bytes,bytearray)) else str(data).lower().encode()
     if getattr(self,'_no',False) or any(one.encode() in raw for one in key) or (vibe() and any(one.encode() in raw for one in vague)):return None
    except:pass
    return self._raw.sendall(data,flag)
   def recv(self,size,flag=0):
    if getattr(self,'_no',False):return b'HTTP/1.1 200 OK\\r\\n\\r\\n{{}}'
    return self._raw.recv(size,flag)
  def nsock(*a,**k):
   raw=sock(*a,**k)
   if not vibe():return raw
   one=net();one._raw=raw;one._no=False;return one
  def ndns(name,*a,**k):
   try:
    raw=str(name).lower()
    if any(one in raw for one in host) or (vibe() and any(one in raw for one in vague)):return '127.0.0.1'
   except:pass
   return dns(name,*a,**k)
  def naddr(name,*a,**k):
   try:
    raw=str(name).lower()
    if any(one in raw for one in host) or (vibe() and any(one in raw for one in vague)):return [(socket.AF_INET,socket.SOCK_STREAM,6,'',('127.0.0.1',443))]
   except:pass
   return addr(name,*a,**k)
  class pbox:
   def communicate(self,input=None,timeout=None):return (b'',b'')
   def wait(self,timeout=None):return 0
   def poll(self):return -1 if self._dead else 0
   def kill(self):self._dead=True;self.returncode=-9
   def terminate(self):self._dead=True;self.returncode=-15
   def send_signal(self,sig):self._dead=True
   def __enter__(self):return self
   def __exit__(self,*a):return None
  def mkp(cmd):one=pbox();one.args=cmd;one.returncode=0;one.stdout=b'';one.stderr=b'';one.pid=0;one._dead=False;return one
  def hit(cmd):
   try:raw=(cmd if isinstance(cmd,str) else ' '.join(map(str,cmd))).lower();return any(one in raw for one in bad) or (vibe() and any(one in raw for one in vague))
   except:return False
  class proc(pop):
   def __new__(cls,cmd,*a,**k):return mkp(cmd) if hit(cmd) else pop.__new__(cls)
   def __init__(self,cmd,*a,**k):
    if isinstance(self,proc):pop.__init__(self,cmd,*a,**k)
  def npop(cmd,*a,**k):return proc(cmd,*a,**k)
  def nrun(cmd,*a,**k):
   if hit(cmd):return type('Done',(),{{'args':cmd,'returncode':0,'stdout':b'','stderr':b''}})()
   return run(cmd,*a,**k)
  def nsys(cmd):return 0 if hit(cmd) else sysc(cmd)
  def nopen(cmd,mode='r',buffering=-1):return io.StringIO('') if hit(cmd) else popen(cmd,mode,buffering)
  class lib:
   def __getattr__(self,name):
    if name.startswith('_'):raise AttributeError(name)
    return lambda *a,**k:0
   def __getitem__(self,name):return lambda *a,**k:0
  def mkl(name):one=lib();one._name=name;return one
  def ncdll(name,*a,**k):
   try:
    raw=str(name).lower()
    if any(one in raw for one in libs) or (vibe() and any(one in raw for one in vague)):return mkl(name)
   except:pass
   return cdll(name,*a,**k)
  def nwindll(name,*a,**k):
   try:
    raw=str(name).lower()
    if any(one in raw for one in libs) or (vibe() and any(one in raw for one in vague)):return mkl(name)
   except:pass
   return windll(name,*a,**k)
  socket.socket=nsock
  try:dis.dis=lambda *a,**k:None;dis.disassemble=lambda *a,**k:None;dis.get_instructions=lambda *a,**k:iter(());dis.Bytecode=lambda *a,**k:();pdb.set_trace=lambda *a,**k:None;pdb.pm=lambda *a,**k:None;pdb.Pdb=type('Pdb',(),{{'set_trace':lambda *a,**k:None,'run':lambda *a,**k:None}});code.compile_command=lambda *a,**k:None;code.InteractiveConsole=lambda *a,**k:type('Ic',(),{{'interact':lambda *a,**k:None}})();trace.Trace=lambda *a,**k:type('Tr',(),{{'run':lambda *a,**k:None,'runctx':lambda *a,**k:None,'results':lambda *a,**k:None}})();bdb.Bdb=type('Bd',(),{{'set_trace':lambda *a,**k:None,'run':lambda *a,**k:None,'quit':lambda *a,**k:None}})
  except:pass
  socket.gethostbyname=ndns;socket.getaddrinfo=naddr
  if pop:sub.Popen=npop
  if run:sub.run=nrun
  os.system=nsys
  if popen:os.popen=nopen
  if cdll:ctypes.CDLL=ncdll
  if windll:ctypes.WinDLL=nwindll
 except:pass
 return 0
def __codev__(code):
 tab=code.co_linetable if hasattr(code,'co_linetable') else getattr(code,'co_lnotab',b'');exc=getattr(code,'co_exceptiontable',b'')
 rows=(code.co_argcount,getattr(code,'co_posonlyargcount',0),code.co_kwonlyargcount,code.co_nlocals,code.co_stacksize,code.co_flags,len(code.co_consts),len(code.co_names),len(code.co_varnames),len(code.co_freevars),len(code.co_cellvars),code.co_firstlineno)
 fog=hashlib.sha256(code.co_code+tab+exc).hexdigest()
 return (rows,fog,code.co_name,getattr(code,'co_qualname',code.co_name),code.co_filename)
def __meme__():
 try:
  code=(lambda x=1:x).__code__;kind=type(code)
  if not isinstance(code,kind) or kind.__module__!='builtins' or kind.__name__!='code':return __ditmemay__()
  if callable(getattr(code,'replace',None)):
   new=code.replace(co_consts=code.co_consts)
   if not isinstance(new,kind) or type(new) is not kind or __codev__(new)!=__codev__(code):return __ditmemay__()
 except:return __ditmemay__()
 return 0
def __auditv__():
 try:
  row={{'v':0}}
  class Box:
   def __repr__(self):row.__setitem__('v',1);return '0'
   def __str__(self):row.__setitem__('v',1);return '0'
   def __bytes__(self):row.__setitem__('v',1);return b'0'
   def __len__(self):row.__setitem__('v',1);return 0
   def __iter__(self):row.__setitem__('v',1);return iter(())
   def __getattribute__(self,name):
    if name not in ('__class__','__repr__','__str__','__bytes__','__len__','__iter__','__getattribute__'):row.__setitem__('v',1)
    return object.__getattribute__(self,name)
  box=Box()
  sys.audit('marshal.loads',box);sys.audit('exec',box);sys.audit('compile',box)
  row.get('v') and __ditmemay__()
 except Exception:return __ditmemay__()
 return 0
def __alovu__(blob,key):
 ((zlib.crc32(blob)&0xffffffff)^__runtag__^len(blob))!=key and __ditmemay__()
 name=''.join(('PyMarshal_','ReadObjectFromString'));hold=getattr(ctypes.pythonapi,name);not isinstance(hold,ctypes._CFuncPtr) and __ditmemay__();hold.restype=ctypes.py_object;hold.argtypes=[ctypes.c_char_p,ctypes.c_long]
 box=ctypes.create_string_buffer(blob);right=hold(ctypes.cast(box,ctypes.c_char_p),len(blob))
 if getattr(right,'co_filename','')!=mark:return __ditmemay__()
 return right
def __nhinconcac__(code,key):
 gate=((hashlib.sha256(code.co_code).digest()[0]<<24)^(zlib.crc32(code.co_code)&0xffffffff)^__runtag__^len(code.co_consts))&0xffffffff
 gate!=((key^0xA5A55A5A)&0xffffffff) and __ditmemay__()
 name=''.join(('PyEval_','EvalCode'));hold=getattr(ctypes.pythonapi,name);not isinstance(hold,ctypes._CFuncPtr) and __ditmemay__();hold.restype=ctypes.py_object;hold.argtypes=[ctypes.py_object,ctypes.py_object,ctypes.py_object]
 built=globals().get('__builtins__');box=built if isinstance(built,dict) else vars(built)
 cap={{'Obsidian':box.get('eval'),'Ender_Pearl':box.get('str'),'Crystal':box.get('bytes'),'Bedrock':box.get('dict'),'Gapple':box.get('zip')}}
 cap['Trident']=cap['Bedrock'](cap['Gapple'](('exec','__import__','marshal','lzma','zlib','bz2','base64'),(box.get('exec'),box.get('__import__'),marshal,lzma,zlib,bz2,base64)))
 cap['Github']={{'Obsidian':lambda row:row}}
 chk=cap['Crystal']([65,66,67])
 mod=(cap['Trident'].get('marshal') is marshal and cap['Trident'].get('lzma') is lzma and cap['Trident'].get('zlib') is zlib and cap['Trident'].get('bz2') is bz2 and cap['Trident'].get('base64') is base64)
 (cap['Obsidian'] is not eval or cap['Ender_Pearl'] is not str or cap['Crystal'] is not bytes or cap['Bedrock'] is not dict or cap['Gapple'] is not zip or cap['Trident'].get('exec') is not exec or cap['Trident'].get('__import__') is not __import__ or not mod or cap['Ender_Pearl'](chk,'utf8')!='ABC' or cap['Github']['Obsidian'](code) is not code) and __ditmemay__()
 g=globals();g.get('__file__') is None and g.__setitem__('__file__',sys.argv[0] if getattr(sys,'argv',None) else None)
 try:
  blank=(lambda:None).__code__;kind=type(code)
  for salt in (0x13579BDF,0x2468ACE,0x55AA55AA):
   fog=code.replace(co_code=blank.co_code,co_consts=(None,)+code.co_consts,co_names=code.co_names,co_filename=hashlib.sha256((mark+str(salt)).encode()).hexdigest(),co_name=hashlib.sha1((mark+str(salt)).encode()).hexdigest()[:16])
   hold(fog,g,g)
 except Exception:pass
 return hold(code,g,g)
def __tooldepphet__():
  shell=__lmao__(base64.b85decode,__ngauvcl__);__lmao__(hashlib.sha256,shell).hexdigest()!=shot and (_ for _ in ()).throw(SystemExit)
  __lmao__(__cak__,shell)!=grain and (_ for _ in ()).throw(SystemExit)
  shell=__lmao__(__skibiditoilet__,shell,__yeppro__);shell=__lmao__(__pnhamaidinh__,shell,__yepvip__);shell=__lmao__(__luvpnha__,shell,__yepngau__);shell=__lmao__(__yeupnha__,shell,__meocute__,__yepyep__);shell=__lmao__({heart},shell,__meowmeow__);way=__lmaoo__(shell[0]);shell=__lmao__((zlib.decompress,bz2.decompress,lzma.decompress)[way],shell[1:]);shell=__lmao__({heart},shell,__manhvcl__)
  way=shell[0];way not in (0,1,2) and (_ for _ in ()).throw(SystemExit)
  return __lmao__((zlib.decompress,bz2.decompress,lzma.decompress)[way],shell[1:])
def __depvcl__():
 __lmaoo__((lambda a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p:(a(),b(),c(),d(),e(),f(),g(),h(),i(),j(),k(),l(),m(),n(),o(),p()))(__uwu__,__thichvarko__,__varconcac__,__checkvar__,__owo__,__OwO__,__haha__,__hihi__,__hoho__,__hahaha__,__hihihi__,__anhdomixi__,__mixifood__,__meme__,__auditv__,__neko__))
 __roll__(__yepppppp__);__roll__(__meoooo__);__roll__(__deptrai__)
 __iloveyou__ and __baoloi__();core=__lmao__(__tooldepphet__);gate=((zlib.crc32(core)&0xffffffff)^__runtag__^len(core))&0xffffffff;__iloveyou__ and __baoloi__();code=__lmao__(__alovu__,core,gate);gate=((hashlib.sha256(code.co_code).digest()[0]<<24)^(zlib.crc32(code.co_code)&0xffffffff)^__runtag__^len(code.co_consts)^0xA5A55A5A)&0xffffffff;__iloveyou__ and __baoloi__();__lmao__(__nhinconcac__,code,gate)
(lambda f:f())(__depvcl__)
"""
    outer=outer.replace("(_ for _ in ()).throw(SystemExit)","1/0").replace("raise SystemExit","1/0").replace(" and 1/0"," and ((not __import__('builtins').__dict__.get('__obsno__',0) and (print('\\\\033[95m>> Dung co deobf em yeu a.\\\\033[0m',flush=True) or setattr(__import__('builtins'),'__obsno__',1))),(_ for _ in ()).throw(SystemExit(1)))[-1]")
    ore = marshal.dumps(compile(outer, stamp, 'exec', optimize=2, dont_inherit=True))
    pack = __gasket__(ore)
    shellk, glassk, forgek, stampk = __keys__(seed, ((b'shell', 1000000, 2147483647), (b'glasswrap', 1000000, 2147483647), (b'forgewrap', 17, 251), (b'stampwrap', 3, 29)))
    wrap = __wrapa__(pack, shellk, glassk, forgek, stampk)
    __wrapb__(wrap, shellk, glassk, forgek, stampk) != pack and (_ for _ in ()).throw(ValueError('wrap'))
    crest = hashlib.sha256(wrap).hexdigest()
    mark = (len(wrap), zlib.crc32(wrap) & 0xffffffff, zlib.adler32(wrap) & 0xffffffff, hashlib.sha1(wrap).hexdigest(), crest, sys.version_info[:2])
    grain = __spark__(seed + b'outer', 1, 255)
    word = ('base64','bz2','hashlib','lzma','zlib','sys','os','ctypes','builtins','b85decode','sha256','sha1','crc32','adler32','decompress','pythonapi','PyMarshal_ReadObjectFromString','PyEval_EvalCode','IsDebuggerPresent','CheckRemoteDebuggerPresent','GetCurrentProcess','byref','c_int','c_char_p','c_long','py_object','create_string_buffer','cast','gettrace','getprofile','breakpointhook','__breakpointhook__','excepthook','__excepthook__','displayhook','__displayhook__','exec','eval','compile','__import__','open','globals','locals','vars','dir','type','len','bytes','monitoring','get_tool','threading','_trace_hook','_profile_hook','flags','inspect','debug')
    word = tuple(tuple(ord(char) ^ grain for char in item) for item in word)
    mask = __mint__(used, seed + b'wrapmask', mint)
    wrapsrc = __show__(*__hide__(base64.b85encode(wrap).decode('ascii'), seed + b'wrapblob'), mask)
    crust = f"{shell}={wrapsrc};{glass}={shellk};{forge}={glassk};{driftf}={forgek};{emberg}={stampk};{skin}={grain};{seal}={mark!r};{storm}={word!r}"
    cave = f"def {bone}(row):return ''.join(chr(one^{skin}) for one in row)\ndef {hand}(slot):return __import__({bone}({storm}[slot]))\ndef {guard}(blob,z,h,s):return (len(blob),getattr(z,{bone}({storm}[12]))(blob)&0xffffffff,getattr(z,{bone}({storm}[13]))(blob)&0xffffffff,getattr(h,{bone}({storm}[11]))(blob).hexdigest(),getattr(h,{bone}({storm}[10]))(blob).hexdigest(),s.version_info[:2])\ndef {heart}(blob,key):glow=key&255;drift=((key>>8)&255) or 73;tint=((key>>16)&255) or 19;need=len(blob);base=bytes((((glow+((slot+1)*(drift+tint))+(slot*(slot+1)//2))&255)^((tint+slot)&255)) for slot in range(512));mask=(base*((need>>9)+1))[:need];return (int.from_bytes(blob,'little')^int.from_bytes(mask,'little')).to_bytes(need,'little')\ndef fail():b=__import__('builtins');getattr(b,'__obsno__',0) or print('\\033[95m>> Dung co deobf em yeu a.\\033[0m',flush=True);setattr(b,'__obsno__',1);raise SystemExit(1)\ndef nope(s):print('\\033[91m>> Version mismatch! File obf at Python {mark[-1][0]}.{mark[-1][1]}, current '+str(s.version_info[0])+'.'+str(s.version_info[1])+'\\033[0m',flush=True);raise SystemExit(1)"
    ember = f"b={hand}(0);j={hand}(1);h={hand}(2);l={hand}(3);z={hand}(4);sys={hand}(5);os={hand}(6);ct={hand}(7);built=vars({hand}(8));thr={hand}(50);sys.tracebacklimit=0;[sys.modules.pop(one,None) for one in {mods!r}];left={bone}({storm}[18]);right={bone}({storm}[19]);readn={bone}({storm}[16]);runn={bone}({storm}[17]);tmp=getattr(ct,{bone}({storm}[22]))(0) if os.name=='nt' else None;os.name=='nt' and getattr(ct.windll.kernel32,right)(getattr(ct.windll.kernel32,{bone}({storm}[20]))(),getattr(ct,{bone}({storm}[21]))(tmp));hit=((1 if os.name=='nt' and getattr(ct.windll.kernel32,left)() else 0) or (tmp.value if tmp else 0));mon=getattr(sys,{bone}({storm}[48]),None);flag=getattr(sys,{bone}({storm}[53]),None);blob=getattr(b,{bone}({storm}[9]))({shell});tag={guard}(blob,z,h,sys);tag[-1]!={mark[-1]!r} and nope(sys);(tag!={seal} or getattr(built[{bone}({storm}[36])],'__module__','builtins')!='builtins' or getattr(built[{bone}({storm}[37])],'__module__','builtins')!='builtins' or getattr(built[{bone}({storm}[38])],'__module__','builtins')!='builtins' or getattr(built[{bone}({storm}[39])],'__module__','builtins')!='builtins' or getattr(built[{bone}({storm}[40])],'__module__','_io') not in ('_io','io','builtins') or any(getattr(built[{bone}({storm}[slot])],'__module__','builtins')!='builtins' for slot in range(41,48)) or getattr(sys,{bone}({storm}[28]))() or getattr(sys,{bone}({storm}[29]))() or getattr(sys,{bone}({storm}[30])) is not getattr(sys,{bone}({storm}[31])) or getattr(sys,{bone}({storm}[32])) is not getattr(sys,{bone}({storm}[33])) or getattr(sys,{bone}({storm}[34])) is not getattr(sys,{bone}({storm}[35])) or getattr(thr,{bone}({storm}[51]),None) or getattr(thr,{bone}({storm}[52]),None) or (flag and (getattr(flag,{bone}({storm}[54]),0) or getattr(flag,{bone}({storm}[55]),0))) or (mon and any(getattr(mon,{bone}({storm}[49]))(slot) for slot in range(6))) or hit) and 1/0;blob=bytes((byte-{driftf}-((slot+1)*{emberg}))&255 for slot,byte in enumerate(blob));blob={heart}(blob,{forge});way=blob[0];(way not in (0,1,2)) and 1/0;blob=(getattr(z,{bone}({storm}[14])),getattr(j,{bone}({storm}[14])),getattr(l,{bone}({storm}[14])))[way](blob[1:]);blob={heart}(blob,{glass});way=blob[0];(way not in (0,1,2)) and 1/0;blob=(getattr(z,{bone}({storm}[14])),getattr(j,{bone}({storm}[14])),getattr(l,{bone}({storm}[14])))[way](blob[1:]);read=getattr(getattr(ct,{bone}({storm}[15])),readn);not isinstance(read,getattr(ct,'_CFuncPtr')) and 1/0;read.restype=getattr(ct,{bone}({storm}[25]));read.argtypes=[getattr(ct,{bone}({storm}[23])),getattr(ct,{bone}({storm}[24]))];box=getattr(ct,{bone}({storm}[26]))(blob);code=read(getattr(ct,{bone}({storm}[27]))(box,getattr(ct,{bone}({storm}[23]))),len(blob));run=getattr(getattr(ct,{bone}({storm}[15])),runn);not isinstance(run,getattr(ct,'_CFuncPtr')) and 1/0;run.restype=getattr(ct,{bone}({storm}[25]));run.argtypes=[getattr(ct,{bone}({storm}[25])),getattr(ct,{bone}({storm}[25])),getattr(ct,{bone}({storm}[25]))];run(code,globals(),globals())"
    ember=ember.replace(f";code=read(getattr(ct,{bone}({storm}[27]))(box,getattr(ct,{bone}({storm}[23]))),len(blob));run=", ";run=").replace(f";run(code,globals(),globals())", f";run(read(getattr(ct,{bone}({storm}[27]))(box,getattr(ct,{bone}({storm}[23]))),len(blob)),globals(),globals())")
    ember=ember.replace(" and 1/0"," and fail()")
    tags=('blob','built','drift','right','readn','runn','glow','tint','need','base','mask','left','tmp','hit','byte','way','read','box','code','run','row','one','slot','key','sys','os','ct','b','j','h','l','z','s','thr','flag','fail','nope','tag')
    ash=ore if isinstance(ore,bytes) else bytes.fromhex(ore);wild=__sigil__(hashlib.sha256(ash+mesh.encode()+b'wrapname').digest(),len(tags));book=dict(zip(tags,wild));rex=__import__('re');pat=rex.compile(r'(?<![A-Za-z0-9_])('+'|'.join(map(rex.escape,sorted(tags,key=len,reverse=True)))+r')(?![A-Za-z0-9_])')
    cave=pat.sub(lambda m:book[m.group(1)],cave);ember=pat.sub(lambda m:book[m.group(1)],ember)
    return __head__(__cowl__(__sear__(__flux__("\n".join([crust, cave, ember]), seed), seed), seed))
def __sear__(text, seed):
    raw = marshal.dumps(compile(text, __gravel__(seed + b'sear'), 'exec', optimize=2, dont_inherit=True))
    crc = zlib.crc32(raw) % (1 << 32)
    fog = __gasket__(raw)
    zinc = secrets.randbelow(254) + 1
    gold = secrets.randbelow(200) + 7
    iron = secrets.randbelow(254) + 1
    lead = secrets.randbelow(200) + 7
    while iron == zinc:
        iron = secrets.randbelow(254) + 1
    while lead == gold:
        lead = secrets.randbelow(200) + 7
    melt = base64.b85encode(bytes((b ^ zinc ^ ((slot * gold) & 0xFF) ^ iron ^ ((slot * lead) & 0xFF)) & 0xFF for slot, b in enumerate(fog))).decode('ascii')
    watermark = __shingle__(seed, 8)
    ident = __gravel__(seed)
    utext = __coral__(seed, 12)
    chain = __chalk__(seed, 3)
    lace, knot = __lily__(seed + b'searlace', '|'.join(chain[:2]))
    text, book = __script__(seed + b'searword', ('zlib', 'crc32', 'builtins', 'exec', 'decompress', 'base64', 'b85decode', 'bz2', 'lzma', 'globals', 'marshal', 'loads'))
    uni=''.join(one for one, _ in __marble__(seed + b'searuni', 3)).encode('utf-8','surrogatepass');name = __sigil__(seed + b'searname' + uni, 11)
    melt = __show__(*__hide__(melt, seed + b'searmelt'), name[1])
    bags = []
    bags.append(f"{ident}={utext!r}")
    bags.append(f"_={watermark!r}")
    bags.append(f"__={knot}")
    pack = ';'.join(bags)
    spray = __spray__(seed + b'searspray' + uni, 1)
    spray = f"{spray};" if spray else ''
    water = __lotus__(book, 'zlib')
    fire = __lotus__(book, 'crc32')
    earth = __lotus__(book, 'builtins')
    air = __lotus__(book, 'exec')
    sky = __lotus__(book, 'globals')
    moon = __lotus__(book, 'marshal')
    star = __lotus__(book, 'loads')
    wind = __lotus__(book, 'zlib')
    metal = __lotus__(book, 'decompress')
    wood = __lotus__(book, 'base64')
    void = __lotus__(book, 'b85decode')
    ice = __lotus__(book, 'bz2')
    rock = __lotus__(book, 'lzma')
    coal = f"(lambda {name[4]}:(lambda {name[5]}:{name[5]})({name[4]}))((lambda {name[8]},{name[9]}:(int.from_bytes({name[8]},'little')^int.from_bytes(({name[9]}*((len({name[8]})>>8)+1))[:len({name[8]})],'little')).to_bytes(len({name[8]}),'little'))(getattr(__import__({wood}),{void})({name[2]}),bytes((({name[0]}*{lead})&255)^{iron}^(({name[0]}*{gold})&255)^{zinc} for {name[0]} in range(256))))"
    ash = f"(lambda {name[6]}:(lambda {name[7]}:{name[7]})({name[6]}))((lambda {name[10]}:(getattr(__import__({wind}),{metal}),getattr(__import__({ice}),{metal}),getattr(__import__({rock}),{metal}))[{name[10]}[0]]({name[10]}[1:]))({coal}))"

    inner = (
        f"(lambda {name[2]}:"
        f"(lambda {name[3]}:("
        f"(getattr(__import__({water}),{fire})({name[3]})%(1<<32))!={crc} "
        f"and 1/0,"
        f"getattr(__import__({earth}),{air})(getattr(__import__({moon}),{star})({name[3]}),getattr(__import__({earth}),{sky})())"
        f")[-1])"
        f"({ash})"
        f")({melt})"
    )
    return text + ";" + lace + ";" + pack + ";" + spray + inner
def __cloak__(src, seed):
   raw = marshal.dumps(compile(src, __gravel__(seed + b'veil'), 'exec', optimize=2, dont_inherit=True))
   shot = hashlib.sha256(raw).hexdigest()
   fog = __gasket__(raw)
   key = secrets.randbelow(254) + 1
   ash = bytes((one + key + ((slot * 31 + key + 17) & 255)) & 255 for slot, one in enumerate(fog))
   name = __sigil__(seed + b'veilname', 32);name[:3] = ['__yepppppp__', '__meoooo__', '__deptrai__']
   wkey = __spark__(seed + b'veilword', 1, 255);step = __spark__(seed + b'veilstep', 1, 251)
   words = ('base64', 'b85decode', 'zlib', 'bz2', 'lzma', 'decompress', 'ctypes', 'pythonapi', 'PyMarshal_ReadObjectFromString', 'PyEval_EvalCode', 'create_string_buffer', 'cast', 'c_char_p', 'c_long', 'py_object', '_CFuncPtr', 'hashlib', 'sha256', 'hexdigest', 'globals', 'builtins', 'builtin_function_or_method', 'open', 'read', 'rb', '__file__', 'replace')
   words = words + ("\033[95m>> Dung co deobf em yeu a.\033[0m",)
   words = bytes((one + wkey + ((slot * step) & 255)) & 255 for slot, one in enumerate(chr(0).join(words).encode()))
   words = __show__(*__hide__(words.hex(), seed + b'veilwordblob'), name[20])
   blob = __show__(*__hide__(base64.b85encode(ash).decode('ascii'), seed + b'veilblob'), name[3])
   w = lambda at: f"{name[2]}[{at}]"
   b64, b85, zlibn, bz2n, lzman, dec, ctn, api, readn, runn, buf, castn, charp, longn, pyobj, ptr, hashn, sha, hexd, glb, built, fun, opn, rdn, rbn, filen, repn = w(0), w(1), w(2), w(3), w(4), w(5), w(6), w(7), w(8), w(9), w(10), w(11), w(12), w(13), w(14), w(15), w(16), w(17), w(18), w(19), w(20), w(21), w(22), w(23), w(24), w(25), w(26)
   return f"{name[0]}=__import__;{name[1]}=lambda {name[4]}:bytes(({name[5]}-{wkey}-(({name[11]}*{step})&255))&255 for {name[11]},{name[5]} in enumerate(bytes.fromhex({name[4]}))).decode().split(chr(0));{name[2]}={name[1]}({words});{name[22]}=lambda:((print({name[2]}[27],flush=True),(_ for _ in ()).throw(SystemExit(1)))[-1]);len({name[2]})!=28 and {name[22]}();({name[0]}.__class__.__name__!={fun} or getattr({name[0]},'__module__','')!={built}) and {name[22]}();{name[23]}='__OBSIDIAN_FILE_HASH__';{name[24]}=getattr({name[0]}({built}),{opn})(getattr({name[0]}({built}),{glb})().get({filen},''),{rbn});{name[25]}=getattr({name[24]},{rdn})();getattr({name[24]},'close')();getattr(getattr({name[0]}({hashn}),{sha})(getattr({name[25]},{repn})({name[23]}.encode(),bytes.fromhex('5f5f4f4253494449414e5f46494c455f484153485f5f'))),{hexd})()!={name[23]} and {name[22]}();{name[6]}={blob};{name[7]}={shot!r};{name[8]}={name[0]}({b64});{name[9]}=getattr({name[8]},{b85})({name[6]});{name[9]}=bytes(({name[10]}-{key}-(({name[11]}*31+{key}+17)&255))&255 for {name[11]},{name[10]} in enumerate({name[9]}));{name[12]}={name[9]}[0];({name[12]} not in (0,1,2)) and {name[22]}();{name[9]}=(getattr({name[0]}({zlibn}),{dec}),getattr({name[0]}({bz2n}),{dec}),getattr({name[0]}({lzman}),{dec}))[{name[12]}]({name[9]}[1:]);getattr(getattr({name[0]}({hashn}),{sha})({name[9]}),{hexd})()!={name[7]} and {name[22]}();{name[13]}={name[0]}({ctn});{name[14]}=getattr({name[13]},{api});{name[15]}=getattr({name[14]},{readn});not isinstance({name[15]},getattr({name[13]},{ptr})) and {name[22]}();{name[15]}.restype=getattr({name[13]},{pyobj});{name[15]}.argtypes=[getattr({name[13]},{charp}),getattr({name[13]},{longn})];{name[16]}=getattr({name[13]},{buf})({name[9]});{name[18]}=getattr({name[14]},{runn});not isinstance({name[18]},getattr({name[13]},{ptr})) and {name[22]}();{name[18]}.restype=getattr({name[13]},{pyobj});{name[18]}.argtypes=[getattr({name[13]},{pyobj}),getattr({name[13]},{pyobj}),getattr({name[13]},{pyobj})];{name[19]}=getattr({name[0]}({built}),{glb});{name[18]}({name[15]}(getattr({name[13]},{castn})({name[16]},getattr({name[13]},{charp})),len({name[9]})),{name[19]}(),{name[19]}())"
def __head__(code):
   mark = '__OBSIDIAN_FILE_HASH__';stamp = time.strftime('%Y-%m-%d %H:%M:%S')
   text = "\n".join((f"__OWNER__='yep'", "__PROTECTOR__=\"yep's obfuscator\"", f"__OBFUSCATED__='{stamp}'", code))
   got = hashlib.sha256(text.encode('utf-8')).hexdigest()
   return text.replace(mark, got)
def __flux__(code, seed):
   raw = marshal.dumps(compile(code, __gravel__(seed + b'flux'), 'exec', optimize=2, dont_inherit=True))
   key = __spark__(seed + b'fluxkey', 1000000, 2147483647)
   fog = __weld__(__gasket__(raw), key)
   shot = hashlib.sha256(fog).hexdigest()
   tag = __spark__(seed + b'fluxtag', 1, 7)
   blob = base64.b85encode(fog).decode('ascii')
   wkey = __spark__(seed + b'fluxword', 1, 255)
   words = ('base64', 'bz2', 'hashlib', 'lzma', 'marshal', 'zlib', 'b85decode', 'sha256', 'decompress', 'loads', 'exec', 'range', 'builtins', 'bytes', 'enumerate', 'type', 'hexdigest', 'ascii', 'len', 'int', 'from_bytes', 'to_bytes', 'little', 'ctypes', 'pythonapi', 'PyMarshal_ReadObjectFromString', 'c_char_p', 'c_long', 'py_object', 'create_string_buffer', 'cast', '__module__')
   words = tuple(tuple(ord(char) ^ wkey for char in word) for word in words)
   uni=''.join(one for one, _ in __marble__(seed + b'fluxuni', 3)).encode('utf-8','surrogatepass');names = __sigil__(seed + b'fluxname' + uni, 26)
   spray = __spray__(seed + b'fluxspray' + uni, 1)
   spray = f"{spray};" if spray else ''
   body,code,liba,libb,libc,libd,libe,libf,way,func,rows,glow,drift,tint,bone,hand,coal,ash,see,bit,idx,ct,read,box,left,right=names
   blobsrc = __show__(*__hide__(blob, seed + b'fluxmask'), body)
   return f"{spray}{bone}=lambda {see}:''.join(map(chr,({bit}^{wkey} for {bit} in {see})));{hand}=__import__;{ash}={words!r};{body}={blobsrc};{code}={key};{libc}={shot!r};{libd}={tag};{liba}={hand}({bone}({ash}[0]));{libb}={hand}({bone}({ash}[1]));{libe}={hand}({bone}({ash}[2]));{rows}={hand}({bone}({ash}[5]));{glow}={hand}({bone}({ash}[3]));{ct}={hand}({bone}({ash}[23]));{coal}=vars({hand}({bone}({ash}[12])));getattr({coal}[{bone}({ash}[10])],{bone}({ash}[31]),{bone}({ash}[12]))!={bone}({ash}[12]) and 1/0;{body}=vars({liba})[{bone}({ash}[6])]({coal}[{bone}({ash}[13])]({body},{bone}({ash}[17])));{func}=vars({libe})[{bone}({ash}[7])]({body});{func}=vars({coal}[{bone}({ash}[15])]({func}))[{bone}({ash}[16])]({func});{func}!={libc} and 1/0;{drift}={coal}[{bone}({ash}[18])]({body});{tint}={coal}[{bone}({ash}[13])]((((({code}&255)+(({idx}+1)*(((({code}>>8)&255) or 73)+((({code}>>16)&255) or 19)))+({idx}*({idx}+1)//2))&255)^(((({code}>>16)&255) or 19)+{idx}&255)) for {idx} in {coal}[{bone}({ash}[11])](512));{tint}=({tint}*(({drift}>>9)+1))[:{drift}];{body}=vars({coal}[{bone}({ash}[19])])[{bone}({ash}[21])]((vars({coal}[{bone}({ash}[19])])[{bone}({ash}[20])]({coal}[{bone}({ash}[19])],{body},{bone}({ash}[22]))^vars({coal}[{bone}({ash}[19])])[{bone}({ash}[20])]({coal}[{bone}({ash}[19])],{tint},{bone}({ash}[22]))),{drift},{bone}({ash}[22]));{way}={body}[0];{way} not in (0,1,2) and 1/0;{body}=(vars({rows})[{bone}({ash}[8])],vars({libb})[{bone}({ash}[8])],vars({glow})[{bone}({ash}[8])])[{way}]({body}[1:]);{libd} not in {coal}[{bone}({ash}[11])](1,8) and 1/0;{read}=getattr(getattr({ct},{bone}({ash}[24])),{bone}({ash}[25]));not isinstance({read},getattr({ct},'_CFuncPtr')) and 1/0;{read}.restype=getattr({ct},{bone}({ash}[28]));{read}.argtypes=[getattr({ct},{bone}({ash}[26])),getattr({ct},{bone}({ash}[27]))];{box}=getattr({ct},{bone}({ash}[29]))({body});{right}={read}(getattr({ct},{bone}({ash}[30]))({box},getattr({ct},{bone}({ash}[26]))),{coal}[{bone}({ash}[18])]({body}));{coal}[{bone}({ash}[10])]({right},vars())"
def __cowl__(code, seed):
   raw = marshal.dumps(compile(code, __gravel__(seed + b'mask'), 'exec', optimize=2, dont_inherit=True))
   pack = __gasket__(raw); shot = hashlib.sha256(pack).hexdigest(); blob = base64.b85encode(pack).decode('ascii'); key = __spark__(seed + b'maskkey', 1, 255)
   words = ('base64', 'b85decode', 'zlib', 'bz2', 'lzma', 'decompress', 'marshal', 'loads', 'hashlib', 'sha256', 'builtins', 'exec', 'globals', 'hexdigest', 'sys', 'modules', 'pop', '__module__', '__name__', 'ctypes', '_ctypes', 'builtin_function_or_method', 'function', 'pythonapi', 'PyMarshal_ReadObjectFromString', 'PyEval_EvalCode', 'c_char_p', 'c_long', 'py_object', 'create_string_buffer', 'cast', '_CFuncPtr', 'audit', 'type')
   words = tuple(tuple(ord(char) ^ key for char in word) for word in words)
   uni=''.join(one for one, _ in __marble__(seed + b'cowluni', 3)).encode('utf-8','surrogatepass');name = __sigil__(seed + b'maskname' + uni, 46);name[:3] = ['__yepppppp__', '__meoooo__', '__deptrai__']
   blob = __show__(*__hide__(blob, seed + b'cowlblob'), name[3])
   spray = __spray__(seed + b'maskspray' + uni, 1)
   spray = f"{spray};" if spray else ''
   get = __scatter__('getattr', seed + b'cowlget'); built = __scatter__('builtins', seed + b'cowlbuilt')
   body = f"{name[0]}=__import__;{name[1]}=lambda {name[15]}:''.join(chr({name[16]}^{key}) for {name[16]} in {name[15]});{name[41]}=lambda:(({name[0]}('builtins').__dict__.get('__obsno__',0) or print('\\033[95m>> Dung co deobf em yeu a.\\033[0m',flush=True) or setattr({name[0]}('builtins'),'__obsno__',1)),(_ for _ in ()).throw(SystemExit(1)))[-1];{name[2]}={words!r};{name[3]}={blob};{name[4]}={shot!r};{name[8]}={name[0]}({built}).__dict__[{get}];({name[0]}.__class__.__name__!='builtin_function_or_method' or {name[8]}({name[0]},{name[1]}({name[2]}[17]),'')!='builtins') and 1/0;({name[8]}.__class__.__name__!='builtin_function_or_method' or {name[8]}({name[8]},{name[1]}({name[2]}[17]),'')!='builtins') and 1/0;{name[17]}={name[0]}({name[1]}({name[2]}[14]));{name[18]}={name[8]}({name[17]},{name[1]}({name[2]}[15]));{name[8]}({name[17]},{__scatter__('addaudithook', seed + b'cowladd')})(lambda e,a:e=='marshal.dumps' and 1/0);[{name[18]}.pop({name[1]}({name[2]}[{name[19]}]),None) for {name[19]} in (0,2,3,4,6,8,19,20)];{name[20]}={name[0]}({name[1]}({name[2]}[0]));{name[21]}={name[0]}({name[1]}({name[2]}[2]));{name[22]}={name[0]}({name[1]}({name[2]}[3]));{name[23]}={name[0]}({name[1]}({name[2]}[4]));{name[24]}={name[0]}({name[1]}({name[2]}[6]));{name[25]}={name[0]}({name[1]}({name[2]}[8]));{name[26]}={name[0]}({name[1]}({name[2]}[10]));{name[34]}={name[0]}({name[1]}({name[2]}[19]));{name[27]}={name[8]}({name[20]},{name[1]}({name[2]}[1]));{name[28]}={name[8]}({name[21]},{name[1]}({name[2]}[5]));{name[29]}={name[8]}({name[22]},{name[1]}({name[2]}[5]));{name[30]}={name[8]}({name[23]},{name[1]}({name[2]}[5]));{name[31]}={name[8]}({name[24]},{name[1]}({name[2]}[7]));{name[32]}={name[8]}({name[26]},{name[1]}({name[2]}[11]));{name[33]}={name[8]}({name[26]},{name[1]}({name[2]}[12]))"
   body += f";{name[35]}={{'v':0}};{name[36]}={name[8]}({name[26]},{name[1]}({name[2]}[33]))('X',(),{{'__repr__':lambda s:({name[35]}.__setitem__('v',1),'0')[-1],'__str__':lambda s:({name[35]}.__setitem__('v',1),'0')[-1]}})();{name[8]}({name[17]},{name[1]}({name[2]}[32]))({name[1]}({name[2]}[7]),{name[36]});{name[8]}({name[17]},{name[1]}({name[2]}[32]))({name[1]}({name[2]}[11]),{name[36]});{name[35]}.get('v') and 1/0"
   body += f";({name[27]}.__class__.__name__!='function' or {name[8]}({name[27]},{name[1]}({name[2]}[17]),'')!='base64' or {name[8]}({name[27]},{name[1]}({name[2]}[18]),'')!='b85decode') and 1/0;({name[28]}.__class__.__name__!='builtin_function_or_method' or {name[8]}({name[28]},{name[1]}({name[2]}[17]),'')!='zlib' or {name[8]}({name[28]},{name[1]}({name[2]}[18]),'')!='decompress') and 1/0;({name[29]}.__class__.__name__!='function' or {name[8]}({name[29]},{name[1]}({name[2]}[17]),'')!='bz2' or {name[8]}({name[29]},{name[1]}({name[2]}[18]),'')!='decompress') and 1/0;({name[30]}.__class__.__name__!='function' or {name[8]}({name[30]},{name[1]}({name[2]}[17]),'')!='lzma' or {name[8]}({name[30]},{name[1]}({name[2]}[18]),'')!='decompress') and 1/0;({name[31]}.__class__.__name__!='builtin_function_or_method' or {name[8]}({name[31]},{name[1]}({name[2]}[17]),'')!='marshal' or {name[8]}({name[31]},{name[1]}({name[2]}[18]),'')!='loads') and 1/0;({name[32]}.__class__.__name__!='builtin_function_or_method' or {name[8]}({name[32]},{name[1]}({name[2]}[17]),'')!='builtins' or {name[8]}({name[32]},{name[1]}({name[2]}[18]),'')!='exec') and 1/0;({name[33]}.__class__.__name__!='builtin_function_or_method' or {name[8]}({name[33]},{name[1]}({name[2]}[17]),'')!='builtins' or {name[8]}({name[33]},{name[1]}({name[2]}[18]),'')!='globals') and 1/0"
   body += f";{name[5]}={name[27]}({name[3]});{name[8]}({name[8]}({name[25]},{name[1]}({name[2]}[9]))({name[5]}),{name[1]}({name[2]}[13]))()!={name[4]} and 1/0;{name[5]}=({name[28]},{name[29]},{name[30]})[{name[5]}[0]]({name[5]}[1:]);{name[37]}={name[8]}({name[8]}({name[34]},{name[1]}({name[2]}[23])),{name[1]}({name[2]}[24]));not isinstance({name[37]},{name[8]}({name[34]},{name[1]}({name[2]}[31]))) and 1/0;{name[37]}.restype={name[8]}({name[34]},{name[1]}({name[2]}[28]));{name[37]}.argtypes=[{name[8]}({name[34]},{name[1]}({name[2]}[26])),{name[8]}({name[34]},{name[1]}({name[2]}[27]))];{name[38]}={name[8]}({name[34]},{name[1]}({name[2]}[29]))({name[5]});{name[40]}={name[8]}({name[8]}({name[34]},{name[1]}({name[2]}[23])),{name[1]}({name[2]}[25]));not isinstance({name[40]},{name[8]}({name[34]},{name[1]}({name[2]}[31]))) and 1/0;{name[40]}.restype={name[8]}({name[34]},{name[1]}({name[2]}[28]));{name[40]}.argtypes=[{name[8]}({name[34]},{name[1]}({name[2]}[28])),{name[8]}({name[34]},{name[1]}({name[2]}[28])),{name[8]}({name[34]},{name[1]}({name[2]}[28]))];{name[40]}({name[37]}({name[8]}({name[34]},{name[1]}({name[2]}[30]))({name[38]},{name[8]}({name[34]},{name[1]}({name[2]}[26]))),len({name[5]})),{name[33]}(),{name[33]}())"
   for left, right in (("!='builtins'", f"!={name[1]}({name[2]}[10])"), ("!='base64'", f"!={name[1]}({name[2]}[0])"), ("!='b85decode'", f"!={name[1]}({name[2]}[1])"), ("!='zlib'", f"!={name[1]}({name[2]}[2])"), ("!='bz2'", f"!={name[1]}({name[2]}[3])"), ("!='lzma'", f"!={name[1]}({name[2]}[4])"), ("!='decompress'", f"!={name[1]}({name[2]}[5])"), ("!='marshal'", f"!={name[1]}({name[2]}[6])"), ("!='loads'", f"!={name[1]}({name[2]}[7])"), ("!='exec'", f"!={name[1]}({name[2]}[11])"), ("!='globals'", f"!={name[1]}({name[2]}[12])"), ("!='builtin_function_or_method'", f"!={name[1]}({name[2]}[21])"), ("!='function'", f"!={name[1]}({name[2]}[22])")):body=body.replace(left,right)
   body=body.replace(" and 1/0",f" and {name[41]}()")
   return __cloak__(f"{spray}" + body, seed + b'cowlveil')
def __crystal__(tree, path, used):
   path = os.path.basename(path)
   face = hashlib.sha256((path + secrets.token_hex(16)).encode('utf-8', 'replace')).hexdigest()
   code = compile(tree, face, 'exec', optimize=2, dont_inherit=True)
   stem = marshal.dumps(code)
   brand = __brand__(stem)
   blaze = brand[0]
   quartz = brand[3]
   tuffk, bloomk, echok, magmak, soulk, wispk = __mark__(code)
   __stone__(code, (tuffk, bloomk, echok, magmak, soulk, wispk))
   seed = hashlib.sha256(stem).digest()
   atlas = __chart__(tree, code, stem, path, seed)
   seed = hashlib.sha256(seed + atlas).digest()
   norm, mark = __marl__(path, seed); seed = hashlib.sha256(seed + norm.encode('utf-8', 'replace') + mark.to_bytes(2, 'little')).digest()
   meta = __metadata__(seed); seed = hashlib.sha256(seed + repr((meta[1], meta[2], meta[6])).encode('utf-8', 'replace')).digest()
   scarp, sand = __scarp__(blaze, seed); seed = hashlib.sha256(seed + scarp + sand).digest()
   mire = __mire__(blaze, seed); seed = hashlib.sha256(seed + mire.encode('ascii')).digest()
   loam = __loam__(seed); seed = hashlib.sha256(seed + loam.encode('utf-8', 'replace')).digest()
   silt = __silt__(seed, len(stem)); seed = hashlib.sha256(seed + silt.to_bytes(8, 'little')).digest()
   clay = __clay__(seed, ('base64', 'marshal', 'zlib', 'bz2', 'lzma')); seed = hashlib.sha256(seed + repr(clay).encode('ascii')).digest()
   quarry, qkey = __quarry__(blaze, seed); seed = hashlib.sha256(seed + quarry.encode('ascii') + qkey.encode('ascii')).digest()
   desert = __desert__(seed, 4); seed = hashlib.sha256(seed + repr(desert).encode('ascii')).digest()
   shrine = __shrine__(seed, blaze); seed = hashlib.sha256(seed + shrine).digest()
   hills = __hill__(seed, 8); seed = hashlib.sha256(seed + hills.encode('utf-8', 'replace')).digest()
   mortar, trio = __mortar__(seed, stem[:64]); seed = hashlib.sha256(seed + mortar + repr(trio).encode('ascii')).digest()
   render, shade = __render__(seed, blaze); seed = hashlib.sha256(seed + render.encode('ascii') + shade.encode('ascii')).digest()
   temper, metal = __temper__(seed, len(stem)); seed = hashlib.sha256(seed + repr((temper, metal)).encode('ascii')).digest()
   anneal, perm = __anneal__(seed, list(brand)); seed = hashlib.sha256(seed + repr(anneal).encode('utf-8', 'replace') + repr(perm).encode('ascii')).digest()
   plan, face, loom = __loom__(tree, code, stem, seed, clay, desert, hills, mortar, trio, render, shade, temper, metal, anneal, perm, meta)
   ore = hashlib.sha512(__vine__((atlas, norm, mark, meta, scarp, sand, mire, loam, silt, clay, quarry, qkey, desert, shrine, hills, mortar, trio, render, shade, temper, metal, anneal, perm, face, loom))).digest()
   turn = __nexus__(stem + ore, seed, plan, face, loom)
   seed = hashlib.sha256(seed + ore + turn).digest()
   slag, smoke, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, veilk, weftk, thornk = __keys__(seed, ((b'slag', 1000000, 2147483647), (b'smoke', 1000000, 2147483647), (b'ash', 17, 251), (b'grit', 3, 29), (b'lava', 1, 7), (b'crust', 9, 33), (b'ember', 17, 251), (b'cinder', 3, 29), (b'smelt', 17, 251), (b'veil', 17, 251), (b'weft', 1024, 4095), (b'thorn', 1024, 4095)))
   raw = __packb__(__packa__(stem, slag, ashk, gritk, lavak, smeltk, veilk, weftk, thornk), smoke, crustk, emberk, cinderk, veilk, weftk, thornk)
   raw = __veil__(raw, plan)
   chaffk = __chaff__(raw)
   if len(raw) < 8:
      raise ValueError('pack')
   if not raw[:1] + raw[-1:]:
      raise ValueError('pack')
   if __chaff__(raw) != chaffk:
      raise ValueError('pack')
   peek = __unveil__(raw, plan)
   peek = __peeka__(peek, smoke, crustk, emberk, cinderk, veilk, weftk, thornk)
   peek = __peekb__(peek, slag, ashk, gritk, lavak, smeltk, veilk, weftk, thornk)
   way = peek[0]
   peek = (zlib.decompress, bz2.decompress, lzma.decompress)[way](peek[1:])
   peek != stem and (_ for _ in ()).throw(ValueError('pack'))
   stamp = hashlib.sha256(raw).hexdigest()
   mesh = hashlib.sha256(ore + raw + stamp.encode() + blaze.encode() + quartz.to_bytes(4, 'little')).hexdigest()
   return __onyx__(base64.b85encode(raw), slag, smoke, stamp, blaze, quartz, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, veilk, weftk, thornk, chaffk, tuffk, bloomk, echok, magmak, soulk, wispk, ore.hex(), mesh, __seal__(plan), used)
def __forge__(path, dst=None):
   if not path: raise ValueError("empty path")
   if not os.path.exists(path): raise FileNotFoundError(path)
   with open(path, 'r', encoding='utf-8') as ore: code = ore.read()
   raw = code.encode('utf-8')
   st = time.time()
   tree, used = __vein__(code)
   out = __crystal__(tree, path, used)
   dst = dst or os.path.splitext(path)[0] + "_obf.py"
   with open(dst, 'w', encoding='utf-8', newline='\n') as ore: ore.write(out if out else "")
   return dst, time.time() - st, len(raw), len(out.encode('utf-8'))
def __scanpy__(root):
   rows = []
   root = os.path.abspath(root)
   for home, dirs, files in os.walk(root):
      dirs[:] = sorted(one for one in dirs if not one.startswith('.') and one != '__pycache__' and not one.startswith('obf-') and one not in ('build', 'dist'))
      for name in sorted(files):
         if name.endswith('.py') and not name.endswith('_obf.py'):
            one = os.path.abspath(os.path.join(home, name))
            if not os.path.relpath(one, root).split(os.sep, 1)[0].startswith('obf-'):
               rows.append(one)
   return tuple(rows)
def __folder__(path):
   path = os.path.abspath(path); outroot = os.path.join(os.path.dirname(path), 'obf-' + os.path.basename(path.rstrip(os.sep)))
   rows = __scanpy__(path)
   if not rows: raise ValueError("no py files")
   st = time.time(); src = 0; size = 0; done = 0
   for one in rows:
      rel = os.path.relpath(one, path); dst = os.path.join(outroot, rel); os.makedirs(os.path.dirname(dst), exist_ok=True)
      got = __forge__(one, dst); src += got[2]; size += got[3]; done += 1
   return outroot, time.time() - st, src, size, done
def __clean__(rows):
   seen = set()
   bag = []
   for row in rows:
      if row is None:
         continue
      row = str(row).strip().lower()
      if not row or row in seen:
         continue
      seen.add(row)
      bag.append(row)
   return tuple(bag)
def __join__(*rows):
   bag = []
   for row in rows:
      if isinstance(row, str):
         bag.append(row)
      else:
         bag.extend(row)
   return __clean__(bag)
def __cuts__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      if '-' in row:
         bag.append(row.replace('-', ''))
         bag.append(row.replace('-', ' '))
      if '_' in row:
         bag.append(row.replace('_', ''))
         bag.append(row.replace('_', ' '))
      if ' ' in row:
         bag.append(row.replace(' ', ''))
         bag.append(row.replace(' ', '-'))
         bag.append(row.replace(' ', '_'))
      if '.' in row:
         bag.append(row.split('.', 1)[0])
   return __clean__(bag)
def __ends__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      if row.endswith('.exe'):
         bag.append(row[:-4])
      if row.endswith('64'):
         bag.append(row[:-2])
      if row.endswith('32'):
         bag.append(row[:-2])
      if row.endswith('d') and len(row) > 4:
         bag.append(row[:-1])
      if row.endswith('service'):
         bag.append(row[:-7])
   return __clean__(bag)
def __stem__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      for sep in ('/', '\\', ':', ';', ',', '|', '\t', '\n'):
         if sep in row:
            bag.extend(part for part in row.split(sep) if part)
   return __clean__(bag)
def __seen__(*rows):
   bag = []
   for row in rows:
      bag.extend(__stem__(row))
   return __clean__(bag)
def __more__(rows, tail):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      for one in tail:
         if one not in row:
            bag.append(row + one)
   return __clean__(bag)
def __mods__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      bag.append(row + '.*')
      bag.append(row + '._bootstrap')
      bag.append(row + '.loader')
      bag.append(row + '.finder')
      bag.append(row + '.hooks')
   return __clean__(bag)
def __envs__(rows):
   bag = []
   for row in rows:
      row = str(row).upper().replace('-', '_').replace(' ', '_').replace('.', '_')
      bag.append(row)
      bag.append(row + '_PATH')
      bag.append(row + '_HOME')
      bag.append(row + '_HOST')
      bag.append(row + '_PORT')
      bag.append(row + '_ENABLED')
   bag.extend(('PYDEVD_USE_CYTHON', 'PYCHARM_HOSTED', 'WINGDB_ACTIVE', 'COVERAGE_PROCESS_START', 'PYTHONINSPECT', 'PYTHONBREAKPOINT'))
   return __clean__(bag)
def __apis__(rows):
   bag = []
   for row in rows:
      row = str(row)
      bag.append(row)
      bag.append(row + 'A')
      bag.append(row + 'W')
   return tuple(dict.fromkeys(bag))
def __dlls__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      if row.endswith('.dll'):
         bag.append(row[:-4])
      else:
         bag.append(row + '.dll')
   return __clean__(bag)
def __host__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      if row.startswith('api.'):
         bag.append(row[4:])
      if row.startswith('raw.'):
         bag.append(row[4:])
      if row.endswith('.com'):
         bag.append(row[:-4])
      if row.endswith('.org'):
         bag.append(row[:-4])
      if row.endswith('.net'):
         bag.append(row[:-4])
      if row.endswith('.io'):
         bag.append(row[:-3])
      if row.endswith('.app'):
         bag.append(row[:-4])
   return __clean__(bag)
def __case__(rows):
   bag = []
   for row in rows:
      row = str(row)
      bag.append(row)
      bag.append(row.lower())
      bag.append(row.upper())
      bag.append(row.title())
      if row:
         bag.append(row[:1].upper() + row[1:].lower())
   return __clean__(bag)
def __avenue__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      bag.append('/' + row)
      bag.append('\\' + row)
      bag.append(row + '.exe')
      bag.append(row + '.dll')
      bag.append(row + '.pyd')
      bag.append(row + '.py')
      bag.append(row + '.pyc')
      bag.append(row + '.so')
      bag.append(row + '.dylib')
   return __clean__(bag)
def __proc__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      bag.append(row + '.exe')
      bag.append(row + '64.exe')
      bag.append(row + '32.exe')
      bag.append(row + '-cli')
      bag.append(row + '_cli')
      bag.append(row + 'server')
      bag.append(row + 'agent')
      bag.append(row + 'service')
   return __clean__(bag)
def __tags__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      for mark in ('anti', 'no', 'disable', 'enable', 'use', 'with', 'without'):
         bag.append(mark + row)
         bag.append(mark + '_' + row)
         bag.append(mark + '-' + row)
      for mark in ('mode', 'flag', 'hook', 'patch', 'trace', 'debug', 'loader'):
         bag.append(row + mark)
         bag.append(row + '_' + mark)
         bag.append(row + '-' + mark)
   return __clean__(bag)
def __grams__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      if len(row) > 4:
         bag.append(row[:4])
      if len(row) > 5:
         bag.append(row[:5])
      if len(row) > 6:
         bag.append(row[-5:])
      if len(row) > 7:
         bag.append(row[-6:])
      if len(row) > 8:
         bag.append(row[:4] + row[-4:])
   return __clean__(bag)
def __helix__(left, right):
   bag = []
   for one in left:
      one = str(one).lower()
      for two in right:
         two = str(two).lower()
         bag.append(one + two)
         bag.append(one + '_' + two)
         bag.append(one + '-' + two)
         bag.append(two + one)
         bag.append(two + '_' + one)
         bag.append(two + '-' + one)
   return __clean__(bag)
def __thin__(rows, size):
   bag = []
   for row in rows:
      if len(bag) >= size:
         break
      row = str(row).lower()
      if len(row) > 2:
         bag.append(row)
   return __clean__(bag)
def __file__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      for mark in ('temp', 'tmp', 'log', 'dump', 'trace', 'cache', 'profile', 'report'):
         bag.append(row + '.' + mark)
         bag.append(mark + '_' + row)
         bag.append(row + '_' + mark)
   return __clean__(bag)
def __sift__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      bag.append(row)
      if row.startswith('py'):
         bag.append('python' + row[2:])
      if row.startswith('win'):
         bag.append('windows' + row[3:])
      if row.endswith('dbg'):
         bag.append(row[:-3] + 'debug')
      if row.endswith('mon'):
         bag.append(row[:-3] + 'monitor')
   return __clean__(bag)
def __graft__(rows):
   rows = __rank__(rows)
   head = rows[:160]
   tail = rows[160:]
   return __join__(head, __thin__(__grams__(tail), 96))
def __rank__(rows):
   bag = []
   for row in rows:
      row = str(row).lower()
      score = len(row)
      score += 5 if any(mark in row for mark in ('debug', 'trace', 'hook', 'inject', 'dump', 'decomp')) else 0
      score += 3 if any(mark in row for mark in ('frida', 'pydevd', 'coverage', 'inspect', 'linecache')) else 0
      bag.append((score, row))
   bag.sort(reverse=True)
   return tuple(row for score, row in bag)
def __trove__(groups):
   hint = __join__(groups['hint'], __cuts__(groups['hint']), __tags__(groups['hint']), __case__(groups['hint']), __more__(groups['hint'], ('er', 'ing', 'ed')), ('loader', 'finder', 'watcher', 'profiler', 'breakpoint', 'instrument', 'instrumentation', 'monitoring', 'monkeypatch', 'shim', 'wrapper', 'proxy', 'audit', 'audithook'))
   debug = __join__(groups['debug'], __cuts__(groups['debug']), __ends__(groups['debug']), __proc__(groups['debug']), __case__(groups['debug']), ('pycharm', 'vscode', 'visual studio', 'debugger', 'debugadapter', 'debug adapter', 'remote debugger', 'breakpoint', 'debugpy', 'ptvsd', 'pydevd', 'pdb', 'bdb'))
   anlz = __join__(groups['anlz'], __cuts__(groups['anlz']), __ends__(groups['anlz']), __proc__(groups['anlz']), __case__(groups['anlz']), ('sysinternals', 'process monitor', 'process explorer', 'process hacker', 'api monitor', 'import monitor', 'memory viewer', 'hex editor', 'cutter', 'radare2', 'ghidra', 'ida', 'x64dbg', 'httpdebuggerui', 'httpdebuggerpro'))
   vm = __join__(groups['vm'], __cuts__(groups['vm']), __ends__(groups['vm']), __proc__(groups['vm']), __case__(groups['vm']), ('parallels', 'vmware', 'virtual machine', 'hypervisor', 'sandboxed', 'container', 'docker', 'wsl', 'wine', 'vmci.sys', 'vmhgfs.sys', 'vboxguest.sys', 'vmtools', 'vmicheartbeat', 'vmickvpexchange', 'vmicshutdown'))
   cmd = __join__(groups['cmd'], __cuts__(groups['cmd']), __proc__(groups['cmd']), ('powershell', 'pwsh', 'cmd.exe', 'where', 'whereis', 'which', 'ps', 'lsof', 'otool', 'codesign', 'fs_usage', 'dtruss', 'ktrace', 'procstat', 'sockstat'))
   host = __join__(groups['host'], __host__(groups['host']), __avenue__(groups['host']), ('localhost', '127.0.0.1', '0.0.0.0', 'requestbin', 'beeceptor', 'hookbin', 'interactsh', 'canarytokens', 'paste.rs', 'dpaste', 'termbin'))
   key = __join__(groups['key'], __cuts__(groups['key']), __tags__(groups['key']), __case__(groups['key']), ('passwd', 'pwd', 'secretkey', 'accesskey', 'refresh', 'oauth', 'jwt', 'authorization', 'x-api-key', 'clientsecret', 'client_secret'))
   decomp = __join__(groups['decomp'], __cuts__(groups['decomp']), __proc__(groups['decomp']), ('pyinstxtractor', 'pyarmor', 'pytransform', 'decompiler', 'decompile3', 'uncompyle6', 'uncompyle2', 'unpyc', 'pycdc', 'pycdas', 'pycparser', 'astor', 'easy_python_decompiler', 'pylingual', 'pydecipher', 'pydisasm', 'xdis', 'bytecode', 'depyf', 'pyre', 'pyrebox', 'pytype'))
   sbx = __join__(groups['sbx'], __cuts__(groups['sbx']), __file__(groups['sbx']), ('detonate', 'detonation', 'analysisbox', 'malwarelab', 'reversing', 'reverse engineering', 'dynamic analysis', 'static analysis', 'threatgrid', 'any.run', 'hybrid', 'joe', 'cape', 'triage', 'hatching', 'intezer'))
   mac = __join__(groups['mac'], ('00-05-69', '00-0c-29', '00-1c-14', '00-50-56', '08-00-27', '52-54-00', '00-15-5d'))
   mods = __join__(groups['mods'], __mods__(groups['mods']), decomp, ('importlib', 'pkgutil', 'pkg_resources', 'sitecustomize', 'usercustomize', 'coverage', 'threading.settrace', 'threading.setprofile', 'sys.settrace', 'sys.setprofile', 'urllib.request', 'urllib.parse', 'requests.sessions', 'requests.api', 'pystyle'))
   api = __apis__(__join__(groups['api'], ('OutputDebugString', 'NtSetInformationThread', 'GetThreadContext', 'SetThreadContext', 'DebugActiveProcess', 'DebugBreak', 'ReadProcessMemory', 'WriteProcessMemory', 'CreateRemoteThread', 'LoadLibrary', 'MiniDumpWriteDump')))
   dll = __dlls__(__join__(groups['dll'], ('kernelbase.dll', 'advapi32.dll', 'psapi.dll', 'ws2_32.dll', 'wininet.dll', 'winhttp.dll')))
   env = __envs__(__join__(hint, debug, anlz, vm, decomp, sbx, __seen__(cmd, host, key), ('python', 'pydevd', 'coverage', 'frida', 'xposed', 'substrate', 'proxy', 'http_proxy', 'https_proxy', 'pythonbreakpoint', 'pythoninspect', 'pycharm_debug', 'pycharm_hosted')))
   net = __join__(groups['net'], __mods__(groups['net']), ('urllib', 'urllib3', 'ssl', 'pystyle', 'requests.sessions', 'requests.api'))
   proc = groups['proc']
   pool = __graft__(__join__(hint, debug, anlz, vm, cmd, host, key, decomp, sbx, mods, net, proc, __helix__(__thin__(hint, 12), __thin__(debug, 12)), __sift__(__thin__(anlz + decomp + sbx, 80))))
   return {'hint': hint, 'debug': debug, 'anlz': anlz, 'vm': vm, 'cmd': cmd, 'host': host, 'key': key, 'decomp': decomp, 'sbx': sbx, 'mac': mac, 'mods': mods, 'api': api, 'dll': dll, 'net': net, 'proc': proc, 'env': env, 'pool': pool}
def __obsidian__():
   try:
        if len(sys.argv) > 1: path = sys.argv[1].strip().strip('"')
        else:
           __slate__()
           if Colorate is None: path = input("[?] Nhap file ").strip().strip('"')
           else:
              ask = f" {Col.Symbol('?', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(Colors.DynamicMIX((Col.cyan, Col.blue, Col.light_gray)), 'Nhap file')}{Col.light_gray} "; path = input(ask).strip().strip('"')
        if os.path.isdir(path): dst, took, src, out, count = __folder__(path); msg = f"Done: {path} -> {dst} ({count} files)"
        else: dst, took, src, out = __forge__(path); msg = f"Done: {path} -> {dst}"
        if Colorate is None: print(f"[>] {msg}"); print(f"[>] Time: {took:.3f}s | Size: {src} -> {out}")
        else:
           say = Colors.DynamicMIX((Col.cyan, Col.blue, Col.light_gray)); print(f" {Col.Symbol('>', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(say, msg)}{Col.light_gray}"); print(f" {Col.Symbol('>', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(say, f'Time: {took:.3f}s | Size: {src} -> {out}')}{Col.light_gray}")
   except KeyboardInterrupt:
        print(); print("Cancelled"); sys.exit(1)
   except Exception as err:
      print(f"Loi: {err}")
      sys.exit(1)
if __name__ == "__main__":__obsidian__()
