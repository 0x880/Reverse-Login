import requests
from Reverse_Data import Hash_Data

class Login:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-EG,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5,fr;q=0.4',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://trade.topbos.com',
            'Pragma': 'no-cache',
            'Referer': 'https://trade.topbos.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }

    def Req(self):
        Hash = Hash_Data().Data_Login()
        print(Hash)

        data = 'v=' +Hash+ ''

        r = requests.post('https://trade.topbos.com/trade/pwdLogin', headers=self.headers, data=data).text
        print(r);print("Login Done")



Login().Req()