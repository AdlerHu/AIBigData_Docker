import requests
import pandas as pd
import datetime


def crawl():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.132 Safari/537.36'}
    url = 'https://www.taifex.com.tw/cht/3/dailyFXRate'
    ss = requests.session()

    today = str(datetime.date.today()).replace('-', '/')

    data = {'queryStartDate': '2020/01/01', 'queryEndDate': today}

    resp = ss.post(url, headers=headers, data=data)

    df = pd.read_html(resp.text)[2]
    tmp_list = df['日期']
    date_list = []
    exchange_rate_list = df['美元／新台幣']

    for date in tmp_list:
        date_list.append(date.replace('/', '-'))

    return date_list, exchange_rate_list


def main():

    date_list, exchange_rate_list = crawl()

    for i in range(len(exchange_rate_list)):
        print('%s, %4.2f' % (date_list[i], exchange_rate_list[i]))


if __name__ == '__main__':
    main()
