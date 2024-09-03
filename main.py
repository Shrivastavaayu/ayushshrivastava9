#decode 001.sec contact any decode script +919958790640
import requests
import os
import re
import sys
import time
import json
import http.server
import socketserver
import threading
from requests.exceptions import RequestException

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'   MR MAFIYA INXIDE')

def execute_server():
    PORT = int(os.environ.get('PORT', 4000))
    with socketserver.TCPServer(('', PORT), MyHandler) as httpd:
        print(f'Server running at http://localhost:{PORT}')
        httpd.serve_forever()

def validate_password():
    print('[[>]] ===================M4FIY4=S3RV3R=RUNNING===================')
    with open('password.txt', 'r') as file:
        password = file.read().strip()

    try:
        pwd = requests.get('https://pastebin.com/raw/wEiJXrN3').text.strip()
    except RequestException as e:
        print(f'[!] Error fetching password: {e}')
        sys.exit()

    if pwd != password:
        print('Password Has Been Changed By Author..!! Please Contact Script Author Mafiya... !! Thank You..')
        sys.exit()

def read_cookie(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f'File Not Found! Please Enter Valid File: {file_path}')
        return None

def make_request(url, headers, cookie):
    try:
        response = requests.get(url, headers=headers, cookies={'Cookie': cookie})
        return response.text
    except RequestException as e:
        print(f'[!] Error making request: {e}')
        return None

def mafiya():
    cookies_data = read_cookie('cookie.txt')
    if not cookies_data:
        return

    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 '
            'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
        )
    }

    valid_cookies = []

    for cookie in cookies_data:
        response = make_request('https://business.facebook.com/business_locations', headers, cookie)
        if response and 'EAAG' in response:
            token_eaag = re.search(r'(EAAG\w+)', response)
            if token_eaag:
                valid_cookies.append((cookie, token_eaag.group(1)))

    if not valid_cookies:
        print('[!] No valid cookie found. Exiting...')
        return

    id_post = int(open('post.txt').readline().strip())
    commenter_name = open('name.txt').readline().strip()
    delay = int(open('speed.txt').readline().strip())
    comments = open('file.txt', 'r').readlines()

    x, cookie_index = 0, 0

    while True:
        try:
            time.sleep(delay)
            comment = comments[x].strip()
            comment_with_name = f'{commenter_name}: {comment}'
            current_cookie, token_eaag = valid_cookies[cookie_index]

            data = {'message': comment_with_name, 'access_token': token_eaag}
            response2 = requests.post(
                f'https://graph.facebook.com/{id_post}/comments/', 
                data=data, 
                cookies={'Cookie': current_cookie}
            ).json()

            current_time = time.strftime('%Y-%m-%d %I:%M:%S %p')

            if 'id' in response2:
                print(f'Post id: {id_post}')
                print(f'  - Time: {current_time}')
                print(f'COOKIE NUMBER: {cookie_index + 1}')
                print(f'Comment sent: {comment_with_name}')
                x = (x + 1) % len(comments)
                cookie_index = (cookie_index + 1) % len(valid_cookies)
            else:
                print(f'[!] Status: Failure')
                print(f'COOKIE NUMBER: {cookie_index + 1}')
                print(f'Link: https://m.basic.facebook.com/{id_post}')
                print(f'Comments: {comment_with_name}\n')
                x = (x + 1) % len(comments)
                cookie_index = (cookie_index + 1) % len(valid_cookies)

        except RequestException as e:
            print(f'[!] Error making request: {e}')
            time.sleep(5.5)
        except Exception as e:
            print(f'[!] An unexpected error occurred: {e}')
            break

def main():
    validate_password()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    mafiya()

if __name__ == '__main__':
    main()
