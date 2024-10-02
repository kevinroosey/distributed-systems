# Local Area Networks (LANs)
A Local Area Network comprises a set of hosts that are connected and can
communicate with each other using hardware addressing. See
"Local Area Network," on Wikipedia.
The hosts are connected using cables and either hubs
(see “Ethernet hub,” on Wikipedia) (also known as repeaters)
or switches (See “Network switch,” on Wikipedia), which are also known
as bridges. See "Bridging (networking)," on Wikipedia.
Hosts can also be connected by radio signals, known as a Wireless LAN
(WLAN) or simply, WiFi (which is simply a brand and does not stand
for anything). WLANs utilize the IEEE 802.11x standards for wireless
communication.

Each NIC is assigned a MAC, or Media Access Control, address (see MAC address).
Typically, the MAC address consists of six byte-size integers, written in hexadecimal;
it is known as EUI-48 (Extended Unique Identifier), formerly MAC-48. 

The first three bytes consist of the manufacturer's identifier or OUI (Organizationally
Unique Identifier).
The remaining three bytes uniquely identify the device. Originally, these bytes were
burned into the chip, but today they may be set by an admin.
IPv6 makes use of the newer MAC address standard, which contains eight bytes
and is known as EUI-64. The additional two bytes are used as part of the device
identifier.
The MAC address is used by the LAN to identify each host connected to it;
consequently, each MAC address on a LAN must be unique.
IP addresses are also assigned to each host. The IP address is the conceptual,
as opposed to the physical, address of the host.
An IP address may be assigned permanently to a machine. Because the address
does not change, it is known as a static IP address.
Alternatively, an IP address may be assigned dynamically to a host by another
host, typically a router. This approach is known as DHCP, Dynamic Host
Configuration Protocol (See Dynamic Host Configuration Protocol," on Wikipedia).
DHCP is routinely used for laptops and mobile devices. Static assignment is
reserved for routers, large computers, and workstations, i.e., computers that do not move.

In Ethernet, all packets are transmitted over the LAN and, therefore, each host can
'hear' all local transmissions.
Typically, the NIC listens only for transmissions that contain its MAC address in the
packet header.
You can place your NIC into 'promiscuous' mode, which causes the NIC to listen
for all packets. Promiscuous mode is used by network sniffers to view all of the
traffic that occurs over the LAN.
