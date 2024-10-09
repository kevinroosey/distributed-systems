## Internet Protocol (IP): Generally

Transmitting packets relies on a variety of software and firmware that is divided into layers. The older model for layering is known as the **OSI Model**, which has seven (7) layers. A later model, the **TCP/IP Model**, contains five (5) of these layers.

For a comparison, see [this reference](http://www.snmptools.net/netbasics/layers/).

### Examples of Various Protocols in Their Respective Layers

Overview of the flow of data across the network can be found [here](https://en.wikipedia.org/wiki/Internet_protocol_suite#Key_architectural_principles).

For a deeper dive into the use of layers, refer to [The TCP/IP Guide](http://www.tcpipguide.com/free/t_IPDatagramEncapsulation.htm).

---

## Packet Fragmentation

- The maximum size of an IP packet depends on the underlying network.
- Regular Ethernet frames are limited to **1500 bytes of payload**.
- This size limitation is known generically as the **Maximum Transmission Unit (MTU)**.
- Consequently, if a host is trying to send an IP packet that is larger than the MTU, it must divide the packet into **fragments**.
- Using data in the IP header, the **destination host** can piece together the fragments back into their original form; this process is known as **reassembly**.
- Note that **routers along the way never reassemble packets**; they merely pass them along to the destination host.


## Internet Protocol (IP): Version 4 (IPv4)

### IP Header

- The format of the header is explained in ["IPv4" on Wikipedia](https://en.wikipedia.org/wiki/IPv4#Header).
- The header is 20 bytes in length, longer if options are present.
- There are many fields in the header, notably:
  - **Version** - the version of IP; in this case, 4
  - **IHL** - the length of the header
  - **Total length** - the total length of the packet (header + payload)
  - **Protocol** - the type of payload packet; usually TCP or UDP
  - **Source IP Address**
  - **Destination IP Address**

### Special Use Addresses

- Certain IP addresses are reserved for special uses.
  - **127.0.0.0/8** is reserved for loopback addresses, i.e., localhost.
  - **10.0.0.0/8** is reserved for private networks (16 million addresses).
  - **192.168.0.0/16** is also reserved for private networks (64k addresses).

### IPv4 Address Exhaustion

- Although the four bytes of IPv4 provide potentially 4 billion addresses, IPv4 addresses were exhausted in 2011.
- More than 4 billion hosts using IPv4 can connect to the Internet because of **Network Address Translation (NAT)**, which will be discussed later.

## Internet Protocol (IP): Version 6 (IPv6)

IPv6 was devised in 1995 to address limitations of IPv4, primarily the limited address space.

- Addresses are comprised of 16 octets (8-bit bytes). Hence, an IPv6 address has **128 bits**.
- \(2^{128} = 340,282,366,920,938,463,463,374,607,431,768,211,456\) possible addresses.

> "The earth is about 4.5 billion years old. If we had been assigning IPv6 addresses at a rate of 1 billion per second since the earth was formed, we would have by now used up less than one trillionth of the address space....The earth's surface area is about 510 trillion square meters. If a typical computer has a footprint of about a tenth of a square meter, we would have to stack computers 10 billion high blanketing the entire surface of the earth to use up that same trillionth of the address space."  
> *(Source: "IPv6 Address Size and Address Space", retrieved Oct. 22, 2017, from [The TCP/IP Guide](http://www.tcpipguide.com/free/t_IPv6AddressSizeandAddressSpace-2.htm))*

### IPv6 Address Format

- IPv6 addresses are expressed in **hexadecimal** to make them shorter and easier to convert to binary.
- Each address is subdivided into eight (8) two-byte values, expressed with four hexadecimal digits.
- The two-byte values are separated by colons `(:)`, rather than periods `(.)` as in IPv4.

Example:
`805B:2D9D:DC28:0000:0000:FC57:D4C8:1FFF`

- An IPv6 address can also contain an IPv4 address, embedded as the last 4 bytes. This is known as **mixed notation**.

Example:
`805B:2D9D:DC28::FC57:212.200.31.255`

- The first **64 bits** of the address is the **network prefix**, while the last **64 bits** comprise the **interface identifier**.
- IPv6 addresses can be generated based on the network prefix and the device’s **MAC address**, allowing hosts to configure their own IPv6 addresses.

### IPv6 Header

- IPv6 relies on a **single main header** with additional optional headers.
- The main header is **40 bytes long** and is simplified compared to IPv4.  
  [More details on the IPv6 header](http://www.tcpipguide.com/free/t_IPv6DatagramMainHeaderFormat.htm)

### Key Changes from IPv4

- **Larger Address Space**: IPv6 addresses are 128 bits long, expanding the address space from around 4 billion to over 300 trillion trillion trillion addresses.
- **Autoconfiguration**: IPv6 permits generating IP addresses based on device IDs, such as Ethernet MAC addresses, enabling hosts to self-configure.
- **Routing System Support**: IPv6 supports modern routing systems and allows for easy expansion as the Internet grows.
- **Fragmentation**: Fragmentation is only handled by the source host, which can discover the **MTU** for the path to the destination. Routers are not permitted to fragment packets.


## Transmission Control Protocol (TCP)

### Header

For more details, see the [TCP/IP Guide](http://www.tcpipguide.com/free/t_TCPMessageSegmentFormat-3.htm).

### Establishing a Virtual Connection: The 3-Way Handshake

- **SYN bit**
  - Short for "synchronize"
  - This bit is used to establish a virtual connection
- **ACK bit**
  - Short for "acknowledgment"
- **Procedure**  
  Refer to the [TCP 3-Way Handshake in the TCP/IP Guide](http://www.tcpipguide.com/free/t_TCPConnectionEstablishmentProcessTheThreeWayHandsh-3.htm).

### Reliability and Flow Control

- **PAR – Positive Acknowledgment and Retransmission**  
  See the [TCP/IP Guide](http://www.tcpipguide.com/free/t_TCPSlidingWindowAcknowledgmentSystemForDataTranspo-3.htm).
- **Message Identification and Time Limits**  
  Adding metadata that identifies messages and sets time limits improves performance.  
  For more information, check the [TCP/IP Guide](http://www.tcpipguide.com/free/t_TCPSlidingWindowAcknowledgmentSystemForDataTranspo-4.htm).
- **Sliding Window**
  - TCP uses a sliding window approach.
  - Resources on sliding window:
    - **State** - [TCP/IP Guide](http://www.tcpipguide.com/free/t_TCPSlidingWindowAcknowledgmentSystemForDataTranspo5.htm)
    - **The Window** - [TCP/IP Guide](http://www.tcpipguide.com/free/t_TCPSlidingWindowAcknowledgmentSystemForDataTranspo6.htm)
    - **After Transmission** - [TCP/IP Guide](http://www.tcpipguide.com/free/t_TCPSlidingWindowAcknowledgmentSystemForDataTranspo8.htm)

### Termination

- For more information on TCP connection termination, see the [TCP/IP Guide](http://www.tcpipguide.com/free/t_TCPConnectionTermination-2.htm).
- **TIME_WAIT**: Time to wait to receive the last "fin" response.
  - The network stack will handle this problem, but you will see sockets in this state when viewing the output of `netstat`.

### Congestion Avoidance

- TCP uses an algorithm called **Slow Start** to regulate traffic flow.
  - In brief, TCP initially sends a small amount of data and then increases the amount until a packet is dropped.
  - When a packet is dropped, TCP reduces the amount of data being sent.
  - This approach helps avoid network congestion.

