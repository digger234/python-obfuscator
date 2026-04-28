# Quy tắc làm rối code cho Aegis Obfuscator

## Tận dụng hàm λ (凱\_.λ)

- **QUAN TRỌNG**: Khi nói "lambda" tức là hàm `λ` (凱\_.λ), KHÔNG PHẢI keyword `lambda` của Python
- Hàm `λ` tạo ra nested lambda wrapper rất mạnh, khó reverse
- Phải sử dụng `L=凱_.λ` rồi gọi `{L()}` hoặc `{L(v=f'...')}`

> [!CAUTION] > **KHÔNG được spam L() calls** trong opaque/dead/霧 int - sẽ gây chậm với file lớn!
> Chỗ dùng L() nhiều nhất là: junk, chaos, protect, anti, bypass, shield, state

## Tận dụng Unicode (hàm α)

- Hàm `α` (凱\_.α) tạo tên biến random unicode
- Dùng `_=凱_.α` rồi gọi `_()` để tạo tên biến
- Unicode string spam: `sp=''.join(chr(r.randint(0x4e00,0x9fff))for _ in range(n))`
- `霧` - String obfuscation với XOR layers
- `霧int` - Integer obfuscation

## Phân biệt các nhóm hàm

- `junk` (闘) - Code rác KHÔNG chạy, chỉ làm nhiễu
- `chaos` (魔) - Code CÓ chạy nhưng không ảnh hưởng kết quả
- `protect` (鎧) - Bảo vệ code khỏi bị phân tích
- `anti` (凰) - Chống debug, VM, analysis tools
- `bypass` (鏡) - Chống decompiler, bypass tools
- `shield` (盾) - Bảo vệ các protection functions
- `state` (態) - Control flow flattening
