import requests
from django.test import TestCase

# Create your tests here.


if __name__ == '__main__':
    print('hello')
    node_map = {
        "node_memory_MemTotal": "内存大小",
    }

    res = requests.get('http://1.116.151.44:9100/metrics')
    if res.status_code == 200:
        lines = str(res.text).split('\n')
        print(len(lines))
        for l in lines:
            if str(l).find('node_memory') > -1:
                print(l)

    else:
        print(res.status_code)
