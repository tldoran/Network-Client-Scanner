import scapy.all as scapy

def scan(ip):

  arp_request = scapy.ARP(pdst=ip)

  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

  arp_request_broadcast = broadcast/arp_request

  answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

  print("IP\t\t\tMAC Address\n-----------------------------------------")

  for element in answered_list:
    print(element[1].psrc + "\t\t" + element[1].hwsrc)


scan("10.0.2.1/24") #Input your own ip address here, use ifconfig before running to find the ip address of your connected network .1/24 meaning to scan all from 1-254
