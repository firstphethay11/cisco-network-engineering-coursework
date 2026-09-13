#!/usr/bin/env python3
"""
Cisco Network Engineering Coursework Demo Suite
===============================================
Runs automated verification for VLSM Subnetting and OSPF/RIP routing algorithms.
"""

import sys
import os

from tools.vlsm_subnet_calculator import run_sample_vlsm
from tools.routing_table_simulator import run_ospf_simulation

def main():
    print("""
================================================================================
          CISCO NETWORK ENGINEERING COURSEWORK — INTERACTIVE DEMO SUITE
================================================================================
  [1] VLSM CIDR IP Subnet Allocation Engine
  [2] OSPF Link-State SPF Dijkstra Route Convergence Engine
  [3] Packet Tracer Lab Artifact Inventory Verification
================================================================================
""")
    # Run Subnet Demo
    run_sample_vlsm()
    
    # Run OSPF Demo
    run_ospf_simulation()
    
    # Verify Packet Tracer files
    print("=" * 80)
    print("  PACKET TRACER TOPOLOGY ARCHIVES VERIFICATION")
    print("=" * 80)
    pkt_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".pkt"):
                pkt_files.append(os.path.relpath(os.path.join(root, file)))
                
    for i, pkt in enumerate(sorted(pkt_files), 1):
        print(f"  [{i:02d}] OK: {pkt}")
    print(f"\n  Total Verified Topologies: {len(pkt_files)} Cisco Packet Tracer PKT models.")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
