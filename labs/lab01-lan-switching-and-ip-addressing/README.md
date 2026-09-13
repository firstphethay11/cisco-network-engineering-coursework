# Lab 01: LAN Switching Fundamentals & IP Addressing

## Overview
Lab 01 establishes foundational campus local area networking (LAN) concepts, focusing on Layer 2 Ethernet switching, collision and broadcast domain isolation, media access control (MAC) address tables, and structured IPv4 classful/classless addressing.

## Network Topologies (`topologies/`)
- [`Unite 1.pkt`](topologies/Unite%201.pkt): Peer-to-peer and star topology host configuration with static IPv4 addressing and ICMP reachability verification.
- [`Unite2.pkt`](topologies/Unite2.pkt): Multi-switch hierarchical topology exploring broadcast propagation and ARP resolution.
- [`Unite 3.pkt`](topologies/Unite%203.pkt): End-to-end host-to-gateway verification with default gateways and subnet boundary analysis.

## Key Technical Objectives
1. **Layer 2 Forwarding**: Understand store-and-forward switching mechanisms, CAM (Content Addressable Memory) table population, and frame filtering.
2. **IP Addressing & Subnetting**: Implement `/24` private address blocks (RFC 1918) with corresponding default gateways on host interfaces.
3. **Connectivity Verification**: Perform ping sweeps and trace ARP table generation using Cisco IOS simulation modes.

## Cisco IOS Reference Commands
```cisco
! Verify switch MAC address learning
Switch# show mac address-table

! Verify interface status and line protocol
Switch# show ip interface brief
Switch# show interfaces status

! Configure administrative management interface
Switch(config)# interface vlan 1
Switch(config-if)# ip address 192.168.1.2 255.255.255.0
Switch(config-if)# no shutdown
Switch(config)# ip default-gateway 192.168.1.1
```
