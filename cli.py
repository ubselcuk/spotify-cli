from login import *
from spotify import *
import argparse

parser = argparse.ArgumentParser(
    prog='spotify-cli',
    description='Command line interface for spotify.',
    epilog='Sorularınızı yazabilirsiniz',
    add_help=False)

parser.add_argument('-h','--help',  action='store_true')

parser.add_argument('-n', '--next', action='store_true', help='next song')
parser.add_argument('-b', '--prev', action='store_true')
parser.add_argument('-d', '--device', action='store_true')
parser.add_argument('-r', '--repeat', type=str, metavar='')
parser.add_argument('-v', '--volume', type=int, metavar='')
parser.add_argument('-i', '--now_playing', action='store_true')
parser.add_argument('-s', '--stop', '--pause', action='store_true')
parser.add_argument('-p', '--play', '--start',  action='store_true')

parser.add_argument('--current_user', action='store_true')
parser.add_argument('--delete_user',  action='store_true')
parser.add_argument('--client_id',  type=str, metavar='')
parser.add_argument('--client_secret',  type=str, metavar='')
parser.add_argument('--redirect_uri',  type=str, metavar='')
parser.add_argument('--username',  type=str, metavar='')

args = parser.parse_args()

if args.help:
    print('Command line interface for spotify.')

elif args.next:
    next()
elif args.prev:
    prev()
elif args.device:
    device()
elif args.repeat:
    repeat(args.repeat)
elif args.volume:
    volume(args.volume)
elif args.now_playing:
    now_playing()
elif args.stop:
    pause()
elif args.play:
    start()

elif args.current_user:
    current_user()
elif args.delete_user:
    delete_user()
elif args.client_id:
    client_id(args.client_id)
elif args.client_secret:
    client_secret(args.client_secret)
elif args.redirect_uri:
    redirect_uri(args.redirect_uri)
elif args.username:
    username(args.username)