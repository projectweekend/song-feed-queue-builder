import os
from datetime import date
from pika_pack import Sender
from lib import database


DOCKER_MONGO_IP_PORT = '{0}:{1}'.format(
    os.getenv('DB_PORT_27017_TCP_ADDR'),
    os.getenv('DB_PORT_27017_TCP_PORT'))
MONGO_URL = os.getenv('MONGO_URL', 'mongodb://{0}/test'.format(DOCKER_MONGO_IP_PORT))
DOCKER_RABBIT_IP_PORT = '{0}:{1}'.format(
    os.getenv('RABBIT_PORT_5672_TCP_ADDR'),
    os.getenv('RABBIT_PORT_5672_TCP_PORT'))
RABBIT_URL = os.getenv('RABBIT_URL', 'amqp://{0}/'.format(DOCKER_RABBIT_IP_PORT))


def main():
    sender = Sender(RABBIT_URL, 'song-feed')
    db = database.connect(MONGO_URL)
    query = {
        'last_processed': {
            '$ne': date.isoformat(date.today())
        }
    }
    playlists = db.playlists.find(query)
    for playlist in playlists:
        sender.send('song-feed', playlist)


if __name__ == '__main__':
    main()
