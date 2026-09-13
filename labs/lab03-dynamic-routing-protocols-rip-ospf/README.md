# Lab 03: Dynamic Routing Protocols (OSPFv2 & RIPv2)

## Overview
Lab 03 covers interior gateway protocols (IGPs), comparing distance-vector (RIPv2) and link-state (OSPFv2) algorithms across multi-router enterprise topologies. It explores neighbor adjacency formation, Shortest Path First (SPF) metric computation, passive interfaces, and route redistribution.

## Network Topologies (`topologies/`)
- [`LAB-3.1.pkt`](topologies/LAB-3.1.pkt): Baseline multi-hop routing environment with static route convergence.
- [`LAB-3.1-designed.pkt`](topologies/LAB-3.1-designed.pkt): Optimized physical layout and link design for dual-homed connectivity.
- [`LAB-3.2.pkt`](topologies/LAB-3.2.pkt): RIPv2 deployment with split-horizon, auto-summary disabled, and broadcast reduction.
- [`LAB-3.3.pkt`](topologies/LAB-3.3.pkt): Single-Area OSPFv2 (Area 0) backbone deployment with wildcard mask calculation and DR/BDR election.
- [`final.pkt`](topologies/final.pkt): Integrated enterprise lab convergence scenario with multi-protocol redistribution.

## Protocol Comparison Matrix
| Parameter | RIPv2 | OSPFv2 |
| :--- | :--- | :--- |
| **Routing Algorithm** | Distance-Vector (Bellman-Ford) | Link-State (Dijkstra SPF) |
| **Metric** | Hop Count (Max 15) | Cost (Reference BW / Interface BW) |
| **Convergence Speed** | Slow (30s periodic updates) | Fast (Triggered Link-State Advertisements) |
| **Subnet Support** | VLSM / CIDR (Classless) | VLSM / CIDR (Classless) |
| **Administrative Distance** | 120 | 110 |
| **Multicast Group** | `224.0.0.9` | `224.0.0.5` (AllSPFRouters), `224.0.0.6` (DR/BDR) |

## Cisco IOS Routing Configuration
```cisco
! OSPFv2 Backbone Configuration (Core-R1)
Router(config)# router ospf 1
Router(config-router)# router-id 1.1.1.1
Router(config-router)# network 10.1.1.0 0.0.0.3 area 0
Router(config-router)# network 192.168.10.0 0.0.0.255 area 0
Router(config-router)# passive-interface GigabitEthernet 0/1.10

! RIPv2 Branch Configuration (Branch-R3)
Router(config)# router rip
Router(config-router)# version 2
Router(config-router)# no auto-summary
Router(config-router)# network 10.2.2.0
Router(config-router)# network 192.168.30.0
Router(config-router)# passive-interface GigabitEthernet 0/1

! Mutual Redistribution on Autonomous System Boundary Router (Border-R2)
Router(config)# router ospf 1
Router(config-router)# redistribute rip subnets
Router(config)# router rip
Router(config-router)# redistribute ospf 1 metric 2
```
