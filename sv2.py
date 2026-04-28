#!/bin/python3

__INFO__ = {
    'Obfuscator': 'Shenron',
    'Obfuscator Owner': 'Nguyễn Xuân Trịnh',
    'Theme': 'Dragon Ball',
    'Contact': 'https://t.me/CalceIsMe',
    'Obfuscator Code Writing Process': 'https://www.youtube.com/watch?v=8yXEvIRFCwc&list=PLS0WF70AJy04pZ-OQwlsjuXiJL_3B9Oc4&index=4'
}

BANNER = """⠀⠀⠀⠀⢨⠊⠀⢀⢀⠀⠀⠀⠈⠺⡵⡱⠀⠀⠀⢠⠃⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢰⡁⠉⠊⠙⢎⣆⠀⠀⠀⠀⢩⢀⠜⠀⠀⠀
⠀⠀⠀⢠⠃⠀⠀⢸⢸⡀⠀⠀⠀⠀⠘⢷⡡⠀⠀⠎⠀⢰⣧⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠈⣐⢤⣀⣀⢙⠦⠀⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⢀⠃⠀⠀⠀⡌⢸⠃⠀⠀⠀⢀⠀⠀⠑⢧⡸⠀⢀⣿⢻⡀⠀⠀⣻⠀⠀⠀⠀⠀⣠⡴⠛⠉⠀⠀⠀⠑⢝⣦⠀⠀⠀⢰⠠⠁⠀⠀
⠀⠀⠌⠀⠀⠀⡘⣖⣄⢃⠀⠀⠀⠈⢦⡀⠀⡜⡇⠀⣼⠃⠈⢷⣶⢿⠟⠀⠀⠀⢠⠞⠁⠀⣀⠄⠂⣶⣶⣦⠆⠋⠓⠀⢀⣀⡇⠀⠀⠀
⠡⡀⡇⠀⢰⣧⢱⠊⠘⡈⠄⠀⠀⡀⠘⣿⢦⣡⢡⢰⡇⢀⠤⠊⡡⠃⠀⠀⢀⡴⠁⢀⠔⠊⠀⠀⢠⣿⠟⠁⠀⢀⠀⢀⠾⣤⣀⠀⠀⡠
⡀⠱⡇⠀⡆⢃⠀⠀⠀⠃⠀⠀⠀⣧⣀⣹⡄⠙⡾⡏⠀⡌⣠⡾⠁⠀⠀⣠⠊⢠⠔⠁⠀⠀⠀⠀⣸⡏⠀⠀⠀⢨⣪⡄⢻⣥⠫⡳⢊⣴
⠀⠀⢡⢠⠀⢸⡆⠀⣀⠀⠀⠀⠀⠈⣛⢛⣁⣀⠘⣧⣀⢱⡿⠀⠀⢀⡔⢁⢔⠕⠉⠐⣄⣠⠤⠶⠛⠁⢀⣀⠀⠀⠉⠁⠈⠷⣞⠔⡕⣿
⢄⡀⠘⢸⠀⣘⠇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠤⡑⢎⡉⢨⠁⠀⣠⢏⠔⠁⠘⣤⠴⢊⣡⣤⠴⠖⠒⠻⠧⣐⠓⠀⠀⠀⠀⠈⠀⡜⠀⠇
⠤⡈⠑⠇⠡⣻⢠⠊⠉⠉⠉⠑⠒⠤⣀⠀⠀⠀⠈⣾⣄⢘⣫⣜⠮⢿⣆⡴⢊⢥⡪⠛⠉⠀⠀⠀⠀⢀⠄⠂⠁⠀⠀⠀⠀⠀⠀⢧⡀⠈
⠁⠈⠑⠼⣀⣁⣇⠀⣴⡉⠉⠉⠀⠒⡢⠌⣐⡂⠶⣘⢾⡾⠿⢅⠀⣠⣶⡿⠓⠁⢠⠖⣦⡄⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢎⢳
⠀⠀⠀⠀⠉⣇⣿⢜⠙⢷⡄⠀⠀⠀⣄⣠⠼⢶⡛⣡⢴⠀⢀⠛⠱⡀⠀⠀⠀⠀⢀⠎⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡋⠮⡈
⠀⠀⢀⣖⠂⢽⡈⠀⠈⠑⠻⡦⠖⢋⣁⡴⠴⠊⣉⡠⢻⡖⠪⢄⡀⢈⠆⠀⠀⢠⠊⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⡵⢤⣃
⠀⠀⠸⢠⡯⣖⢵⡀⠀⠀⣠⣤⠮⠋⠁⠀⠀⠀⠀⠀⠸⣌⢆⢱⡾⠃⢀⠠⠔⠁⣀⢸⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⡸⠚⡸⠈⠁
⠤⢀⣀⢇⢡⠸⡗⢔⡄⠸⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⡩⠔⢉⡠⠔⠂⠉⢀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢁⠎⢀⡠⠔
⠀⠀⠀⠘⡌⢦⡃⣎⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠠⡟⠠⡐⣋⠤⠀⣀⠤⠐⠂⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢉⠉⠁⠀⠀
⠤⠀⠀⠀⠰⡀⠈⠻⡤⠚⢄⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠈⠂⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⢸⠀⢀⠤⠊
⣀⠀⠀⠀⠀⠘⠢⡑⢽⡬⢽⢆⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡶⠟⣉⣉⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠈⡖⠓⠒⠂
⠀⢈⣑⣒⡤⠄⠀⠈⠑⠥⣈⠙⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣁⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⣠⡻⠀⠀⠀⠇⠐⡔⣡
⠉⠉⠁⠀⠒⠒⠒⠒⠀⠤⠤⠍⣒⡗⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⢠⡞⢡⠃⠀⠀⠀⢸⠀⠸⣡
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠈⣶⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⣠⡔⠉⠀⡎⠀⠀⠀⠀⢸⠀⠀⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⣀⢼⠀⠀⠀⢉⡄⠈⠐⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⡜⡡⣾⠃⠀⠀⠸⠀⠀⠀⠀⠀⠀⡧⢄⡈
⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠉⠀⡆⠀⠀⠀⠈⡵⢄⡀⠀⠀⠙⠂⠄⣀⡀⠤⠊⠉⢀⣀⣠⡴⢿⣟⠞⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⡗⠢⢌
⠀⠀⠀⠀⡠⠔⠉⠀⠀⢀⡠⡤⠇⠀⠀⢀⠀⠰⣣⠈⠐⠤⡀⠀⡀⠈⠙⢍⠉⣉⠤⠒⠉⣠⣟⢮⠂⡄⠀⣼⠁⠀⡆⠀⠀⠀⠀⢡⣀⠀
⣿⡷⠖⠉⠀⠀⡠⠔⣪⣿⠟⣫⠀⠀⠀⢸⠀⠀⢩⢆⠀⠀⠈⠑⢳⠤⠄⠠⠭⠤⠐⠂⢉⣾⢮⠃⢠⠃⢰⡹⠀⢰⠀⠀⠀⠀⠀⢸⡉⣳
⠉⠀⢀⡠⠒⠉⣠⠾⠋⢁⠔⠹⠀⠀⠀⡈⡇⠀⠀⢫⣆⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⣘⢾⠃⢀⠏⣠⡳⠁⠀⣾⠀⠀⠀⠀⠀⠀⠈⠉"""

import ast, random, pickle, base64, bz2, zlib, lzma, time, sys, string, secrets
from ast import *

sys.setrecursionlimit(99999999)

ver = str(sys.version_info.major)+'.'+str(sys.version_info.minor)

try:
    from pystyle import *
except ModuleNotFoundError:
    print('>> Installing Module')
    __import__('os').system(f'pip{ver} install pystyle')
    from pystyle import *

System.Clear()

string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
cust = '🐉🐲⭐✦✧✨💫🌠⚡🔥💥☄️🌪❄️🌀🥋🥊⚔️👊🙌👐🟠🔴🟡🟢🔵🟣⚫⚪👽🤖👺🐢🐒🦍👑💎🔮🍑🍗🍚🍶🏯⛩⛰🛡👑🧙\u200d♂️🤜🤛😡😤🥵🤯🌌🌍🌑☀️🌠'

e = dict(zip(string, cust))
d = {v: k for k, v in e.items()}

def enc(s: str) -> str:
    noisy = s.encode().hex()                
    mapped = ''.join(e.get(c, c) for c in noisy)
    return f'shenron("{mapped}")'

buitlins = ['__import__', 'abs', 'all', 'any', 'ascii', 'bin', 'breakpoint', 'callable', 'chr', 'compile', 'delattr', 'dir', 'divmod', 'eval', 'exec', 'format', 'getattr', 'globals', 'hasattr', 'hash', 'hex', 'id', 'input', 'isinstance', 'issubclass', 'iter', 'aiter', 'len', 'locals', 'max', 'min', 'next', 'anext', 'oct', 'ord', 'pow', 'print', 'repr', 'round', 'setattr', 'sorted', 'sum', 'vars', 'None', 'Ellipsis', 'NotImplemented', 'False', 'True', 'bool', 'memoryview', 'bytearray', 'bytes', 'classmethod', 'complex', 'dict', 'enumerate', 'filter', 'float', 'frozenset', 'property', 'int', 'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'staticmethod', 'str', 'super', 'tuple', 'type', 'zip']
anti = """
print(' ' * len('>> Running...'), end='\\r')
if str(capsule_add('sys').exit) != '<built-in function exit>':
    raise fn
if str(print) != '<built-in function print>':
    raise fn
if str(exec) != '<built-in function exec>':
    raise fn
if str(input) != '<built-in function input>':
    raise fn
if str(len) != '<built-in function len>':
    raise fn
if str(capsule_add('marshal').loads) != '<built-in function loads>':
    raise fn
if str(capsule_add('pickle').loads) != '<built-in function loads>':
    raise fn

if len(open(__file__, 'rb').read().splitlines()) != 66:
    raise fn

if __INFO__ != {
    'Obfuscator': 'ShenronV2',
    'Obfuscator Owner': 'Nguyễn Xuân Trịnh',
    'Theme': 'Dragon Ball',
    'Contact': 'https://t.me/CalceIsMe',
    'Obfuscator Code Writing Process': 'https://www.youtube.com/watch?v=8yXEvIRFCwc&list=PLS0WF70AJy04pZ-OQwlsjuXiJL_3B9Oc4&index=4'
}:
    raise __INFO__
"""

anti = anti+"""
import builtins
def __antihook__():
    try:
        for name in ("exec", "eval", "print", "compile", "__import__", "open"):
            if not hasattr(builtins, name):raise fn
            func = getattr(builtins, name)
            if hasattr(func, "__wrapped__") or hasattr(func, "__code__"):raise fn
            if "built-in function" not in str(func):raise fn
        for frame in __import__('inspect').stack():
            fname = (frame.filename or "").lower()
            if any(x in fname for x in ["pydevd", "debugpy", "pdb", "frida", "uncompyle"]):raise fn
    except SystemExit:raise fn
    except:raise fn
__antihook__()
"""

def var_con_cak():
    return ''.join(random.choices([chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()], k=11))

v = var_con_cak()
args = var_con_cak()
kwds = var_con_cak()
d = var_con_cak()
k = var_con_cak()
c = var_con_cak()
arg_ = var_con_cak()
s = var_con_cak()

SANH = f"""#!/bin/python{ver}
# -*- coding: utf-8 -*-

__INFO__ = {{
    'Obfuscator': 'ShenronV2',
    'Obfuscator Owner': 'Nguyễn Xuân Trịnh',
    'Theme': 'Dragon Ball',
    'Contact': 'https://t.me/CalceIsMe',
    'Obfuscator Code Writing Process': 'https://www.youtube.com/watch?v=8yXEvIRFCwc&list=PLS0WF70AJy04pZ-OQwlsjuXiJL_3B9Oc4&index=4'
}}

class CapsuleCorp(object):

    def __init__(self):
        if str(__import__("sys").version_info.major)+"."+str(__import__("sys").version_info.minor) != "{ver}":
            print(f'>> Your Python Version Is {{str(__import__("sys").version_info.major)+"."+str(__import__("sys").version_info.minor)}}.\\n>> Please Install Python {ver} To Run This File!')
            __import__('sys').exit()
        else:
            print('>> Running...', end='\\r')

    def __call__(self, *{args}, **{kwds}):
        global yamcha, bulma, capsule, radar, shenron, frieza, goku, vegeta, gohan, trunks, capsule, kamehameha, capsule_add
        globals()['frieza'] = eval('lave'[::-1])
        globals()['goku'] = frieza('rts'[::-1])
        globals()['vegeta'] = frieza('setyb'[::-1])
        globals()['gohan'] = frieza(('tcid')[::-1])
        globals()['bulma'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        globals()['capsule'] = "🐉🐲⭐✦✧✨💫🌠⚡🔥💥☄️🌪❄️🌀🥋🥊⚔️👊🙌👐🟠🔴🟡🟢🔵🟣⚫⚪👽🤖👺🐢🐒🦍👑💎🔮🍑🍗🍚🍶🏯⛩⛰🛡👑🧙‍♂️🤜🤛😡😤🥵🤯🌌🌍🌑☀️🌠"
        globals()['trunks'] = frieza('piz'[::-1])
        globals()['radar'] = gohan(trunks(bulma, capsule))
        {d} = {{{v}: {k} for {k}, {v} in radar.items()}}
        globals()['shenron'] = lambda {s}: getattr(vegeta,"fromhex")(goku().join(({d}.get({c},{c}) for {c} in {s}))).decode()
        globals()['capsule_add'] = frieza({enc('__tropmi__')}[::-1])
        globals()['kamehameha'] = getattr(capsule_add({enc('types')}), {enc('FunctionType')})
        globals()['yamcha'] = frieza({enc('tni')}[::-1])

CapsuleCorp()()

class DragonRadar(object):

    def __init__(self, *{args}):
        setattr(self,"dragonball1",{enc('base64')})
        setattr(self,"dragonball2",{enc('bz2')})
        setattr(self,"dragonball3",{enc('zlib')})
        setattr(self,"dragonball4",{enc('lzma')})
        setattr(self,"{arg_}",{args}[0])

    def scan(self):
        return getattr(capsule_add(getattr(self,"dragonball4")),{enc("decompress")})(getattr(capsule_add(getattr(self,"dragonball3")),{enc("decompress")})(getattr(capsule_add(getattr(self,"dragonball2")),{enc("decompress")})(getattr(capsule_add(getattr(self,"dragonball1")),{enc("a85decode")})(getattr(self,"{arg_}")))))

class ShenronSummoner(object):

    def __init__(self):
        setattr(self,"dragonball5",{enc('ctypes')})
        setattr(self,"dragonball6",radar)
        setattr(self,"dragonball7",kamehameha)

    def wish(self,{arg_}):
        __dragon__=capsule_add({enc("ctypes")});ShenronV2=getattr(getattr(__dragon__,{enc("pythonapi")}),{enc("PyRun_String")});setattr(ShenronV2,shenron("🤯🤜🥵😤🤯🤛🤯😡🤯🌍🤯♂🥵😤"),__dragon__.py_object);setattr(ShenronV2,shenron("🥵️🤯🤜🥵🤯🤯😡🤯🌍🤯♂🥵😤🤯🤛"),[__dragon__.c_char_p,__dragon__.c_int,__dragon__.py_object,__dragon__.py_object]);ShenronV2({arg_},(len("🐉")<<8)+1,globals(),globals())

    def __call__(self,*{args},**{kwds}):
        self.wish(DragonRadar({args}[0]).scan())

try:ShenronSummoner()(BYTECODE)
except Exception as e:print(e)
except KeyboardInterrupt:pass"""

def _args(name):
    return ast.arguments(
        posonlyargs=[],
        args=[ast.arg(arg=name)],
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[]
    )

def obfstr(s):
    OFFSET = random.randint(*random.choice([(0x1F620, 0x1F625), (0x0300, 0x036F), (12353, 12355)]))
    k1 = random.randint(1000, 9999)
    k2 = random.randint(100, 999)
    lst = [chr((vars(__import__('builtins'))['ord'](c) ^ k1) + OFFSET ^ k2) for c in s]
    v = var_con_cak()
    offset_expr = ast.BinOp(ast.BinOp(ast.Constant(OFFSET ^ 0xAAAA), ast.BitXor(), ast.Constant(0xAAAA)), ast.Add(), ast.Constant(0))
    k1_expr = ast.BinOp(ast.Constant(k1 ^ 0x1234), ast.BitXor(), ast.Constant(0x1234))
    k2_expr = ast.BinOp(ast.Constant(k2 ^ 0x4321), ast.BitXor(), ast.Constant(0x4321))
    decode_expr = ast.Call(ast.Name('chr', ast.Load()), [ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name('ord', ast.Load()), [ast.Name(v, ast.Load())], []), ast.BitXor(), k2_expr), ast.Sub(), offset_expr), ast.BitXor(), k1_expr)], [])
    lam3 = ast.Lambda(args=_args(var_con_cak()), body=ast.Call(func=ast.Attribute(value=ast.Call(ast.Name('goku', ast.Load()), [], []), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=decode_expr, generators=[ast.comprehension(target=ast.Name(v, ast.Store()), iter=ast.List([ast.Constant(x) for x in lst], ast.Load()), ifs=[], is_async=0)])], keywords=[]))
    fake_lam = ast.Lambda(_args(var_con_cak()), ast.Constant(random.randint(100000, 999999)))
    lam2 = ast.Lambda(_args(var_con_cak()), ast.Call(lam3, [ast.Call(fake_lam, [ast.Constant(0)], [])], []))
    lam1 = ast.Lambda(_args(var_con_cak()), ast.Call(lam2, [ast.Constant('Minh Anh Dep zai')], []))
    lam0 = ast.Lambda(_args(var_con_cak()), ast.Call(lam1, [ast.Constant('Minh Anh Dep zai')], []))
    return ast.Call(lam1, [ast.Constant('Minh Anh Dep zai')], [])

def obfint(i):
    haha=2010-i
    lam3=ast.Lambda(_args(var_con_cak()),
        ast.Call(ast.Name("yamcha",ast.Load()),
            [ast.BinOp(ast.Constant(2010),ast.Sub(),ast.Constant(haha))],[]))
    lam2=ast.Lambda(_args(var_con_cak()),
        ast.Call(lam3,[ast.Constant("Trinh Dep Trai")],[]))
    lam1=ast.Lambda(_args(var_con_cak()),
        ast.Call(lam2,[ast.Constant("Trinh Dep Trai")],[]))
    return ast.Call(lam1,[ast.Constant("Trinh Dep Trai")],[])

def joinstr(f):
    if not isinstance(f, ast.JoinedStr):
        return f
    vl = []
    for i in f.values:
        if isinstance(i, ast.Constant):
            vl.append(i)
        elif isinstance(i, ast.FormattedValue):
            value_expr = i.value
            if i.conversion == 115:
                value_expr = Call(func=Name(id='goku', ctx=Load()), args=[value_expr], keywords=[])
            elif i.conversion == 114:
                value_expr = Call(func=Name(id='repr', ctx=Load()), args=[value_expr], keywords=[])
            elif i.conversion == 97:
                value_expr = Call(func=Name(id='ascii', ctx=Load()), args=[value_expr], keywords=[])
            if i.format_spec:
                if isinstance(i.format_spec, ast.JoinedStr):
                    spec_expr = joinstr(i.format_spec)
                elif isinstance(i.format_spec, ast.Constant):
                    spec_expr = i.format_spec
                elif isinstance(i.format_spec, ast.FormattedValue):
                    spec_parts = []
                    spec_value = i.format_spec.value
                    if i.format_spec.conversion == 115:
                        spec_value = Call(func=Name(id='goku', ctx=Load()), args=[spec_value], keywords=[])
                    elif i.format_spec.conversion == 114:
                        spec_value = Call(func=Name(id='repr', ctx=Load()), args=[spec_value], keywords=[])
                    elif i.format_spec.conversion == 97:
                        spec_value = Call(func=Name(id='ascii', ctx=Load()), args=[spec_value], keywords=[])
                    spec_expr = spec_value
                else:
                    spec_expr = i.format_spec
                value_expr = Call(func=Name(id='format', ctx=Load()), args=[value_expr, spec_expr], keywords=[])
            elif i.conversion == -1:
                value_expr = Call(func=Name(id='goku', ctx=Load()), args=[value_expr], keywords=[])
            vl.append(value_expr)
        elif hasattr(i, 'values') and isinstance(i, ast.JoinedStr):
            vl.append(joinstr(i))
        else:
            vl.append(Call(func=Name(id='goku', ctx=Load()), args=[i], keywords=[]))
    if not vl:
        return Constant(value='')
    if len(vl) == 1 and isinstance(vl[0], ast.Constant):
        return vl[0]
    return Call(func=Attribute(value=Constant(value=''), attr='join', ctx=Load()), args=[Tuple(elts=vl, ctx=Load())], keywords=[])

class cv(ast.NodeTransformer):

    def visit_JoinedStr(self, node):
        node = joinstr(node)
        return node

class hide(ast.NodeTransformer):

    def visit_Name(self, node):
        if node.id in buitlins:
            node = Call(func=Name(id='getattr', ctx=Load()), args=[Call(func=Name(id='capsule_add', ctx=Load()), args=[Constant(value='builtins')], keywords=[]), Constant(value=node.id)], keywords=[])
        return node
    
class obf(ast.NodeTransformer):

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            node = obfstr(node.value)
        elif isinstance(node.value, int):
            node = obfint(node.value)
        return node

def gen_jcode(code):
    men = var_con_cak()
    trinhdeptrai = var_con_cak()
    quadeptrai = var_con_cak()
    return [Assign(targets=[Name(id=trinhdeptrai, ctx=Store())], value=Constant(value=men), lineno=0), Assign(targets=[Name(id=quadeptrai, ctx=Store())], value=Constant(value=True), lineno=0), If(test=BoolOp(op=And(), values=[Compare(left=Name(id=trinhdeptrai, ctx=Load()), ops=[Eq()], comparators=[Constant(value=men)]), Compare(left=Name(id=quadeptrai, ctx=Load()), ops=[NotEq()], comparators=[Constant(value=True)])]), body=[Expr(value=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Constant(value='dit me may')))], orelse=[If(test=BoolOp(op=And(), values=[Compare(left=Name(id=trinhdeptrai, ctx=Load()), ops=[Eq()], comparators=[Constant(value=men)]), Compare(left=Name(id=quadeptrai, ctx=Load()), ops=[NotEq()], comparators=[Constant(value=False)])]), body=[Try(body=[Expr(value=Tuple(elts=[BinOp(left=Constant(value=1), op=Div(), right=Constant(value=0)), BinOp(left=Constant(value=123), op=Div(), right=Constant(value=0)), BinOp(left=Constant(value=12312321312), op=Div(), right=Constant(value=0))], ctx=Load()))], handlers=[ExceptHandler(body=[code])], orelse=[], finalbody=[])], orelse=[If(test=BoolOp(op=Or(), values=[Compare(left=Name(id=trinhdeptrai, ctx=Load()), ops=[Eq()], comparators=[Constant(value='gay')]), Compare(left=Name(id=quadeptrai, ctx=Load()), ops=[Eq()], comparators=[Constant(value=False)])]), body=[Expr(value=Call(func=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='cai lon cha nha may')], keywords=[])), args=[], keywords=[]))], orelse=[While(test=Constant(value=True), body=[Pass()], orelse=[]), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='cai dit thang cha may')], keywords=[]))])])])]

class junk(ast.NodeTransformer):

    def visit_Module(self, node):
        for i, j in enumerate(node.body):
            if isinstance(j, (ast.FunctionDef, ast.ClassDef)):
                self.visit(j)
            node.body[i] = [gen_jcode(j)]
        return node

    def visit_FunctionDef(self, node):
        for i, j in enumerate(node.body):
            node.body[i] = [gen_jcode(j)]
        return node

    def visit_ClassDef(self, node):
        for i, j in enumerate(node.body):
            node.body[i] = [gen_jcode(j)]
        return node

nghich = ''.join(random.sample([chr(i) for i in range(0xAC00, 0xD7A4)], 11))

def speed(code):
    import ast, random, base64
    code = ast.parse(code) if isinstance(code, str) else code
    nghich = ''.join(random.sample([chr(i) for i in range(44032, 55204) if chr(i).isidentifier()], 11))

    class __chanbomayde__(ast.NodeTransformer):

        def __init__(self):
            self.injected = False
            self.decoder_name = f'____{nghich}___'

        def coder(self):
            b_name = ''.join(map(chr, [98, 97, 115, 101, 54, 52]))
            d_name = ''.join(map(chr, [98, 56, 53, 100, 101, 99, 111, 100, 101]))
            import_b = ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[ast.Constant(b_name)], keywords=[])
            get_decode = ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[import_b, ast.Constant(d_name)], keywords=[])
            call_decode = ast.Call(func=get_decode, args=[ast.Name(id='x', ctx=ast.Load())], keywords=[])
            final_call = ast.Call(func=ast.Name(id='str', ctx=ast.Load()), args=[call_decode, ast.Constant('utf-8'), ast.Constant('concak')], keywords=[])
            return ast.FunctionDef(name=self.decoder_name, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Return(value=final_call)], decorator_list=[])

        def visit_Module(self, node):
            self.generic_visit(node)
            if not self.injected:
                node.body.insert(0, self.coder())
                self.injected = True
            return node

        def visit_Constant(self, node):
            if not isinstance(node.value, str):
                return node
            if not node.value:
                return node
            try:
                raw = node.value.encode('utf-8', 'concak')
            except Exception:
                return node
            encoded = base64.b85encode(raw)
            encoded_str = str(encoded, 'ascii')
            return ast.Call(func=ast.Name(id=self.decoder_name, ctx=ast.Load()), args=[ast.Constant(encoded_str)], keywords=[])
    transformer = __chanbomayde__()
    code = transformer.visit(code)
    ast.fix_missing_locations(code)
    return code

def speed1(code):
    code = ast.parse(code) if isinstance(code, str) else code

    class UnicodeObf(ast.NodeTransformer):

        def __init__(self):
            self.injected = False
            self.decoder_name = f'__{nghich}___'

        def obfstringv1(self):
            ord_name = ''.join(map(chr, [111, 114, 100]))
            chr_name = ''.join(map(chr, [99, 104, 114]))
            join_name = ''.join(map(chr, [106, 111, 105, 110]))
            return ast.FunctionDef(name=self.decoder_name, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='x'), ast.arg(arg='o')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Return(value=ast.Call(func=ast.Attribute(value=ast.Constant(''), attr=join_name, ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.Call(func=ast.Name(id=chr_name, ctx=ast.Load()), args=[ast.BinOp(left=ast.Call(func=ast.Name(id=ord_name, ctx=ast.Load()), args=[ast.Name(id='c', ctx=ast.Load())], keywords=[]), op=ast.Sub(), right=ast.Name(id='o', ctx=ast.Load()))], keywords=[]), generators=[ast.comprehension(target=ast.Name(id='c', ctx=ast.Store()), iter=ast.Name(id='x', ctx=ast.Load()), ifs=[], is_async=0)])], keywords=[]))], decorator_list=[])

        def visit_Module(self, node):
            self.generic_visit(node)
            if not self.injected:
                decoder = self.obfstringv1()
                node.body.insert(0, decoder)
                self.injected = True
            return node

        def visit_Constant(self, node):
            if not isinstance(node.value, str):
                return node
            if not node.value:
                return node
            OFFSET = random.randint(*random.choice([(0x1F620, 0x1F625), (0x0300, 0x036F), (12353, 12355)]))
            encoded = ''.join(vars(__builtins__)['chr'](vars(__builtins__)['ord'](c) + OFFSET) for c in node.value)
            return ast.Call(func=ast.Name(id=self.decoder_name, ctx=ast.Load()), args=[ast.Constant(encoded), ast.Constant(OFFSET)], keywords=[])
    transformer = UnicodeObf()
    code = transformer.visit(code)
    ast.fix_missing_locations(code)
    return code

import string as meo
__daucau_an_toan__ = meo.punctuation.replace('"', '').replace('\\', '')
__cothenoilaratngau__ = (meo.ascii_lowercase + meo.digits + meo.ascii_uppercase + meo.hexdigits + __daucau_an_toan__)
def rn1(s, junk="!@#6$%.().1.>.ⰲⰲⰲ.?2^#$ⰲⰲⰲ#$56^&*()__AnhNguyenCoder___!@#$%^&ⰲⰲⰲ*@#$ⰲⰲⰲ%()_"):
    key = f"{junk}{random.randint(0,9999)}"
    return f"('%({key})s' % {{{repr(key)}:{repr(s)}}})"
def obflz(__devailol__):
    if not __devailol__:
        return '""'
    __taisaoemyeu__ = __devailol__.encode('utf-8').hex()
    __codengauvcl__ = ''.join(secrets.choice(__cothenoilaratngau__) for _ in range(len(__taisaoemyeu__)))
    __cotloi__ = "".join(j + p for j, p in zip(__codengauvcl__, __taisaoemyeu__))
    __cothethoi__ = lzma.compress(__cotloi__.encode())
    return f'getattr(__import__{rn1("builtins")},{rn1("exec")})(bytes.fromhex(__import__{rn1("lzma")}.decompress({repr(__cothethoi__)}).decode()[1::2]).decode())'

print(Colorate.Diagonal(Colors.DynamicMIX((Col.orange, Col.red)), BANNER))
print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.orange)), ' '*19+'Obfuscator: ShenronV2'))
print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.orange)), ' '*19+'Author: NguyenXuanTrinh'))
print(Colorate.Diagonal(Colors.DynamicMIX((Col.orange, Col.red)), ' '*19+'Telegram: @CalceIsMe'))
print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.orange)), ' '*19+'Github: @nguyenxuantrinhdznotpd'))
print()
cyyy =  Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red))

while True:
    file_name = input(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), ">> Enter Your File Name: "))
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            code = anti+f.read()
            code = ast.parse(code)
        break
    except FileNotFoundError:
        print(Colorate.Horizontal(Colors.red_to_white, "File Not Found.\n"))
        
hide_builtins = True if input(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), ">> Do You Want To Hide Builtins (Y/n): ")) != 'n' else False
junk_code = True if input(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), ">> Do You Want To Add Junk Code (Recommend Yes) (Y/n): ")) != 'n' else False

print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Starting...'))
st = time.time()
print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Converting F-String To Join String...'))
code = cv().visit(code)

if hide_builtins:
    print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Hiding Builtins...'))
    code = hide().visit(code)

print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Obfuscating Content...'))
code = obf().visit(code)
code = speed(code)
code = speed1(code)

if junk_code:
    print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Adding Junk Code...'))
    code = junk().visit(code)

print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Compiling...'))
code = ast.unparse(code)
code = code.encode()

print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Compressing...'))
code = base64.a85encode(bz2.compress(zlib.compress(lzma.compress(code))))

open("obf-"+file_name,'wb').write(SANH.replace("BYTECODE", str(code)).encode())
print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), f'>> Saved in {"obf-"+file_name}'))
print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), f'>> Done in {time.time()-st:.3f}s'))