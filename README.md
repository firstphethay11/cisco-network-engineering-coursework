<div align="center">

# Cisco Network Engineering Coursework

**Enterprise Networking • Dynamic Routing Protocols • VLAN Segmentation • ACL & NAT Security**  
*Department of Computer Engineering, Faculty of Engineering and Architecture, RMUTI*

[![Cisco Packet Tracer](https://img.shields.io/badge/Cisco_Packet_Tracer-v8.2+-005073?style=flat&logo=cisco&logoColor=white)](https://www.netacad.com/courses/packet-tracer)
[![CCNA Curriculum](https://img.shields.io/badge/CCNA-Enterprise_Core-1BA0D7?style=flat&logo=cisco&logoColor=white)](https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html)
[![OSPF & RIP](https://img.shields.io/badge/Routing-OSPFv2_%7C_RIPv2-3b82f6?style=flat)](https://datatracker.ietf.org/doc/html/rfc2328)
[![Security ACL NAT](https://img.shields.io/badge/Security-ACL_%7C_NAT_PAT-dc2626?style=flat)](https://datatracker.ietf.org/doc/html/rfc3022)
[![Python Tools](https://img.shields.io/badge/Tools-VLSM_&_Dijkstra_SPF-10b981?style=flat&logo=python&logoColor=white)](tools/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](LICENSE)

</div>

---

## Executive Summary

This repository houses an engineering-grade collection of **Cisco Packet Tracer (`.pkt`)** network simulation architectures, modular lab blueprints, automated subnetting tools, and Cisco IOS configuration scripts developed throughout the Computer Networks & Data Communications curriculum.

All topologies follow standard **Cisco CCNA (Cisco Certified Network Associate)** routing, switching, and security guidelines — featuring 802.1Q virtual LAN segmentation, Router-on-a-Stick inter-VLAN routing, single-area OSPFv2 backbone convergence, RIPv2 mutual redistribution, Extended Access Control List (ACL) traffic filtering, and Port Address Translation (PAT / NAT Overload).

---

### Cisco Packet Tracer Lab 01 Topology (Ring Backbone & LAN Switching)

<div align="center">
  <table>
    <tr>
      <td width="45%" align="center">
        <b>Packet Tracer Topology (Lab 01)</b><br/><br/>
        <img src="docs/screenshots/lab01-packet-tracer-topology.png" width="90%" alt="Lab 01 Packet Tracer Ring Topology"/>
      </td>
      <td width="55%" valign="middle">
        <h4>Cisco 2620XM Multi-Router Redundant Ring Architecture</h4>
        <ul>
          <li><b>Ring Backbone:</b> 4x Cisco 2620XM routers connected via Serial WIC-2T links.</li>
          <li><b>Switched LAN Access:</b> 4x Cisco 2950-24 Catalyst switches with 8 host endpoints.</li>
          <li><b>Central Network Services:</b> Dedicated TFTP / Configuration Management Server (<code>Server-A</code>).</li>
          <li><b>Console OOB Management:</b> Rollover console interfaces for out-of-band router recovery.</li>
          <li><b>Lab Theory:</b> Includes verified answers for Cisco IOS memory architecture (RAM, NVRAM, Flash, TFTP) and configuration backups.</li>
        </ul>
        <p align="left"><a href="labs/lab01-lan-switching-and-ip-addressing/"><b>Explore Lab 01 Documentation &amp; Topologies &rarr;</b></a></p>
      </td>
    </tr>
  </table>
</div>

### Cisco Packet Tracer Lab 02 Suite (VLANs, Spanning Tree & WLAN)

<div align="center">
  <table>
    <tr>
      <td width="33%" align="center">
        <b>Lab 2.1: Multi-Switch VLANs</b><br/><br/>
        <img src="docs/screenshots/lab02-1-vlan-multi-switch.png" width="100%" alt="Lab 2.1 Multi-Switch VLAN Segmentation"/><br/>
        <small>VLAN 11 Green &amp; VLAN 12 Yellow isolation</small>
      </td>
      <td width="33%" align="center">
        <b>Lab 2.2: Spanning Tree Protocol</b><br/><br/>
        <img src="docs/screenshots/lab02-2-stp-root-bridge.png" width="100%" alt="Lab 2.2 Spanning Tree Protocol"/><br/>
        <small>Switch C Root Bridge &amp; Fa 0/1 Loop Blocking</small>
      </td>
      <td width="33%" align="center">
        <b>Lab 2.3: Wireless LAN (WLAN)</b><br/><br/>
        <img src="docs/screenshots/lab02-3-wlan-architecture.png" width="100%" alt="Lab 2.3 Wireless LAN Architecture"/><br/>
        <small>WRT300N Wireless Routers &amp; Central Server</small>
      </td>
    </tr>
  </table>
  <p><a href="labs/lab02-vlan-trunking-and-switching/"><b>View Complete Lab 02 Documentation &amp; Topologies &rarr;</b></a></p>
</div>

### Cisco Packet Tracer Lab 03 Suite (VLSM Subnetting, RIP & OSPF Area 0)

<div align="center">
  <table>
    <tr>
      <td width="33%" align="center">
        <b>Lab 3.1: VLSM Subnetting</b><br/><br/>
        <img src="docs/screenshots/lab03-1-vlsm-subnetting-topology.png" width="100%" alt="Lab 3.1 VLSM Subnetting"/><br/>
        <small>Binary /26, /27, /30 Hierarchical Allocation</small>
      </td>
      <td width="33%" align="center">
        <b>Lab 3.2: RIP Dynamic Routing</b><br/><br/>
        <img src="docs/screenshots/lab03-2-rip-routing-tables.png" width="100%" alt="Lab 3.2 RIP Dynamic Routing"/><br/>
        <small>Hop Count Metric &amp; 4-Router RIB Convergence</small>
      </td>
      <td width="33%" align="center">
        <b>Lab 3.3: OSPF Area 0 Backbone</b><br/><br/>
        <img src="docs/screenshots/lab03-3-ospf-area0-backbone.png" width="100%" alt="Lab 3.3 OSPF Area 0 Backbone"/><br/>
        <small>Link-State Shortest Path First (SPF) Tree</small>
      </td>
    </tr>
  </table>
  <p><a href="labs/lab03-dynamic-routing-protocols-rip-ospf/"><b>View Complete Lab 03 Documentation &amp; Topologies &rarr;</b></a></p>
</div>

### Cisco Packet Tracer Lab 04 (Border Security, ACL & NAT/PAT Overload)

<div align="center">
  <table>
    <tr>
      <td width="45%" align="center">
        <b>Packet Tracer Topology (Lab 4.1)</b><br/><br/>
        <img src="docs/screenshots/lab04-1-nat-acl-topology.png" width="90%" alt="Lab 4.1 Border Gateway NAT and ACL Topology"/>
      </td>
      <td width="55%" valign="middle">
        <h4>Enterprise Border Security &amp; Address Translation Architecture</h4>
        <ul>
          <li><b>Inside Private Subnets:</b> Dual departmental segments (<code>10.10.10.0/24</code> &amp; <code>172.16.0.0/24</code>) routed via <code>Router-A</code>.</li>
          <li><b>Dynamic PAT Overload:</b> Translates multiple RFC 1918 private IP addresses to public Serial WAN IP (<code>202.28.28.14/28</code>).</li>
          <li><b>Outside ISP Services:</b> Public DMZ subnet (<code>203.158.207.0/24</code>) providing DNS (<code>.11</code>) and external DHCP (<code>.1</code>).</li>
          <li><b>Extended ACL 101 Filtering:</b> Granular packet filtering enforcing DNS (UDP 53) and HTTP (TCP 80) access while dropping Telnet and unauthorized inbound probes.</li>
        </ul>
        <p align="left"><a href="labs/lab04-enterprise-services-acl-nat/"><b>Explore Lab 04 Documentation &amp; Topologies &rarr;</b></a></p>
      </td>
    </tr>
  </table>
</div>

---

## Repository Structure & Topology Catalog

```
cisco-network-engineering-coursework/
├── final-project-routing-protocols/        # Capstone Multi-Site Enterprise Architecture
│   ├── README.md                           # Final project design documentation
│   └── topology/
│       └── Final-RoutingProtocols-1.pkt    # Complete OSPF + RIPv2 + ISP Edge simulation
├── labs/
│   ├── lab01-lan-switching-and-ip-addressing/
│   │   ├── README.md                       # L2 Ethernet, CAM tables, IPv4 addressing
│   │   └── topologies/
│   │       ├── Unite 1.pkt                 # P2P & star topology host configuration
│   │       ├── Unite2.pkt                  # Multi-switch broadcast domain analysis
│   │       └── Unite 3.pkt                 # Subnet boundary & default gateway verification
│   ├── lab02-vlan-trunking-and-switching/
│   │   ├── README.md                       # 802.1Q trunking, Router-on-a-Stick (RoaS)
│   │   └── topologies/
│   │       ├── LAB-2.1.pkt                 # Single-switch VLAN broadcast containment
│   │       ├── LAB-2.2.pkt                 # Multi-switch 802.1Q tagged uplinks
│   │       └── LAP-2.3.pkt                 # Router-on-a-Stick sub-interface routing
│   ├── lab03-dynamic-routing-protocols-rip-ospf/
│   │   ├── README.md                       # OSPFv2 Link-State & RIPv2 Distance-Vector
│   │   └── topologies/
│   │       ├── LAB-3.1.pkt                 # Multi-hop static route benchmark
│   │       ├── LAB-3.1-designed.pkt        # Optimized dual-homed physical layout
│   │       ├── LAB-3.2.pkt                 # RIPv2 split-horizon & VLSM updates
│   │       ├── LAB-3.3.pkt                 # Single-Area OSPFv2 backbone (Area 0)
│   │       └── final.pkt                   # Multi-protocol redistribution scenario
│   └── lab04-enterprise-services-acl-nat/
│       ├── README.md                       # Network security, ACLs, and NAT/PAT
│       └── topologies/
│           └── LAB-4.1.pkt                 # Extended ACL 101 & PAT Overload Gateway
├── tools/                                  # Algorithmic Network Automation Utilities
│   ├── vlsm_subnet_calculator.py           # RFC 1878 VLSM & CIDR address allocator
│   └── routing_table_simulator.py          # Dijkstra SPF & OSPF convergence engine
├── docs/
│   └── screenshots/                        # High-resolution architectural blueprints
│       ├── 01-final-routing-protocols-topology.png
│       ├── 02-vlan-trunking-topology.png
│       ├── 03-ospf-rip-routing-table-simulation.png
│       └── 04-acl-nat-security-topology.png
├── run_demo.py                             # 1-Command interactive demo & verification suite
├── LICENSE                                 # MIT Open Source License
└── .gitignore                              # Clean repository exclusion patterns
```

---

## Technical Competency Matrix

| Domain | Technical Topics | Hardware / IOS Models | Cisco Protocols & Standards |
| :--- | :--- | :--- | :--- |
| **Layer 2 Switching** | VLAN segmentation, 802.1Q trunking, DTP, Native VLAN | Cisco Catalyst 2960-24TT | IEEE 802.1Q, 802.3u, CAM tables |
| **Inter-VLAN Routing** | Router-on-a-Stick (RoaS), sub-interfaces, encapsulation | Cisco 1941, 2901, 2911 ISR | 802.1Q Sub-if tagging |
| **Interior Gateway Protocols** | Distance-Vector vs. Link-State, SPF algorithm, DR/BDR | Cisco 2911 Modular ISR | OSPFv2 (RFC 2328), RIPv2 (RFC 2453) |
| **Edge Route Redistribution** | ASBR mutual redistribution, default-information originate | Cisco 2911 Edge Router | Autonomous System Boundary Routing |
| **IPv4 Address Planning** | Variable-Length Subnet Masking (VLSM), CIDR, Wildcard | All Routers & Endpoints | RFC 1878, RFC 4632 |
| **Network Security** | Standard & Extended IP ACLs, port-based packet filtering | Cisco Security ISR | Named / Numbered ACLs (1-199) |
| **Address Translation** | Dynamic Port Address Translation (PAT / NAT Overload) | Cisco NAT Border Gateway | RFC 1631, RFC 3022 |

---

## Algorithmic Subnetting & Routing Tools

The `tools/` directory provides Python utilities to calculate subnets and simulate routing convergence without launching Packet Tracer:

### 1. VLSM Subnet Calculator (`tools/vlsm_subnet_calculator.py`)
Allocates subnets in descending host count order, guaranteeing optimal IP block efficiency:

```bash
python tools/vlsm_subnet_calculator.py
```

```
==============================================================================================
  CISCO CCNA VLSM SUBNET ALLOCATION TABLE — Base: 192.168.0.0/24
==============================================================================================
Subnet / Segment          | Req  | Alloc | Network / CIDR     | Usable Range                   
----------------------------------------------------------------------------------------------
VLAN 20 (Faculty/Staff)   | 60   | 62    | 192.168.0.0/26     | 192.168.0.1 - 192.168.0.62     
VLAN 10 (Management)      | 28   | 30    | 192.168.0.64/27    | 192.168.0.65 - 192.168.0.94    
VLAN 30 (Student Lab)     | 14   | 14    | 192.168.0.96/28    | 192.168.0.97 - 192.168.0.110   
WAN Link (R1-R2 P2P)      | 2    | 2     | 192.168.0.112/30   | 192.168.0.113 - 192.168.0.114  
WAN Link (R2-R3 P2P)      | 2    | 2     | 192.168.0.116/30   | 192.168.0.117 - 192.168.0.118  
==============================================================================================
```

### 2. OSPF Dijkstra SPF Simulator (`tools/routing_table_simulator.py`)
Computes least-cost paths and builds the routing information base (RIB):

```bash
python tools/routing_table_simulator.py
```

### 3. One-Command Interactive Demo Suite (`run_demo.py`)
Validates all 13 `.pkt` files and executes the subnet and routing engines simultaneously:

```bash
python run_demo.py
```

---

## Cisco IOS Configuration Blueprint Reference

### 1. 802.1Q Inter-VLAN Router-on-a-Stick
```cisco
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
!
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
```

### 2. Single-Area OSPFv2 Backbone (Area 0)
```cisco
router ospf 1
 router-id 1.1.1.1
 network 10.1.1.0 0.0.0.3 area 0
 network 192.168.10.0 0.0.0.255 area 0
 passive-interface GigabitEthernet0/0.10
```

### 3. Extended ACL 101 & PAT Overload
```cisco
ip access-list extended ENTERPRISE_FIREWALL
 permit tcp 192.168.1.0 0.0.0.255 any eq 80
 permit tcp 192.168.1.0 0.0.0.255 any eq 443
 permit udp 192.168.1.0 0.0.0.255 any eq 53
 deny tcp any any eq 23
 deny ip any any
!
access-list 1 permit 192.168.1.0 0.0.0.255
ip nat inside source list 1 interface Serial0/1/0 overload
```

---

## Getting Started & Software Requirements

1. **Cisco Packet Tracer**: Download and install [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer) (Version 8.0 or newer recommended).
2. **Open Topology**:
   - Launch Cisco Packet Tracer.
   - Click `File -> Open` (or `Ctrl+O`) and navigate to any desired `.pkt` file inside `labs/` or `final-project-routing-protocols/`.
3. **Simulation Mode**:
   - Toggle to **Simulation Mode** (`Shift+S`) to inspect packet PDUs (ARP, ICMP, OSPF Hello, RIP Updates) traversing the network step-by-step.

---

## License

This project is open-source and licensed under the [MIT License](LICENSE).
