# Lab 04: Enterprise Network Services (ACL Security & NAT/PAT)

## Overview
Lab 04 implements border security filtering and IPv4 address translation, protecting private enterprise subnets against unauthorized inbound traffic while enabling multiple internal hosts to access public Internet services via Port Address Translation (PAT / NAT Overload).

## Network Topologies (`topologies/`)
- [`LAB-4.1.pkt`](topologies/LAB-4.1.pkt): Complete NAT/PAT gateway with standard/extended access control lists (ACL) filtering web, DNS, and ICMP traffic.

## Security Policy Matrix
| Traffic Class | Source IP | Destination | Port / Protocol | Action |
| :--- | :--- | :--- | :--- | :--- |
| **Web Browsing (HTTP)** | `192.168.1.0/24` | Any Public IP | TCP Port 80 | **PERMIT** |
| **Secure Web (HTTPS)** | `192.168.1.0/24` | Any Public IP | TCP Port 443 | **PERMIT** |
| **Domain Name Resolution** | `192.168.1.0/24` | Any Public IP | UDP Port 53 | **PERMIT** |
| **Insecure Management** | Any Source | Any Target | TCP Port 23 (Telnet) | **DENY & LOG** |
| **Unsolicited Inbound** | Public WAN | `192.168.1.0/24` | Any Protocol | **DENY (Default)** |

## Cisco IOS Security & NAT Blueprint
```cisco
! 1. Extended Access Control List 101
Gateway(config)# ip access-list extended SECURE_FIREWALL
Gateway(config-ext-nacl)# permit tcp 192.168.1.0 0.0.0.255 any eq 80
Gateway(config-ext-nacl)# permit tcp 192.168.1.0 0.0.0.255 any eq 443
Gateway(config-ext-nacl)# permit udp 192.168.1.0 0.0.0.255 any eq 53
Gateway(config-ext-nacl)# deny tcp any any eq 23
Gateway(config-ext-nacl)# deny ip any any

! Apply ACL to inbound direction of inside interface
Gateway(config)# interface GigabitEthernet 0/0
Gateway(config-if)# ip access-group SECURE_FIREWALL in

! 2. Dynamic PAT (NAT Overload) Configuration
Gateway(config)# access-list 1 permit 192.168.1.0 0.0.0.255
Gateway(config)# ip nat inside source list 1 interface Serial0/1/0 overload

Gateway(config)# interface GigabitEthernet 0/0
Gateway(config-if)# ip nat inside

Gateway(config)# interface Serial 0/1/0
Gateway(config-if)# ip nat outside
```
