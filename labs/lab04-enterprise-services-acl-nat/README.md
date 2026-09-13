# Lab 04: Enterprise Network Services (ACL Security & NAT/PAT)

## Overview
Lab 04 implements border security filtering and IPv4 address translation, protecting private enterprise subnets against unauthorized inbound traffic while enabling multiple internal departmental networks to access public Internet services via Port Address Translation (PAT / NAT Overload).

---

## Lab Architecture & Packet Tracer Topology

<div align="center">
  <img src="screenshots/lab04-1-nat-acl-topology.png" width="85%" alt="Cisco Packet Tracer Lab 04.1 NAT and ACL Topology"/>
  <p><i>Figure 4.1: Enterprise Dual-LAN Border Gateway with PAT Overload across Public WAN to ISP Services</i></p>
</div>

### Network Addressing & Interface Inventory
| Network Segment | Subnet / CIDR | Router Interface (Gateway) | Devices &amp; Servers Attached | NAT Role |
| :--- | :--- | :--- | :--- | :--- |
| **Inside LAN 1** | `10.10.10.0/24` | `Router-A` Fa0/0 (`10.10.10.254`) | `Switch-A1`, `PC-A1`, `PC-A2` | Inside Local |
| **Inside LAN 2** | `172.16.0.0/24` | `Router-A` Fa0/1 (`172.16.0.254`) | `Switch-A2`, `PC-A3`, `DHCP Server-A` (`172.16.0.11`) | Inside Local |
| **Public WAN Link** | `202.28.28.0/28` | `Router-A` Se0/0 (`.14`) &harr; `Router-B` Se0/0 (`.1`) | Point-to-Point Serial Link (`255.255.255.240`) | Inside Global / Outside Local |
| **Outside / ISP LAN** | `203.158.207.0/24` | `Router-B` Fa0/0 (`203.158.207.254`) | `Switch-B`, `DNS Server-B` (`.11`), `DHCP Server-B` (`.1`) | Outside Global |

---

## Security Policy Matrix (Extended ACL 101)

| Policy ID | Traffic Classification | Source Network | Destination Network | Protocol &amp; Port | Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rule 1** | Domain Name Resolution (DNS) | Inside Subnets (`10.10.10.0`, `172.16.0.0`) | `DNS Server-B` (`203.158.207.11`) | UDP Port 53 | **PERMIT** |
| **Rule 2** | Web Browsing (HTTP) | Inside Subnets | Any Public Host | TCP Port 80 | **PERMIT** |
| **Rule 3** | Secure Web (HTTPS) | Inside Subnets | Any Public Host | TCP Port 443 | **PERMIT** |
| **Rule 4** | Insecure Telnet Access | Any Source | Any Destination | TCP Port 23 | **DENY &amp; LOG** |
| **Rule 5** | Unsolicited Inbound Traffic | Outside Public WAN | Inside Private LANs | Any Protocol | **DENY (Implicit)** |

---

## Cisco IOS Security & NAT Blueprint

```cisco
! ==============================================================================
! 1. Router-A (Enterprise Border Gateway) Configuration
! ==============================================================================

! Define Inside and Outside NAT Interfaces
Router-A(config)# interface FastEthernet 0/0
Router-A(config-if)# ip address 10.10.10.254 255.255.255.0
Router-A(config-if)# ip nat inside
Router-A(config-if)# no shutdown

Router-A(config)# interface FastEthernet 0/1
Router-A(config-if)# ip address 172.16.0.254 255.255.255.0
Router-A(config-if)# ip nat inside
Router-A(config-if)# no shutdown

Router-A(config)# interface Serial 0/0
Router-A(config-if)# ip address 202.28.28.14 255.255.255.240
Router-A(config-if)# ip nat outside
Router-A(config-if)# no shutdown

! Define Standard ACL matching all Inside Private subnets
Router-A(config)# access-list 1 permit 10.10.10.0 0.0.0.255
Router-A(config)# access-list 1 permit 172.16.0.0 0.0.0.255

! Enable Dynamic PAT (Port Address Translation / NAT Overload)
Router-A(config)# ip nat inside source list 1 interface Serial0/0 overload

! Default Static Route pointing to ISP Gateway
Router-A(config)# ip route 0.0.0.0 0.0.0.0 202.28.28.1

! Extended Access Control List 101 for Traffic Filtering
Router-A(config)# ip access-list extended BORDER_FIREWALL
Router-A(config-ext-nacl)# permit udp 10.10.10.0 0.0.0.255 host 203.158.207.11 eq 53
Router-A(config-ext-nacl)# permit udp 172.16.0.0 0.0.0.255 host 203.158.207.11 eq 53
Router-A(config-ext-nacl)# permit tcp 10.10.10.0 0.0.0.255 any eq 80
Router-A(config-ext-nacl)# permit tcp 172.16.0.0 0.0.0.255 any eq 80
Router-A(config-ext-nacl)# permit tcp any any established
Router-A(config-ext-nacl)# deny tcp any any eq 23
Router-A(config-ext-nacl)# deny ip any any

Router-A(config)# interface FastEthernet 0/0
Router-A(config-if)# ip access-group BORDER_FIREWALL in

! ==============================================================================
! 2. Verification Commands
! ==============================================================================
Router-A# show ip nat translations
Router-A# show ip nat statistics
Router-A# show access-lists
```

---

## Topologies in Repository (`topologies/`)
- [`LAB-4.1.pkt`](topologies/LAB-4.1.pkt): Complete NAT/PAT gateway with standard and extended access control lists (ACL) filtering web, DNS, and ICMP traffic.
