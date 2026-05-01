import ast
import base64
import bz2
import hashlib
import lzma
import marshal
import math
import os
import sys
import time
import secrets
import zlib
try:
    from pystyle import Col, Colorate, Colors
except:
    Col = None
    Colorate = None
    Colors = None
if sys.version_info < (3, 10):
    print("Python 3.10+ required")
    sys.exit(1)
def __slate__():
   if Colorate is None:
        print(); print("OBSIDIAN"); print("dense fused shell // deobf thu di"); print(); return
   mix = Colors.DynamicMIX((Col.cyan, Col.blue, Col.light_gray)); glow = Colors.DynamicMIX((Col.blue, Col.cyan, Col.light_gray)); print()
   for row in ("   ____  ____  _____ ___ ____ ___    _    _   _", "  / __ )/ __ \\/ ___//  _/ __ \\_ _|  / \\  | \\ | |", " / __  / / / /\\__ \\ / // / / /| |  / _ \\ |  \\| |", "/ /_/ / /_/ /___/ // // /_/ / | | / ___ \\| |\\  |", "/_____/\\____//____/___/\\____/ |___/_/   \\_\\_| \\_|"): print(Colorate.Diagonal(mix, row))
   glow and print(Colorate.Diagonal(glow, "             dense fused shell // deobf thu di")); print()
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
        if name in used: continue
        if name.isidentifier(): used.add(name); return name
def __tuff__(code): return (code.co_code, code.co_consts, code.co_names, code.co_varnames, code.co_freevars, code.co_cellvars)
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
   for one in __vine__(__tuff__(code)): mark ^= one; mark *= 16777619; mark &= 0xffffffff
   return mark
def __drip__(code):
   kind = type(code); hold = [code]; seen = set(); rows = []
   while hold:
        one = hold.pop()
        if not isinstance(one, kind): continue
        mark = id(one)
        if mark in seen: continue
        seen.add(mark); rows.append(one)
        for item in one.co_consts:
             if isinstance(item, kind): hold.append(item)
   return tuple(rows)
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
   if len(blob) > 4096:
        pick = (0, zlib.compress(blob, 6))
   elif len(blob) < 512:
        pick = min(((0, zlib.compress(blob, 9)), (1, bz2.compress(blob, 9)), (2, lzma.compress(blob, format=lzma.FORMAT_ALONE, preset=6))), key=lambda row: len(row[1]))
   else:
        pick = min(((0, zlib.compress(blob, 6)), (1, bz2.compress(blob, 9)), (2, lzma.compress(blob, format=lzma.FORMAT_ALONE, preset=6))), key=lambda row: len(row[1]))
   return bytes([pick[0]]) + pick[1]
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
def __peeka__(blob, smoke, crustk, emberk, cinderk, veilk, weftk, thornk): peek=__weld__(__spine__(__unsnare__(__unshroud__(__unravel__(__thorn__(__pair__(blob), thornk + 1), weftk + 1), veilk ^ 0x5A), emberk, cinderk), crustk), smoke); mode=peek[0]; return (zlib.decompress, bz2.decompress, lzma.decompress)[mode](peek[1:])
def __peekb__(blob, slag, ashk, gritk, lavak, smeltk, veilk, weftk, thornk): return __weld__(__unsnare__(__unwhorl__(__scald__(__unshroud__(__unravel__(__thorn__(__pair__(blob), thornk), weftk), veilk), smeltk), lavak), ashk, gritk), slag)
def __corea__(blob, leftk, rightk, mistk, dustk, cloakk, lanek, spurk): return __thorn__(__ravel__(__shroud__(__snare__(__weld__(__gasket__(__weld__(blob, leftk)), rightk), mistk, dustk), cloakk), lanek), spurk)
def __coreb__(blob, leftk, rightk, mistk, dustk, cloakk, lanek, spurk): peek=__weld__(__unsnare__(__unshroud__(__unravel__(__thorn__(blob, spurk), lanek), cloakk), mistk, dustk), rightk); mode=peek[0]; return __weld__((zlib.decompress, bz2.decompress, lzma.decompress)[mode](peek[1:]), leftk)
def __wrapa__(blob, shellk, glassk, forgek, stampk): return __snare__(__weld__(__gasket__(__weld__(blob, shellk)), glassk), forgek, stampk)
def __wrapb__(blob, shellk, glassk, forgek, stampk): peek=__weld__(__unsnare__(blob, forgek, stampk), glassk); mode=peek[0]; return __weld__((zlib.decompress, bz2.decompress, lzma.decompress)[mode](peek[1:]), shellk)
def __mark__(code): return __glow__(code), __bloom__(code), __echo__(code), __magma__(code), __soul__(code), __wisp__(code)
def __key__(seed):
   slag, smoke = __spark__(seed + b'slag', 1000000, 2147483647), __spark__(seed + b'smoke', 1000000, 2147483647)
   ashk, gritk, lavak, crustk = __spark__(seed + b'ash', 17, 251), __spark__(seed + b'grit', 3, 29), __spark__(seed + b'lava', 1, 7), __spark__(seed + b'crust', 9, 33)
   emberk, cinderk, smeltk, veilk = __spark__(seed + b'ember', 17, 251), __spark__(seed + b'cinder', 3, 29), __spark__(seed + b'smelt', 17, 251), __spark__(seed + b'veil', 17, 251)
   weftk, thornk = __spark__(seed + b'weft', 4, 19), __spark__(seed + b'thorn', 2, 11)
   return slag, smoke, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, veilk, weftk, thornk
def __corek__(seed):
   leftk, rightk = __spark__(seed + b'glass', 1000000, 2147483647), __spark__(seed + b'forge', 1000000, 2147483647)
   mistk, dustk, cloakk, lanek, spurk = __spark__(seed + b'mist', 17, 251), __spark__(seed + b'dust', 3, 29), __spark__(seed + b'cloak', 17, 251), __spark__(seed + b'lane', 4, 19), __spark__(seed + b'spur', 2, 11)
   return leftk, rightk, mistk, dustk, cloakk, lanek, spurk
def __wrapk__(seed):
   shellk, glassk = __spark__(seed + b'shell', 1000000, 2147483647), __spark__(seed + b'glasswrap', 1000000, 2147483647)
   forgek, stampk = __spark__(seed + b'forgewrap', 17, 251), __spark__(seed + b'stampwrap', 3, 29)
   return shellk, glassk, forgek, stampk
def __brand__(blob):
    return hashlib.sha256(blob).hexdigest(), hashlib.sha1(blob).hexdigest(), hashlib.md5(blob).hexdigest(), __flare__(blob), zlib.adler32(blob) ^ zlib.crc32(blob)
def __carapace__(raw, seed, kind):
    salt = __mist__(seed + kind + b'salt', len(raw) or 1); off = __spark__(seed + kind + b'off', 0x3040, 0x30ff); lift = __spark__(seed + kind + b'lift', 0x120, 0x780); key = __spark__(seed + kind + b'key', 11, 251)
    wide = ''.join(chr((one ^ salt[slot]) + off) for slot, one in enumerate(raw)); ring = [((one ^ key) + lift) for one in raw]; text = raw.hex(); fog = __mist__(seed + kind + b'weave', len(text) or 1).hex()[:len(text)]
    weave = ''.join(one + two for one, two in zip(fog, text)); veil = base64.b85encode(bytes(one ^ salt[slot] for slot, one in enumerate(raw))).decode('ascii'); shot, coal, soot, ember, glass = __brand__(raw)
    return (kind.decode('ascii'), wide, off, salt.hex(), weave, ring, lift, key, veil, shot, coal, soot, ember, glass)
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
    return ''.join(bag) if len(bag) >= 4 else 'なにこれ'
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
    scripts = [
        (0x4e00, 0x9faf, 'CJK'),
        (0x3041, 0x3096, 'Hiragana'),
        (0x30a1, 0x30fa, 'Katakana'),
        (0xac00, 0xd7a3, 'Korean'),
        (0x0400, 0x04ff, 'Cyrillic'),
        (0x0370, 0x03ff, 'Greek'),
        (0x0900, 0x097f, 'Devanagari'),
        (0x0e00, 0x0e7f, 'Thai'),
        (0x0980, 0x09ff, 'Bengali'),
        (0x1200, 0x137f, 'Ethiopic'),
        (0x10a0, 0x10ff, 'Georgian'),
        (0x13a0, 0x13ff, 'Cherokee'),
        (0x1400, 0x167f, 'UCAS'),
        (0x1680, 0x169f, 'Ogham'),
        (0x16a0, 0x16ff, 'Runic'),
    ]
    bag = []
    for slot in range(count):
        fog = __mist__(seed + b'slategen' + slot.to_bytes(4, 'little'), 16)
        left, right, name = scripts[fog[0] % len(scripts)]
        width = (fog[1] % 6) + 4
        text = []
        for char in range(width):
            ch = chr(left + (int.from_bytes(fog[2 + char * 2:4 + char * 2], 'little') % (right - left + 1)))
            text.append(ch)
        bag.append((''.join(text), name))
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
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)): rows.append((type(node).__name__, len(node.elts), type(node.ctx).__name__, tuple(type(one).__name__ for one in node.elts[:32])))
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
        tab = getattr(one, 'co_linetable', getattr(one, 'co_lnotab', b'')); exc = getattr(one, 'co_exceptiontable', b'')
        arg = (one.co_argcount, getattr(one, 'co_posonlyargcount', 0), one.co_kwonlyargcount, one.co_nlocals, one.co_stacksize, one.co_flags)
        raw = (hashlib.sha256(one.co_code).hexdigest(), hashlib.sha1(tab).hexdigest(), hashlib.sha1(exc).hexdigest())
        con = tuple((slot, type(val).__name__, len(val.co_code) if isinstance(val, type(one)) else len(val) if isinstance(val, (str, bytes, tuple)) else val.bit_length() if isinstance(val, int) else 0) for slot, val in enumerate(one.co_consts[:128]))
        rows.append((getattr(one, 'co_qualname', one.co_name), one.co_name, one.co_filename, one.co_firstlineno, arg, raw, con, tuple(one.co_freevars), tuple(one.co_cellvars)))
    fog = __mix__(seed, tuple(rows))
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
        rows.extend((slot, name, len(name), zlib.adler32(name.encode('utf-8', 'replace')) & 0xffffffff) for slot, name in enumerate(one.co_varnames))
    fog = __mix__(seed, (__hist__(rows), len(rows), len(set(row[1] for row in rows))))
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
        raw = marshal.dumps(one)
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
        data = __vine__(__tuff__(one))
        rows.append((one.co_name, len(data), zlib.crc32(data) & 0xffffffff, zlib.adler32(data) & 0xffffffff))
    fog = __mix__(seed, tuple(rows))
    return (len(rows), fog.hex())
def __dig__(code, seed):
    rows = []
    for one in __drip__(code):
        rows.append((hashlib.sha256(__vine__(__tuff__(one))).hexdigest(), hashlib.sha1(one.co_code).hexdigest(), one.co_name))
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
        rows.append((one.co_name, len(marshal.dumps(one)), len(one.co_code), len(one.co_consts), len(one.co_names), len(one.co_varnames)))
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
        raw = marshal.dumps(one)
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
def __chart__(tree, code, stem, path, seed):
    rows = [fn(tree, seed + tag) for tag, fn in ((b'shape', __shapeid__), (b'literal', __literal__), (b'label', __label__), (b'flow', __flow__), (b'call', __call__), (b'scope', __scope__), (b'module', __module__), (b'set', __set__), (b'sub', __sub__), (b'bin', __bin__), (b'cmp', __cmp__), (b'form', __form__), (b'trap', __trap__), (b'pat', __pat__), (b'ret', __ret__), (b'loop', __loop__), (b'comp', __comp__), (b'ann', __ann__), (b'ref', __ref__), (b'depth', __depth__), (b'tile', __tile__), (b'context', __context__), (b'discard', __discard__), (b'wth', __wth__), (b'body', __body__), (b'glyph', __glyph__), (b'alph', __alph__), (b'span', __span__), (b'gram', __gram__))]
    rows.extend(fn(tree, seed + tag) for tag, fn in ((b'tok', __tok__), (b'atom', __atom__), (b'num', __num__), (b'txt', __txt__), (b'bop', __bop__), (b'cmpr', __cmpr__), (b'dial', __dial__), (b'asgn', __asgn__), (b'river', __river__), (b'catch', __catch__), (b'mask', __mask__), (b'coil', __coil__), (b'fmt', __fmt__), (b'match', __match__), (b'imp', __imp__), (b'func', __func__), (b'arg', __arg__), (b'clan', __clan__), (b'deco', __deco__), (b'anno', __anno__)))
    rows.extend(fn(tree, seed + tag) for tag, fn in ((b'out', __out__), (b'slice', __slice__), (b'seq', __seq__), (b'paper', __paper__), (b'lineage', __lineage__), (b'tree', __tree__), (b'leaf', __leaf__), (b'edge', __edge__), (b'order', __order__), (b'nom', __nom__), (b'attr', __attr__), (b'kwd', __kwd__), (b'place', __place__), (b'sym', __sym__), (b'api', __api__), (b'lit', __lit__), (b'blend', __blend__), (b'block', __block__), (b'expr', __expr__), (b'stmt', __stmt__), (b'hash', __hash__), (b'trace', __trace__), (b'wheel', __wheel__), (b'level', __level__), (b'wrap', __wrap__), (b'source', __source__), (b'middle', __middle__), (b'tail', __tail__), (b'field', __field__), (b'wide', __wide__), (b'den', __den__)))
    rows.extend(fn(code, seed + tag) for tag, fn in ((b'op', __op__), (b'constant', __constant__), (b'line', __line__), (b'free', __free__), (b'window', __window__), (b'vmap', __vmap__), (b'pool', __pool__), (b'ord', __ord__), (b'sig', __sig__), (b'byte', __byte__), (b'blob', __blob__), (b'opcode', __opcode__), (b'quad', __quad__), (b'const', __const__), (b'nam', __nam__), (b'var', __var__), (b'cell', __cell__), (b'tab', __tab__), (b'except', __except__), (b'coord', __coord__), (b'fname', __fname__), (b'argv', __argv__), (b'flag', __flag__), (b'mar', __mar__), (b'slot', __slot__), (b'ordr', __ordr__), (b'pack', __pack__), (b'dig', __dig__), (b'pond', __pond__), (b'stk', __stk__)))
    rows.extend(fn(code, seed + tag) for tag, fn in ((b'qual', __qual__), (b'size', __size__), (b'rng', __rng__), (b'duo', __duo__), (b'tri', __tri__), (b'oct', __oct__), (b'cnt', __cnt__), (b'dep', __dep__), (b'kind', __kind__), (b'pak', __pak__), (b'trail', __trail__), (b'split', __split__), (b'xor', __xor__), (b'sum', __sum__), (b'layout', __layout__), (b'mesh', __mesh__), (b'gate', __gate__), (b'fold', __fold__)))
    rows.extend((__salt__(tree, code, seed + b'salt').hex(), __ring__(tree, code, seed + b'ring')))
    mark = (os.path.basename(path), len(stem), hashlib.sha256(stem).hexdigest(), zlib.crc32(stem) & 0xffffffff, zlib.adler32(stem) & 0xffffffff)
    core = __vine__((tuple(rows), mark))
    fog = hashlib.sha512(core).digest()
    salt = __mist__(seed + b'atlas' + fog, 64)
    return hashlib.blake2b(fog + salt + core[:4096], digest_size=64).digest()
def __vein__(code):
    tree = ast.parse(code)
    seed = hashlib.sha256(code.encode('utf-8')).digest()
    store = []
    plain = []
    seen = {}
    dust = {'__import__','abs','all','any','ascii','bin','breakpoint','callable','chr','classmethod','compile','delattr','dir','divmod','eval','exec','format','getattr','globals','hasattr','hash','hex','id','input','isinstance','issubclass','iter','len','locals','max','memoryview','min','next','oct','open','ord','pow','print','property','repr','round','setattr','slice','sorted','staticmethod','sum','vars','bool','bytearray','bytes','complex','dict','enumerate','filter','float','frozenset','int','list','map','object','range','reversed','set','str','super','tuple','type','zip'}
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
    blob, keep, load, proof, tint, rune, dawn, dusk, kiln, loom, reef, wave, mire, sootf, brimf, crustf, ashf, flaref, cask, spinef, huskf, barkf = [__mint__(used, seed, mint) for slot in range(22)]
    tick = [0]
    gate = [0]
    def __cast__(node, kind, skip):
        for field, value in ast.iter_fields(node):
            if field in skip:
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
        raiser = ast.Raise(exc=ast.Call(func=ast.Name(id='Exception', ctx=ast.Load()), args=[ast.Name(id=flag, ctx=ast.Load())], keywords=[]))
        real = []
        junk = []
        for slot, one in enumerate(body):
            cond = ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=err, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(rock + 1)])
            real.append(ast.If(test=cond, body=[one], orelse=[]))
            tick[0] += 1
            fake = __spark__(seed + b'ledgejunk' + tick[0].to_bytes(4, 'little'), 10**5, 10**8)
            jcond = ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=err, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(fake)])
            junk.append(ast.If(test=jcond, body=[ast.Assign(targets=[ast.Name(id=trap, ctx=ast.Store())], value=ast.Constant(fake))], orelse=[]))
        handler = ast.ExceptHandler(type=ast.Name(id='Exception', ctx=ast.Load()), name=err, body=real + junk)
        wrap = ast.Try(body=[bump, raiser], handlers=[handler], orelse=[], finalbody=[])
        return [init, wrap]
    def __gorge__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        rock = __spark__(seed + b'gorge' + tick[0].to_bytes(4, 'little'), 10**4, 10**7)
        nest = ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=slag)], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Name(id=slag, ctx=ast.Load())), args=[ast.Constant(rock)], keywords=[])
        for _ in range(__spark__(seed + b'gorgedepth' + tick[0].to_bytes(4, 'little'), 2, 5)):
            wrap = __mint__(used, seed, mint)
            nest = ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=wrap)], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Name(id=wrap, ctx=ast.Load())), args=[nest], keywords=[])
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
        return ast.While(test=ast.Constant(False), body=[ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(utext)), ast.Expr(value=ast.Call(func=ast.Name(id='len', ctx=ast.Load()), args=[ast.Name(id=coal, ctx=ast.Load())], keywords=[]))], orelse=[])
    def __dune__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        rock = __spark__(seed + b'dune' + tick[0].to_bytes(4, 'little'), 10**6, 10**9)
        utext = ''.join(chr(__spark__(seed + b'duneu' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x1200, 0x137f)) for s in range(8))
        inner = ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(utext))
        outer = ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Constant(rock))
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Try(body=[inner], handlers=[], orelse=[], finalbody=[outer])], orelse=[])
    def __cairn__():
        tick[0] += 1
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        utext = ''.join(chr(__spark__(seed + b'cairnu' + tick[0].to_bytes(4, 'little') + s.to_bytes(2, 'little'), 0x0e00, 0x0e7f)) for s in range(6))
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(utext)), ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Call(func=ast.Name(id='type', ctx=ast.Load()), args=[ast.Constant(None)], keywords=[]))], orelse=[])
    def __cinder__():
        tick[0] += 1
        bag = []
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        glass = __mint__(used, seed, mint)
        rock = __spark__(seed + b'junk' + tick[0].to_bytes(4, 'little'), 10**7, 10**9)
        text = ['obsidian', 'glass', 'ash', 'vein'][__spark__(seed + b'text' + tick[0].to_bytes(4, 'little'), 0, 3)]
        bag.append(ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(rock)), ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Constant(text)), ast.Expr(value=ast.Call(func=ast.Name(id='str', ctx=ast.Load()), args=[ast.Name(id=glass, ctx=ast.Load())], keywords=[]))], orelse=[ast.Pass()]))
        bag.append(__seam__())
        bag.append(__gorge__())
        slag2 = __mint__(used, seed, mint)
        coal2 = __mint__(used, seed, mint)
        rock2 = __spark__(seed + b'ujunk' + tick[0].to_bytes(4, 'little'), 0x4e00, 0x9fff)
        utext = ''.join(chr(__spark__(seed + b'uchar' + tick[0].to_bytes(4, 'little') + slot.to_bytes(2, 'little'), 0x4e00, 0x9fff)) for slot in range(8))
        bag.append(ast.If(test=ast.Compare(left=ast.Constant(rock2), ops=[ast.Lt()], comparators=[ast.Constant(0)]), body=[ast.Assign(targets=[ast.Name(id=slag2, ctx=ast.Store())], value=ast.Constant(utext)), ast.Expr(value=ast.Call(func=ast.Name(id='len', ctx=ast.Load()), args=[ast.Name(id=coal2, ctx=ast.Load())], keywords=[]))], orelse=[ast.Pass()]))
        bag.append(__knoll__())
        bag.append(__dale__())
        bag.append(__scree__())
        bag.append(__cliff__())
        bag.append(__reef__())
        bag.append(__dune__())
        bag.append(__cairn__())
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
        wrappers = [0, 1, 2]
        for one in body:
            if done < 3 and not isinstance(one, (ast.Global, ast.Nonlocal)) and not (isinstance(one, ast.ImportFrom) and one.module == '__future__'):
                pick = wrappers[done % 3]
                if pick == 0:
                    bag.append(ast.Try(body=[ast.Expr(value=ast.BinOp(left=ast.Constant(1), op=ast.Div(), right=ast.Constant(0)))], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()), name=None, body=[one])], orelse=[], finalbody=[]))
                elif pick == 1:
                    bag.append(ast.Try(body=[ast.Expr(value=ast.BinOp(left=ast.Constant(1), op=ast.Mod(), right=ast.Constant(1)))], handlers=[ast.ExceptHandler(type=None, name=None, body=[ast.Pass()])], orelse=[one], finalbody=[]))
                else:
                    bag.append(ast.Try(body=[ast.Expr(value=ast.Call(func=ast.Name(id='type', ctx=ast.Load()), args=[ast.Constant(None)], keywords=[]))], handlers=[], orelse=[], finalbody=[one]))
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
        name = __mint__(used, seed, mint)
        return ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=name)], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Name(id=name, ctx=ast.Load())), args=[node], keywords=[])
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
                out = ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=name)], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.IfExp(test=ast.Name(id=name, ctx=ast.Load()), body=one, orelse=ast.Name(id=name, ctx=ast.Load()))), args=[out], keywords=[])
            return out
        if isinstance(node.op, ast.Or):
            for one in vals[1:]:
                name = __mint__(used, seed + b'or' + len(vals).to_bytes(2, 'little'), mint)
                out = ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=name)], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.IfExp(test=ast.Name(id=name, ctx=ast.Load()), body=ast.Name(id=name, ctx=ast.Load()), orelse=one)), args=[out], keywords=[])
            return out
        return node
    def __ember__(val):
        key = ('s', val) if isinstance(val, str) else ('b', val)
        if key not in seen:
            seen[key] = len(store)
            raw = val.encode('utf-8') if isinstance(val, str) else val
            kind = b's' if isinstance(val, str) else b'b'
            store.append(__carapace__(raw, seed + len(store).to_bytes(4, 'little'), kind))
            plain.append(val)
        return ast.Call(func=ast.Name(id=load, ctx=ast.Load()), args=[ast.Constant(seen[key])], keywords=[])
    def __rift__(val):
        size = len(val)
        if size < 4:
            return [val]
        fog = hashlib.sha256(seed + type(val).__name__.encode('ascii', 'ignore') + size.to_bytes(4, 'little')).digest(); bag = []; slot = 0; at = 0
        while slot < size:
            left = size - slot; step = min(7, left); take = 1 + (fog[at % len(fog)] % step)
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
        return __fuse__(__rift__(val), 's')
    def __haze__(val):
        return __fuse__(__rift__(val), 'b')
    def __count__(val):
        off = 97 + ((abs(val) * 1315423911 + seed[0]) % 999903); key = 17 + ((abs(val) * 2654435761 + seed[1]) % 65519); ash = 33 + ((abs(val) * 2246822519 + seed[2]) % 65503)
        if (seed[3] + abs(val)) & 1:
            core = ((val ^ key) + ash) - off
            return ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.Constant(core), op=ast.Add(), right=ast.Constant(off)), op=ast.Sub(), right=ast.Constant(ash)), op=ast.BitXor(), right=ast.Constant(key))
        core = ((val + off) ^ key) + ash
        return ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.Constant(core), op=ast.Sub(), right=ast.Constant(ash)), op=ast.BitXor(), right=ast.Constant(key)), op=ast.Sub(), right=ast.Constant(off))
    def __float__(val):
        return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id='float', ctx=ast.Load()), __ember__('fromhex')], keywords=[]), args=[__stray__(val.hex())], keywords=[])
    def __plex__(val):
        return ast.Call(func=ast.Name(id='complex', ctx=ast.Load()), args=[__float__(float(val.real)), __float__(float(val.imag))], keywords=[])
    def __truth__(val):
        left = (seed[4] & 1) + 1
        return ast.Compare(left=ast.Constant(left), ops=[ast.Eq()], comparators=[ast.Constant(left if val else left + 1)])
    def __void__():
        return ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Constant(None)), args=[], keywords=[])
    def __dot__():
        return ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Constant(Ellipsis)), args=[], keywords=[])
    def __slab__():
        raw = marshal.dumps(tuple(plain))
        core = base64.b85encode(zlib.compress(raw, 9)).decode('ascii')
        test = __mist__(seed + b'proof', 48)
        gold = base64.b85encode(test).decode('ascii')
        check = zlib.crc32(test) + zlib.adler32(test)
        text = f"""{blob}={core!r}
{proof}={gold!r}
{keep}=None
{tint}={{}}
def {dawn}(v,o,p):
 rows=bytes.fromhex(p)
 len(rows)!=len(v) and (_ for _ in ()).throw(RuntimeError('bad'))
 return bytes(((ord(one)-o)^rows[slot]) for slot,one in enumerate(v))
def {dusk}(v):
 (len(v)&1) and (_ for _ in ()).throw(RuntimeError('bad'))
 return bytes.fromhex(v[1::2])
def {kiln}(v,o,p):
 return bytes((((one-o)&255)^p) for one in v)
def {loom}(v,p):
 rows=bytes.fromhex(p)
 fog=__import__('base64').b85decode(v.encode())
 len(rows)!=len(fog) and (_ for _ in ()).throw(RuntimeError('bad'))
 return bytes(one^rows[slot] for slot,one in enumerate(fog))
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
 return (__import__('hashlib').sha256(blob).hexdigest(),__import__('hashlib').sha1(blob).hexdigest(),__import__('hashlib').md5(blob).hexdigest(),{reef}(blob),__import__('zlib').adler32(blob)^__import__('zlib').crc32(blob))
def {rune}(k,v,o,p,r,u,l,f,t,h,s,e,g,m):
  rows={mire}(v,o)
  spin={sootf}(u)
  (rows[0]!=spin[0] or rows[0]!=len(bytes.fromhex(p)) or rows[0]!=len(__import__('base64').b85decode(t.encode()))) and (_ for _ in ()).throw(RuntimeError('bad'))
  {brimf}(r)
  {huskf}(len(bytes.fromhex(p)),rows[0])
  spec={cask}(r)
  spec[1]!=(rows[0]*4) and (_ for _ in ()).throw(RuntimeError('bad'))
  ash={ashf}({dawn}(v,o,p),{dusk}(r))
  ash={ashf}(ash,{kiln}(u,l,f))
  ash={ashf}(ash,{loom}(t,p))
  fog={crustf}(ash)
  fog[0]!=rows[0] and (_ for _ in ()).throw(RuntimeError('bad'))
  tips={flaref}(ash)
  tips[2]!=rows[0] and (_ for _ in ()).throw(RuntimeError('bad'))
  spin={spinef}(ash)
  (spin[0]^spin[1])!=m and (_ for _ in ()).throw(RuntimeError('bad'))
  rows={wave}(ash)
  (rows[0]!=h or rows[1]!=s or rows[2]!=e or rows[3]!=g or rows[4]!=m) and (_ for _ in ()).throw(RuntimeError('bad'))
  return ash if k=='b' else ash.decode('utf-8')
def {load}(i):
 global {keep}
 if {keep} is None:
   row=__import__('base64').b85decode({proof}.encode());(__import__('zlib').crc32(row)+__import__('zlib').adler32(row)!={check}) and (_ for _ in ()).throw(RuntimeError('bad'))
   {keep}=tuple({barkf}(__import__('zlib').decompress(__import__('base64').b85decode({blob}.encode()))))
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
        if keepfuture and store:
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
            if node.name and __token__(node.name) and not (wall[0] > 0 and room[0] == 0):
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
            if isinstance(node.ctx, ast.Load) and node.id in dust and node.id not in bind:
                return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__('builtins')], keywords=[]), __ember__(node.id)], keywords=[])
            return node
        if isinstance(node, ast.JoinedStr):
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
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__('builtins')], keywords=[]), __ember__('list')], keywords=[]), args=[ast.Tuple(elts=node.elts, ctx=ast.Load())], keywords=[])
        if isinstance(node, ast.Tuple) and isinstance(node.ctx, ast.Load) and not any(isinstance(one, ast.Starred) for one in node.elts):
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__('builtins')], keywords=[]), __ember__('tuple')], keywords=[]), args=[ast.List(elts=node.elts, ctx=ast.Load())], keywords=[])
        if isinstance(node, ast.Slice):
            return ast.Call(func=ast.Name(id='slice', ctx=ast.Load()), args=[__gloom__(node.lower) if node.lower else ast.Constant(None), __gloom__(node.upper) if node.upper else ast.Constant(None), __gloom__(node.step) if node.step else ast.Constant(None)], keywords=[])
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
            for alias in node.names:
                bag.append(ast.Assign(targets=[ast.Name(id=alias.asname or alias.name, ctx=ast.Store())], value=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__(mod)], keywords=[ast.keyword(arg='fromlist', value=ast.List(elts=[__ember__(alias.name)], ctx=ast.Load())), ast.keyword(arg='level', value=ast.Constant(node.level))]), __ember__(alias.name)], keywords=[])))
            return bag
        if isinstance(node, ast.Set) and node.elts:
            name = __mint__(used, seed, mint)
            return ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=ast.arg(arg=name), kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__('builtins')], keywords=[]), __ember__('set')], keywords=[]), args=[ast.Name(id=name, ctx=ast.Load())], keywords=[])), args=node.elts, keywords=[])
        if isinstance(node, ast.Dict) and node.keys and all(isinstance(one, ast.Constant) and isinstance(one.value, str) and one.value.isidentifier() and not __import__('keyword').iskeyword(one.value) for one in node.keys if one is not None):
            name = __mint__(used, seed, mint)
            return ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=ast.arg(arg=name), defaults=[]), body=ast.Name(id=name, ctx=ast.Load())), args=[], keywords=[ast.keyword(arg=one.value, value=two) for one, two in zip(node.keys, node.values)])
        if isinstance(node, ast.Call):
            keys = []
            gate = {'super','eval','exec','globals','locals','vars','dir','hasattr','getattr','setattr','__import__','type','isinstance','issubclass'}
            for one in node.keywords:
                if one.arg is None:
                    keys.append(one)
                else:
                    keys.append(ast.keyword(arg=None, value=ast.Dict(keys=[__ember__(one.arg)], values=[one.value])))
            node.keywords = keys
            if not (isinstance(node.func, ast.Name) and node.func.id in gate):
                node.func = __gloom__(node.func)
            return node
        if isinstance(node, ast.Compare) and len(node.ops) == 1 and len(node.comparators) == 1:
            look = {ast.Eq: '__eq__', ast.NotEq: '__ne__', ast.Lt: '__lt__', ast.LtE: '__le__', ast.Gt: '__gt__', ast.GtE: '__ge__'}
            op = look.get(type(node.ops[0]))
            if op:
                return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.left, __ember__(op)], keywords=[]), args=[node.comparators[0]], keywords=[])
        if isinstance(node, ast.BinOp) and (op := {ast.Add: 'add', ast.Sub: 'sub', ast.Mult: 'mul', ast.Div: 'truediv', ast.FloorDiv: 'floordiv', ast.Mod: 'mod', ast.Pow: 'pow', ast.LShift: 'lshift', ast.RShift: 'rshift', ast.BitOr: 'or_', ast.BitXor: 'xor', ast.BitAnd: 'and_'}.get(type(node.op))): return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__('operator')], keywords=[]), __ember__(op)], keywords=[]), args=[node.left, node.right], keywords=[])
        if isinstance(node, ast.UnaryOp) and (name := __mint__(used, seed, mint)): return ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=name)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=ast.UnaryOp(op=node.op, operand=ast.Name(id=name, ctx=ast.Load()))), args=[node.operand], keywords=[])
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
            return node
        if isinstance(node, ast.Assert):
            node.test = __gloom__(node.test)
            return node
        if isinstance(node, ast.Return) and node.value is not None:
            node.value = __gloom__(node.value)
            return node
        if isinstance(node, ast.Raise) and node.exc is not None:
            node.exc = __gloom__(node.exc)
            return node
        if isinstance(node, ast.FormattedValue):
            node.value = __gloom__(node.value)
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
        if isinstance(node, ast.Call) and node.keywords:
            node = __mesa__(node)
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
            return ast.copy_location(__count__(node.value), node)
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
    blob, left, right, skin, heart, bone, hand, guard, split, stampf, prove, openf, runf, coref, sink, seal, storm, shell, hold, wake, brim, shale, cove, drift, emberf, talc, shalef, quill, moss, dune, gully, shalex, beryl, gnarl, scarp, obsf, tufff, vinef, glowf, rift, cull, thorn, flake, peat, cliff, frost, shardf, veilf, basaltf, hollow, marrow, briar, huskf, grovef, miref, shardy, cragf, fenf, screef, drusef, codonf, evalf = [__mint__(used, seed, mint) for slot in range(62)]
    inner = f"""import base64,bz2,hashlib,lzma,marshal,sys,zlib
{blob}={rack!r}
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
def {heart}(blob,key):
 rows=bytearray()
 glow=key&255
 drift=((key>>8)&255) or 73
 tint=((key>>16)&255) or 19
 for slot,byte in enumerate(blob):
  glow=(glow+drift+slot+tint)&255
  rows.append(byte^glow^((tint+slot)&255))
 return bytes(rows)
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
 if 'builtins' in rows and mark=='builtins' and 'built-in' not in text:
  raise SystemExit
 return hold
def {hand}():
 built=__import__('builtins');sys=__import__('sys')
 {bone}('exec',built,('builtins',))
 {bone}('eval',built,('builtins',))
 {bone}('compile',built,('builtins',))
 {bone}('open',built,('builtins','io','_io'))
 {bone}('__import__',built,('builtins',))
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
def {huskf}(code):
 {shardf}(code)!={rift} and (_ for _ in ()).throw(SystemExit)
 {basaltf}(code)!={cull} and (_ for _ in ()).throw(SystemExit)
 {hollow}(code)!={thorn} and (_ for _ in ()).throw(SystemExit)
 {marrow}(code)!={flake} and (_ for _ in ()).throw(SystemExit)
 {briar}(code)!={peat} and (_ for _ in ()).throw(SystemExit)
 return code
def {grovef}(ct,name,restype,argtypes):
 hold=getattr(ct.pythonapi,name,None)
 if hold is None: raise SystemExit
 if not callable(hold): raise SystemExit
 hold.restype=restype;hold.argtypes=argtypes
 return hold
def {miref}(blob):
 ct=__import__('ctypes');left=marshal.loads(blob);{huskf}(left);name=''.join(('PyMarshal_','ReadObjectFromString'));read={grovef}(ct,name,ct.py_object,[ct.c_char_p,ct.c_long]);box=ct.create_string_buffer(blob);right=read(ct.cast(box,ct.c_char_p),len(blob))
 {huskf}(right)
 {shardf}(left)!={shardf}(right) and (_ for _ in ()).throw(SystemExit)
 {basaltf}(left)!={basaltf}(right) and (_ for _ in ()).throw(SystemExit)
 {marrow}(left)!={marrow}(right) and (_ for _ in ()).throw(SystemExit)
 {briar}(left)!={briar}(right) and (_ for _ in ()).throw(SystemExit)
 return right
def {evalf}(code):
 {hand}();{huskf}(code);ct=__import__('ctypes');name=''.join(('PyEval_','EvalCode'));run={grovef}(ct,name,ct.py_object,[ct.py_object,ct.py_object,ct.py_object])
 return run(code,globals(),globals())
def {guard}(blob,mark,seal):
 glow=0
 slot=0
 while slot < len(blob):
  row=blob[slot:slot+16]
  for byte in row:
   glow=(glow+byte)&0xffffffff
   glow=((glow<<7)|(glow>>25))&0xffffffff
   glow^=(byte*131)&0xffffffff
  slot += 16
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
 while slot < len(blob):
  hold.append(len(blob[slot:slot+16]))
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
 rows=[(byte^slot)&255 for slot,byte in enumerate(blob)]
 if not rows:
  raise SystemExit
 rows=(len(rows),sum(rows)&0xffffffff,min(rows),max(rows))
 if rows[1]==0:
  raise SystemExit
 if rows[3]<rows[2]:
  raise SystemExit
 return rows
def {beryl}(blob):
 rows=(len(blob),sum(blob)&0xffffffff)
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
 rows=blob[::2]
 rows=(len(rows),sum(rows)&0xffffffff)
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
 tab=base64.b85decode({codonf}[0].encode());inv=base64.b85decode({codonf}[1].encode());salt=base64.b85decode({codonf}[2].encode());add,step,twist,turn,drift,mask={codonf}[3];sig={codonf}[4]
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
 mode=shell[0];shell=(zlib.decompress,bz2.decompress,lzma.decompress)[mode](shell[1:])
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
 mode=shell[0]
 if mode not in (0,1,2):
  raise SystemExit
 shell=shell[1:]
 return (zlib.decompress,bz2.decompress,lzma.decompress)[mode](shell)
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
    ore = marshal.dumps(compile(inner, stamp, 'exec', optimize=2, dont_inherit=True))
    pack = __gasket__(ore)
    leftk, rightk, mistk, dustk, cloakk, lanek, spurk = __corek__(seed)
    probe = __corea__(pack, leftk, rightk, mistk, dustk, cloakk, lanek, spurk)
    core = pack
    core = __weld__(core, leftk)
    core = __gasket__(core)
    core = __weld__(core, rightk)
    core = __snare__(core, mistk, dustk)
    core = __shroud__(core, cloakk)
    core = __ravel__(core, lanek)
    core = __thorn__(core, spurk)
    graink = __chaff__(core)
    probe != core and (_ for _ in ()).throw(ValueError('core'))
    __coreb__(probe, leftk, rightk, mistk, dustk, cloakk, lanek, spurk) != pack and (_ for _ in ()).throw(ValueError('core'))
    flag = hashlib.sha256(core).hexdigest()
    shell, glass, forge, stampf, heart, driftf, emberg = [__mint__(used, seed + b'wrap', mint) for slot in range(7)]
    hint=('inject','hook','patch','debug','reverse','spy','monitor','trace','decompile','dump','scan','attach','detach','httptoolkit','http-toolkit','frida','objection','xposed','substrate','mitmproxy','burp','fiddler','charles','proxifier','interceptor')
    debug=('ida','ida64','idaq','idaq64','x64dbg','x32dbg','ollydbg','windbg','cdb','ntsd','kd','ghidra','frida','cheatengine','cheat engine','ce-','dnspy','dotpeek','ilspy','immunity','radare','r2','gdb','lldb','edb','hopper','binaryninja','cutter')
    anlz=('procmon','procmon64','procexp','procexp64','wireshark','fiddler','charles','mitmproxy','burp','processhacker','process hacker','apimonitor','httpdebuggerpro','tcpview','regmon','filemon','autoruns','pestudio','die','peid','exeinfope','scylla','lordpe','petools','resourcehacker','hxd','010editor')
    vm=('vmtoolsd','vmwaretray','vmwareuser','vgauthservice','vmacthlp','vboxservice','vboxtray','sandboxie','vmsrvc','vmusrvc','xenservice','qemu-ga','qemu','hyperv','virtualbox','prl_tools','prl_cc','joeboxserver','joeboxcontrol')
    cmd=('tasklist','wmic','netstat','handle','listdlls','strings','dumpbin','objdump','nm ','readelf','strace','ltrace','scanmem','artmoney','gameguardian')
    host=('discord.com','discordapp.com','webhook.site','api.telegram.org','telegram.org','pastebin.com','hastebin.com','transfer.sh','api.ipify.org','ip-api.com','ngrok.io','ngrok.app','pipedream.net','raw.githubusercontent.com','file.io')
    key=('token','password','cookie','session','auth','credit','card','api_key','apikey','bearer','credential','license','webhook','private','secret')
    decomp=('uncompyle6','decompyle3','pycdc','unpyc','pycparser','astor','uncompyle2','easy_python_decompiler','uncompyle','pyc2py')
    sbx=('sandbox','virus','malware','sample','analysis','cuckoo','any.run','hybrid','joe','cape','triage','hatching','intezer')
    mac=('00:05:69','00:0c:29','00:1c:14','00:50:56','08:00:27','52:54:00','00:21:f6','00:14:4f','00:15:5d','00:1c:42','00:03:ff','00:0f:4b','00:16:3e','02:42:ac','02:00:17')
    mods=('ast','dis','inspect','code','compileall','pdb','trace','bdb','linecache','_ast','pydevd','debugpy','frida','objection') + decomp
    api=('NtQueryInformationProcess','IsDebuggerPresent','CheckRemoteDebuggerPresent','VirtualProtect','MiniDumpWriteDump')
    dll=('ntdll.dll','kernel32.dll','user32.dll','dbghelp.dll')
    outer = f"""import base64,bz2,ctypes,gc,hashlib,lzma,marshal,os,platform,socket,sys,uuid,zlib
tag=False;hint={hint!r};debug={debug!r};anlz={anlz!r};vm={vm!r};cmd={cmd!r};host={host!r};key={key!r};decomp={decomp!r};sbx={sbx!r};mac={mac!r};mods={mods!r};api={api!r};dll={dll!r}
base=id(globals().get('__builtins__'));trid=id(sys.settrace);prid=id(sys.setprofile);meta=len(sys.meta_path) if hasattr(sys,'meta_path') else 0;path=len(sys.path_hooks) if hasattr(sys,'path_hooks') else 0
blob={base64.b85encode(core).decode('ascii')!r};left={leftk};right={rightk};add={mistk};step={dustk};veil={cloakk};span={lanek};spur={spurk};grain={graink!r};shot={flag!r};mark={stamp!r}
def bad():raise SystemExit
def boom():
 global tag;tag=True;return True
def wake():
  sys.tracebacklimit=0
  try:gc.collect()
  except:pass
  return 0
def cloak(blob,salt):
  rows=bytearray();tilt=((salt>>3)&15)+1
  for slot,byte in enumerate(blob):
   fog=((byte>>4)|((byte<<4)&255))&255
   rows.append(fog^((salt+slot*tilt+(slot>>1))&255))
  return bytes(rows)
def unlace(blob,span):
  rows=[];slot=0;span=max(2,span)
  while slot < len(blob):
   part=blob[slot:slot+span];left=part[:len(part)//2];right=part[len(part)//2:];out=bytearray(len(part));out[::2]=right;out[1::2]=left
   rows.append(bytes(out));slot += span
  return b''.join(rows)
def scree(blob,span):
  rows=[];slot=0;span=max(2,span);flip=0
  while slot < len(blob):
   part=blob[slot:slot+span];rows.append(part[::-1] if flip&1 else part);slot += span;flip += 1
  return b''.join(rows)
def sift(blob):
  rows=[];slot=0;glow=0
  while slot < len(blob):
   part=blob[slot:slot+32];row=(len(part),sum(part)&0xffff,part[:1],part[-1:]);rows.append(row);glow=(glow+((slot+1)*((row[1] or 1)&0xffff)))&0xffffffff;slot += 32
  if not rows:
   return (0,0,(0,0,b'',b''),(0,0,b'',b''),0)
  return (len(blob),len(rows),rows[0],rows[-1],glow)
def wash():
 for one in mods:
  try:sys.modules.pop(one,None)
  except:pass
 try:rows=list(sys.modules)
 except:rows=[]
 for one in rows:
  low=str(one).lower()
  for word in hint+decomp+sbx:
   if word in low:
    try:del sys.modules[one]
    except:pass
    break
 return 0
def leash():
 if hasattr(sys,'meta_path'):
  try:
   for one in list(sys.meta_path):
    low=(getattr(one,'__module__','')+' '+type(one).__name__).lower()
    for word in hint+decomp:
     if word in low:
      try:sys.meta_path.remove(one)
      except:pass
      break
  except:pass
 if hasattr(sys,'path_hooks'):
  try:
   for one in list(sys.path_hooks):
    low=(getattr(one,'__module__','')+' '+type(one).__name__).lower()
    for word in hint+decomp:
     if word in low:
      try:sys.path_hooks.remove(one)
      except:pass
      break
  except:pass
 return 0
def gate(name,home,need):
 hold=getattr(home,name,None)
 if hold is None or not callable(hold):return boom()
 if getattr(hold,'__name__',name)!=name:return boom()
 rows=need if isinstance(need,tuple) else (need,)
 if getattr(hold,'__module__',None) not in rows:return boom()
 if hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__):return boom()
 return hold
def mesh():
 built=__import__('builtins')
 gate('exec',built,('builtins',));gate('eval',built,('builtins',));gate('compile',built,('builtins',));gate('open',built,('builtins','io','_io'));gate('__import__',built,('builtins',));gate('loads',marshal,('marshal',));gate('decompress',zlib,('zlib',));gate('decompress',bz2,('bz2','_bz2'));gate('decompress',lzma,('lzma','_lzma'))
 for one in (eval,exec,compile,__import__,open,type,getattr,setattr):
  if hasattr(one,'__wrapped__') or (hasattr(one,'__closure__') and one.__closure__):return boom()
 return 0
def hush():
 for one in (lambda:sys.gettrace() is None,lambda:sys.getprofile() is None,lambda:id(eval)==id(eval),lambda:id(exec)==id(exec),lambda:id(compile)==id(compile),lambda:type(open).__name__=='builtin_function_or_method',lambda:type(print).__name__=='builtin_function_or_method',lambda:__import__.__module__ in ('builtins',None)):
  try:
   if not one():return boom()
  except:return boom()
 return 0
def comb():
 built=globals().get('__builtins__');rows=('exec','eval','compile','open','__import__','print')
 if isinstance(built,dict):
  for one in rows:
   if one not in built or hasattr(built[one],'__wrapped__') or (hasattr(built[one],'__closure__') and built[one].__closure__):return boom()
 else:
  for one in rows:
   hold=getattr(built,one,None)
   if hold is None or hasattr(hold,'__wrapped__') or (hasattr(hold,'__closure__') and hold.__closure__):return boom()
 return 0
def pine():
 if id(sys.settrace)!=trid or id(sys.setprofile)!=prid:return boom()
 hold=id(globals().get('__builtins__'))
 if base and hold!=base:return boom()
 if hasattr(sys,'meta_path') and len(sys.meta_path)>meta+2:return boom()
 if hasattr(sys,'path_hooks') and len(sys.path_hooks)>path+2:return boom()
 return 0
def nail():
 for one in (exec,eval,compile):
  try:one.__code__;return boom()
  except AttributeError:pass
  except:return boom()
 return 0
def iron():
 if os.name!='nt':return 0
 try:
  if ctypes.windll.kernel32.IsDebuggerPresent():return boom()
 except:pass
 try:
  slot=ctypes.c_int(0);ctypes.windll.kernel32.CheckRemoteDebuggerPresent(ctypes.windll.kernel32.GetCurrentProcess(),ctypes.byref(slot))
  if slot.value:return boom()
 except:pass
 return 0
def coal():
 if os.name!='nt':return 0
 try:
  hold=ctypes.windll.ntdll.NtQueryInformationProcess;flag=ctypes.c_ulong(0);side=hold(ctypes.windll.kernel32.GetCurrentProcess(),0x1F,ctypes.byref(flag),ctypes.sizeof(flag),None)
  if not side and not flag.value:return boom()
 except:pass
 return 0
def frost():
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
    if row[0] in (0xE9,0xEB) or (row[0]==0xFF and row[1]==0x25):return boom()
 except:pass
 return 0
class Box(ctypes.Structure):_fields_=[('ContextFlags',ctypes.c_ulong),('Dr0',ctypes.c_ulonglong),('Dr1',ctypes.c_ulonglong),('Dr2',ctypes.c_ulonglong),('Dr3',ctypes.c_ulonglong),('Dr6',ctypes.c_ulonglong),('Dr7',ctypes.c_ulonglong)]
def shard():
 if os.name!='nt':return 0
 try:
  box=Box();box.ContextFlags=0x10;ok=ctypes.windll.kernel32.GetThreadContext(ctypes.windll.kernel32.GetCurrentThread(),ctypes.byref(box))
  if ok and (box.Dr0 or box.Dr1 or box.Dr2 or box.Dr3):return boom()
 except:pass
 return 0
def ember():
 rows=[]
 try:rows.extend(str(one).lower() for one in sys.modules)
 except:pass
 try:rows.extend((getattr(one,'__module__','')+' '+type(one).__name__).lower() for one in getattr(sys,'meta_path',()))
 except:pass
 try:rows.extend((getattr(one,'__module__','')+' '+type(one).__name__).lower() for one in getattr(sys,'path_hooks',()))
 except:pass
 text=' '.join(str(one).lower() for one in sys.argv);rows.append(text)
 for word in hint+debug+anlz+vm+decomp+sbx:
  if any(word in one for one in rows):return boom()
 for word in cmd+host:
  if word in text:return boom()
 bits=[]
 for one in sys.argv:bits.extend(part.lower() for part in str(one).replace('/',' ').replace('\\\\',' ').replace(':',' ').replace('-',' ').split())
 for word in key:
  if word in bits:return boom()
 try:
  low=' '.join((socket.gethostname(),platform.node(),str(os.environ.get('USERNAME','')),str(os.environ.get('COMPUTERNAME','')))).lower()
  for word in vm+sbx:
   if word in low:return boom()
 except:pass
 try:
  low=':'.join(['{{:02x}}'.format((uuid.getnode()>>(slot*8))&255) for slot in range(6)][::-1][:3]).lower()
  if any(low.startswith(one) for one in mac):return boom()
 except:pass
 return 0
def read(blob):
 left=marshal.loads(blob)
 if getattr(left,'co_filename','')!=mark:return boom()
 name=''.join(('PyMarshal_','ReadObjectFromString'));hold=getattr(ctypes.pythonapi,name);hold.restype=ctypes.py_object;hold.argtypes=[ctypes.c_char_p,ctypes.c_long]
 box=ctypes.create_string_buffer(blob);right=hold(ctypes.cast(box,ctypes.c_char_p),len(blob))
 if getattr(right,'co_filename','')!=mark or type(left) is not type(right) or getattr(left,'co_name','')!=getattr(right,'co_name',''):return boom()
 return right
def fire(code):
 name=''.join(('PyEval_','EvalCode'));hold=getattr(ctypes.pythonapi,name);hold.restype=ctypes.py_object;hold.argtypes=[ctypes.py_object,ctypes.py_object,ctypes.py_object]
 return hold(code,globals(),globals())
def fetch():
  shell=base64.b85decode(blob.encode());hashlib.sha256(shell).hexdigest()!=shot and (_ for _ in ()).throw(SystemExit)
  sift(shell)!=grain and (_ for _ in ()).throw(SystemExit)
  shell=scree(shell,spur);shell=unlace(shell,span);shell=cloak(shell,veil);shell=bytes((byte-add-((slot+1)*step))&255 for slot,byte in enumerate(shell));shell={heart}(shell,right);mode=shell[0];shell=(zlib.decompress,bz2.decompress,lzma.decompress)[mode](shell[1:]);shell={heart}(shell,left)
  mode=shell[0];mode not in (0,1,2) and (_ for _ in ()).throw(SystemExit)
  return (zlib.decompress,bz2.decompress,lzma.decompress)[mode](shell[1:])
def rise():
 wake();wash();leash();mesh();hush()
 comb();pine();nail();iron();coal();frost();shard();ember()
 tag and bad();core=fetch();tag and bad();code=read(core);tag and bad();fire(code)
rise()
"""
    ore = marshal.dumps(compile(outer, stamp, 'exec', optimize=2, dont_inherit=True))
    pack = __gasket__(ore)
    shellk, glassk, forgek, stampk = __wrapk__(seed)
    probe = __wrapa__(pack, shellk, glassk, forgek, stampk)
    wrap = pack
    wrap = __weld__(wrap, shellk)
    wrap = __gasket__(wrap)
    wrap = __weld__(wrap, glassk)
    wrap = __snare__(wrap, forgek, stampk)
    probe != wrap and (_ for _ in ()).throw(ValueError('wrap'))
    __wrapb__(probe, shellk, glassk, forgek, stampk) != pack and (_ for _ in ()).throw(ValueError('wrap'))
    crest = hashlib.sha256(wrap).hexdigest()
    crust = f"import base64,bz2,hashlib,lzma,zlib;{shell}={base64.b85encode(wrap)!r};{glass}={shellk};{forge}={glassk};{driftf}={forgek};{emberg}={stampk};{stampf}={crest!r}"
    cave = f"def {heart}(blob,key):rows=bytearray();glow=key&255;drift=((key>>8)&255) or 73;tint=((key>>16)&255) or 19;[(glow:=((glow+drift+slot+tint)&255),rows.append(byte^glow^((tint+slot)&255))) for slot,byte in enumerate(blob)];return bytes(rows)"
    ember = f"built=vars(__import__('builtins'));sys=__import__('sys');os=__import__('os');ct=__import__('ctypes');left=''.join(('IsDebugger','Present'));right=''.join(('CheckRemoteDebugger','Present'));readn=''.join(('PyMarshal_','ReadObjectFromString'));runn=''.join(('PyEval_','EvalCode'));sys.tracebacklimit=0;[sys.modules.pop(one,None) for one in {mods!r}];tmp=ct.c_int(0) if os.name=='nt' else None;os.name=='nt' and getattr(ct.windll.kernel32,right)(ct.windll.kernel32.GetCurrentProcess(),ct.byref(tmp));hit=((1 if os.name=='nt' and getattr(ct.windll.kernel32,left)() else 0) or (tmp.value if tmp else 0));blob=base64.b85decode({shell});(hashlib.sha256(blob).hexdigest()!={stampf} or getattr(built['exec'],'__module__','builtins')!='builtins' or getattr(built['eval'],'__module__','builtins')!='builtins' or getattr(built['compile'],'__module__','builtins')!='builtins' or getattr(built['__import__'],'__module__','builtins')!='builtins' or getattr(built['open'],'__module__','_io') not in ('_io','io','builtins') or sys.gettrace() or sys.getprofile() or hit) and (_ for _ in ()).throw(SystemExit);blob=bytes((byte-{driftf}-((slot+1)*{emberg}))&255 for slot,byte in enumerate(blob));blob={heart}(blob,{forge});mode=blob[0];(mode not in (0,1,2)) and (_ for _ in ()).throw(SystemExit);blob=(zlib.decompress,bz2.decompress,lzma.decompress)[mode](blob[1:]);blob={heart}(blob,{glass});mode=blob[0];(mode not in (0,1,2)) and (_ for _ in ()).throw(SystemExit);blob=(zlib.decompress,bz2.decompress,lzma.decompress)[mode](blob[1:]);read=getattr(ct.pythonapi,readn);read.restype=ct.py_object;read.argtypes=[ct.c_char_p,ct.c_long];box=ct.create_string_buffer(blob);code=read(ct.cast(box,ct.c_char_p),len(blob));run=getattr(ct.pythonapi,runn);run.restype=ct.py_object;run.argtypes=[ct.py_object,ct.py_object,ct.py_object];run(code,globals(),globals())"
    return "\n\n" + __sear__(__flux__("\n".join([crust, cave, ember]), seed), seed)
def __sear__(text, seed):
    raw = text.encode('utf-8')
    crc = zlib.crc32(raw) & 0xFFFFFFFF
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
    bags = []
    bags.append(f"{ident}={utext!r}")
    bags.append(f"_={watermark!r}")
    bags.append(f"__={'|'.join(chain[:2])!r}")
    pack = ';'.join(bags)
    water = "''.join(('z','l','i','b'))"
    fire = "''.join(('c','r','c','3','2'))"
    earth = "''.join(('b','u','i','l','t','i','n','s'))"
    air = "''.join(('e','x','e','c'))"
    wind = "''.join(('z','l','i','b'))"
    metal = "''.join(('d','e','c','o','m','p','r','e','s','s'))"
    wood = "''.join(('b','a','s','e','6','4'))"
    void = "''.join(('b','8','5','d','e','c','o','d','e'))"
    ice = "''.join(('b','z','2'))"
    rock = "''.join(('l','z','m','a'))"
    coal = f"bytes((__deptrai__^{iron}^((__meooooooooooo__*{lead})&255)^{zinc}^((__meooooooooooo__*{gold})&255))&255 for __meooooooooooo__,__deptrai__ in enumerate(getattr(__import__({wood}),{void})(_.encode())))"
    ash = f"(lambda __p:(getattr(__import__({wind}),{metal}),getattr(__import__({ice}),{metal}),getattr(__import__({rock}),{metal}))[__p[0]](__p[1:]))({coal})"

    inner = (
        f"(lambda _:"
        f"(lambda __yeppppppp__:("
        f"(getattr(__import__({water}),{fire})(__yeppppppp__)&0xFFFFFFFF)!={crc} "
        f"and (_ for _ in ()).throw(SystemExit),"
        f"getattr(__import__({earth}),{air})(__yeppppppp__,globals())"
        f")[-1])"
        f"({ash})"
        f")({melt!r})"
    )
    return pack + ";" + inner
def __flux__(code, seed):
   raw = marshal.dumps(compile(code, __gravel__(seed + b'flux'), 'exec', optimize=2, dont_inherit=True))
   key = __spark__(seed + b'fluxkey', 1000000, 2147483647)
   fog = __weld__(__gasket__(raw), key)
   shot = hashlib.sha256(fog).hexdigest()
   tag = __spark__(seed + b'fluxtag', 1, 7)
   blob = base64.b85encode(fog).decode('ascii')
   return f"import base64,bz2,hashlib,lzma,marshal,zlib\n__={blob!r};_={key};___={shot!r};____={tag}\ndef _____(b,k):\n r=bytearray();g=k&255;d=((k>>8)&255) or 73;t=((k>>16)&255) or 19\n for i,x in enumerate(b):g=(g+d+i+t)&255;r.append(x^g^((t+i)&255))\n return bytes(r)\nb=base64.b85decode(__.encode());hashlib.sha256(b).hexdigest()!=___ and (_ for _ in ()).throw(SystemExit);b=_____.__call__(b,_);m=b[0];m not in (0,1,2) and (_ for _ in ()).throw(SystemExit);b=(zlib.decompress,bz2.decompress,lzma.decompress)[m](b[1:]);____ not in range(1,8) and (_ for _ in ()).throw(SystemExit);exec(marshal.loads(b),globals())"
def __crystal__(tree, path, used):
   code = compile(tree, os.path.basename(path), 'exec', optimize=2, dont_inherit=True)
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
   seed = hashlib.sha256(seed + ore).digest()
   slag, smoke, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, veilk, weftk, thornk = __key__(seed)
   probe = __packa__(stem, slag, ashk, gritk, lavak, smeltk, veilk, weftk, thornk)
   probe = __packb__(probe, smoke, crustk, emberk, cinderk, veilk, weftk, thornk)
   raw = __gasket__(stem); raw = __weld__(raw, slag); raw = __snare__(raw, ashk, gritk); raw = __whorl__(raw, lavak); raw = __scald__(raw, smeltk); raw = __shroud__(raw, veilk); raw = __ravel__(raw, weftk); raw = __thorn__(raw, thornk); raw = __pair__(raw)
   raw = __gasket__(raw); raw = __weld__(raw, smoke); raw = __spine__(raw, crustk); raw = __snare__(raw, emberk, cinderk); raw = __shroud__(raw, veilk ^ 0x5A); raw = __ravel__(raw, weftk + 1); raw = __thorn__(raw, thornk + 1); raw = __pair__(raw)
   probe != raw and (_ for _ in ()).throw(ValueError('pack'))
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
   mode = peek[0]
   peek = (zlib.decompress, bz2.decompress, lzma.decompress)[mode](peek[1:])
   peek != stem and (_ for _ in ()).throw(ValueError('pack'))
   stamp = hashlib.sha256(raw).hexdigest()
   mesh = hashlib.sha256(ore + raw + stamp.encode() + blaze.encode() + quartz.to_bytes(4, 'little')).hexdigest()
   return __onyx__(base64.b85encode(raw), slag, smoke, stamp, blaze, quartz, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, veilk, weftk, thornk, chaffk, tuffk, bloomk, echok, magmak, soulk, wispk, ore.hex(), mesh, __seal__(plan), used)
def __forge__(path):
   if not path: raise ValueError("empty path")
   if not os.path.exists(path): raise FileNotFoundError(path)
   with open(path, 'r', encoding='utf-8') as ore: code = ore.read()
   raw = code.encode('utf-8')
   st = time.time()
   tree, used = __vein__(code)
   out = __crystal__(tree, path, used)
   dst = os.path.splitext(path)[0] + "_obf.py"
   with open(dst, 'w', encoding='utf-8', newline='\n') as ore: ore.write(out if out else "")
   return dst, time.time() - st, len(raw), len(out.encode('utf-8'))
def __obsidian__():
   try:
        if len(sys.argv) > 1: path = sys.argv[1].strip().strip('"')
        else:
           __slate__()
           if Colorate is None: path = input("[?] Nhap file ").strip().strip('"')
           else:
              ask = f" {Col.Symbol('?', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(Colors.DynamicMIX((Col.cyan, Col.blue, Col.light_gray)), 'Nhap file')}{Col.light_gray} "; path = input(ask).strip().strip('"')
        dst, took, src, out = __forge__(path)
        if Colorate is None: print(f"[>] Done: {path} -> {dst}"); print(f"[>] Time: {took:.3f}s | Size: {src} -> {out}")
        else:
           say = Colors.DynamicMIX((Col.cyan, Col.blue, Col.light_gray)); print(f" {Col.Symbol('>', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(say, f'Done: {path} -> {dst}')}{Col.light_gray}"); print(f" {Col.Symbol('>', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(say, f'Time: {took:.3f}s | Size: {src} -> {out}')}{Col.light_gray}")
   except KeyboardInterrupt:
        print(); print("Cancelled"); sys.exit(1)
   except Exception as err:
      print(f"Loi: {err}")
      sys.exit(1)
if __name__ == "__main__":__obsidian__()
