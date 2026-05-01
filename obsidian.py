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
   if isinstance(data, int): return data.to_bytes(8, 'little', signed=True)
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
   pick = min(((0, zlib.compress(blob, 9)), (1, bz2.compress(blob, 9)), (2, lzma.compress(blob, preset=9))), key=lambda row: len(row[1])); return bytes([pick[0]]) + pick[1]
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
        part = blob[slot:slot + span]; left = part[:len(part) // 2]; right = part[len(part) // 2:]; out = bytearray(); ash = 0; ember = 0
        for turn in range(len(part)):
             if turn & 1: out.append(left[ash]); ash += 1
             else: out.append(right[ember]); ember += 1
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
def __packb__(blob, smoke, crustk, emberk, cinderk, veilk, weftk, thornk): return __pair__(__thorn__(__ravel__(__shroud__(__snare__(__spine__(__weld__(zlib.compress(blob, 9), smoke), crustk), emberk, cinderk), veilk ^ 0x5A), weftk + 1), thornk + 1))
def __peeka__(blob, smoke, crustk, emberk, cinderk, veilk, weftk, thornk): return zlib.decompress(__weld__(__spine__(__unsnare__(__unshroud__(__unravel__(__thorn__(__pair__(blob), thornk + 1), weftk + 1), veilk ^ 0x5A), emberk, cinderk), crustk), smoke))
def __peekb__(blob, slag, ashk, gritk, lavak, smeltk, veilk, weftk, thornk): return __weld__(__unsnare__(__unwhorl__(__scald__(__unshroud__(__unravel__(__thorn__(__pair__(blob), thornk), weftk), veilk), smeltk), lavak), ashk, gritk), slag)
def __corea__(blob, leftk, rightk, mistk, dustk, cloakk, lanek, spurk): return __thorn__(__ravel__(__shroud__(__snare__(__weld__(zlib.compress(__weld__(blob, leftk), 9), rightk), mistk, dustk), cloakk), lanek), spurk)
def __coreb__(blob, leftk, rightk, mistk, dustk, cloakk, lanek, spurk): return __weld__(zlib.decompress(__weld__(__unsnare__(__unshroud__(__unravel__(__thorn__(blob, spurk), lanek), cloakk), mistk, dustk), rightk)), leftk)
def __wrapa__(blob, shellk, glassk, forgek, stampk): return __snare__(__weld__(zlib.compress(__weld__(blob, shellk), 9), glassk), forgek, stampk)
def __wrapb__(blob, shellk, glassk, forgek, stampk): return __weld__(zlib.decompress(__weld__(__unsnare__(blob, forgek, stampk), glassk)), shellk)
def __marks__(code): return __glow__(code), __bloom__(code), __echo__(code), __magma__(code), __soul__(code), __wisp__(code)
def __keys__(seed):
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
def __talus__(code, expected):
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
def __corals__(seed, count):
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
def __hills__(seed, width):
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
def __basalts__(seed, count, used):
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
def __marbles__(seed, count):
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
def __kilns__(seed, depth, width):
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
    stones = __marbles__(seed + b'meta', 4)
    rubble = __rubble__(seed + b'meta', 4)
    grout = __grout__(seed + b'meta', 8)
    return (watermarks, chain, traps, marks, stones, rubble, grout)
def __vein__(code):
    tree = ast.parse(code)
    seed = hashlib.sha256(code.encode('utf-8')).digest()
    store = []
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
    def __locks__(args):
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
    def __basalt__(node, kind, skip):
        for field, value in ast.iter_fields(node):
            if field in skip:
                continue
            if isinstance(value, list):
                bag = []
                for item in value:
                    if isinstance(item, ast.AST):
                        item = __shape__(item) if kind == 'shape' else __stone__(item)
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
                item = __shape__(value) if kind == 'shape' else __stone__(value)
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
            cond = ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=err, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(rock)])
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
        names = __basalts__(seed + tick[0].to_bytes(4, 'little'), 2, used)
        kiln = __kilns__(seed + tick[0].to_bytes(4, 'little'), 2, 3)
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
    def __dots__():
        return ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Constant(Ellipsis)), args=[], keywords=[])
    def __slab__():
        raw = marshal.dumps(store)
        core = base64.b85encode(zlib.compress(raw, 9)).decode('ascii')
        test = __mist__(seed + b'proof', 48)
        gold = base64.b85encode(test).decode('ascii')
        check = zlib.crc32(test) + zlib.adler32(test)
        text = f"""{blob}={core!r}
{proof}={gold!r}
{keep}=None
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
   {tint}=__import__('base64').b85decode({proof}.encode());(__import__('zlib').crc32({tint})+__import__('zlib').adler32({tint})!={check}) and (_ for _ in ()).throw(RuntimeError('bad'))
   {keep}=tuple({rune}(*row) for row in {barkf}(__import__('zlib').decompress(__import__('base64').b85decode({blob}.encode()))))
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
            one = __stone__(one)
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
            hold = __locks__(node.args)
            lock.append(hold); room[0] += 1
            node = __basalt__(node, 'shape', {'body'})
            node.body = __core__(node.body, 'shape', False)
            room[0] -= 1; lock.pop()
            return node
        if isinstance(node, ast.AsyncFunctionDef):
            if wall[0] == 0 and __token__(node.name):
                node.name = __pick__(node.name)
            hold = __locks__(node.args)
            lock.append(hold); room[0] += 1
            node = __basalt__(node, 'shape', {'body'})
            node.body = __core__(node.body, 'shape', False)
            room[0] -= 1; lock.pop()
            return node
        if isinstance(node, ast.ClassDef):
            if wall[0] == 0 and __token__(node.name):
                node.name = __pick__(node.name)
            node = __basalt__(node, 'shape', {'body'})
            wall[0] += 1
            node.body = __core__(node.body, 'shape', False)
            wall[0] -= 1
            return node
        if isinstance(node, ast.ExceptHandler):
            node = __basalt__(node, 'shape', set())
            if node.name and __token__(node.name) and not (wall[0] > 0 and room[0] == 0):
                node.name = __pick__(node.name)
            return node
        if isinstance(node, ast.MatchStar):
            if node.name and __token__(node.name):
                node.name = __pick__(node.name)
            return node
        if isinstance(node, ast.MatchAs):
            node = __basalt__(node, 'shape', set())
            if node.name and __token__(node.name):
                node.name = __pick__(node.name)
            return node
        if isinstance(node, ast.MatchMapping):
            node = __basalt__(node, 'shape', set())
            if node.rest and __token__(node.rest):
                node.rest = __pick__(node.rest)
            return node
        if isinstance(node, ast.Lambda):
            hold = __locks__(node.args)
            lock.append(hold); room[0] += 1
            node = __basalt__(node, 'shape', set())
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
        node = __basalt__(node, 'shape', set())
        if isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Load):
            return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, __ember__(node.attr)], keywords=[])
        if isinstance(node, ast.Subscript) and isinstance(node.ctx, ast.Load):
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, __ember__('__getitem__')], keywords=[]), args=[node.slice], keywords=[])
        if isinstance(node, ast.List) and isinstance(node.ctx, ast.Load):
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__('builtins')], keywords=[]), __ember__('list')], keywords=[]), args=[ast.Tuple(elts=node.elts, ctx=ast.Load())], keywords=[])
        if isinstance(node, ast.Tuple) and isinstance(node.ctx, ast.Load) and not any(isinstance(one, ast.Starred) for one in node.elts):
            return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__('builtins')], keywords=[]), __ember__('tuple')], keywords=[]), args=[ast.List(elts=node.elts, ctx=ast.Load())], keywords=[])
        if isinstance(node, ast.Slice):
            return ast.Call(func=ast.Name(id='slice', ctx=ast.Load()), args=[node.lower or ast.Constant(None), node.upper or ast.Constant(None), node.step or ast.Constant(None)], keywords=[])
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
            for gen in node.generators:
                gen.iter = __gloom__(gen.iter)
                gen.ifs = [__gloom__(one) for one in gen.ifs]
            return node
        if isinstance(node, ast.DictComp):
            for gen in node.generators:
                gen.iter = __gloom__(gen.iter)
                gen.ifs = [__gloom__(one) for one in gen.ifs]
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
        if isinstance(node, ast.Call) and node.keywords:
            node = __mesa__(node)
            return node
        return node
    def __stone__(node):
        if node is None:
            return None
        if isinstance(node, ast.Module):
            node.body = __core__(node.body, 'stone', True)
            return node
        node = __basalt__(node, 'stone', set())
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
            return ast.copy_location(__dots__(), node)
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
    tree = __stone__(tree)
    ast.fix_missing_locations(tree)
    return tree, used
def __onyx__(rack, slag, smoke, stamp, blaze, quartz, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, veilk, weftk, thornk, chaffk, tuffk, bloomk, echok, magmak, soulk, wispk, used):
    seed = hashlib.sha256(stamp.encode() + blaze.encode() + quartz.to_bytes(4, 'little')).digest()
    mint = [0]
    blob, left, right, skin, heart, bone, hand, guard, split, stampf, prove, openf, runf, coref, sink, seal, storm, shell, hold, wake, brim, shale, cove, drift, emberf, talc, shalef, quill, moss, dune, gully, shalex, beryl, gnarl, scarp, obsf, tufff, vinef, glowf, rift, cull, thorn, flake, peat, cliff, frost, shardf, veilf, basaltf, hollow, marrow, briar, huskf, grovef, miref, shardy, cragf, fenf, screef, drusef = [__mint__(used, seed, mint) for slot in range(60)]
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
  return data.to_bytes(8,'little',signed=True)
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
def {shardy}(code):
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
   part=blob[slot:slot+span];left=part[:len(part)//2];right=part[len(part)//2:];out=bytearray();ash=0;ember=0
   for turn in range(len(part)):
    if turn&1:
     out.append(left[ash]);ash += 1
    else:
     out.append(right[ember]);ember += 1
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
def {stampf}(blob):
 {hand}()
 shell=base64.b85decode({blob})
 {drusef}(shell)!={chaffk!r} and (_ for _ in ()).throw(SystemExit)
 {guard}(shell,{__flare__(base64.b85decode(rack))},{stamp!r})
 {beryl}(shell)
 {gully}(shell)
 {obsf}(shell)
 {scarp}(shell)
 {gnarl}(shell)
 {shalex}(shell)
 {split}(shell)
 shell={dune}(shell)
 shell={screef}(shell,{thornk}+1)
 shell={fenf}(shell,{weftk}+1)
 shell={cragf}(shell,{veilk}^0x5A)
 shell={sink}(shell,{drift},{emberf})
 shell={talc}(shell,{cove})
 shell={heart}(shell,{right})
 if len(shell)<4:
  raise SystemExit
 shell=zlib.decompress(shell)
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
 {shardy}({coref})
{runf}()
"""
    ore = marshal.dumps(compile(inner, stamp, 'exec', optimize=2, dont_inherit=True))
    pack = __gasket__(ore)
    leftk, rightk, mistk, dustk, cloakk, lanek, spurk = __corek__(seed)
    probe = __corea__(pack, leftk, rightk, mistk, dustk, cloakk, lanek, spurk)
    core = pack
    core = __weld__(core, leftk)
    core = zlib.compress(core, 9)
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
   part=blob[slot:slot+span];left=part[:len(part)//2];right=part[len(part)//2:];out=bytearray();ash=0;ember=0
   for turn in range(len(part)):
    if turn&1:
     out.append(left[ash]);ash += 1
    else:
     out.append(right[ember]);ember += 1
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
  shell=scree(shell,spur);shell=unlace(shell,span);shell=cloak(shell,veil);shell=bytes((byte-add-((slot+1)*step))&255 for slot,byte in enumerate(shell));shell={heart}(shell,right);shell=zlib.decompress(shell);shell={heart}(shell,left)
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
    wrap = zlib.compress(wrap, 9)
    wrap = __weld__(wrap, glassk)
    wrap = __snare__(wrap, forgek, stampk)
    probe != wrap and (_ for _ in ()).throw(ValueError('wrap'))
    __wrapb__(probe, shellk, glassk, forgek, stampk) != pack and (_ for _ in ()).throw(ValueError('wrap'))
    crest = hashlib.sha256(wrap).hexdigest()
    crust = f"import base64,bz2,hashlib,lzma,zlib;{shell}={base64.b85encode(wrap)!r};{glass}={shellk};{forge}={glassk};{driftf}={forgek};{emberg}={stampk};{stampf}={crest!r}"
    cave = f"def {heart}(blob,key):rows=bytearray();glow=key&255;drift=((key>>8)&255) or 73;tint=((key>>16)&255) or 19;[(glow:=((glow+drift+slot+tint)&255),rows.append(byte^glow^((tint+slot)&255))) for slot,byte in enumerate(blob)];return bytes(rows)"
    ember = f"built=vars(__import__('builtins'));sys=__import__('sys');os=__import__('os');ct=__import__('ctypes');left=''.join(('IsDebugger','Present'));right=''.join(('CheckRemoteDebugger','Present'));readn=''.join(('PyMarshal_','ReadObjectFromString'));runn=''.join(('PyEval_','EvalCode'));sys.tracebacklimit=0;[sys.modules.pop(one,None) for one in {mods!r}];tmp=ct.c_int(0) if os.name=='nt' else None;os.name=='nt' and getattr(ct.windll.kernel32,right)(ct.windll.kernel32.GetCurrentProcess(),ct.byref(tmp));hit=((1 if os.name=='nt' and getattr(ct.windll.kernel32,left)() else 0) or (tmp.value if tmp else 0));blob=base64.b85decode({shell});(hashlib.sha256(blob).hexdigest()!={stampf} or getattr(built['exec'],'__module__','builtins')!='builtins' or getattr(built['eval'],'__module__','builtins')!='builtins' or getattr(built['compile'],'__module__','builtins')!='builtins' or getattr(built['__import__'],'__module__','builtins')!='builtins' or getattr(built['open'],'__module__','_io') not in ('_io','io','builtins') or sys.gettrace() or sys.getprofile() or hit) and (_ for _ in ()).throw(SystemExit);blob=bytes((byte-{driftf}-((slot+1)*{emberg}))&255 for slot,byte in enumerate(blob));blob={heart}(blob,{forge});blob=zlib.decompress(blob);blob={heart}(blob,{glass});mode=blob[0];(mode not in (0,1,2)) and (_ for _ in ()).throw(SystemExit);blob=(zlib.decompress,bz2.decompress,lzma.decompress)[mode](blob[1:]);read=getattr(ct.pythonapi,readn);read.restype=ct.py_object;read.argtypes=[ct.c_char_p,ct.c_long];box=ct.create_string_buffer(blob);code=read(ct.cast(box,ct.c_char_p),len(blob));run=getattr(ct.pythonapi,runn);run.restype=ct.py_object;run.argtypes=[ct.py_object,ct.py_object,ct.py_object];run(code,globals(),globals())"
    return "\n\n" + __sear__(__flux__("\n".join([crust, cave, ember]), seed), seed)
def __sear__(text, seed):
    raw = text.encode('utf-8')
    crc = zlib.crc32(raw) & 0xFFFFFFFF
    fog = lzma.compress(raw, preset=9)
    zinc = secrets.randbelow(254) + 1
    gold = secrets.randbelow(200) + 7
    iron = secrets.randbelow(254) + 1
    lead = secrets.randbelow(200) + 7
    while iron == zinc:
        iron = secrets.randbelow(254) + 1
    while lead == gold:
        lead = secrets.randbelow(200) + 7
    silk = bytes((b ^ zinc ^ ((slot * gold) & 0xFF)) & 0xFF for slot, b in enumerate(fog))
    wool = bytes((b ^ iron ^ ((slot * lead) & 0xFF)) & 0xFF for slot, b in enumerate(silk))
    melt = base64.b85encode(wool).decode('ascii')
    watermark = __shingle__(seed, 8)
    ident = __gravel__(seed)
    utext = __corals__(seed, 12)
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
    wind = "''.join(('l','z','m','a'))"
    metal = "''.join(('d','e','c','o','m','p','r','e','s','s'))"
    wood = "''.join(('b','a','s','e','6','4'))"
    void = "''.join(('b','8','5','d','e','c','o','d','e'))"

    inner = (
        f"(lambda _:"
        f"(lambda __yeppppppp__:("
        f"(getattr(__import__({water}),{fire})(__yeppppppp__)&0xFFFFFFFF)!={crc} "
        f"and (_ for _ in ()).throw(SystemExit),"
        f"getattr(__import__({earth}),{air})(__yeppppppp__,globals())"
        f")[-1])"
        f"(getattr(__import__({wind}),{metal})("
        f"bytes((__deptrai__^{zinc}^((__meoooooooooo__*{gold})&255))&255 for __meoooooooooo__,__deptrai__ in enumerate("
        f"bytes((__deptrai__^{iron}^((__meoooooooooo__*{lead})&255))&255 for __meoooooooooo__,__deptrai__ in enumerate("
        f"getattr(__import__({wood}),{void})(_.encode())"
        f"))"
        f"))"
        f"))"
        f")({melt!r})"
    )
    return pack + ";" + inner
def __flux__(code, seed):
   seam = lambda: "".join(secrets.choice([chr(i) for i in range(97, 122)]) for _ in range(6))
   lode, pith = "__init__", seam(); rind, husk, pulp = secrets.randbelow(254) + 1, secrets.randbelow(254) + 1, secrets.randbelow(254) + 1
   bark, cork = 5, secrets.randbelow(44) * 2 + 11
   tags = ['lx','ex','st','ad','sb','ml','np','li','ai','si','mi','at','dp','sw','rt','pp','rv']
   slab = list(range(256)); secrets.SystemRandom().shuffle(slab); grid = {k:[] for k in tags}
   for slot, val in enumerate(slab): grid[tags[slot % len(tags)]].append(val)
   pick = lambda t: secrets.choice(grid[t]); acc = secrets.randbelow(254) + 1; tape = [pick('li'), acc]
   for _ in range(secrets.randbelow(5) + 8):
       kind, func = secrets.choice([('ad',lambda a,b:((a^b)+2*(a&b))&0xFF), ('sb',lambda a,b:((a^((256-b)&0xFF))+2*(a&((256-b)&0xFF)))&0xFF), ('ml',lambda a,b:(a*b)%256)]); val = secrets.randbelow(254) + 1
       tape.extend([pick({'ad':'ai','sb':'si','ml':'mi'}[kind]), val]); acc = func(acc, val)
   tape.extend([pick('li'), (rind - acc) % 256, pick('ad'), pick('st')])
   for _ in range(secrets.randbelow(3) + 2):
       tape.extend([pick('at'), pick('np'), pick('dp'), pick('pp'), pick('rv'), pick('np')])
   tape.extend([pick('lx'), pick('ex')])
   dye, weave, knot = secrets.randbelow(8999) + 1000, secrets.randbelow(449) * 2 + 101, secrets.randbelow(899) + 100
   vex = [b ^ ((dye + i * weave + knot) & 0xFF) for i, b in enumerate(tape)]; rune, eth = bytearray(), rind
   for byte in code.encode('utf-8'): rune.append((byte ^ eth ^ husk ^ pulp) & 0xFF); eth = (eth * bark + cork) % 256
   shard = base64.b85encode(lzma.compress(bytes(rune), preset=9)).decode('ascii')
   ops = {f'__{t}__': 'pass' for t in tags}
   ops['__lx__'] = f'__rock__=__import__("lzma").decompress(__import__("base64").b85decode("{shard}".encode()));__dust__=bytearray();[(__dust__.append((__sand__^self.__acc__[0]^self.__fog__^self.__haze__)&255),self.__acc__.__setitem__(0,(self.__acc__[0]*self.__bark__+self.__cork__)%256)) for __sand__ in __rock__];self.__stk__.append(__dust__.decode("utf-8"))'
   ops['__ex__'] = 'exec(self.__stk__.pop(),globals())'; ops['__st__'] = 'self.__acc__[0]=self.__stk__.pop()&0xFF'
   ops['__ad__'] = '__right__=self.__stk__.pop();__left__=self.__stk__.pop();self.__stk__.append(((__left__^__right__)+2*(__left__&__right__))&0xFF)'
   ops['__sb__'] = '__right__=self.__stk__.pop();__left__=self.__stk__.pop();__flip__=(256-__right__)&0xFF;self.__stk__.append(((__left__^__flip__)+2*(__left__&__flip__))&0xFF)'
   ops['__ml__'] = '__right__=self.__stk__.pop();__left__=self.__stk__.pop();self.__stk__.append((__left__*__right__)%256)'
   ops['__np__'] = "self.__acc__[0]^=0x42 if getattr(__import__('sys'),'gettrace',lambda:None)() else 0"
   ops['__at__'] = "[__import__('os')._exit(1) for _ in [None] if __import__('os').name=='nt' and getattr(getattr(__import__('ctypes'),'windll',None),'kernel32',None) and getattr(__import__('ctypes').windll.kernel32,''.join(('IsDebugger','Present')),lambda:0)()]"
   ops['__dp__'] = 'self.__stk__.append(self.__stk__[-1]) if self.__stk__ else None'
   ops['__sw__'] = '(self.__stk__.__setitem__(-1,self.__stk__[-2]),self.__stk__.__setitem__(-2,self.__stk__[-1])) if len(self.__stk__)>1 else None'
   ops['__rt__'] = 'self.__stk__.insert(0,self.__stk__.pop()) if len(self.__stk__)>1 else None'
   ops['__pp__'] = 'self.__stk__.pop() if self.__stk__ else None'
   ops['__rv__'] = 'self.__stk__.reverse()'
   ops['__li__'] = f'__byte__=0 if self.__ptr__>=len(self.__ore__) else (self.__ore__[self.__ptr__]^((self.__dye__[0]+self.__ptr__*{weave}+{knot})&0xFF))&0xFF;self.__ptr__+=1;self.__stk__.append(__byte__)'
   ops['__ai__'] = f'__byte__=0 if self.__ptr__>=len(self.__ore__) else (self.__ore__[self.__ptr__]^((self.__dye__[0]+self.__ptr__*{weave}+{knot})&0xFF))&0xFF;self.__ptr__+=1;__left__=self.__stk__.pop();self.__stk__.append(((__left__^__byte__)+2*(__left__&__byte__))&0xFF)'
   ops['__si__'] = f'__byte__=0 if self.__ptr__>=len(self.__ore__) else (self.__ore__[self.__ptr__]^((self.__dye__[0]+self.__ptr__*{weave}+{knot})&0xFF))&0xFF;self.__ptr__+=1;__left__=self.__stk__.pop();__flip__=(256-__byte__)&0xFF;self.__stk__.append(((__left__^__flip__)+2*(__left__&__flip__))&0xFF)'
   ops['__mi__'] = f'__byte__=0 if self.__ptr__>=len(self.__ore__) else (self.__ore__[self.__ptr__]^((self.__dye__[0]+self.__ptr__*{weave}+{knot})&0xFF))&0xFF;self.__ptr__+=1;__left__=self.__stk__.pop();self.__stk__.append((__left__*__byte__)%256)'
   cls = seam(); out = f"import sys\nimport os\nclass {cls}:\n    def {lode}(self):self.__stk__=[];self.__acc__=[0];self.__fog__={husk};self.__haze__={pulp};self.__bark__={bark};self.__cork__={cork}\n"
   for tag, body in ops.items(): out += f"    def {tag}(self):\n        {body}\n"
   out += f"    def {pith}(self,__rock__):\n        self.__ore__=__rock__;self.__ptr__=0;self.__dye__=[{dye}];__catcatcat__={{}}\n"
   for tag in tags:
       for val in grid[tag]: out += f"        __catcatcat__[{val}]=self.__{tag}__\n"
   out += f"        while self.__ptr__<len(self.__ore__):__byte__=(self.__ore__[self.__ptr__]^((self.__dye__[0]+self.__ptr__*{weave}+{knot})&0xFF))&0xFF;self.__ptr__+=1;__catcatcat__.get(__byte__,self.__np__)()\n{cls}().{pith}({vex})"
   return out
def __glass__(tree, path, used):
   code = compile(tree, os.path.basename(path), 'exec', optimize=2, dont_inherit=True)
   stem = marshal.dumps(code)
   brand = __brand__(stem)
   blaze = brand[0]
   quartz = brand[3]
   tuffk, bloomk, echok, magmak, soulk, wispk = __marks__(code)
   seed = hashlib.sha256(stem).digest()
   slag, smoke, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, veilk, weftk, thornk = __keys__(seed)
   probe = __packa__(stem, slag, ashk, gritk, lavak, smeltk, veilk, weftk, thornk)
   probe = __packb__(probe, smoke, crustk, emberk, cinderk, veilk, weftk, thornk)
   raw = __gasket__(stem); raw = __weld__(raw, slag); raw = __snare__(raw, ashk, gritk); raw = __whorl__(raw, lavak); raw = __scald__(raw, smeltk); raw = __shroud__(raw, veilk); raw = __ravel__(raw, weftk); raw = __thorn__(raw, thornk); raw = __pair__(raw)
   raw = zlib.compress(raw, 9); raw = __weld__(raw, smoke); raw = __spine__(raw, crustk); raw = __snare__(raw, emberk, cinderk); raw = __shroud__(raw, veilk ^ 0x5A); raw = __ravel__(raw, weftk + 1); raw = __thorn__(raw, thornk + 1); raw = __pair__(raw)
   probe != raw and (_ for _ in ()).throw(ValueError('pack'))
   chaffk = __chaff__(raw)
   if len(raw) < 8:
      raise ValueError('pack')
   if not raw[:1] + raw[-1:]:
      raise ValueError('pack')
   if __chaff__(raw) != chaffk:
      raise ValueError('pack')
   peek = __peeka__(raw, smoke, crustk, emberk, cinderk, veilk, weftk, thornk)
   peek = __peekb__(peek, slag, ashk, gritk, lavak, smeltk, veilk, weftk, thornk)
   mode = peek[0]
   peek = (zlib.decompress, bz2.decompress, lzma.decompress)[mode](peek[1:])
   peek != stem and (_ for _ in ()).throw(ValueError('pack'))
   stamp = hashlib.sha256(raw).hexdigest()
   return __onyx__(base64.b85encode(raw), slag, smoke, stamp, blaze, quartz, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, veilk, weftk, thornk, chaffk, tuffk, bloomk, echok, magmak, soulk, wispk, used)
def __forge__(path):
   if not path: raise ValueError("empty path")
   if not os.path.exists(path): raise FileNotFoundError(path)
   with open(path, 'r', encoding='utf-8') as ore: code = ore.read()
   raw = code.encode('utf-8')
   st = time.time()
   tree, used = __vein__(code)
   out = __glass__(tree, path, used)
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
