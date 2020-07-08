# IP Spoofing - Smurf Attack

>> ICMP Echo attack  - flood the target with ping traffic

## Usage

```
$ python main.py -h
usage: smurf_attack.py [-h] -s Source -d Destination [-c Count] [-l Length] [-r Raw]

optional arguments:
  -h, --help            show this help message and exit
  -s Source, --src Source
                        choose valid ip address to attack
  -d Destination, --dst Destination
                        choose valid,alive ip address to supply the echo-responses
  -c Count, --count Count
                        specify how much ping requests to send[def=1000]
  -l Length, --length Length
                        specify which size the packet will be[def=74 when length is 32]
  -r Raw, --raw Raw     specify raw data to send over the ping

```

Example:

```
$ python main.py -s 10.11.12.13 -d 14.15.16.17 -c 10000 -l 200
```

## Requirements

- [scapy](https://pypi.org/project/scapy/)
- [argparse](https://pypi.org/project/argparse/)

Example using pip:

```
pip install -r requirements.txt
```

Tested with python 3.7, 3.8.
