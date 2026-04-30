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
        print()
        print("OBSIDIAN")
        print("dense fused shell // deobf thu di")
        print()
        return
   mix = Colors.DynamicMIX((Col.cyan, Col.blue, Col.light_gray))
   glow = Colors.DynamicMIX((Col.blue, Col.cyan, Col.light_gray))
   print()
   for row in ("   ____  ____  _____ ___ ____ ___    _    _   _", "  / __ )/ __ \\/ ___//  _/ __ \\_ _|  / \\  | \\ | |", " / __  / / / /\\__ \\ / // / / /| |  / _ \\ |  \\| |", "/ /_/ / /_/ /___/ // // /_/ / | | / ___ \\| |\\  |", "/_____/\\____//____/___/\\____/ |___/_/   \\_\\_| \\_|"):
      print(Colorate.Diagonal(mix, row))
   if glow:
        print(Colorate.Diagonal(glow, "             dense fused shell // deobf thu di"))
   print()
def __mist__(seed, need):
   if isinstance(seed, str):
        seed = seed.encode('utf-8')
   else:
      if not isinstance(seed, (bytes, bytearray)):
           seed = repr(seed).encode('utf-8')
   bag = bytearray()
   last = hashlib.sha256(seed).digest()
   slot = 0
   while len(bag) < need:
        last = hashlib.sha256(last + seed + slot.to_bytes(8, 'little')).digest()
        if last:
             bag.extend(last)
        slot += 1
   return bytes(bag[:need])
def __spark__(seed, low, high):
   if high <= low:
        return low
   fog = __mist__(seed, 8)
   return low + (int.from_bytes(fog, 'little') % (high - low + 1))
def __twist__(count, seed):
   walk = list(range(count))
   if count < 2:
        return walk
   fog = __mist__(seed, count * 8)
   at = 0
   for slot in range(count - 1, 0, -1):
        pick = int.from_bytes(fog[at:at + 8], 'little') % (slot + 1)
        if pick != slot:
             walk[slot], walk[pick] = walk[pick], walk[slot]
        at += 8
   return walk
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
def __husk__(parts, seed):
   fake = []; fill = max(2, len(parts) // 4 or 1)
   for slot in range(fill):
        fog = hashlib.sha256(__mist__(seed + slot.to_bytes(4, 'little'), 48)).digest(); size = __spark__(seed + b'wide' + slot.to_bytes(4, 'little'), 24, 45); fake.append(base64.b85encode(fog).decode('ascii')[:size])
   mix = [(slot, 1, one) for slot, one in enumerate(parts)] + [(-1, 0, one) for one in fake]; walk = __twist__(len(mix), seed + b'mesh'); mix = [mix[slot] for slot in walk]; bag = [one[2] for one in mix]; back = [0] * len(parts)
   for slot, one in enumerate(mix):
        if one[1]: back[one[0]] = slot
   return bag, back
def __mint__(used, seed, mint):
   while True:
        fog = seed + mint[0].to_bytes(4, 'little'); skin = hashlib.sha256(fog).digest(); wide = 3 + (skin[0] % 3); name = "__" + ''.join(chr(0x4e00 + (int.from_bytes(skin[1 + slot * 2:3 + slot * 2], 'little') % 20992)) for slot in range(wide)) + "__"
        mint[0] += 1
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
def __gasket__(blob):
   pick = min(((0, zlib.compress(blob, 9)), (1, bz2.compress(blob, 9)), (2, lzma.compress(blob, preset=9))), key=lambda row: len(row[1])); return bytes([pick[0]]) + pick[1]
def __sieve__(text, span):
   bag = []; slot = 0
   while slot < len(text):
        bag.append(text[slot:slot + span]); slot += span
   return bag
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
def __brand__(blob):
   shot = hashlib.sha256(blob).hexdigest()
   coal = hashlib.sha1(blob).hexdigest()
   soot = hashlib.md5(blob).hexdigest()
   ember = __flare__(blob)
   glass = zlib.adler32(blob) ^ zlib.crc32(blob)
   return shot, coal, soot, ember, glass
def __carapace__(raw, seed, kind):
   salt = __mist__(seed + kind + b'salt', len(raw) or 1)
   off = __spark__(seed + kind + b'off', 0x3040, 0x30ff)
   lift = __spark__(seed + kind + b'lift', 0x120, 0x780)
   key = __spark__(seed + kind + b'key', 11, 251)
   wide = ''.join(chr((one ^ salt[slot]) + off) for slot, one in enumerate(raw))
   ring = [((one ^ key) + lift) for one in raw]
   text = raw.hex()
   fog = __mist__(seed + kind + b'weave', len(text) or 1).hex()[:len(text)]
   weave = ''.join(one + two for one, two in zip(fog, text))
   veil = base64.b85encode(bytes(one ^ salt[slot] for slot, one in enumerate(raw))).decode('ascii')
   shot, coal, soot, ember, glass = __brand__(raw)
   return (kind.decode('ascii'), wide, off, salt.hex(), weave, ring, lift, key, veil, shot, coal, soot, ember, glass)
def __vein__(code):
    tree = ast.parse(code)
    seed = hashlib.sha256(code.encode('utf-8')).digest()
    used = set()
    bind = set()
    store = []
    seen = {}
    dust = {'__import__','abs','all','any','ascii','bin','breakpoint','callable','chr','classmethod','compile','delattr','dir','divmod','eval','exec','format','getattr','globals','hasattr','hash','hex','id','input','isinstance','issubclass','iter','len','locals','max','memoryview','min','next','oct','open','ord','pow','print','property','repr','round','setattr','slice','sorted','staticmethod','sum','vars','bool','bytearray','bytes','complex','dict','enumerate','filter','float','frozenset','int','list','map','object','range','reversed','set','str','super','tuple','type','zip'}
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used.add(node.id)
            if isinstance(node.ctx, (ast.Store, ast.Del)):
                bind.add(node.id)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            used.add(node.name)
            bind.add(node.name)
        elif isinstance(node, ast.arg):
            used.add(node.arg)
            bind.add(node.arg)
        elif isinstance(node, ast.alias):
            name = node.asname or node.name.split('.')[0]
            used.add(name)
            bind.add(name)
        elif isinstance(node, ast.ExceptHandler) and node.name:
            bind.add(node.name)
    mint = [0]
    blob, keep, load, proof, tint, rune, dawn, dusk, kiln, loom, reef, wave, mire, sootf, brimf, crustf, ashf, flaref, cask, spinef, huskf = [__mint__(used, seed, mint) for slot in range(21)]
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
    def __cinder__():
        slag = __mint__(used, seed, mint)
        coal = __mint__(used, seed, mint)
        glass = __mint__(used, seed, mint)
        tick[0] += 1
        rock = __spark__(seed + b'junk' + tick[0].to_bytes(4, 'little'), 10**7, 10**9)
        text = ['obsidian', 'glass', 'ash', 'vein'][__spark__(seed + b'text' + tick[0].to_bytes(4, 'little'), 0, 3)]
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=slag, ctx=ast.Store())], value=ast.Constant(rock)), ast.Assign(targets=[ast.Name(id=coal, ctx=ast.Store())], value=ast.Constant(text)), ast.Expr(value=ast.Call(func=ast.Name(id='str', ctx=ast.Load()), args=[ast.Name(id=glass, ctx=ast.Load())], keywords=[]))], orelse=[ast.Pass()])
    def __smoke__(body):
        bag = []
        done = 0
        for one in body:
            if done < 1 and not isinstance(one, (ast.Global, ast.Nonlocal)) and not (isinstance(one, ast.ImportFrom) and one.module == '__future__'):
                bag.append(ast.Try(body=[ast.Expr(value=ast.BinOp(left=ast.Constant(1), op=ast.Div(), right=ast.Constant(0)))], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()), name=None, body=[one])], orelse=[], finalbody=[]))
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
    def __ember__(val):
        key = ('s', val) if isinstance(val, str) else ('b', val)
        if key not in seen:
            seen[key] = len(store)
            raw = val.encode('utf-8') if isinstance(val, str) else val
            kind = b's' if isinstance(val, str) else b'b'
            store.append(__carapace__(raw, seed + len(store).to_bytes(4, 'little'), kind))
        return ast.Call(func=ast.Name(id=load, ctx=ast.Load()), args=[ast.Constant(seen[key])], keywords=[])
    def __slab__():
        raw = repr(store).encode('utf-8')
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
  {keep}=tuple({rune}(*row) for row in __import__('ast').literal_eval(__import__('zlib').decompress(__import__('base64').b85decode({blob}.encode())).decode('utf-8')))
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
                tail.insert(0, __cinder__())
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
        if isinstance(node, ast.FunctionDef):
            node = __basalt__(node, 'shape', {'body'})
            node.body = __core__(node.body, 'shape', False)
            return node
        if isinstance(node, ast.AsyncFunctionDef):
            node = __basalt__(node, 'shape', {'body'})
            node.body = __core__(node.body, 'shape', False)
            return node
        if isinstance(node, ast.ClassDef):
            node = __basalt__(node, 'shape', {'body'})
            node.body = __core__(node.body, 'shape', False)
            return node
        if isinstance(node, ast.Name):
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
            lock = {'super','eval','exec','globals','locals','vars','dir','hasattr','getattr','setattr','__import__','type','isinstance','issubclass'}
            for one in node.keywords:
                if one.arg is None:
                    keys.append(one)
                else:
                    keys.append(ast.keyword(arg=None, value=ast.Dict(keys=[__ember__(one.arg)], values=[one.value])))
            node.keywords = keys
            if not (isinstance(node.func, ast.Name) and node.func.id in lock):
                node.func = __gloom__(node.func)
            return node
        if isinstance(node, ast.Compare) and len(node.ops) == 1 and len(node.comparators) == 1:
            look = {ast.Eq: '__eq__', ast.NotEq: '__ne__', ast.Lt: '__lt__', ast.LtE: '__le__', ast.Gt: '__gt__', ast.GtE: '__ge__'}
            op = look.get(type(node.ops[0]))
            if op:
                return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.left, __ember__(op)], keywords=[]), args=[node.comparators[0]], keywords=[])
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
        if isinstance(node, ast.Lambda):
            node.body = __gloom__(node.body)
            return node
        if isinstance(node, ast.FormattedValue):
            node.value = __gloom__(node.value)
            return node
        if isinstance(node, ast.Starred):
            node.value = __gloom__(node.value)
            return node
        return node
    def __stone__(node):
        if node is None:
            return None
        if isinstance(node, ast.Module):
            node.body = __core__(node.body, 'stone', True)
            return node
        node = __basalt__(node, 'stone', set())
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value:
            return ast.copy_location(__ember__(node.value), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, bytes) and node.value:
            return ast.copy_location(__ember__(node.value), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, bool):
            return node
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and not (-1 <= node.value <= 1):
            off = 97 + ((abs(node.value) * 1315423911 + seed[0]) % 999903)
            key = 17 + ((abs(node.value) * 2654435761 + seed[1]) % 65519)
            ash = 33 + ((abs(node.value) * 2246822519 + seed[2]) % 65503)
            core = ((node.value + off) ^ key) + ash
            return ast.copy_location(ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.Constant(core), op=ast.Sub(), right=ast.Constant(ash)), op=ast.BitXor(), right=ast.Constant(key)), op=ast.Sub(), right=ast.Constant(off)), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, float) and math.isfinite(node.value):
            return ast.copy_location(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id='float', ctx=ast.Load()), __ember__('fromhex')], keywords=[]), args=[__ember__(node.value.hex())], keywords=[]), node)
        return node
    tree = __shape__(tree)
    ast.fix_missing_locations(tree)
    tree = __stone__(tree)
    ast.fix_missing_locations(tree)
    return tree, used
def __onyx__(bag, back, slag, smoke, stamp, blaze, quartz, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, tuffk, used):
    seed = hashlib.sha256(stamp.encode() + blaze.encode() + quartz.to_bytes(4, 'little')).digest()
    mint = [0]
    rack, trail, left, right, skin, heart, bone, hand, mesh, fold, spark, proof, guard, trace, carve, split, stampf, prove, openf, runf, coref, sink, seal, storm, shell, hold, wake, brim, shale, cove, drift, emberf, talc, glare, cliff, frost, shalef, quill, moss, dune, ridge, gully, splint, marrow, flake, shalex, thorn, beryl, rift, shaley, cull, gnarl, hollow, scarp, shardf, veilf, basaltf, obsf, oref, slagf, tufff, vinef, glowf = [__mint__(used, seed, mint) for slot in range(63)]
    inner = f"""import base64,bz2,hashlib,lzma,marshal,sys,zlib
{rack}={bag!r}
{trail}={back!r}
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
 built=__import__('builtins')
 {bone}('exec',built,('builtins',))
 {bone}('eval',built,('builtins',))
 {bone}('compile',built,('builtins',))
 {bone}('open',built,('builtins','io','_io'))
 {bone}('__import__',built,('builtins',))
 {bone}('loads',__import__('marshal'),('marshal',))
 {bone}('decompress',__import__('zlib'),('zlib',))
 {bone}('decompress',__import__('bz2'),('bz2','_bz2'))
 {bone}('decompress',__import__('lzma'),('lzma','_lzma'))
 if __import__('sys').gettrace():
  raise SystemExit
 if __import__('sys').getprofile():
  raise SystemExit
 if getattr(__import__('sys'),'meta_path',None) is None:
  raise SystemExit
def {mesh}(parts,trail):
 rows=[]
 for slot in trail:
  rows.append(parts[slot])
 return base64.b85decode(''.join(rows).encode())
def {fold}(blob):
 rows=[]
 slot=0
 while slot < len(blob):
  rows.append(blob[slot:slot+16])
  slot += 16
 return rows
def {spark}(rows):
 glow=0
 for row in rows:
  for byte in row:
   glow=(glow+byte)&0xffffffff
   glow=((glow<<7)|(glow>>25))&0xffffffff
   glow^=(byte*131)&0xffffffff
 return glow
def {proof}(blob):
 return (hashlib.sha256(blob).hexdigest(),hashlib.sha1(blob).hexdigest(),hashlib.md5(blob).hexdigest())
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
def {guard}(blob,mark,seal):
 rows={fold}(blob)
 glow={spark}(rows)
 if glow!=mark:
  raise SystemExit
 shard,ember,onyx={proof}(blob)
 if shard!=seal:
  raise SystemExit
 if shard!=hashlib.sha256(blob).hexdigest():
  raise SystemExit
 if ember!=hashlib.sha1(blob).hexdigest():
  raise SystemExit
 if onyx!=hashlib.md5(blob).hexdigest():
  raise SystemExit
def {trace}(blob):
 hold=[]
 for row in {fold}(blob):
  hold.append(len(row))
 if not hold:
  raise SystemExit
 if max(hold)<=0:
  raise SystemExit
 return hold
def {carve}(blob):
 rows={trace}(blob)
 glow=0
 for slot,row in enumerate(rows):
  glow=(glow+((slot+1)*row))&0xffffffff
  glow=((glow<<5)|(glow>>27))&0xffffffff
 return glow
def {split}(blob):
 glow={carve}(blob)
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
def {glare}(blob):
 if len(blob)<4:
  raise SystemExit
 return zlib.decompress(blob)
def {cliff}(blob):
 if len(blob)<2:
  raise SystemExit
 mode=blob[0]
 if mode not in (0,1,2):
  raise SystemExit
 return mode,blob[1:]
def {frost}(blob):
 return (__import__('zlib').adler32(blob),__import__('zlib').crc32(blob),len(blob),blob[:4],blob[-4:])
def {ridge}(blob):
 rows=[]
 for slot,byte in enumerate(blob):
  rows.append((byte^slot)&255)
 if not rows:
  raise SystemExit
 return (len(rows),sum(rows)&0xffffffff,min(rows),max(rows))
def {gully}(blob):
 rows={ridge}(blob)
 if rows[1]==0:
  raise SystemExit
 if rows[3]<rows[2]:
  raise SystemExit
 return rows
def {thorn}(blob):
 return (len(blob),sum(blob)&0xffffffff)
def {beryl}(blob):
 rows={thorn}(blob)
 if rows[0]<4:
  raise SystemExit
 if rows[1]==0:
  raise SystemExit
 return rows
def {splint}(blob):
 return (blob[:8],blob[-8:],len(blob))
def {marrow}(left,right):
 if left!=right:
  raise SystemExit
 return left
def {flake}(blob):
 rows={frost}(blob)
 rows[2]<8 and (_ for _ in ()).throw(SystemExit)
 return rows
def {rift}(blob):
 return (blob[:2],blob[-2:],len(set(blob[:16])) if blob else 0)
def {shaley}(left,right):
 left!=right and (_ for _ in ()).throw(SystemExit)
 return left
def {cull}(blob):
 rows={frost}(blob)
 (rows[0]^rows[1])==0 and (_ for _ in ()).throw(SystemExit)
 return rows
def {gnarl}(blob):
 rows={rift}(blob)
 rows[0]==rows[1] and (_ for _ in ()).throw(SystemExit)
 return rows
def {hollow}(blob):
 rows=blob[-16:] if len(blob)>16 else blob
 return (len(rows),len(set(rows)))
def {scarp}(blob):
 rows={hollow}(blob)
 rows[0] and rows[1]==0 and (_ for _ in ()).throw(SystemExit)
 return rows
def {shardf}(blob):
 rows=blob[:16] if len(blob)>16 else blob
 return (len(rows),len(set(rows)))
def {veilf}(left,right):
 left!=right and (_ for _ in ()).throw(SystemExit)
 return left
def {basaltf}(blob):
 rows=blob[::2]
 return (len(rows),sum(rows)&0xffffffff)
def {obsf}(blob):
 rows={basaltf}(blob)
 rows[0]==0 and (_ for _ in ()).throw(SystemExit)
 return rows
def {oref}(blob):
 rows=blob[:1]+blob[-1:]
 if not rows:
  raise SystemExit
 return (len(rows),sum(rows)&0xffffffff)
def {slagf}(blob):
 rows=len(blob)
 rows<1 and (_ for _ in ()).throw(SystemExit)
 return rows
def {shalex}(blob):
 rows={splint}(blob)
 rows[2]<16 and (_ for _ in ()).throw(SystemExit)
 return rows
def {shalef}(blob):
 rows={frost}(blob)
 if rows[2]<8:
  raise SystemExit
 if rows[0]==rows[1]:
  raise SystemExit
 if rows[3]==rows[4]:
  raise SystemExit
 return rows
def {stampf}(blob):
 {hand}()
 shell={mesh}({rack},{trail})
 {guard}(shell,{__flare__(base64.b85decode(''.join(bag[slot] for slot in back).encode()))},{stamp!r})
 {beryl}(shell)
 {gully}(shell)
 {obsf}(shell)
 {scarp}(shell)
 {gnarl}(shell)
 {shalex}(shell)
 {split}(shell)
 shell={dune}(shell)
 shell={sink}(shell,{drift},{emberf})
 shell={talc}(shell,{cove})
 shell={heart}(shell,{right})
 shell={glare}(shell)
 shell={dune}(shell)
 shell={moss}(shell,{smeltk})
 shell={hold}(shell,{shale})
 shell={sink}(shell,{wake},{brim})
 shell={heart}(shell,{left})
 mode,shell={cliff}(shell)
 return (zlib.decompress,bz2.decompress,lzma.decompress)[mode](shell)
def {prove}(blob):
 {guard}(blob,{quartz},{blaze!r})
 {oref}(blob)
 {slagf}(blob)
 {shaley}({cull}(blob)[2],len(blob))
 {veilf}({shardf}(blob)[0],len(blob[:16]))
 {marrow}({flake}(blob)[2],len(blob))
 {shalef}(blob)
 return marshal.loads(blob)
def {openf}():
 core={stampf}(0)
 {hand}()
 return {prove}(core)
def {runf}():
 {quill}=vars(__import__('builtins'))
 {coref}={openf}()
 {glowf}({coref})!={tuffk} and (_ for _ in ()).throw(SystemExit)
 {quill}['exec']({coref},globals())
{runf}()
"""
    core = inner.encode('utf-8')
    core = __gasket__(core)
    leftk = __spark__(seed + b'glass', 1000000, 2147483647)
    rightk = __spark__(seed + b'forge', 1000000, 2147483647)
    mistk = __spark__(seed + b'mist', 17, 251)
    dustk = __spark__(seed + b'dust', 3, 29)
    core = __weld__(core, leftk)
    core = zlib.compress(core, 9)
    core = __weld__(core, rightk)
    core = __snare__(core, mistk, dustk)
    flag = hashlib.sha256(core).hexdigest()
    parts = __sieve__(base64.b85encode(core).decode('ascii'), 72)
    bag, back = __husk__(parts, seed + b'wrap')
    rack, trail, glass, forge, stampf, heart = [__mint__(used, seed + b'wrap', mint) for slot in range(6)]
    crust = f"import base64,bz2,hashlib,lzma,zlib;{rack}={bag!r};{trail}={back!r};{glass}={leftk};{forge}={rightk};{stampf}={flag!r}"
    cave = f"def {heart}(blob,key):rows=bytearray();glow=key&255;drift=((key>>8)&255) or 73;tint=((key>>16)&255) or 19;[(glow:=((glow+drift+slot+tint)&255),rows.append(byte^glow^((tint+slot)&255))) for slot,byte in enumerate(blob)];return bytes(rows)"
    ember = f"blob=base64.b85decode(''.join({rack}[slot] for slot in {trail}).encode());(hashlib.sha256(blob).hexdigest()!={stampf} or getattr(getattr(__import__('builtins'),'exec'),'__module__','builtins')!='builtins' or getattr(getattr(__import__('builtins'),'eval'),'__module__','builtins')!='builtins' or getattr(getattr(__import__('builtins'),'compile'),'__module__','builtins')!='builtins' or getattr(getattr(__import__('builtins'),'__import__'),'__module__','builtins')!='builtins' or getattr(getattr(__import__('builtins'),'open'),'__module__','_io') not in ('_io','io','builtins') or __import__('sys').gettrace() or __import__('sys').getprofile()) and (_ for _ in ()).throw(SystemExit);blob=bytes((byte-{mistk}-((slot+1)*{dustk}))&255 for slot,byte in enumerate(blob));blob={heart}(blob,{forge});blob=zlib.decompress(blob);blob={heart}(blob,{glass});mode=blob[0];(mode not in (0,1,2)) and (_ for _ in ()).throw(SystemExit);blob=blob[1:];vars(__import__('builtins'))['exec']((zlib.decompress,bz2.decompress,lzma.decompress)[mode](blob).decode(),globals())"
    return "\n\n" + "\n".join([crust, cave, ember])
def __glass__(tree, path, used):
   code = compile(tree, os.path.basename(path), 'exec', optimize=2, dont_inherit=True); raw = marshal.dumps(code); blaze, coal, soot, quartz, glass = __brand__(raw); tuffk = __glow__(code); seed = hashlib.sha256(raw).digest()
   slag = __spark__(seed + b'slag', 1000000, 2147483647); smoke = __spark__(seed + b'smoke', 1000000, 2147483647); ashk = __spark__(seed + b'ash', 17, 251); gritk = __spark__(seed + b'grit', 3, 29); lavak = __spark__(seed + b'lava', 1, 7); crustk = __spark__(seed + b'crust', 9, 33); emberk = __spark__(seed + b'ember', 17, 251); cinderk = __spark__(seed + b'cinder', 3, 29); smeltk = __spark__(seed + b'smelt', 17, 251)
   raw = __gasket__(raw); raw = __weld__(raw, slag); raw = __snare__(raw, ashk, gritk); raw = __whorl__(raw, lavak); raw = __scald__(raw, smeltk); raw = __pair__(raw); raw = zlib.compress(raw, 9); raw = __weld__(raw, smoke); raw = __spine__(raw, crustk); raw = __snare__(raw, emberk, cinderk); raw = __pair__(raw)
   stamp = hashlib.sha256(raw).hexdigest(); parts = __sieve__(base64.b85encode(raw).decode('ascii'), 84); bag, back = __husk__(parts, seed + b'outer')
   return __onyx__(bag, back, slag, smoke, stamp, blaze, quartz, ashk, gritk, lavak, crustk, emberk, cinderk, smeltk, tuffk, used)
def __forge__(path):
   if not path:
        raise ValueError("empty path")
   if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as ore:
             code = ore.read()
   else:
      raise FileNotFoundError(path)
   raw = code.encode('utf-8')
   st = time.time()
   tree, used = __vein__(code)
   out = __glass__(tree, path, used)
   dst = os.path.splitext(path)[0] + "_obf.py"
   with open(dst, 'w', encoding='utf-8', newline='\n') as ore:
        if out:
             ore.write(out)
        else:
           ore.write("")
   return dst, time.time() - st, len(raw), len(out.encode('utf-8'))
def __obsidian__():
   try:
        if len(sys.argv) > 1:
             path = sys.argv[1].strip().strip('"')
        else:
           __slate__()
           if Colorate is None:
                path = input("[?] Nhap file ").strip().strip('"')
           else:
              ask = f" {Col.Symbol('?', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(Colors.DynamicMIX((Col.cyan, Col.blue, Col.light_gray)), 'Nhap file')}{Col.light_gray} "
              path = input(ask).strip().strip('"')
        dst, took, src, out = __forge__(path)
        if Colorate is None:
             print(f"[>] Done: {path} -> {dst}")
             print(f"[>] Time: {took:.3f}s | Size: {src} -> {out}")
        else:
           say = Colors.DynamicMIX((Col.cyan, Col.blue, Col.light_gray))
           print(f" {Col.Symbol('>', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(say, f'Done: {path} -> {dst}')}{Col.light_gray}")
           print(f" {Col.Symbol('>', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(say, f'Time: {took:.3f}s | Size: {src} -> {out}')}{Col.light_gray}")
   except KeyboardInterrupt:
        print()
        print("Cancelled")
        sys.exit(1)
   except Exception as err:
      print(f"Loi: {err}")
      sys.exit(1)
if __name__ == "__main__":__obsidian__()
