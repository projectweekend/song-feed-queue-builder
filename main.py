import json
from datetime import date
from boto import sqs
from boto.dynamodb2.table import Table


def playlists_to_process():
    accounts = Table('accounts')
    target_date = date.isoformat(date.today())
    return accounts.scan(last_processed__ne=target_date)


def playlists_queue():
    conn = sqs.connect_to_region('us-east-1')
    return conn.create_queue('song-feed-playlists-to-process')


def main():
    q = playlists_queue()
    for playlist in playlists_to_process():
        body = json.dumps(dict(playlist.items()))
        print(body)
        q.write(q.new_message(body=body))


if __name__ == '__main__':
    main()
