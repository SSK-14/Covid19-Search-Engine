"""
Script to format data into .I .T .W
"""
from  data.local_news_data.crawler.utils import clean_raw, clean_search_crawl, process_jsonl


def main():
    # CBS Baltimore
    df = process_jsonl(filename='data/local_news_data/jsonloutput/cbs/2021-10-12T06-30-03-cbs.jsonl')
    df.to_csv('data/local_news_data/cbs/baltimore.cbslocal.csv', index=False)
    clean_raw(path='data/local_news_data/cbs', filename='baltimore.cbslocal.csv', new_filename='CBS.ALL')

    # WBALTV
    df = process_jsonl(filename='data/local_news_data/jsonloutput/wbaltv/2021-09-28T05-01-44-wbaltv.jsonl')
    df.to_csv('data/local_news_data/wbaltv/wbaltv.csv', index=False)
    clean_raw(path='data/local_news_data/wbaltv', filename='wbaltv.csv', new_filename='WBALTV.ALL')

    # Baltimore Sun
    clean_search_crawl(path='data/local_news_data/baltimore_sun', filename='baltimore.sun.csv',
                       new_filename='BALTIMORE_SUN.ALL')


if __name__ == '__main__':
    main()
