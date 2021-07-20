#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from login import *
from spotify import *

def heeelp():
        print('''
   ---------------------------------------
   |                                     |
   |             SPOTIFY-CLI             |
   |                                     |
   | Command line interface for spotify. |
   |    Written by Utku Baris Selcuk.    |
   |                                     |
   | Arguments:                          |
   |                                     |
   | h             | shows help          |
   | help          | message             |
   |-------------------------------------|
   | next          | skips to            |
   | n             | next track          |
   |-------------------------------------|
   | b             | returns to          |
   | back          | previous            |
   | prev          | track               |
   |-------------------------------------|
   | d             | shows the currently |
   | device        | active device       |
   | devices       | and user            |
   |-------------------------------------|
   | r             | track repeat        |
   | repeat        | options             |
   |-------------------------------------|
   | v             | changes the volume  |
   | volume        | from 1 to 100       |
   |-------------------------------------|
   | np            | shows the track     |
   | now playing   | and the artist      |
   |-------------------------------------|
   | s             | pauses the track    |
   | stop          | if the track        |
   | pause         | is playing          |
   |-------------------------------------|
   | p             | starts the track    |
   | play          | if the track        |
   | start         | is stopped          |
   |-------------------------------------|
   | cu            | shows user          |
   | current user  | information         |
   |-------------------------------------|
   | !du           | deletes user        |
   | delete user   | information         |
   |-------------------------------------|
   | !ci           | changes             |
   | client id     | client id           |
   |-------------------------------------|
   | !cs           | changes             |
   | client secret | client secret       |
   |-------------------------------------|
   | !ru           | changes             |
   | redirect uri  | redirect uri        |
   |-------------------------------------|
   | !u            | changes             |
   | username      | username            |
   |-------------------------------------|
   |                                     |
   |  For more detailed information,     |
   |  you can visit the github page.     |
   |                                     |
   |  github.com/ubselcuk/spotify-cli    |
   |                                     |
   ---------------------------------------
            ''')



if __name__ == "__main__":





    if (
        sys.argv[1] == 'help' or
        sys.argv[1] == 'h'
        ):
        heeelp()

    elif(
        sys.argv[1] == 'next' or
        sys.argv[1] == 'n'
        ):
        next()

    elif(
        sys.argv[1] == 'prev' or
        sys.argv[1] == 'back' or
        sys.argv[1] == 'b'
        ):
        prev()

    elif(
        sys.argv[1] == 'device' or
        sys.argv[1] == 'devices' or
        sys.argv[1] == 'd'
        ):
        device()

    elif(
        sys.argv[1] == 'repeat' or
        sys.argv[1] == 'r'
        ):
        try:
            repeat(sys.argv[2])
        except:
            print('Try again by selecting one of the options.\nOptions: track, context, off')

    elif(
        sys.argv[1] == 'volume' or
        sys.argv[1] == 'v'
        ):
        volume(int(sys.argv[2]))

    elif((
        sys.argv[1] == 'now' and
        sys.argv[2] == 'playing') or
        sys.argv[1] == 'np'
        ):
        now_playing()

    elif(
        sys.argv[1] == 'stop' or
        sys.argv[1] == 'pause' or
        sys.argv[1] == 's'
        ):
        pause()

    elif(
        sys.argv[1] == 'play' or
        sys.argv[1] == 'start' or
        sys.argv[1] == 'p'
        ):
        start()

    elif((
        sys.argv[1] == 'current' and
        sys.argv[2] == 'user') or
        sys.argv[1] == 'cu'
        ):
        current_user()

    elif((
        sys.argv[1] == 'delete' and
        sys.argv[2] == 'user') or
        sys.argv[1] == '!du'
        ):
        delete_user()

    elif((
        sys.argv[1] == 'client' and
        sys.argv[2] == 'id') or
        sys.argv[1] == '!ci'
        ):
        client_id(sys.argv[3])

    elif((
        sys.argv[1] == 'client' and
        sys.argv[2] == 'secret') or
        sys.argv[1] == '!cs'
        ):
        client_secret(sys.argv[3])

    elif((
        sys.argv[1] == 'redirect' and
        sys.argv[2] == 'uri') or
        sys.argv[1] == '!ru'
        ):
        redirect_uri(sys.argv[3])

    elif(
        sys.argv[1] == 'username' or
        sys.argv[1] == '!u'
        ):
        username(sys.argv[2])

    else:
        print('pls use help')


    