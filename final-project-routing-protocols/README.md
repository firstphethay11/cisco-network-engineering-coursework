# Final Project: Multi-Area Dynamic Routing & Enterprise Edge Architecture

## Overview
The capstone final project synthesizes all semester networking competencies into an end-to-end enterprise topology. It models a corporate multi-site architecture comprising an OSPF Area 0 core backbone, a legacy RIPv2 branch office domain, mutual route redistribution, and an ISP edge boundary with default static route propagation.

## Network Topologies (`topology/`)
- [`Final-RoutingProtocols-1.pkt`](topology/Final-RoutingProtocols-1.pkt): The production capstone Cisco Packet Tracer simulation topology with full convergence and end-to-end multi-site reachability.

## Architectural Highlights
1. **Multi-Protocol Redistribution**: Border-R2 functions as an Autonomous System Boundary Router (ASBR), translating link-state LSAs into distance-vector hop metrics and vice-versa.
2. **Default Route Injection**: Propagates `0.0.0.0/0` quad-zero default routes downstream into OSPF (`default-information originate`) to allow enterprise-wide egress to simulated ISP edge `203.0.113.1`.
3. **802.1Q Inter-VLAN Gateway**: Segmented internal VLANs (Management, Finance, Branch) communicating seamlessly across the routed WAN core.

## End-to-End Verification Checklist
- [x] OSPF Neighbor state: `FULL/DR` between Core-R1 and Border-R2.
- [x] RIPv2 Database: Branch-R3 learns redistributed OSPF routes as external Type 2 (`O E2`).
- [x] WAN Egress: All hosts can resolve external addresses through default route gateway.
- [x] ICMP Verification: 100% ping success rate (`5/5`) across inter-protocol domains.
