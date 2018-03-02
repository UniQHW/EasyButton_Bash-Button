# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Author       : Patrick Pedersen <ctx.xda@gmail.com>

import os
import serial
import argparse
import configparser

from pathlib import Path

class Event:
    def __init__(self, event_section):

        try:
            self.sig = event_section['sig'];

        except KeyError:
            print("ERROR")
            print("--------------------------------------------------------------------")
            print("Bash Button: sig property not provided for: " + event_section.name)
            print("--------------------------------------------------------------------")

        try:
            if 'cmd' in event_section:
                self.cmd = event_section['cmd']
            else:
                self.cmd = "bash " + event_section['script']

        except KeyError:
            print("ERROR")
            print("--------------------------------------------------------------------")
            print("Bash Button: cmd or script property not provided for: " + event_section.name)
            print("--------------------------------------------------------------------")

        if 'print' in event_section:
            self.show_output = bool(event_section['print'])

class Handler:
    def __init__(self):
        self.events = []

    def addEvent(self, event):
        self.events.append(event)

    def handle(self, sig):
        for event in self.events:
            if event.sig == sig:
                process = os.popen(event.cmd)
                if event.show_output:
                    stdout = process.read().strip()
                    print(stdout)
                    process.close()

## ENTRY POINT ##
def main():
    # Args
    parser = argparse.ArgumentParser(description="Bootstrap bash scripts to your Easy Button!")
    parser.add_argument('-c', help="Configuration file", default=str(Path.home()) + "/.config/bash-button/bash-button.cfg")
    args = parser.parse_args()

    # Read configuration file
    cfg = configparser.ConfigParser()
    cfg.read(args.c)
    cfg.sections()

    tty = None
    handler = Handler()

    for section in cfg.sections():

        # Set TTY Path
        if not tty and section == "device":
            try:
                tty = cfg['device']['tty']

            except KeyError:
                print("ERROR")
                print("--------------------------------------------------------------------")
                print("Bash Button: No tty specified!")
                print("--------------------------------------------------------------------")

        # Add event to handler
        elif "event_" in section[0:6]:
            handler.addEvent(Event(cfg[section]))

        # Unknown section
        else:
            print("ERROR")
            print("--------------------------------------------------------------------")
            print("Bash Button: Unsupported section: " + section)
            print("--------------------------------------------------------------------")
            exit(-1)

    # Read tty
    while True:
        with serial.Serial(tty) as ser:
            while True:
                handler.handle(ser.readline().decode('utf-8').strip())
