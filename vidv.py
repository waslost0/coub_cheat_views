import aiohttp
import asyncio
import random
import sys
import argparse
import re
import time

CONFIG = {
    'url': '',
    'threads': 50
}


class CheatVideoViews:
    def __init__(self):
        self.requestCount = 0
        self.startTime = time.time()

    @staticmethod
    async def request_increment_view_count():
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(f"https://coub.com/coubs/{CONFIG['url']}/increment_views?player=html5&type=site&platform=desktop",data={
                    "player":"html5",
                    "type": "site",
                    "platform":"desktop"                    
                    }, headers={
                    "cookie": '',
                    "user-agent": f'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/{(random.random() * 600)}.36 (KHTML, like Gecko) Chrome/{(random.random() * 59)}.0.3029.110 Safari/${(random.random() * 1000)}.36',
                    "sec-fetch-mode": "cors",
                    "referer": "https://vk.com",
                    "X-Requested-With": "XMLHttpRequest",
                    "content-type": "application/x-www-form-urlencoded"
                }) as response:
                    
                    return response
                   
        except Exception as e:
            print(e)

    async def start(self):
        while True:
            response = await self.request_increment_view_count()
            print(
                f" Time from start: {int(time.time() - self.startTime)}  Requests counts: {self.requestCount}")
            self.requestCount = self.requestCount + 1
            await asyncio.sleep(random.randrange(0, 2))


async def asynchronous():
    script = CheatVideoViews()
    tasks = [asyncio.ensure_future(script.start()) for i in range(0, int(CONFIG['threads']))]
    await asyncio.wait(tasks)

def get_uid_vid(url):
    try:
       
        match = re.findall('view/(.+)', str(url))
   
        CONFIG['url'] =  str(match[0])
        print(CONFIG)
    except IndexError as e:
        print('Invalid input')
        raise e


def main():
    ioloop = asyncio.get_event_loop()
    print('Asynchronous:')
    ioloop.run_until_complete(asynchronous())
    ioloop.close()

def get_threads(threads):
    CONFIG['threads'] = threads



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='VidViews')
    parser.add_argument('-t', '--threads', type=int, help='Threads count\n -t 50')
    parser.add_argument('-u', '--url', type=str, help='Url\n -u https://coub.com/view/28uyg0')

    args = parser.parse_args()


    try:
        if args.threads:
            get_threads(args.threads)
        get_uid_vid(args.url)
        main()
    except Exception as e:
        print('URL is required.\n')
        print(e)
    print('\nInput example: vidv.py -u https://coub.com/view/28uyg0 -t 100')


