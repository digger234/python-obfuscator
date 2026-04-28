import requests, time, datetime, os, json

os.system("cls" if os.name == "nt" else "clear")
key = input("Nhập Key: ")
link = input("Link Profile: ")
delay = int(input("Nhập Delay (Nên để 180s): "))

def followtiktok(key, link):
    cookies = {
        '_gcl_au': '1.1.1794597456.1762092614',
        '_ga': 'GA1.1.1400119809.1762092615',
        'cf_clearance': '9qndrLtVGgyZ2qd_TejUcVml2zm_yri3fzEj5x_7EA8-1763531239-1.2.1.1-Ezq_affxUIevmP7OMWTDZB9ISUH0_RfrKXJcM0FeqOR0f3p.KSQ3RzgUHaJ0UD5P2mmbEwdZGBqwJfFYw1dATSlGa1XvLESJnFbW8q4KFDYyP_W5bclFvHmHUH6hXDS7GoexYtPRQ7Z8CCFgYsb6WWT3B9LbpF8CpiSLTZ7RkjQfYdD3lQGwFkV9GFJiCO5VvskQRdXpIojtLwSa.CDRI1ikzRFOwMg.CycXgSukty4',
        '_ga_PVY0H7ZJP0': 'GS2.1.s1763531241$o5$g1$t1763531410$j14$l0$h0',
        'XSRF-TOKEN': 'eyJpdiI6IktvT0UrcVl3REcrdmorMlVaVGRGRFE9PSIsInZhbHVlIjoib2FQVUpsQVlVOFBacXRIa2crdWJRdUhrTzNFSjZRclB0ZlNFM2lTMlQ2ckVINitJSXhXZHRKd05YZmw5QWVaMmpmRHdqZ0grNm5EYjJua0s1TE1JWFg5WEh3NThjbm9PSjUxVU5ENHVzeWlUVjNxZ1NiS29EMTVMR0FpNDFZWmUiLCJtYWMiOiIyOTQ5ZTZhYTU0MGFlZjBjM2NjNTI3ZDQ1MjViZDE1ZGY5MDdhODVlNWJiYTlmOWEzYTg4Y2ZiMzAxZWVlMThkIiwidGFnIjoiIn0%3D',
        'likevn_session': 'eyJpdiI6Ill5djlFcXVaQndaZWZvV09OWTlFekE9PSIsInZhbHVlIjoiS3lJVG1uZUMvMlhtSm92Q0NHWUVDSkYvOE5wdG8rY0FTL1ZRVzRSUmRpbzBmaHhucDlmL21NYkVwUi94Y1BEWmRNMnFBSjMrcjA5S1NDZmM1c1pmQm9VYTl4VTkzTklVZ0RMaVF0dE84Z2VQMyt3RXlkUTZaRGV2aFg4NVN3NXEiLCJtYWMiOiJlNmI3ODgxM2E0Yjc5ZWI4Mzg5ODY0YmRkOTE2ZDNiMjBmYjA3OTM4MzZjMjZkZGZlNDZmMjMzNzJiMGRjNDVjIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'api-token': key,
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://like.vn',
        'priority': 'u=1, i',
        'referer': 'https://like.vn/mua-follow-tiktok',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'x-csrf-token': 'JgV9XdHzjN9y3sns4WPk5GLow3OCD9wOrCqxUBo2',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': '_gcl_au=1.1.1794597456.1762092614; _ga=GA1.1.1400119809.1762092615; cf_clearance=9qndrLtVGgyZ2qd_TejUcVml2zm_yri3fzEj5x_7EA8-1763531239-1.2.1.1-Ezq_affxUIevmP7OMWTDZB9ISUH0_RfrKXJcM0FeqOR0f3p.KSQ3RzgUHaJ0UD5P2mmbEwdZGBqwJfFYw1dATSlGa1XvLESJnFbW8q4KFDYyP_W5bclFvHmHUH6hXDS7GoexYtPRQ7Z8CCFgYsb6WWT3B9LbpF8CpiSLTZ7RkjQfYdD3lQGwFkV9GFJiCO5VvskQRdXpIojtLwSa.CDRI1ikzRFOwMg.CycXgSukty4; _ga_PVY0H7ZJP0=GS2.1.s1763531241$o5$g1$t1763531410$j14$l0$h0; XSRF-TOKEN=eyJpdiI6IktvT0UrcVl3REcrdmorMlVaVGRGRFE9PSIsInZhbHVlIjoib2FQVUpsQVlVOFBacXRIa2crdWJRdUhrTzNFSjZRclB0ZlNFM2lTMlQ2ckVINitJSXhXZHRKd05YZmw5QWVaMmpmRHdqZ0grNm5EYjJua0s1TE1JWFg5WEh3NThjbm9PSjUxVU5ENHVzeWlUVjNxZ1NiS29EMTVMR0FpNDFZWmUiLCJtYWMiOiIyOTQ5ZTZhYTU0MGFlZjBjM2NjNTI3ZDQ1MjViZDE1ZGY5MDdhODVlNWJiYTlmOWEzYTg4Y2ZiMzAxZWVlMThkIiwidGFnIjoiIn0%3D; likevn_session=eyJpdiI6Ill5djlFcXVaQndaZWZvV09OWTlFekE9PSIsInZhbHVlIjoiS3lJVG1uZUMvMlhtSm92Q0NHWUVDSkYvOE5wdG8rY0FTL1ZRVzRSUmRpbzBmaHhucDlmL21NYkVwUi94Y1BEWmRNMnFBSjMrcjA5S1NDZmM1c1pmQm9VYTl4VTkzTklVZ0RMaVF0dE84Z2VQMyt3RXlkUTZaRGV2aFg4NVN3NXEiLCJtYWMiOiJlNmI3ODgxM2E0Yjc5ZWI4Mzg5ODY0YmRkOTE2ZDNiMjBmYjA3OTM4MzZjMjZkZGZlNDZmMjMzNzJiMGRjNDVjIiwidGFnIjoiIn0%3D',
    }

    data = {
        'objectId': link,
        'server_order': '6',
        'free': '1',
        'giftcode': '',
        'amount': '10',
        'note': '',
    }

    response = requests.post('https://like.vn/api/mua-follow-tiktok/order', cookies=cookies, headers=headers, data=data)
    return response

start = time.time()
os.system("cls" if os.name == "nt" else "clear")
print("Bắt đầu chạy.. Nhấn Ctrl + C để dừng nha bấy bề <3\n")

try:
    while True:
        resp = followtiktok(key, link)
        print("\n-------------------------------")
        print("Thời gian:", datetime.datetime.now())
        print("Status:", resp.status_code)
        try:
            parsed = json.loads(resp.text)
            print("Response:", json.dumps(parsed, ensure_ascii=False))
        except:
            print("Response:", resp.text)
        print("-------------------------------\n")
        elapsed = int(time.time() - start)
        print("Đã chạy:", str(datetime.timedelta(seconds=elapsed)))
        time.sleep(delay)

except KeyboardInterrupt:
    print("\nĐã dừng rồi!")