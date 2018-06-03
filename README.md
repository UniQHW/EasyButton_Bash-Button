# Bash Button
> This project is part of my [Easy Button Project](https://github.com/UniQHW/EasyButton)

Bootstrap bash scripts to your EasyButton!

## Overview

Bash button is a simple python server that can execute bash commands and bash scripts on the push of my modified/hacked Staples Easy Button. Which scripts to be executed on which event is configured trough a simple configuration file.

![Gif](WATCHME.gif)

## Contents
- [Preparation](#preparation)
- [Arduino](#arduino)
	- [Installation](#installation)
- [Bash Button](#bash-button)
	- [Dependencies](#dependencies)
	- [Installation](#installation)
	- [Configuration File](#configuration-file)
		- [`[device]`](#device)
		- [`[event_*]`](#event)
	- [Usage](#usage)
- [Hacking](#hacking)
	- [Directories](#directories)
- [License](#license)

## Preparation

Bash button is part of my [Easy Button Project](https://github.com/UniQHW/EasyButton), and as a result, relies on my modifications applied to the button. To replicate those modifications to your very own easy button, refer to [this overview](https://github.com/UniQHW/EasyButton#hacking)

After the required modifications have been applied, proceed by grabbing a local copy of this project:
```bash
git clone https://github.com/UniQHW/EasyButton_Bash-Button
```

## Arduino
The Arduino uses a simple implementation of my [Easy Button Handler Interface](https://github.com/UniQHW/EasyButton_Handler). The handler serves the serial bus with a total of two events:

|Action|Signal|
|---------|--------|
|onPush()|0|
|onQuickPush()|1|

To implement additional events, please see [this table](https://github.com/UniQHW/EasyButton_Handler#events)  

### Installation

To flash the Arduino with the bash button handler, import the [handler interface library]((https://github.com/UniQHW/EasyButton_EasyButtonHandler/README.md#installation)) and the [arduino/Main.ino](https://github.com/UniQHW/EasyButton_Bash-Button/tree/master/arduino) file into a Arduino IDE.

Ensure that your Arduino is properly connected and can be accessed. Finally, click the flash button (the arrow button) to flash the handler onto the Arduino.

## Bash Button

The bash button server evaluates the serial console (typically located at `/dev/ttyACM0` on Linux machines) for any incoming signals. If a signal matches an event specified in the configuration file, the assigned bash command or script will be executed.

### Dependencies
The following dependencies are required for the server to work:

- [Python]() >= 3.4

**On Ubuntu 17.10 systems**, these dependencies can be installed with the following commands:
```bash
$ sudo apt install python3
```

For other distributions, please refer to your distribution specific package manager.

### Installation
To install bash button, execute the [setup.py](https://github.com/UniQHW/EasyButton_Bash-Button/setup.py) script with the `install` argument provided

```bash
$ sudo python3 setup.py install
```

### Configuration File
Strapping scripts to signals is made possible trough a configuration file.

By default, Bash Button will search for a configuration file in `~/.config/bash-button/bash-button.cfg`.

**Example Configuration:**
```cfg
[device]
tty=/dev/ttyACM0

[event_Push]
sig=0
cmd=echo Hello World
print=True

[event_QuickPush]
sig=1
script=~/projects/BashButton/git_push.sh
print=True
```

It is highly recommended to download the example configuration as seen above, to `~/.config/bash-button/` and then adjust it according to your requirements.

```bash
mkdir -p ~/.config-bash-button/bash-button.cfg
wget https://raw.githubusercontent.com/UniQHW/EasyButton_Bash-Button/bash-button.cfg
```

#### `[device]`

The device section stores necessary data in order to establish communication with the Arduino.

##### Properties
|Property|Constraint|Description|
|--------|----------|-----------|
|tty     |Required  |Path to the serial console|

#### `[event_*]`

Event sections must begin with the `event_` prefix and may be named as desired. They define which bash command or script is to be executed upon the retrieval of a specified signal.

##### Properties
|Property|Constraint|Description|
|--------|----------|-----------|
|sig     |Required  |Awaited signal (See [here](#Arduino))|
|cmd     |Required unless the `script` property has been set |Bash command to be executed|
|script  |Required unless the `cmd` property has been set|Bash script to be executed|
|Print|Optional|Defines whether the output of the command should be displayed in the terminal|

### Usage
```
usage: bash-button.py [-h] [-c C]

Bootstrap bash scripts to your Easy Button!

optional arguments:
  -h, --help  show this help message and exit
  -c C        Configuration file
```

To execute the bash button python server, simply run:
```bash
$ bash-button
```

From here on, the server will listen for the events listed  
in the configuration file.

To execute the server in the background, simply fork the process using the `&` specifier:
```
$ bash-button &
```

## Hacking
In the case of interest in modifying this software, the following information may point to greater results:

### Directories

- [`/BashButton`](https://github.com/UniQHW/EasyButton_Bash-Button/BashButton) - Stores code for the bash button server.

- [`/arduino`](https://github.com/UniQHW/EasyButton_Bash-Button/BashButton) - Provides the default code running on the Arduino. For changes to this package, I highly recommend looking at the [handler interface](https://github.com/UniQHW/EasyButton_Handler) that has been implemented in this project.

## License

All files found under this repository fall under the [General Public License v3](https://en.wikipedia.org/wiki/GNU_General_Public_License)
```
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
