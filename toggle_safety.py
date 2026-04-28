import os, sys

home = os.path.expanduser('~')
key_file = os.path.join(home, '.aegis_owner')

def toggle():
    if os.path.exists(key_file):
        try:
            os.remove(key_file)
            print(f"[-] ĐÃ TẮT CHẾ ĐỘ AN TOÀN. Đã xóa file khóa: {key_file}")
            print("(!) CẨN THẬN! Code bị obfuscate có thể NỔ (BOMB) máy bạn bây giờ.")
        except Exception as e:
            print(f"[!] Lỗi khi xóa file: {e}")
    else:
        try:
            with open(key_file, 'w') as f:
                f.write('AEGIS OWNER KEY - DO NOT SHARE')
            print(f"[+] ĐÃ BẬT CHẾ ĐỘ AN TOÀN. Đã tạo file khóa: {key_file}")
            print("(*) Bạn đã an toàn 100% trước bom của chính mình.")
        except Exception as e:
            print(f"[!] Lỗi khi tạo file: {e}")

if __name__ == "__main__":
    toggle()
    input("\nẤn Enter để thoát...")
