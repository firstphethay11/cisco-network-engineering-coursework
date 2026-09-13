# Lab 02: Virtual LAN (VLAN) Trunking & Inter-VLAN Routing

## Overview
Lab 02 explores enterprise logical network segmentation using IEEE 802.1Q tagged encapsulation, Dynamic Trunking Protocol (DTP), native VLAN security, and Router-on-a-Stick (RoaS) sub-interface architecture for inter-VLAN routing.

## Network Topologies (`topologies/`)
- [`LAB-2.1.pkt`](topologies/LAB-2.1.pkt): Single-switch VLAN segmentation with broadcast boundary containment.
- [`LAB-2.2.pkt`](topologies/LAB-2.2.pkt): Multi-switch 802.1Q trunking link over Gigabit uplinks with native VLAN configuration.
- [`LAP-2.3.pkt`](topologies/LAP-2.3.pkt): Router-on-a-Stick (RoaS) configuration using Cisco 2911 ISR with sub-interfaces terminating multiple 802.1Q tags.

## Logical Segmentation Matrix
| VLAN ID | VLAN Name | Subnet Range | Gateway (RoaS Sub-if) | Default Access Ports |
| :--- | :--- | :--- | :--- | :--- |
| **VLAN 10** | Management | `192.168.10.0/24` | `192.168.10.1` (Gi0/0.10) | Fa0/1 - Fa0/8 |
| **VLAN 20** | Faculty & Staff | `192.168.20.0/24` | `192.168.20.1` (Gi0/0.20) | Fa0/9 - Fa0/16 |
| **VLAN 30** | Student Lab | `192.168.30.0/24` | `192.168.30.1` (Gi0/0.30) | Fa0/17 - Fa0/24 |
| **VLAN 99** | Native / Parking | Unrouted | None | Fa0/24 (Trunk Native) |

## Cisco IOS Configuration Blueprint
```cisco
! Switch 802.1Q Trunk Configuration
Switch(config)# vlan 10,20,30,99
Switch(config-vlan)# exit
Switch(config)# interface FastEthernet 0/24
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk native vlan 99
Switch(config-if)# switchport trunk allowed vlan 10,20,30,99

! Router-on-a-Stick (RoaS) Sub-interface Configuration
Router(config)# interface GigabitEthernet 0/0
Router(config-if)# no ip address
Router(config-if)# no shutdown

Router(config)# interface GigabitEthernet 0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0

Router(config)# interface GigabitEthernet 0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.20.1 255.255.255.0

Router(config)# interface GigabitEthernet 0/0.30
Router(config-subif)# encapsulation dot1Q 30
Router(config-subif)# ip address 192.168.30.1 255.255.255.0
```
