import sys
import os
import random
import ast
import zlib
import secrets
import string
import struct
import warnings
from pystyle import Col, Colorate, Colors
warnings.filterwarnings('ignore', category=SyntaxWarning)
sys.setrecursionlimit(1000000)
import marshal
import types


def __enderman__():return "".join(__import__("random").sample([chr(i) for i in range(97, 122)], k=5))
def __creeper__():return "".join(__import__("random").sample([chr(i) for i in range(97, 122)], k=2))
def __nhincaigi__():return ''.join(__import__('random').choices([chr(i) for i in range(0x4e00, 0x9fff)], k=3))
def __yeppppppp__():return "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=1))
def __lamgidau__():return random.randint(1000, 9999)
def __khonglamgidau__():return random.choice([True, False])
def __thaygiantroi__():return "".join(__import__("random").sample([chr(i) for i in range(97, 122)], k=3))
def __ngauroicacem__(__stone__):return (__stone__.co_code, __stone__.co_consts, __stone__.co_names, __stone__.co_varnames, __stone__.co_freevars, __stone__.co_cellvars)
def __void__(__block__):
    if isinstance(__block__, (list, tuple)):return b''.join(__void__(__item__) for __item__ in __block__)
    elif isinstance(__block__, bytes):return __block__
    elif isinstance(__block__, str):return __block__.encode('utf-8')
    elif isinstance(__block__, int):return __block__.to_bytes(8, 'little', signed=True)
    elif __block__ is None:return b'N'
    elif isinstance(__block__, float):return __import__('struct').pack('<d', __block__)
    elif isinstance(__block__, bool):return b'T' if __block__ else b'F'
    elif isinstance(__block__, type(Ellipsis)):return b'E'
    elif isinstance(__block__, complex):return __import__('struct').pack('<dd', __block__.real, __block__.imag)
    elif isinstance(__block__, type((lambda: 1).__code__)):return __void__(__ngauroicacem__(__block__))
    else:return str(__block__).encode('utf-8')

def __steve__(__message__: str) -> str:
    return f""" {Col.Symbol('>', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(Colors.DynamicMIX((Col.cyan, Col.pink)), __message__)}{Col.light_gray}"""

def __vailon__(__message__, *args, **kwargs):return print(__steve__(__message__), *args, **kwargs)

def __portal__(__netherstar__):
    __beacons__ = __import__("zlib").decompress(__netherstar__).decode("utf-8")
    __emerald__ = __beacons__[1::2]
    return bytes.fromhex(__emerald__).decode("utf-8")

def __netherrack__(__glowstone__):
    if not __glowstone__:return '""'
    __redstone__ = __glowstone__.encode('utf-8').hex()
    __lapis__ = ''.join(secrets.choice(string.ascii_letters) for _ in range(len(__redstone__)))
    __goldingot__ = "".join(j + p for j, p in zip(__lapis__, __redstone__))
    __slimeball__ = zlib.compress(__goldingot__.encode())
    return f'__portal__({repr(__slimeball__)})'

def __magmacream__(__lava__):
    if len(__lava__) < 3: return __netherrack__(__lava__)
    __chunks__ = []
    __i__ = 0
    while __i__ < len(__lava__):
        __l__ = random.randint(1, 3)
        __chunks__.append(__lava__[__i__:__i__+__l__])
        __i__ += __l__
    __parts__ = [__netherrack__(__magma__) if __khonglamgidau__() else repr(__magma__) for __magma__ in __chunks__]
    return f"str().join([{','.join(__parts__)}])"

def __sieuvip__(__inventory__, __quartz__, __key__, __amethyst__=0):
    __key__[0] = (__key__[0] * 1664525 + 1013904223) & 0xFFFFFFFF
    [
        lambda: __inventory__.append(__amethyst__ ^ (__key__[0] & 0xFFFFFF)), 
        lambda: __inventory__.append((lambda __b__, __a__: ((((__a__ ^ (__key__[0] & 0xFFFFFF)) ^ (__b__ ^ (__key__[0] & 0xFFFFFF))) + 2 * ((__a__ ^ (__key__[0] & 0xFFFFFF)) & (__b__ ^ (__key__[0] & 0xFFFFFF)))) % 0xFFFFFF) ^ (__key__[0] & 0xFFFFFF))(__inventory__.pop(), __inventory__.pop())), 
        lambda: __inventory__.append((lambda __b__, __a__: (((__a__ ^ (__key__[0] & 0xFFFFFF)) + (~(__b__ ^ (__key__[0] & 0xFFFFFF)) + 1)) % 0xFFFFFF) ^ (__key__[0] & 0xFFFFFF))(__inventory__.pop(), __inventory__.pop())),
        lambda: __inventory__.append((((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) * (__inventory__.pop() ^ (__key__[0] & 0xFFFFFF))) % 0xFFFFFF) ^ (__key__[0] & 0xFFFFFF)), 
        lambda: __inventory__.append((((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) // ((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) + 1)) ^ (__key__[0] & 0xFFFFFF))),
        lambda: __inventory__.append(((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) ^ (__inventory__.pop() ^ (__key__[0] & 0xFFFFFF))) ^ (__key__[0] & 0xFFFFFF)),
        lambda: __inventory__.append(((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) | (__inventory__.pop() ^ (__key__[0] & 0xFFFFFF))) ^ (__key__[0] & 0xFFFFFF)),
        lambda: __inventory__.append(((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) & (__inventory__.pop() ^ (__key__[0] & 0xFFFFFF))) ^ (__key__[0] & 0xFFFFFF)),
        lambda: __inventory__.append((((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) << 1) % 0xFFFFFF) ^ (__key__[0] & 0xFFFFFF)),
        lambda: __inventory__.append(((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) >> 1) ^ (__key__[0] & 0xFFFFFF)),
        lambda: __inventory__.append(((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) % ((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) + 1)) ^ (__key__[0] & 0xFFFFFF)),
        lambda: __inventory__.append((~(__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) & 0xFFFFFF) ^ (__key__[0] & 0xFFFFFF)),
        lambda: __inventory__.append((lambda __x__: (((__x__ << 1) | (__x__ >> 23)) & 0xFFFFFF) ^ (__key__[0] & 0xFFFFFF))(__inventory__.pop() ^ (__key__[0] & 0xFFFFFF))),
        lambda: __inventory__.append((~((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) ^ (__inventory__.pop() ^ (__key__[0] & 0xFFFFFF))) & 0xFFFFFF) ^ (__key__[0] & 0xFFFFFF)),
        lambda: __inventory__.append((~((__inventory__.pop() ^ (__key__[0] & 0xFFFFFF)) & (__inventory__.pop() ^ (__key__[0] & 0xFFFFFF))) & 0xFFFFFF) ^ (__key__[0] & 0xFFFFFF)),
        __inventory__.pop,
        lambda: sys.exit(0) if sys.gettrace() else None
    ][__quartz__]() if __quartz__ != 15 else None
    if __quartz__ == 15: return __inventory__.pop()

def __bat__(__count__=3):
    __trash__ = []
    for _ in range(__count__):
        __trash__.append(ast.Assign(targets=[ast.Name(id="__" + __enderman__() + "__", ctx=ast.Store())], value=ast.Constant(value=__lamgidau__())))
    return __trash__

def __sniffer__(__node__, __map__):
    if __node__ in __map__: return __map__[__node__]
    __name__ = "__" + __enderman__() + "__"
    __map__[__node__] = __name__
    return __name__

class __bedrocktransformer__(ast.NodeTransformer):
    def __mine__(self, __n__):
        __method__ = "__mine" + __n__.__class__.__name__.lower() + "__"
        __miner__ = getattr(self, __method__, self.__gen__)
        return __miner__(__n__)
    def __gen__(self, __n__):
        for __field__, __old__ in ast.iter_fields(__n__):
            if isinstance(__old__, list):
                __new__ = []
                for __v__ in __old__:
                    if isinstance(__v__, ast.AST):
                        __v__ = self.__mine__(__v__)
                        if __v__ is None: continue
                        elif not isinstance(__v__, ast.AST):
                            __new__.extend(__v__)
                            continue
                    __new__.append(__v__)
                __n__.__dict__[__field__] = __new__
            elif isinstance(__old__, ast.AST):
                __new__ = self.__mine__(__old__)
                if __new__ is None: delattr(__n__, __field__)
                else: setattr(__n__, __field__, __new__)
        return __n__

def __elytra__(__t__):
    class __Elytra__(__bedrocktransformer__):
        def __minejoinedstr__(self, __n__):
            __args__ = []
            __fmt__ = ""
            for __v__ in __n__.values:
                if isinstance(__v__, ast.Constant) and isinstance(__v__.value, str):__fmt__ += __v__.value.replace("{", "{{").replace("}", "}}")
                elif isinstance(__v__, ast.FormattedValue):
                    __args__.append(self.__mine__(__v__.value))
                    __fmt__ += "{}"
            return ast.Call(func=ast.Attribute(value=ast.Constant(value=__fmt__), attr="format", ctx=ast.Load()), args=__args__, keywords=[])
        def __mineattribute__(self, __n__):
            self.__gen__(__n__)
            if isinstance(__n__.ctx, ast.Load):return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[__n__.value, ast.Constant(value=__n__.attr)], keywords=[])
            return __n__
        def __mineassign__(self, __n__):
            self.__gen__(__n__)
            if len(__n__.targets) == 1 and isinstance(__n__.targets[0], ast.Attribute):
                __t__ = __n__.targets[0]
                if isinstance(__t__.ctx, ast.Store):return ast.Expr(value=ast.Call(func=ast.Name(id='setattr', ctx=ast.Load()), args=[__t__.value, ast.Constant(value=__t__.attr), __n__.value], keywords=[]))
            return __n__
        def __minecall__(self, __n__):
            self.__gen__(__n__)
            __k__ = []
            for __kw__ in __n__.keywords:
                if __kw__.arg is not None:__k__.append(ast.keyword(arg=None, value=ast.Dict(keys=[ast.Constant(value=__kw__.arg)], values=[__kw__.value])))
                else:__k__.append(__kw__)
            __n__.keywords = __k__
            return __n__
    return __Elytra__().__mine__(__t__)

def __phantom__(b: bytes):
    __inventory__ = []
    __i__ = 0
    __slot__ = "__" + __enderman__() + "__"
    __stack__ = 3
    while __i__ < len(b):
        __block__ = b[__i__:__i__+__stack__]
        __biome__ = random.choice(['+', '*', '<<', '^'])
        __enchant__ = random.randint(100000, 999999)
        for __j__, __byte__ in enumerate(__block__):
            __idx__ = __i__ + __j__
            __key__ = __byte__
            if __biome__ == '^':
                __potion__ = f"{__enchant__} ^ {~__key__ ^ ~__enchant__}"
            elif __biome__ == '<<':
                __shift__ = random.randint(1, 4)
                __potion__ = f"{__key__ << __shift__} >> {__shift__}"
            elif __biome__ == '+':
                __potion__ = f"{__key__ + __enchant__} - {__enchant__}"
            elif __biome__ == '*':
                __potion__ = f"{__key__ * __enchant__} // {__enchant__}"
            else:
                __potion__ = str(__key__)
            __inventory__.append(f"{__potion__} if {__slot__} == {__idx__} else")
        __i__ += __stack__
    __inventory__.append("0") 
    __book__ = " ".join(__inventory__)
    return f"(lambda {__slot__}: bytes([({__book__}) for {__slot__} in range({len(b)})]))(b'{__yeppppppp__()}')"

def __strider__(f: float):
    return f"float('{f}')"

def __cobblestone__(__val__):
    if isinstance(__val__, bool):
        __n__ = __creeper__()
        if __val__: return f'(lambda {__n__}: {__n__} == {__n__})(1)'
        else: return f'(lambda {__n__}: {__n__} != {__n__})(1)'
    if isinstance(__val__, int):
        __offset__ = __lamgidau__()
        return f'(lambda __x__: __x__ - {__offset__})({__val__ + __offset__})'
    return str(__val__)

def __zombie__(__iron__, __gold__):
    __shulkerbox__ = []
    __diamond__ = __gold__ + 1
    for __idx__ in range(random.randint(1, 3)):
        __phantom__ = "__" + __enderman__() + "__"
        __glowitem__ = ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[ast.Constant(value=0)], keywords=[])
        __elytra__ = [ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=__glowitem__, attr='args'), slice=ast.Constant(value=0)), ops=[ast.Eq()], comparators=[ast.Constant(value=__diamond__)]), body=[ast.Assign(targets=[ast.Name(id=__phantom__)], value=ast.Constant(value=random.randint(0xFF, 0xFFFF)), lineno=None), ast.Expr(value=ast.Constant(value=__yeppppppp__()))], orelse=[])]
        __shulkerbox__.extend(__elytra__)
        __diamond__ += 1
    return __shulkerbox__

def __netherite__(__emerald__):
    if isinstance(__emerald__, bool):
        return repr(__emerald__)
    if isinstance(__emerald__, int):
        __nugget__ = random.randint(1000000, 9999999)
        __pickaxe__ = "__" + __enderman__() + "__"
        return f"(lambda {__pickaxe__}: {__pickaxe__} - {__nugget__})({__emerald__ + __nugget__})"
    return str(__emerald__)

def __anchor__(__glowstone__):
    __obsidian__ = ast.Constant(value=__lamgidau__())
    __lichen__ = ast.Constant(value=__lamgidau__())
    return ast.Match(
        subject=ast.Compare(left=__obsidian__, ops=[ast.Eq()], comparators=[__lichen__]),
        cases=[
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=True)),
                body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[], keywords=[]))]
            ),
             ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=False)),
                body=[ast.Assign(targets=[ast.Name(id="__" + __enderman__() + "__")], value=ast.Constant(value=__nhincaigi__()))]
            )
        ]
    )

def __gateway__(__t__):
    class __EndGateway__(__bedrocktransformer__):
        def __minefunctiondef__(self, __n__):
             __dim__ = []
             for __s__ in __n__.body:
                 __b__ = __s__
                 for __loop__ in range(1):
                     __flint__ = "__" + __enderman__() + "__"
                     __b__ = ast.Try(
                         body=[__anchor__(None)],
                         handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name=__flint__, body=[__b__])],
                         orelse=[],
                         finalbody=[]
                     )
                     __b__.body.append(ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[], keywords=[])))
                 __dim__.append(__b__)
             __n__.body = __dim__
             return self.__gen__(__n__)
    return __EndGateway__().__mine__(__t__)

def __endercrystal__(__tree__):
    def __gravel__(__wither__, __height__):
        __shulkers__ = []
        __ylevel__ = __height__ + 1
        for __loop__ in range(random.randint(1, 5)):
            __nametag__ = "__" + __enderman__() + "__"
            __nbt__ = [ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=__wither__), attr='args'), slice=ast.Constant(value=0)), ops=[ast.Eq()], comparators=[ast.Constant(value=__ylevel__)]), body=[ast.Assign(targets=[ast.Name(id=__nametag__)], value=ast.Constant(value=__void__(random.randint(0xFFFFF, 0xFFFFFFFFFFFF))), lineno=None)], orelse=[])]
            __shulkers__.extend(__nbt__)
            __ylevel__ += 1
        return __shulkers__
    def __soulsand__(__seed__, __count__=5):
        __rottenflesh__ = []
        for __idx__ in range(__count__):
            __xplevel__ = __seed__ + __idx__ + 1
            __mobname__ = "__" + __enderman__() + "__"
            __rottenflesh__.append(ast.Assign(targets=[ast.Name(id=__mobname__, ctx=ast.Store(), lineno=__xplevel__)], value=ast.Constant(value=__lamgidau__(), lineno=__xplevel__), lineno=__xplevel__))
        return __rottenflesh__
    def __basalt__(__chunks__):
        __entity__ = "__" + __enderman__() + "__"
        __wither__ = "__" + __enderman__() + "__"
        __fortress__ = [
            ast.AugAssign(target=ast.Name(id=__entity__), op=ast.Add(), value=ast.Constant(value=1)),
            ast.Try(
                body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[ast.Name(id=__entity__)], keywords=[]))],
                handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name=__wither__, body=[])],
                orelse=[],
                finalbody=[]
            )
        ]
        for __ore__ in __chunks__:
            __fortress__[1].handlers[0].body.append(ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=__wither__), attr='args'), slice=ast.Constant(value=0)), ops=[ast.Eq()], comparators=[ast.Constant(value=1)]), body=[__ore__], orelse=[]))
        __fortress__[1].handlers[0].body.extend(__gravel__(__wither__, len(__chunks__) + 1))
        __fortress__[1].handlers[0].body.extend(__soulsand__(__seed__=100))
        __node__ = ast.Assign(targets=[ast.Name(id=__entity__)], value=ast.Constant(value=0), lineno=None)
        return [__node__] + __fortress__
    def __observer__(__ore__):
        __mineshaft__ = __ore__.body
        __entity__ = "__" + __enderman__() + "__"
        __wither__ = "__" + __enderman__() + "__"
        __fortress__ = [
            ast.AugAssign(target=ast.Name(id=__entity__), op=ast.Add(), value=ast.Constant(value=1)),
            ast.Try(
                body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[ast.Name(id=__entity__)], keywords=[]))],
                handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name=__wither__, body=[])],
                orelse=[],
                finalbody=[]
            )
        ]
        for __block__ in __mineshaft__:
            __fortress__[1].handlers[0].body.append(ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=__wither__), attr='args'), slice=ast.Constant(value=0)), ops=[ast.Eq()], comparators=[ast.Constant(value=1)]), body=[__block__], orelse=[]))
        __fortress__[1].handlers[0].body.extend(__gravel__(__wither__, len(__mineshaft__) + 1))
        __ore__.body = [ast.Assign(targets=[ast.Name(id=__entity__)], value=ast.Constant(value=0), lineno=None)] + __fortress__
        return __ore__
    def __dispenser__(__ore__):
        if isinstance(__ore__, ast.FunctionDef): return __observer__(__ore__)
        return __ore__
    __ravine__ = []
    for __ore__ in __tree__.body:
        if isinstance(__ore__, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if random.choice([True, False]): __ravine__.append(__dispenser__(__ore__))
            else: __ravine__.append(__ore__)
        elif isinstance(__ore__, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
             if random.choice([True, False]): __ravine__.extend(__basalt__([__ore__]))
             else: __ravine__.append(__ore__)
        elif isinstance(__ore__, ast.Expr):
             if random.choice([True, False]): __ravine__.extend(__basalt__([__ore__]))
             else: __ravine__.append(__ore__)
        else:
            __ravine__.append(__ore__)
    __tree__.body = __ravine__
    return __tree__

def __guardian__(__target__):
    for __ore__ in ast.walk(__target__):
        if hasattr(__ore__, 'body') and isinstance(__ore__.body, list):
            __spawner__ = []
            for __golem__ in __ore__.body:
                if random.choice([True, False]):
                    __shield__ = ast.If(
                        test=ast.Compare(
                            left=ast.Constant(value=__lamgidau__()),
                            ops=[ast.Eq()],
                            comparators=[ast.Constant(value=__lamgidau__())]
                        ),
                        body=[ast.Pass()],
                        orelse=[__golem__]
                    ) if random.choice([True, False]) else ast.If(
                            test=ast.Compare(
                            left=ast.Constant(value=1),
                            ops=[ast.Eq()],
                            comparators=[ast.Constant(value=1)]
                        ),
                        body=[__golem__],
                        orelse=[ast.Pass()]
                    )
                    __spawner__.append(__shield__)
                else:
                    __spawner__.append(__golem__)
            __ore__.body = __spawner__
    return __target__

def __wither__(__acacia__):
    __soulsoil__ = []
    for __ore__ in __acacia__.body:
        if isinstance(__ore__, ast.FunctionDef):
            __iron__ = "__" + __enderman__() + "__"
            __soulsoil__.extend(__zombie__(__iron__, 10))
            __soulsoil__.append(__ore__)
            if hasattr(__ore__, 'body'):
                __ore__.body.insert(0, ast.Expr(value=ast.Constant(value=__nhincaigi__())))
        else:
            __soulsoil__.append(__ore__)
    __acacia__.body = __soulsoil__
    return __acacia__

def __blaze__():
    __v1__ = ast.Constant(value=__lamgidau__())
    __v2__ = ast.Constant(value=__lamgidau__())
    return ast.Match(
        subject=ast.Compare(left=__v1__, ops=[ast.Eq()], comparators=[__v2__]),
        cases=[
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=True)),
                body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[], keywords=[]))]
            ),
             ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=False)),
                body=[ast.Assign(targets=[ast.Name(id="__" + __enderman__() + "__")], value=ast.Constant(value=__nhincaigi__()))]
            )
        ]
    )

def __piston__(__target__):
    for __ore__ in ast.walk(__target__):
        if hasattr(__ore__, 'body') and isinstance(__ore__.body, list):
            __newbody__ = []
            for __stmt__ in __ore__.body:
                if random.choice([True, False]):
                    __pred__ = ast.If(
                        test=ast.Compare(
                            left=ast.Constant(value=__lamgidau__()),
                            ops=[ast.Eq()],
                            comparators=[ast.Constant(value=__lamgidau__())]
                        ),
                        body=[ast.Pass()],
                        orelse=[__stmt__]
                    ) if random.choice([True, False]) else ast.If(
                         test=ast.Compare(
                            left=ast.Constant(value=1),
                            ops=[ast.Eq()],
                            comparators=[ast.Constant(value=1)]
                        ),
                        body=[__stmt__],
                        orelse=[ast.Pass()]
                    )
                    __newbody__.append(__pred__)
                else:
                    if random.choice([True, False]) and sys.version_info >= (3, 10):
                         __newbody__.append(__blaze__())
                    __newbody__.append(__stmt__)
            __ore__.body = __newbody__
    return __target__

def __stray__(__target__):
    for __ore__ in ast.walk(__target__):
        if hasattr(__ore__, 'body') and isinstance(__ore__.body, list):
            __new__ = []
            for __stmt__ in __ore__.body:
                if random.choice([True, False]):
                     __meomeomeo__ = [
                         [ast.Expr(value=ast.Constant(value=__nhincaigi__())), __stmt__],
                         [ast.parse("eval('0/0')"), ast.parse(f"if '{__yeppppppp__()}' == '{__yeppppppp__()}': {__lamgidau__()}\nelse: pass"), __stmt__],
                         [ast.Expr(value=ast.Constant(value=__thaygiantroi__())), __stmt__]
                     ][random.randint(0, 2)]
                     
                     __wrapper__ = ast.Try(
                        body=__meomeomeo__,
                        handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()), name=None, body=[ast.Pass()])],
                        orelse=[],
                        finalbody=[]
                    )
                     __new__.append(__wrapper__)
                else:
                    __new__.append(__stmt__)
            __ore__.body = __new__
    return __target__

def __chest__(__t__):
    class __Hopper__(__bedrocktransformer__):
        def __mine__(self, __n__):
            if isinstance(__n__, ast.Import):
                return self.__dispenser__(__n__)
            return super().__mine__(__n__)
        def __dispenser__(self, __n__):
            __stmts__ = []
            for alias in __n__.names:
                __stmts__.append(ast.Assign(
                    targets=[ast.Name(id=alias.asname or alias.name, ctx=ast.Store())],
                    value=ast.Call(
                        func=ast.Name(id='__import__', ctx=ast.Load()),
                        args=[ast.Constant(value=alias.name)],
                        keywords=[]
                    )
                ))
            return __stmts__
    return __Hopper__().__mine__(__t__)

def __silverfish__(__target__):
    def __spawner__():
        __name__ = "__" + __enderman__() + "__"
        return ast.FunctionDef(
            name=__name__,
            args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]),
            body=[ast.Expr(value=ast.Constant(value=__nhincaigi__())), ast.Return(value=ast.Constant(value=__lamgidau__()))],
            decorator_list=[]
        )
    __target__.body.insert(random.randint(0, len(__target__.body)), __spawner__())
    return __target__

def __repeater__(__target__):
    for __ore__ in ast.walk(__target__):
        if isinstance(__ore__, ast.FunctionDef):
             __loop__ = ast.While(
                 test=ast.Constant(value=True),
                 body=__ore__.body + [ast.Break()],
                 orelse=[]
             )
             __ore__.body = [__loop__]
    return __target__

def __skeleton__(__birch__):
    __spruce__ = []
    for __bone__ in __birch__:
        __oak__ = __bone__
        for __loop__ in range(1):
            __trident__ = "__" + __creeper__() + "__"
            __guard__ = []
            for __k__ in range(2):
                __guard__.append(ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=__trident__), attr='args'), slice=ast.Constant(value=0)), ops=[ast.Eq()], comparators=[ast.Constant(value=__k__)]), body=[ast.Assign(targets=[ast.Name(id="__" + __enderman__() + "__")], value=ast.Constant(value=__lamgidau__()), lineno=None)], orelse=[]))
            __oak__ = ast.Try(body=[__bone__], handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name=__trident__, body=__guard__)], orelse=[], finalbody=[])
        __spruce__.append(__oak__)
    return __spruce__

def __villager__(__jungle__, __old__, __new__):
    for __trade__ in ast.walk(__jungle__):
        if isinstance(__trade__, ast.FunctionDef) and __trade__.name == __old__:__trade__.name = __new__
        elif isinstance(__trade__, ast.Attribute) and isinstance(__trade__.value, ast.Name) and __trade__.value.id == __old__:__trade__.value.id = __new__
        elif isinstance(__trade__, ast.Call) and isinstance(__trade__.func, ast.Name) and __trade__.func.id == __old__:__trade__.func.id = __new__
        elif isinstance(__trade__, ast.Name) and __trade__.id == __old__:__trade__.id = __new__
    return __jungle__

def __obsidian__(__darkoak__):
    __enderchest__ = {}
    for __ore__ in ast.walk(__darkoak__):
        if isinstance(__ore__, ast.MatchValue): continue
        for __field__, __val__ in ast.iter_fields(__ore__):
            if isinstance(__val__, list):
                __mangrove__ = []
                for __item__ in __val__:
                    if isinstance(__item__, ast.Constant) and isinstance(__item__.value, str):__mangrove__.append(ast.parse(__magmacream__(__item__.value)).body[0].value)
                    elif isinstance(__item__, ast.Constant) and isinstance(__item__.value, bool):__mangrove__.append(ast.parse(__cobblestone__(__item__.value)).body[0].value)
                    elif isinstance(__item__, ast.Constant) and isinstance(__item__.value, int):
                         __mangrove__.append(random.choice([
                             lambda: ast.Name(id=__sniffer__(__item__.value, __enderchest__), ctx=ast.Load()),
                             lambda: ast.parse(__cobblestone__(__item__.value)).body[0].value,
                             lambda: ast.parse(__netherite__(__item__.value)).body[0].value
                         ])())
                    elif isinstance(__item__, ast.Constant) and isinstance(__item__.value, float):__mangrove__.append(ast.parse(__strider__(__item__.value)).body[0].value)
                    elif isinstance(__item__, ast.Constant) and isinstance(__item__.value, bytes):__mangrove__.append(ast.parse(__phantom__(__item__.value)).body[0].value)
                    elif isinstance(__item__, ast.JoinedStr):pass
                    else:__mangrove__.append(__item__)
                setattr(__ore__, __field__, __mangrove__)
            elif isinstance(__val__, ast.Constant) and isinstance(__val__.value, str):setattr(__ore__, __field__, ast.parse(__magmacream__(__val__.value)).body[0].value)
            elif isinstance(__val__, ast.Constant) and isinstance(__val__.value, bool):setattr(__ore__, __field__, ast.parse(__cobblestone__(__val__.value)).body[0].value)
            elif isinstance(__val__, ast.Constant) and isinstance(__val__.value, int):
                 setattr(__ore__, __field__, random.choice([
                     lambda: ast.Name(id=__sniffer__(__val__.value, __enderchest__), ctx=ast.Load()),
                     lambda: ast.parse(__cobblestone__(__val__.value)).body[0].value,
                     lambda: ast.parse(__netherite__(__val__.value)).body[0].value
                 ])())
            elif isinstance(__val__, ast.Constant) and isinstance(__val__.value, float):setattr(__ore__, __field__, ast.parse(__strider__(__val__.value)).body[0].value)
            elif isinstance(__val__, ast.Constant) and isinstance(__val__.value, bytes):setattr(__ore__, __field__, ast.parse(__phantom__(__val__.value)).body[0].value)
            elif isinstance(__val__, ast.JoinedStr):pass
    
    for __val__, __name__ in __enderchest__.items():
        __assign__ = ast.Assign(targets=[ast.Name(id=__name__, ctx=ast.Store())], value=ast.Constant(value=__val__), lineno=None)
        __darkoak__.body.insert(0, __assign__)
        
    return __darkoak__

def __pufferfish__(__target__):
   __poison__ = f"lambda __p__: (lambda __a__, __b__: __a__ + __b__)('{__enderman__()}', '{__creeper__()}')"
   __trap__ = ast.Expr(value=ast.parse(__poison__).body[0].value)
   __target__.body.insert(0, __trap__)
   return __target__


def __nethertravel__(__target__):
    for __node__ in ast.walk(__target__):
        if isinstance(__node__, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if len(__node__.body) < 2: continue
            __optimusprime__ = [__node__.body[__xp__:__xp__+2] for __xp__ in range(0, len(__node__.body), 2)]
            if len(__optimusprime__) < 2: continue
            
            __sieudeptrai__ = "__" + __enderman__() + "__" 
            __vipvai__ = "__" + __enderman__() + "__" 
            __inventory__ = "__" + __enderman__() + "__"
            __seeds__ = list(range(len(__optimusprime__)))
            random.shuffle(__seeds__)
            __mrbeast__ = {__xp__: __obsidian__ for __xp__, __obsidian__ in enumerate(__seeds__)}
            
            __biomes__ = []
            
            for _ in range(5):
                __biomes__.append(ast.match_case(
                    pattern=ast.MatchValue(value=ast.Constant(value=random.randint(1000, 9999))),
                    body=__bat__(5) + [ast.Expr(value=ast.Call(func=ast.Name(id='__sieuvip__', ctx=ast.Load()), args=[ast.Name(id=__inventory__, ctx=ast.Load()), ast.Constant(value=0), ast.Name(id=__lever__, ctx=ast.Load()), ast.Constant(value=random.randint(1, 100))], keywords=[]))] + [ast.Break()]
                ))

            for __xp__, __chunk__ in enumerate(__optimusprime__):
                __obsidian__ = __mrbeast__[__xp__]
                __magma__ = __mrbeast__[__xp__+1] if __xp__ + 1 < len(__optimusprime__) else -1
                
                __xinvailon__ = list(__chunk__)
                
                if random.choice([True, False]):
                    __xinvailon__.insert(0, ast.If(
                        test=ast.Compare(
                            left=ast.Constant(value="bedrock"), 
                            ops=[ast.Eq()], 
                            comparators=[ast.Constant(value="vip")]
                        ),
                        body=[ast.Pass()],
                        orelse=[ast.Expr(value=ast.Call(func=ast.Name(id="exit", ctx=ast.Load()), args=[], keywords=[]))]
                    ))

                if random.choice([True, False]):
                    __ronaldo__ = "__" + __thaygiantroi__() + "__"
                    __wrapped__ = ast.Try(
                        body=__xinvailon__,
                        handlers=[ast.ExceptHandler(type=ast.Name(id='Exception', ctx=ast.Load()), name=__ronaldo__, body=[ast.Pass()])],
                        orelse=[],
                        finalbody=[]
                    )
                    __xinvailon__ = [__wrapped__]

                if random.choice([True, False]):
                    __podzol__ = "__" + __enderman__() + "__"
                    __mycelium__ = ast.Try(
                         body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[ast.Name(id=__podzol__, ctx=ast.Load())], keywords=[]))],
                         handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name=__podzol__, body=[ast.Pass()])],
                         orelse=[],
                         finalbody=[]
                    )
                    __xinvailon__.insert(random.randint(0, len(__xinvailon__)), __mycelium__)

                if not any(isinstance(__stmt__, (ast.Return, ast.Raise, ast.Break, ast.Continue)) for __stmt__ in __xinvailon__):
                     __furnace__ = []
                     __furnace__.append(ast.Expr(value=ast.Call(func=ast.Name(id='__sieuvip__', ctx=ast.Load()), args=[ast.Name(id=__inventory__, ctx=ast.Load()), ast.Constant(value=0), ast.Name(id=__lever__, ctx=ast.Load()), ast.Constant(value=random.randint(1, 100))], keywords=[])))
                     __furnace__.append(ast.Expr(value=ast.Call(func=ast.Name(id='__sieuvip__', ctx=ast.Load()), args=[ast.Name(id=__inventory__, ctx=ast.Load()), ast.Constant(value=15), ast.Name(id=__lever__, ctx=ast.Load())], keywords=[])))
                     __furnace__.append(ast.Expr(value=ast.Call(func=ast.Name(id='__sieuvip__', ctx=ast.Load()), args=[ast.Name(id=__inventory__, ctx=ast.Load()), ast.Constant(value=0), ast.Name(id=__lever__, ctx=ast.Load()), ast.Constant(value=__magma__)], keywords=[])))
                     __furnace__.append(ast.Expr(value=ast.Call(func=ast.Name(id='__sieuvip__', ctx=ast.Load()), args=[ast.Name(id=__inventory__, ctx=ast.Load()), ast.Constant(value=0), ast.Name(id=__lever__, ctx=ast.Load()), ast.Constant(value=0)], keywords=[])))
                     __furnace__.append(ast.Expr(value=ast.Call(func=ast.Name(id='__sieuvip__', ctx=ast.Load()), args=[ast.Name(id=__inventory__, ctx=ast.Load()), ast.Constant(value=1), ast.Name(id=__lever__, ctx=ast.Load())], keywords=[])))
                     __furnace__.append(ast.Expr(value=ast.Call(func=ast.Name(id='__sieuvip__', ctx=ast.Load()), args=[ast.Name(id=__inventory__, ctx=ast.Load()), ast.Constant(value=16), ast.Name(id=__lever__, ctx=ast.Load())], keywords=[])))
                     __furnace__.append(ast.Assign(targets=[ast.Name(id=__sieudeptrai__, ctx=ast.Store())], value=ast.Call(func=ast.Name(id='__sieuvip__', ctx=ast.Load()), args=[ast.Name(id=__inventory__, ctx=ast.Load()), ast.Constant(value=15), ast.Name(id=__lever__, ctx=ast.Load())], keywords=[])))
                     __xinvailon__.extend(__furnace__)
                
                __biomes__.append(ast.match_case(
                    pattern=ast.MatchValue(value=ast.Constant(value=__obsidian__)),
                    body=__xinvailon__
                ))
            
            __biomes__.append(ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=-1)),
                body=[ast.Break()]
            ))
            
            random.shuffle(__biomes__)
            
            __duongdongkichtay__ = ast.While(
                test=ast.Constant(value=True),
                body=[
                    ast.Match(
                        subject=ast.Name(id=__sieudeptrai__, ctx=ast.Load()),
                        cases=__biomes__
                    )
                ],
                orelse=[]
            )
            
            __lever__ = "__" + __enderman__() + "__"
            __hopper__ = ast.Assign(targets=[ast.Name(id=__inventory__, ctx=ast.Store())], value=ast.List(elts=[], ctx=ast.Load()))
            __comparator__ = ast.Assign(targets=[ast.Name(id=__sieudeptrai__, ctx=ast.Store())], value=ast.Constant(value=__mrbeast__[0]))
            
            __lever__ = ast.Assign(targets=[ast.Name(id=__key__, ctx=ast.Store())], value=ast.List(elts=[ast.Constant(value=random.randint(0, 0xFFFFFFFF))], ctx=ast.Load()))
            __node__.body = [__hopper__, __comparator__, __lever__] + [__duongdongkichtay__]
            
    return __target__


def __creaking__():
    def __ancientcity__(__target__, __key__=69):
        def __magmacube__(__val__):
            __high__, __low__ = __val__ & 0b11110000, __val__ & 0b00001111
            return f"(({__high__+10**20}) >> ({__low__+10**30}))" if __val__ > 15 else str(__val__)
        __fx__ = [__magmacube__(ord(__char__) ^ __key__) for __char__ in __target__]
        return f"((lambda __x__: __x__)(lambda *__a__: ''.join([chr(__n__ ^ 64) for __n__ in __a__]))(*[{','.join(__fx__)}]))"
    __s__ = ""
    for _ in range(100):
        __s__ += f"__import__('sys').modules['__main__'],"
    return f"try:__pycdc__=[{__s__}]\nexcept:pass\n{__ancientcity__('Anti-PyCDC')}"

def __endermite__(__target__):
    __code__ = """
__potion__ = getattr(__import__('ctypes'), 'pythonapi')
__recipe__ = getattr(__potion__, 'PyMarshal_ReadObjectFromString')
__enchant__ = getattr(__potion__, 'PyEval_EvalCode')
"""
    __guard__ = ast.parse(__code__).body
    for __node__ in reversed(__guard__):
        __target__.body.insert(0, __node__)
    return __target__

def __warden__(__target__):
    __shrieker__ = """
if __import__('sys').gettrace() is not None:
    __import__('sys').exit(1)
"""
    __guard__ = ast.parse(__shrieker__).body[0]
    __target__.body.insert(0, __guard__)
    __target__.body.insert(0, ast.parse(__creaking__()).body[0])
    return __target__

def __shulker__(__target__):
    __msg__ = __netherrack__("Protected by YepDepTrai")
    __box__ = ast.Expr(value=ast.Call(func=ast.Name(id='print', ctx=ast.Load()), args=[ast.parse(__msg__).body[0].value], keywords=[]))
    __target__.body.insert(0, __box__)
    return __target__

def __witherskeleton__(__code__):
    try:
        __tree__ = ast.parse(__code__)
        for __n__ in ast.walk(__tree__):
            if isinstance(__n__, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef, ast.Module)):
                if __n__.body and isinstance(__n__.body[0], ast.Expr) and isinstance(__n__.body[0].value, ast.Constant) and isinstance(__n__.body[0].value.value, str):__n__.body.pop(0)
        return ast.unparse(__tree__)
    except:return __code__

def __dragonegg__(__code__):
    __pack__ = []
    __visited__ = set()
    def __cartographer__(__obj__):
        if id(__obj__) in __visited__: return
        for __k__ in __obj__.co_consts:
            if isinstance(__k__, types.CodeType): __cartographer__(__k__)
        if id(__obj__) not in __visited__:
            __pack__.append(__obj__)
            __visited__.add(id(__obj__))
    __cartographer__(__code__)
    __mapping__ = {id(__obj__): f"__voidchunk__{__i__}__" for __i__, __obj__ in enumerate(__pack__)}
    __loader__ = []
    for __obj__ in __pack__:
        __name__ = __mapping__[id(__obj__)]
        def __loom__(__a__):
            if isinstance(__a__, types.CodeType): return __mapping__.get(id(__a__), "None")
            return repr(__a__)
        __consts__ = f"({', '.join(__loom__(__k__) for __k__ in __obj__.co_consts)},)" if __obj__.co_consts else "()"
        if sys.version_info >= (3, 11):
            __loader__.append(f"{__name__} = __chunkloader__({__obj__.co_argcount}, {__obj__.co_posonlyargcount}, {__obj__.co_kwonlyargcount}, {__obj__.co_nlocals}, {__obj__.co_stacksize}, {__obj__.co_flags}, {repr(__obj__.co_code)}, {__consts__}, {repr(__obj__.co_names)}, {repr(__obj__.co_varnames)}, {repr(__obj__.co_filename)}, {repr(__obj__.co_name)}, {repr(getattr(__obj__, 'co_qualname', __obj__.co_name))}, {__obj__.co_firstlineno}, {repr(getattr(__obj__, 'co_linetable', b''))}, {repr(getattr(__obj__, 'co_exceptiontable', b''))}, {repr(__obj__.co_freevars)}, {repr(__obj__.co_cellvars)})")
        else:
             __loader__.append(f"{__name__} = __chunkloader__({__obj__.co_argcount}, {getattr(__obj__, 'co_posonlyargcount', 0)}, {__obj__.co_kwonlyargcount}, {__obj__.co_nlocals}, {__obj__.co_stacksize}, {__obj__.co_flags}, {repr(__obj__.co_code)}, {__consts__}, {repr(__obj__.co_names)}, {repr(__obj__.co_varnames)}, {repr(__obj__.co_filename)}, {repr(__obj__.co_name)}, {__obj__.co_firstlineno}, {repr(getattr(__obj__, 'co_lnotab', b''))}, {repr(__obj__.co_freevars)}, {repr(__obj__.co_cellvars)})")
    __entry__ = __mapping__[id(__code__)]
    __header__ = f"def __chunkloader__(*args):return type((lambda:0).__code__)(*args)\n"
    __body__ = "\n".join(__loader__)
    __footer__ = f"\n__import__('marshal')\n__import__('types')\neval({__entry__}, globals(), globals())"
    return __header__ + __body__ + __footer__


def __theend__():
    try:
        if len(sys.argv) > 1:
            __stronghold__ = sys.argv[1]
            if os.path.exists(__stronghold__):
                with open(__stronghold__, 'r', encoding='utf-8') as f:__enchantmenttable__ = f.read()
                __enchantmenttable__ = __witherskeleton__(__enchantmenttable__)
                __bedrock__ = ast.parse(__enchantmenttable__)
                __bedrock__ = __chest__(__bedrock__)
                __bedrock__ = __wither__(__bedrock__)
                __bedrock__ = __silverfish__(__bedrock__)
                __bedrock__ = __repeater__(__bedrock__)
                __bedrock__ = __piston__(__bedrock__)
                __bedrock__ = __warden__(__bedrock__)
                __bedrock__ = __stray__(__bedrock__)
                __bedrock__ = __endermite__(__bedrock__)
                __bedrock__ = __shulker__(__bedrock__)
                __bedrock__ = __guardian__(__bedrock__)
                __bedrock__ = __endercrystal__(__bedrock__)
                __bedrock__ = __gateway__(__bedrock__)
                __bedrock__ = __pufferfish__(__bedrock__)
                __bedrock__ = __obsidian__(__bedrock__)
                __bedrock__ = __elytra__(__bedrock__)
                __bedrock__ = __villager__(__bedrock__, __enderman__(), __enderman__())
                __bedrock__.body = __skeleton__(__bedrock__.body)
                __bedrock__ = __nethertravel__(__bedrock__)
                
                __dragonbreath__ = 'def __portal__(__netherstar__):__beacons__=__import__("zlib").decompress(__netherstar__).decode("utf-8");__emerald__=__beacons__[1::2];return bytes.fromhex(__emerald__).decode("utf-8")'
                __endcrystal__ = ast.parse(__dragonbreath__).body[0]
                __bedrock__.body.insert(0, __endcrystal__)

                ast.fix_missing_locations(__bedrock__)
                try:
                    __compiled__ = compile(__bedrock__, __stronghold__, 'exec')
                    __packed__ = __dragonegg__(__compiled__)
                    __bedrock__ = ast.parse(__packed__)
                except Exception as __e__:
                    pass

                __chorusfruit__ = ast.unparse(__bedrock__)
                __endcity__ = os.path.splitext(__stronghold__)[0] + "_obf.py"
                with open(__endcity__, 'w', encoding='utf-8') as f:f.write(__chorusfruit__)
                __vailon__(f"Successfully obfuscated {__stronghold__} -> {__endcity__}")
            else:__vailon__(f"File not found: {__stronghold__}")
        else:__vailon__("Usage: python bedrock.py <file>")
    except Exception as __e__:__vailon__(f"Error: {__e__}")

if __name__ == "__main__":__theend__()
