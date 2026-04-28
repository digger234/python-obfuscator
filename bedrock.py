import sys
import os
import random
import ast
import zlib
import secrets
import string
import struct
import warnings
import inspect
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

def __nhincaigimanhin__(__stone__):return (__stone__.co_code, __stone__.co_consts, __stone__.co_names, __stone__.co_varnames, __stone__.co_freevars, __stone__.co_cellvars)
def __xinvaicut__(__block__):
    if isinstance(__block__, (list, tuple)):return b''.join(__xinvaicut__(__item__) for __item__ in __block__)
    elif isinstance(__block__, bytes):return __block__
    elif isinstance(__block__, str):return __block__.encode('utf-8')
    elif isinstance(__block__, int):return __block__.to_bytes(8, 'little', signed=True)
    elif __block__ is None:return b'N'
    elif isinstance(__block__, float):return __import__('struct').pack('<d', __block__)
    elif isinstance(__block__, bool):return b'T' if __block__ else b'F'
    elif isinstance(__block__, type(Ellipsis)):return b'E'
    elif isinstance(__block__, complex):return __import__('struct').pack('<dd', __block__.real, __block__.imag)
    elif isinstance(__block__, type((lambda: 1).__code__)):return __xinvaicut__(__nhincaigimanhin__(__block__))
    else:return str(__block__).encode('utf-8')

def __steve__(__message__: str) -> str:
    return f""" {Col.Symbol('>', Col.light_gray, Col.dark_gray)} {Colorate.Diagonal(Colors.DynamicMIX((Col.cyan, Col.pink)), __message__)}{Col.light_gray}"""
def __vailon__(__message__, *args, **kwargs):return print(__steve__(__message__), *args, **kwargs)
def __toolnhindepko__(__netherstar__):
    __beacons__ = __import__("zlib").decompress(__netherstar__).decode("utf-8")
    __emerald__ = __beacons__[1::2]
    return bytes.fromhex(__emerald__).decode("utf-8")
def __netherrack__(__glowstone__):
    if not __glowstone__:return '""'
    __redstone__ = __glowstone__.encode('utf-8').hex()
    __lapis__ = ''.join(secrets.choice(string.ascii_letters) for _ in range(len(__redstone__)))
    __goldingot__ = "".join(j + p for j, p in zip(__lapis__, __redstone__))
    __slimeball__ = zlib.compress(__goldingot__.encode())
    return f'__toolnhindepko__({repr(__slimeball__)})'
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
        if __val__: return f'(lambda: (lambda {__n__}: {__n__} == {__n__})(1) + (len(__xinvaicut__(__nhincaigimanhin__((lambda: 1).__code__))) * 0))()'
        else: return f'(lambda: (lambda {__n__}: {__n__} != {__n__})(1) + (len(__xinvaicut__(__nhincaigimanhin__((lambda: 1).__code__))) * 0))()'
    if isinstance(__val__, int):
        __offset__ = __lamgidau__()
        return f'(lambda __x__: __x__ - {__offset__})({__val__ + __offset__} + (len(__xinvaicut__(__nhincaigimanhin__((lambda: 1).__code__))) * 0))'
    return str(__val__)
def __netherite__(__emerald__):
    if isinstance(__emerald__, bool):
        return repr(__emerald__)
    if isinstance(__emerald__, int):
        __nugget__ = random.randint(1000000, 9999999)
        __pickaxe__ = "__" + __enderman__() + "__"
        return f"(lambda {__pickaxe__}: {__pickaxe__} - {__nugget__})({__emerald__ + __nugget__} + (len(__xinvaicut__(__nhincaigimanhin__((lambda: 1).__code__))) * 0))"
    return str(__emerald__)
def __sniffer__(__node__, __map__):
    if __node__ in __map__: return __map__[__node__]
    __name__ = "__" + __enderman__() + "__"
    __map__[__node__] = __name__
    return __name__
def __deepslate__(__dust__):return ast.parse(__dust__, mode='eval').body
def __dripstone__(__dust__):
    try:
        if __dust__ is None:return None
        if any(isinstance(__echo__, (ast.Await, ast.Yield, ast.YieldFrom)) for __echo__ in ast.walk(__dust__)):return None
        __fog__ = "__" + __enderman__() + "__"
        return __deepslate__(f"(lambda {__fog__}:{__fog__})({ast.unparse(__dust__)})")
    except:return None
def __deadbush__():
    return ast.If(test=ast.Compare(left=ast.Constant(value=False), ops=[ast.Is()], comparators=[ast.Constant(value=True)]), body=[ast.Pass()], orelse=[ast.Pass()])

class __bedrocktransformer__(ast.NodeTransformer):
    def __craft__(self, __n__):
        __method__ = "__craft" + __n__.__class__.__name__.lower() + "__"
        __crafter__ = getattr(self, __method__, self.__gen__)
        return __crafter__(__n__)
    def __gen__(self, __n__):
        for __field__, __old__ in ast.iter_fields(__n__):
            if isinstance(__old__, list):
                __new__ = []
                for __v__ in __old__:
                    if isinstance(__v__, ast.AST):
                        __v__ = self.__craft__(__v__)
                        if __v__ is None: continue
                        elif not isinstance(__v__, ast.AST):
                            __new__.extend(__v__)
                            continue
                    __new__.append(__v__)
                __n__.__dict__[__field__] = __new__
            elif isinstance(__old__, ast.AST):
                __new__ = self.__craft__(__old__)
                if __new__ is None: delattr(__n__, __field__)
                else: setattr(__n__, __field__, __new__)
        return __n__

def __elytra__(__t__):
    class __Elytra__(__bedrocktransformer__):
        def __craftjoinedstr__(self, __n__):
            __args__ = []
            __fmt__ = ""
            for __v__ in __n__.values:
                if isinstance(__v__, ast.Constant) and isinstance(__v__.value, str):__fmt__ += __v__.value.replace("{", "{{").replace("}", "}}")
                elif isinstance(__v__, ast.FormattedValue):
                    __slot__ = len(__args__)
                    __args__.append(self.__craft__(__v__.value))
                    __part__ = "{" + str(__slot__)
                    if __v__.conversion != -1:__part__ += "!" + chr(__v__.conversion)
                    if __v__.format_spec:
                        __spec__ = self.__craft__(__v__.format_spec)
                        if isinstance(__spec__, ast.Constant) and isinstance(__spec__.value, str):__part__ += ":" + __spec__.value.replace("{", "{{").replace("}", "}}")
                        else:
                            __spot__ = len(__args__)
                            __args__.append(__spec__)
                            __part__ += ":{" + str(__spot__) + "}"
                    __fmt__ += __part__ + "}"
                else:
                    __slot__ = len(__args__)
                    __args__.append(self.__craft__(__v__))
                    __fmt__ += "{" + str(__slot__) + "}"
            return ast.Call(func=ast.Attribute(value=ast.Constant(value=__fmt__), attr="format", ctx=ast.Load()), args=__args__, keywords=[])
        def __craftattribute__(self, __n__):
            self.__gen__(__n__)
            if isinstance(__n__.ctx, ast.Load):return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[__n__.value, ast.Constant(value=__n__.attr)], keywords=[])
            return __n__
        def __craftassign__(self, __n__):
            self.__gen__(__n__)
            if len(__n__.targets) == 1 and isinstance(__n__.targets[0], ast.Attribute):
                __t__ = __n__.targets[0]
                if isinstance(__t__.ctx, ast.Store):return ast.Expr(value=ast.Call(func=ast.Name(id='setattr', ctx=ast.Load()), args=[__t__.value, ast.Constant(value=__t__.attr), __n__.value], keywords=[]))
            return __n__
        def __craftcall__(self, __n__):
            self.__gen__(__n__)
            __k__ = []
            for __kw__ in __n__.keywords:
                if __kw__.arg is not None:__k__.append(ast.keyword(arg=None, value=ast.Dict(keys=[ast.Constant(value=__kw__.arg)], values=[__kw__.value])))
                else:__k__.append(__kw__)
            __n__.keywords = __k__
            return __n__
    return __Elytra__().__craft__(__t__)

def __basalt__(__t__):
    class __Basalt__(__bedrocktransformer__):
        def __craftsubscript__(self, __n__):
            self.__gen__(__n__)
            if isinstance(__n__.ctx, ast.Load):
                return ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[__n__.value, ast.Constant(value='__getitem__')], keywords=[]), args=[__n__.slice], keywords=[])
            return __n__
        def __craftassign__(self, __n__):
            self.__gen__(__n__)
            if len(__n__.targets) == 1 and isinstance(__n__.targets[0], ast.Subscript):
                __t__ = __n__.targets[0]
                return ast.Expr(value=ast.Call(
                    func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[__t__.value, ast.Constant(value='__setitem__')], keywords=[]),
                    args=[__t__.slice, __n__.value],
                    keywords=[]
                ))
            return __n__
    return __Basalt__().__craft__(__t__)

def __tnt__(__t__):
    class __TNT__(__bedrocktransformer__):
        def __craftbinop__(self, __n__):
            self.__gen__(__n__)
            __opmap__ = {ast.Add: '__add__', ast.Sub: '__sub__', ast.Mult: '__mul__', ast.Div: '__truediv__', ast.FloorDiv: '__floordiv__', ast.Mod: '__mod__', ast.Pow: '__pow__', ast.LShift: '__lshift__', ast.RShift: '__rshift__', ast.BitOr: '__or__', ast.BitXor: '__xor__', ast.BitAnd: '__and__'}
            if type(__n__.op) in __opmap__:
                return ast.Call(func=ast.Attribute(value=__n__.left, attr=__opmap__[type(__n__.op)], ctx=ast.Load()), args=[__n__.right], keywords=[])
            return __n__
    return __TNT__().__craft__(__t__)

def __firecharge__(__t__):
    class __FireCharge__(__bedrocktransformer__):
        def __craftcompare__(self, __n__):
            self.__gen__(__n__)
            if len(__n__.ops) == 1 and len(__n__.comparators) == 1:
                __opmap__ = {ast.Eq: '__eq__', ast.NotEq: '__ne__', ast.Lt: '__lt__', ast.LtE: '__le__', ast.Gt: '__gt__', ast.GtE: '__ge__'}
                __op__ = type(__n__.ops[0])
                if __op__ in __opmap__:
                    return ast.Call(func=ast.Attribute(value=__n__.left, attr=__opmap__[__op__], ctx=ast.Load()), args=[__n__.comparators[0]], keywords=[])
            return __n__
    return __FireCharge__().__craft__(__t__)

def __glowberry__(__t__):
    class __GlowBerry__(__bedrocktransformer__):
        def __craftset__(self, __n__):
            self.__gen__(__n__)
            if not __n__.elts:return __n__
            try:
                __fog__ = "__" + __enderman__() + "__"
                return __deepslate__(f"(lambda *{__fog__}:set({__fog__}))({','.join(ast.unparse(__v__) for __v__ in __n__.elts)})")
            except:return __n__
        def __craftdict__(self, __n__):
            self.__gen__(__n__)
            try:
                __bits__ = []
                for __k__, __v__ in zip(__n__.keys, __n__.values):
                    if not isinstance(__k__, ast.Constant) or not isinstance(__k__.value, str) or not __k__.value.isidentifier() or __import__('keyword').iskeyword(__k__.value):return __n__
                    __bits__.append(f"{__k__.value}={ast.unparse(__v__)}")
                if not __bits__:return __n__
                __fog__ = "__" + __enderman__() + "__"
                return __deepslate__(f"(lambda **{__fog__}:{__fog__})({','.join(__bits__)})")
            except:return __n__
    return __GlowBerry__().__craft__(__t__)

def __sculk__(__t__):
    class __Sculk__(__bedrocktransformer__):
        def __craftboolop__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__)
            return __fog__ if __fog__ is not None else __n__
        def __craftunaryop__(self, __n__):
            self.__gen__(__n__)
            try:
                __fog__ = "__" + __enderman__() + "__"
                __dust__ = ast.unparse(__n__.operand)
                if isinstance(__n__.op, ast.Not):return __deepslate__(f"(lambda {__fog__}:not {__fog__})({__dust__})")
                elif isinstance(__n__.op, ast.USub):return __deepslate__(f"(lambda {__fog__}:-{__fog__})({__dust__})")
                elif isinstance(__n__.op, ast.UAdd):return __deepslate__(f"(lambda {__fog__}:+{__fog__})({__dust__})")
                elif isinstance(__n__.op, ast.Invert):return __deepslate__(f"(lambda {__fog__}:~{__fog__})({__dust__})")
            except:return __n__
            return __n__
        def __craftcall__(self, __n__):
            self.__gen__(__n__)
            try:
                if isinstance(__n__.func, ast.Name) and __n__.func.id in ('super','eval','exec','globals','locals','vars','dir','hasattr','getattr','setattr','__import__','type','isinstance','issubclass'):return __n__
                if any(isinstance(__dust__, (ast.Await, ast.Yield, ast.YieldFrom)) for __dust__ in ast.walk(__n__)):return __n__
                __fog__ = "__" + __enderman__() + "__"
                __call__ = ast.unparse(__n__)
                __func__ = ast.unparse(__n__.func)
                return __deepslate__(f"(lambda {__fog__}: {__call__.replace(__func__, __fog__, 1)})({__func__})")
            except:return __n__
    return __Sculk__().__craft__(__t__)

def __dripleaf__(__t__):
    class __Dripleaf__(__bedrocktransformer__):
        def __craftif__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.test)
            if __fog__ is not None:__n__.test = __fog__
            if not __n__.orelse:__n__.orelse = [__deadbush__()]
            return __n__
        def __craftwhile__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.test)
            if __fog__ is not None:__n__.test = __fog__
            return __n__
        def __craftifexp__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.test)
            if __fog__ is not None:__n__.test = __fog__
            return __n__
        def __craftassert__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.test)
            if __fog__ is not None:__n__.test = __fog__
            return __n__
        def __craftreturn__(self, __n__):
            self.__gen__(__n__)
            if __n__.value is not None:
                __fog__ = __dripstone__(__n__.value)
                if __fog__ is not None:__n__.value = __fog__
            return __n__
        def __craftraise__(self, __n__):
            self.__gen__(__n__)
            if __n__.exc is not None:
                __fog__ = __dripstone__(__n__.exc)
                if __fog__ is not None:__n__.exc = __fog__
            return __n__
        def __craftaugassign__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.value)
            if __fog__ is not None:__n__.value = __fog__
            return __n__
        def __craftlambda__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.body)
            if __fog__ is not None:__n__.body = __fog__
            return __n__
        def __craftformattedvalue__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.value)
            if __fog__ is not None:__n__.value = __fog__
            return __n__
        def __craftstarred__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.value)
            if __fog__ is not None:__n__.value = __fog__
            return __n__
        def __craftyield__(self, __n__):
            self.__gen__(__n__)
            if __n__.value is not None:
                __fog__ = __dripstone__(__n__.value)
                if __fog__ is not None:__n__.value = __fog__
            return __n__
        def __craftyieldfrom__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.value)
            if __fog__ is not None:__n__.value = __fog__
            return __n__
        def __craftawait__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.value)
            if __fog__ is not None:__n__.value = __fog__
            return __n__
        def __craftlistcomp__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__)
            return __fog__ if __fog__ is not None else __n__
        def __craftsetcomp__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__)
            return __fog__ if __fog__ is not None else __n__
        def __craftdictcomp__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__)
            return __fog__ if __fog__ is not None else __n__
        def __craftgeneratorexp__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__)
            return __fog__ if __fog__ is not None else __n__
        def __craftwith__(self, __n__):
            self.__gen__(__n__)
            for __item__ in __n__.items:
                __fog__ = __dripstone__(__item__.context_expr)
                if __fog__ is not None:__item__.context_expr = __fog__
            return __n__
        def __craftmatch__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.subject)
            if __fog__ is not None:__n__.subject = __fog__
            return __n__
        def __craftslice__(self, __n__):
            self.__gen__(__n__)
            if __n__.lower:
                __fog__ = __dripstone__(__n__.lower)
                if __fog__ is not None:__n__.lower = __fog__
            if __n__.upper:
                __fog__ = __dripstone__(__n__.upper)
                if __fog__ is not None:__n__.upper = __fog__
            if __n__.step:
                __fog__ = __dripstone__(__n__.step)
                if __fog__ is not None:__n__.step = __fog__
            return __n__
        def __craftnamedexpr__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.value)
            if __fog__ is not None:__n__.value = __fog__
            return __n__
        def __craftfor__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.iter)
            if __fog__ is not None:__n__.iter = __fog__
            return __n__
        def __craftasyncfor__(self, __n__):
            self.__gen__(__n__)
            __fog__ = __dripstone__(__n__.iter)
            if __fog__ is not None:__n__.iter = __fog__
            return __n__
        def __craftasyncwith__(self, __n__):
            self.__gen__(__n__)
            for __item__ in __n__.items:
                __fog__ = __dripstone__(__item__.context_expr)
                if __fog__ is not None:__item__.context_expr = __fog__
            return __n__
    return __Dripleaf__().__craft__(__t__)

def __breeze__(__t__):
    class __Breeze__(__bedrocktransformer__):
        def __craftfunctiondef__(self, __n__):
            self.__gen__(__n__)
            __n__.body.insert(0, __deadbush__())
            return __n__
        def __craftasyncfunctiondef__(self, __n__):
            self.__gen__(__n__)
            __n__.body.insert(0, __deadbush__())
            return __n__
        def __craftclassdef__(self, __n__):
            self.__gen__(__n__)
            __n__.body.insert(0, __deadbush__())
            for _ in range(random.randint(1, 2)):
                __stub__ = "__" + __enderman__() + "__"
                __n__.body.append(ast.FunctionDef(name=__stub__, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Pass()], decorator_list=[]))
            return __n__
        def __crafttry__(self, __n__):
            self.__gen__(__n__)
            __fog__ = "__" + __enderman__() + "__"
            __n__.body.insert(0, ast.Assign(targets=[ast.Name(id=__fog__, ctx=ast.Store())], value=ast.Constant(value=random.randint(1000, 99999))))
            __n__.handlers.insert(0, ast.ExceptHandler(type=ast.Name(id='OSError', ctx=ast.Load()), name="__" + __enderman__() + "__", body=[ast.Pass()]))
            return __n__
    return __Breeze__().__craft__(__t__)

def __chest__(__t__):
    class __Hopper__(__bedrocktransformer__):
        def __craft__(self, __n__):
            if isinstance(__n__, ast.Import):
                return self.__dispenser__(__n__)
            elif isinstance(__n__, ast.ImportFrom):
                return self.__dispenserfrom__(__n__)
            return super().__craft__(__n__)
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
        def __dispenserfrom__(self, __n__):
            __stmts__ = []
            __module__ = __n__.module or ''
            __level__ = __n__.level
            for alias in __n__.names:
                __stmts__.append(ast.Assign(
                    targets=[ast.Name(id=alias.asname or alias.name, ctx=ast.Store())],
                    value=ast.Call(
                        func=ast.Name(id='getattr', ctx=ast.Load()),
                        args=[
                            ast.Call(
                                func=ast.Name(id='__import__', ctx=ast.Load()),
                                args=[ast.Constant(value=__module__)],
                                keywords=[
                                    ast.keyword(arg='fromlist', value=ast.List(elts=[ast.Constant(value=alias.name)], ctx=ast.Load())),
                                    ast.keyword(arg='level', value=ast.Constant(value=__level__))
                                ]
                            ),
                            ast.Constant(value=alias.name)
                        ],
                        keywords=[]
                    )
                ))
            return __stmts__
    return __Hopper__().__craft__(__t__)

def __villager__(__jungle__):
    class __IronGolem__(__bedrocktransformer__):
        def __init__(self):
            self.__map__ = {}
            self.__reserved__ = set()
        def __carry__(self, __args__):
            for __a__ in __args__.posonlyargs + __args__.args + __args__.kwonlyargs:self.__craftarg__(__a__)
            if __args__.vararg:self.__craftarg__(__args__.vararg)
            if __args__.kwarg:self.__craftarg__(__args__.kwarg)

        def __craftname__(self, __n__):
            if __n__.id in self.__reserved__: return __n__
            if isinstance(__n__.ctx, ast.Store):
                if __n__.id not in self.__map__: self.__map__[__n__.id] = "__" + __enderman__() + "__"
            if __n__.id in self.__map__: __n__.id = self.__map__[__n__.id]
            return __n__

        def __craftarg__(self, __n__):
            if __n__.arg in self.__reserved__: return __n__
            if __n__.arg not in self.__map__: self.__map__[__n__.arg] = "__" + __enderman__() + "__"
            __n__.arg = self.__map__[__n__.arg]
            return __n__

        def __craftclassdef__(self, __n__):
            self.__oldmap__ = self.__map__.copy()
            self.__oldreserved__ = self.__reserved__.copy()
            if __n__.name not in self.__map__ and __n__.name not in self.__reserved__: self.__map__[__n__.name] = "__" + __enderman__() + "__"
            if __n__.name in self.__map__: __n__.name = self.__map__[__n__.name]
            self.__gen__(__n__)
            self.__map__ = self.__oldmap__
            self.__reserved__ = self.__oldreserved__
            return __n__
        
        def __craftlambda__(self, __n__):
            self.__oldmap__ = self.__map__.copy()
            self.__carry__(__n__.args)
            self.__gen__(__n__)
            self.__map__ = self.__oldmap__
            return __n__

        def __craftfunctiondef__(self, __n__):
            self.__oldmap__ = self.__map__.copy()
            self.__oldreserved__ = self.__reserved__.copy()
            for node in __n__.body:
                if isinstance(node, ast.Global):
                    for name in node.names: self.__reserved__.add(name)
                elif isinstance(node, ast.Nonlocal):
                    for name in node.names: self.__reserved__.add(name)
            if __n__.name not in self.__map__ and __n__.name not in self.__reserved__: self.__map__[__n__.name] = "__" + __enderman__() + "__"
            if __n__.name in self.__map__: __n__.name = self.__map__[__n__.name]
            self.__carry__(__n__.args)
            self.__gen__(__n__)
            self.__map__ = self.__oldmap__
            self.__reserved__ = self.__oldreserved__
            return __n__

        def __craftasyncfunctiondef__(self, __n__):
            self.__oldmap__ = self.__map__.copy()
            self.__oldreserved__ = self.__reserved__.copy()
            for node in __n__.body:
                if isinstance(node, ast.Global):
                    for name in node.names: self.__reserved__.add(name)
                elif isinstance(node, ast.Nonlocal):
                    for name in node.names: self.__reserved__.add(name)
            if __n__.name not in self.__map__ and __n__.name not in self.__reserved__: self.__map__[__n__.name] = "__" + __enderman__() + "__"
            if __n__.name in self.__map__: __n__.name = self.__map__[__n__.name]
            self.__carry__(__n__.args)
            self.__gen__(__n__)
            self.__map__ = self.__oldmap__
            self.__reserved__ = self.__oldreserved__
            return __n__
    return __IronGolem__().__craft__(__jungle__)

def __snowgolem__(__t__):
    class __SnowGolem__(__bedrocktransformer__):
        def __craftname__(self, __n__):
            __whitelist__ = ['print', 'sum', 'len', 'range', 'enumerate', 'zip', 'int', 'str', 'float', 'bool', 'list', 'tuple', 'dict', 'set', 'min', 'max', 'abs', 'round', 'chr', 'ord', 'hex', 'bin', 'oct', 'pow', 'isinstance', 'issubclass', 'hasattr', 'getattr', 'setattr', 'delattr', 'callable', 'type', 'id', 'hash', 'repr', 'open', 'dir', 'vars', 'locals', 'globals', 'eval', 'exec', 'compile', 'memoryview', 'bytearray', 'bytes', 'complex', 'filter', 'map', 'sorted', 'slice', 'reversed']
            if isinstance(__n__.ctx, ast.Load) and __n__.id in __whitelist__:
                 return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[ast.Constant(value='builtins')], keywords=[]), ast.Constant(value=__n__.id)], keywords=[])
            return __n__
    return __SnowGolem__().__craft__(__t__)

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
                    elif isinstance(__item__, ast.Constant) and isinstance(__item__.value, complex):__mangrove__.append(ast.parse(repr(__item__.value)).body[0].value)
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
            elif isinstance(__val__, ast.Constant) and isinstance(__val__.value, complex):setattr(__ore__, __field__, ast.parse(repr(__val__.value)).body[0].value)
            elif isinstance(__val__, ast.Constant) and isinstance(__val__.value, bytes):setattr(__ore__, __field__, ast.parse(__phantom__(__val__.value)).body[0].value)
            elif isinstance(__val__, ast.JoinedStr):pass

    for __val__, __name__ in __enderchest__.items():
        __assign__ = ast.Assign(targets=[ast.Name(id=__name__, ctx=ast.Store())], value=ast.Constant(value=__val__), lineno=None)
        __darkoak__.body.insert(0, __assign__)

    return __darkoak__

def __wither__(__t__):
    class __Wither__(__bedrocktransformer__):
        def __craft__(self, __n__):
            if isinstance(__n__, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Module)):
                self.__gen__(__n__)
                __body__ = []
                for __s__ in __n__.body:
                   if isinstance(__s__, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)): __body__.append(__s__)
                   else:
                       __body__.append(ast.Try(
                           body=[__s__],
                           handlers=[ast.ExceptHandler(type=ast.Name(id='Exception', ctx=ast.Load()), name=None, body=[ast.Pass()])],
                           orelse=[], finalbody=[]
                       ))
                __n__.body = __body__
                return __n__
            return self.__gen__(__n__)
    return __Wither__().__craft__(__t__)

def __witherskeleton__(__code__):
    try:
        __tree__ = ast.parse(__code__)
        for __n__ in ast.walk(__tree__):
            if isinstance(__n__, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef, ast.Module)):
                if __n__.body and isinstance(__n__.body[0], ast.Expr) and isinstance(__n__.body[0].value, ast.Constant) and isinstance(__n__.body[0].value.value, str):__n__.body.pop(0)
        return ast.unparse(__tree__)
    except:return __code__

def __redstonevm__(__payload__):
    import random as _r
    __spawner__ = lambda: "".join(_r.sample([chr(i) for i in range(97, 122)], k=6))
    __init__, __run__ = "__init__", __spawner__()
    __keyval__, __xorone__, __xortwo__ = _r.randint(1, 255), _r.randint(1, 255), _r.randint(1, 255)
    __rollingmul__, __rollingadd__ = 5, _r.randint(11, 99) | 1
    __logops__ = ['lx','ex','st','ad','sb','ml','rt','dp','sw','np','at','pp','rv','ck','jp','cl','sl','sr','nt','md','an','or','li','gh','d2','r3','s2','cs','mu','ab','xo','ai','si','mi']
    __allops__ = list(range(256)); _r.shuffle(__allops__); __opmap__ = {k:[] for k in __logops__}
    for i, v in enumerate(__allops__): __opmap__[__logops__[i % len(__logops__)]].append(v)
    __getop__ = lambda t: _r.choice(__opmap__[t])
    __calcops__, __cur__ = [__getop__('li'), _r.randint(1, 255)], _r.randint(1, 255)
    for _ in range(_r.randint(8, 12)):
        __op__, __fn__ = _r.choice([('ad',lambda x,y:(((x&0xFF)^(y&0xFF))+2*((x&0xFF)&(y&0xFF)))&0xFF), ('sb',lambda x,y:(((x&0xFF)^((256-y)&0xFF))+2*((x&0xFF)&((256-y)&0xFF)))&0xFF), ('ml',lambda x,y:(x*y)%256)])
        __v__ = _r.randint(1, 255)
        if __op__ in ['ad','sb','ml']: __calcops__.extend([__getop__({'ad':'ai','sb':'si','ml':'mi'}[__op__]), __v__])
        else: __calcops__.extend([__getop__('li'), __v__, __getop__(__op__)])
        __cur__ = __fn__(__cur__, __v__)
        __calcops__.extend([__getop__('np'), __getop__('li'), _r.randint(1, 255), __getop__('pp'), __getop__('gh')])
    __calcops__.extend([__getop__('li'), (__keyval__ - __cur__) % 256, __getop__('ad'), __getop__('st')])
    __calcops__.extend([__getop__(x) for x in ['at','np','lx','dp','pp','at','at','ck','ex']])
    __rkseed__, __rkmult__, __rkadd__ = _r.randint(1000, 9999), _r.randint(100, 999) | 1, _r.randint(100, 999)
    __encbc__ = [b ^ ((__rkseed__ + i * __rkmult__ + __rkadd__) & 0xFF) for i, b in enumerate(__calcops__)]
    __encpayload__, __ck__ = [], __keyval__
    for c in __payload__:
        __encpayload__.append(ord(c) ^ __ck__ ^ __xorone__ ^ __xortwo__)
        __ck__ = (__ck__ * __rollingmul__ + __rollingadd__) % 256
    __m__ = {
        '__lx__': f'self.s.append({__encpayload__});t=[];\n  for x in self.s.pop():t.append(chr(((x^self.m[0])^self.x1)^self.x2));self.m[0]=(self.m[0]*self.rm+self.ra)%256\n  self.s.append("".join(t))',
        '__ex__': 'exec(self.s.pop(),globals())',
        '__st__': 'self.m[0]=self.s.pop()&0xFF',
        '__ad__': 'b=self.s.pop();a=self.s.pop();self.s.append((((a&0xFF)^(b&0xFF))+2*((a&0xFF)&(b&0xFF)))&0xFF)',
        '__sb__': 'b=self.s.pop();a=self.s.pop();nb=(256-b)&0xFF;self.s.append((((a&0xFF)^nb)+2*((a&0xFF)&nb))&0xFF)',
        '__ml__': 'b=self.s.pop();a=self.s.pop();self.s.append((a*b)%256)',
        '__rt__': 'self.s.insert(0,self.s.pop())if len(self.s)>1 else None',
        '__dp__': 'self.s.append(self.s[-1])if self.s else None',
        '__sw__': 'self.s[-1],self.s[-2]=self.s[-2],self.s[-1]',
        '__np__': 'pass',
        '__at__': "try:getattr(__import__('ctypes').windll.kernel32,'IsDebuggerPresent')() and __import__('os')._exit(1)\n  except:pass",
        '__pp__': 'self.s.pop()if self.s else None',
        '__rv__': 'self.s.reverse()',
        '__ck__': 'pass',
        '__jp__': 'self.p+=self.s.pop()',
        '__cl__': 'self.s.clear()',
        '__sl__': 'b=self.s.pop();a=self.s.pop();self.s.append(a<<b)',
        '__sr__': 'b=self.s.pop();a=self.s.pop();self.s.append(a>>b)',
        '__nt__': 'self.s.append(not self.s.pop())',
        '__md__': 'b=self.s.pop();a=self.s.pop();self.s.append(a%b)',
        '__an__': 'b=self.s.pop();a=self.s.pop();self.s.append(a&b)',
        '__or__': 'b=self.s.pop();a=self.s.pop();self.s.append(a|b)',
        '__li__': f'x=0 if self.p>=len(self.c) else (self.c[self.p]^((self.dk[0]+self.p*{__rkmult__}+{__rkadd__})&0xFF))&0xFF;self.p+=1;self.s.append(x)',
        '__gh__': 'self.s.insert(len(self.s)//2,0);self.s.pop(0)',
        '__d2__': 'self.s.extend(self.s[-2:])if len(self.s)>=2 else None',
        '__r3__': 'self.s[-3],self.s[-2],self.s[-1]=self.s[-1],self.s[-3],self.s[-2] if len(self.s)>=3 else None',
        '__s2__': 'self.s[-4],self.s[-3],self.s[-2],self.s[-1]=self.s[-2],self.s[-1],self.s[-4],self.s[-3] if len(self.s)>=4 else None',
        '__cs__': 'tc=sum(self.s)&0xFFFF;self.s.append(tc&0xFF);self.s.append((tc>>8)&0xFF)',
        '__mu__': 'pass',
        '__ab__': f'self.s.append({_r.randint(1,255)})',
        '__xo__': 'b=self.s.pop();a=self.s.pop();self.s.append(a^b)',
        '__ai__': f'v=0 if self.p>=len(self.c) else (self.c[self.p]^((self.dk[0]+self.p*{__rkmult__}+{__rkadd__})&0xFF))&0xFF;self.p+=1;a=self.s.pop();self.s.append((((a&0xFF)^(v&0xFF))+2*((a&0xFF)&(v&0xFF)))&0xFF)',
        '__si__': f'v=0 if self.p>=len(self.c) else (self.c[self.p]^((self.dk[0]+self.p*{__rkmult__}+{__rkadd__})&0xFF))&0xFF;self.p+=1;a=self.s.pop();nb=(256-v)&0xFF;self.s.append((((a&0xFF)^nb)+2*((a&0xFF)&nb))&0xFF)',
        '__mi__': f'v=0 if self.p>=len(self.c) else (self.c[self.p]^((self.dk[0]+self.p*{__rkmult__}+{__rkadd__})&0xFF))&0xFF;self.p+=1;a=self.s.pop();self.s.append((a*v)%256)'
    }
    __tower__ = __spawner__()
    __vmsrc__ = f"import sys\nimport os\nclass {__tower__}:\n    def {__init__}(self):self.s=[];self.m=[0];self.k=[{__keyval__}];self.x1={__xorone__};self.x2={__xortwo__};self.rm={__rollingmul__};self.ra={__rollingadd__}\n"
    for k, v in __m__.items():
        __body__ = "\n".join(f"        {__line__}" for __line__ in v.split("\n"))
        __vmsrc__ += f"    def {k}(self):\n{__body__}\n"
    __vmsrc__ += f"    def {__run__}(self,c):\n        self.c=c;self.p=0;self.dk=[{__rkseed__}];m={{}}\n"
    for t in __logops__:
        for o in __opmap__[t]: __vmsrc__ += f"        m[{o}]=self.__{t}__\n"
    __vmsrc__ += f"        while self.p<len(self.c):op=(self.c[self.p]^((self.dk[0]+self.p*{__rkmult__}+{__rkadd__})&0xFF))&0xFF;self.p+=1;m.get(op,self.__np__)()\n{__tower__.replace('__','')}().{__run__}({__encbc__})"
    return __vmsrc__

def __theend__():
    try:
        if len(sys.argv) > 1:
            __stronghold__ = sys.argv[1]
            if os.path.exists(__stronghold__):
                with open(__stronghold__, 'r', encoding='utf-8') as f:__enchantmenttable__ = f.read()
                __enchantmenttable__ = __witherskeleton__(__enchantmenttable__)
                __bedrock__ = ast.parse(__enchantmenttable__)
                __bedrock__ = __chest__(__bedrock__)
                __bedrock__ = __obsidian__(__bedrock__)
                __bedrock__ = __snowgolem__(__bedrock__)
                __bedrock__ = __elytra__(__bedrock__)
                __bedrock__ = __basalt__(__bedrock__)
                __bedrock__ = __tnt__(__bedrock__)
                __bedrock__ = __firecharge__(__bedrock__)
                __bedrock__ = __glowberry__(__bedrock__)
                __bedrock__ = __sculk__(__bedrock__)
                __bedrock__ = __dripleaf__(__bedrock__)
                __bedrock__ = __breeze__(__bedrock__)
                __bedrock__ = __villager__(__bedrock__)
                __bedrock__ = __wither__(__bedrock__)

                __dragonbreath__ = ""
                for __h__ in [__nhincaigimanhin__, __xinvaicut__, __toolnhindepko__]:
                    __dragonbreath__ += inspect.getsource(__h__) + "\n"
                
                __bedrock__.body.insert(0, ast.parse(__dragonbreath__))
                ast.fix_missing_locations(__bedrock__)
                
                __chorusfruit__ = ast.unparse(__bedrock__)
                __vmfinal__ = __redstonevm__(__chorusfruit__)

                __endcity__ = os.path.splitext(__stronghold__)[0] + "_obf.py"
                with open(__endcity__, 'w', encoding='utf-8') as f:f.write(__vmfinal__)
                __vailon__(f"Successfully obfuscated {__stronghold__} -> {__endcity__}")
            else:__vailon__(f"File not found: {__stronghold__}")
        else:__vailon__("Usage: python bedrock.py <file>")
    except Exception as __e__:
        import traceback
        traceback.print_exc()
        __vailon__(f"Error: {__e__}")
        sys.exit(1)

if __name__ == "__main__":__theend__()
