import json
from datetime import date
from boto import sqs
from boto.dynamodb2.table import Table


def playlists_to_process(target_date):
    accounts = Table('accounts')
    attributes = ('spotify_username', 'spotify_playlist_id', )
    return accounts.scan(last_processed__ne=target_date, attributes=attributes)


def playlists_queue():
    conn = sqs.connect_to_region('us-east-1')
    return conn.create_queue('song-feed-playlists-to-process')


def main():
    date_to_process = date.isoformat(date.today())
    q = playlists_queue()
    for playlist in playlists_to_process(date_to_process):
        data = dict(playlist.items())
        body = json.dumps({
            'spotify_username': data['spotify_username'],
            'date_to_process': date_to_process
        })
        q.write(q.new_message(body=body))


if __name__ == '__main__':
    main()
