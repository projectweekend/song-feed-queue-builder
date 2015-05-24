import json
from datetime import date
from boto import sqs
from boto.dynamodb2.table import Table


def accounts_to_process(target_date):
    accounts = Table('accounts')
    attributes = ('spotify_username', )
    return accounts.scan(attributes=attributes)


def playlists_queue():
    conn = sqs.connect_to_region('us-east-1')
    return conn.create_queue('song-feed-playlists-to-process')


def main():
    date_to_process = date.isoformat(date.today())
    q = playlists_queue()
    for playlist in accounts_to_process(date_to_process):
        data = dict(playlist.items())
        q.write(q.new_message(body=json.dumps(data)))


if __name__ == '__main__':
    main()
