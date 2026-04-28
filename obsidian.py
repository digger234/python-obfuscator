import ast
import base64
import bz2
import hashlib
import lzma
import marshal
import math
import os
import random
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
        print("dense fused shell")
        print()
        return
    mix = Colors.DynamicMIX((Col.cyan, Col.blue, Col.light_gray))
    glow = Colors.DynamicMIX((Col.blue, Col.cyan, Col.light_gray))
    print()
    print(Colorate.Diagonal(mix, "   ____  ____  _____ ___ ____ ___    _    _   _"))
    print(Colorate.Diagonal(mix, "  / __ )/ __ \\/ ___//  _/ __ \\_ _|  / \\  | \\ | |"))
    print(Colorate.Diagonal(mix, " / __  / / / /\\__ \\ / // / / /| |  / _ \\ |  \\| |"))
    print(Colorate.Diagonal(mix, "/ /_/ / /_/ /___/ // // /_/ / | | / ___ \\| |\\  |"))
    print(Colorate.Diagonal(mix, "/_____/\\____//____/___/\\____/ |___/_/   \\_\\_| \\_|"))
    print(Colorate.Diagonal(glow, "                  dense fused shell"))
    print()
def __vein__(code, rng):
    tree = ast.parse(code)
    used = set()
    bind = set()
    store = []
    seen = {}
    pool = ['obs', 'veil', 'shard', 'vein', 'slab', 'cave', 'drip', 'ash', 'slag', 'gloom', 'smoke', 'coal', 'flint', 'glass', 'spike', 'night', 'lava', 'ember', 'grit', 'stone', 'forge', 'basalt', 'onyx', 'dust', 'crust']
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
    def __shard__():
        abc = 'abcdefghijklmnopqrstuvwxyz'
        while True:
            name = f"__{rng.choice(pool)}{rng.choice(abc)}{rng.choice(abc)}__"
            if name not in used and name.isidentifier():
                used.add(name)
                return name
    blob = __shard__()
    keep = __shard__()
    load = __shard__()
    proof = __shard__()
    tint = __shard__()
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
        a = __shard__()
        b = __shard__()
        c = __shard__()
        return ast.If(test=ast.Compare(left=ast.Constant(False), ops=[ast.Is()], comparators=[ast.Constant(True)]), body=[ast.Assign(targets=[ast.Name(id=a, ctx=ast.Store())], value=ast.Constant(rng.randint(10**7, 10**9))), ast.Assign(targets=[ast.Name(id=b, ctx=ast.Store())], value=ast.Constant(rng.choice(['obsidian', 'glass', 'ash', 'vein']))), ast.Expr(value=ast.Call(func=ast.Name(id='str', ctx=ast.Load()), args=[ast.Name(id=c, ctx=ast.Load())], keywords=[]))], orelse=[ast.Pass()])
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
        name = __shard__()
        return ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=name)], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Name(id=name, ctx=ast.Load())), args=[node], keywords=[])
    def __ember__(val):
        key = ('s', val) if isinstance(val, str) else ('b', val)
        if key not in seen:
            seen[key] = len(store)
            if isinstance(val, str):
                store.append(('s', base64.b85encode(val.encode('utf-8')).decode('ascii')))
            else:
                store.append(('b', base64.b85encode(val).decode('ascii')))
        return ast.Call(func=ast.Name(id=load, ctx=ast.Load()), args=[ast.Constant(seen[key])], keywords=[])
    def __slab__():
        raw = repr(store).encode('utf-8')
        core = base64.b85encode(zlib.compress(raw, 9)).decode('ascii')
        test = rng.randbytes(rng.randint(32, 64))
        gold = base64.b85encode(test).decode('ascii')
        check = zlib.crc32(test) + zlib.adler32(test)
        text = f"""{blob}={core!r}
{proof}={gold!r}
{keep}=None
def {load}(i):
 global {keep}
 if {keep} is None:
  {tint}=__import__('base64').b85decode({proof}.encode());(__import__('zlib').crc32({tint})+__import__('zlib').adler32({tint})!={check}) and (_ for _ in ()).throw(RuntimeError('bad'))
  {keep}=tuple((__import__('base64').b85decode(v.encode()).decode('utf-8') if k=='s' else __import__('base64').b85decode(v.encode())) for k,v in __import__('ast').literal_eval(__import__('zlib').decompress(__import__('base64').b85decode({blob}.encode())).decode('utf-8')))
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
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Attribute) and isinstance(node.targets[0].ctx, ast.Store):
            bag = node.targets[0]
            return ast.Expr(value=ast.Call(func=ast.Name(id='setattr', ctx=ast.Load()), args=[bag.value, __ember__(bag.attr), node.value], keywords=[]))
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Subscript):
            bag = node.targets[0]
            return ast.Expr(value=ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[bag.value, __ember__('__setitem__')], keywords=[]), args=[bag.slice, node.value], keywords=[]))
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
            name = __shard__()
            return ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], vararg=ast.arg(arg=name), kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[__ember__('builtins')], keywords=[]), __ember__('set')], keywords=[]), args=[ast.Name(id=name, ctx=ast.Load())], keywords=[])), args=node.elts, keywords=[])
        if isinstance(node, ast.Dict) and node.keys and all(isinstance(one, ast.Constant) and isinstance(one.value, str) and one.value.isidentifier() and not __import__('keyword').iskeyword(one.value) for one in node.keys if one is not None):
            name = __shard__()
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
            if node.value & 1:
                off = 97 + ((abs(node.value) * 1315423911) % 999903)
                return ast.copy_location(ast.BinOp(left=ast.Constant(node.value + off), op=ast.Sub(), right=ast.Constant(off)), node)
            key = 17 + ((abs(node.value) * 2654435761) % 65519)
            return ast.copy_location(ast.BinOp(left=ast.Constant(node.value ^ key), op=ast.BitXor(), right=ast.Constant(key)), node)
        if isinstance(node, ast.Constant) and isinstance(node.value, float) and math.isfinite(node.value):
            return ast.copy_location(ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id='float', ctx=ast.Load()), __ember__('fromhex')], keywords=[]), args=[__ember__(node.value.hex())], keywords=[]), node)
        return node
    tree = __shape__(tree)
    ast.fix_missing_locations(tree)
    tree = __stone__(tree)
    ast.fix_missing_locations(tree)
    return tree, used
def __glass__(tree, path, rng, used):
    code = compile(tree, os.path.basename(path), 'exec', optimize=2, dont_inherit=True)
    raw = marshal.dumps(code)
    bag = [(0, zlib.compress(raw, 9)), (1, bz2.compress(raw, 9)), (2, lzma.compress(raw, preset=9))]
    bag.sort(key=lambda x: len(x[1]))
    raw = bytes([bag[0][0]]) + bag[0][1]
    keya = rng.randint(1000000, 2147483647)
    keyb = rng.randint(1000000, 2147483647)
    box = bytearray()
    cur = keya & 255
    step = ((keya >> 8) & 255) or 73
    salt = ((keya >> 16) & 255) or 19
    for i, one in enumerate(raw):
        cur = (cur + step + i + salt) & 255
        box.append(one ^ cur ^ ((salt + i) & 255))
    raw = zlib.compress(bytes(box), 9)
    box = bytearray()
    cur = keyb & 255
    step = ((keyb >> 8) & 255) or 73
    salt = ((keyb >> 16) & 255) or 19
    for i, one in enumerate(raw):
        cur = (cur + step + i + salt) & 255
        box.append(one ^ cur ^ ((salt + i) & 255))
    raw = bytes(box)
    tag = hashlib.sha256(raw).hexdigest()
    blob = []
    text = base64.b85encode(raw).decode('ascii')
    at = 0
    while at < len(text):
        blob.append(text[at:at + 84])
        at += 84
    walk = list(range(len(blob)))
    rng.shuffle(walk)
    bag = [blob[i] for i in walk]
    back = [0] * len(blob)
    for i, one in enumerate(walk):
        back[one] = i
    abc = 'abcdefghijklmnopqrstuvwxyz'
    pool = ['obs', 'veil', 'shard', 'vein', 'slab', 'cave', 'drip', 'ash', 'slag', 'gloom', 'smoke', 'coal', 'flint', 'glass', 'spike', 'night', 'lava', 'ember', 'grit', 'stone', 'forge', 'basalt', 'onyx', 'dust', 'crust']
    def __shard__():
        while True:
            name = f"__{rng.choice(pool)}{rng.choice(abc)}{rng.choice(abc)}__"
            if name not in used and name.isidentifier():
                used.add(name)
                return name
    a = __shard__()
    b = __shard__()
    c = __shard__()
    d = __shard__()
    e = __shard__()
    f = __shard__()
    one = ""
    two = ""
    three = f"import base64,bz2,hashlib,lzma,marshal,zlib;{a}={bag!r};{b}={back!r};{c}={keya};{d}={keyb};{e}={tag!r}"
    four = f"def {f}(x,k):b=bytearray();c=k&255;s=((k>>8)&255) or 73;t=((k>>16)&255) or 19;[(c:=((c+s+i+t)&255),b.append(o^c^((t+i)&255))) for i,o in enumerate(x)];return bytes(b)"
    five = f"x=base64.b85decode(''.join({a}[i] for i in {b}).encode());(hashlib.sha256(x).hexdigest()!={e} or getattr(getattr(__import__('builtins'),'exec'),'__module__','builtins')!='builtins' or getattr(getattr(__import__('builtins'),'eval'),'__module__','builtins')!='builtins' or __import__('sys').gettrace() or __import__('sys').getprofile()) and (_ for _ in ()).throw(SystemExit);x={f}(x,{d});x=zlib.decompress(x);x={f}(x,{c});m=x[0];x=x[1:];vars(__import__('builtins'))['exec'](marshal.loads((zlib.decompress,bz2.decompress,lzma.decompress)[m](x)),globals())"
    return "\n".join([one, two, three, four, five])
def __forge__(path):
    if not path:
        raise ValueError("empty path")
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    raw = code.encode('utf-8')
    rng = random.Random(int(hashlib.sha256(raw).hexdigest()[:16], 16))
    st = time.time()
    tree, used = __vein__(code, rng)
    out = __glass__(tree, path, rng, used)
    dst = os.path.splitext(path)[0] + "_obf.py"
    with open(dst, 'w', encoding='utf-8', newline='\n') as f:
        f.write(out)
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
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
if __name__ == "__main__":__obsidian__()
