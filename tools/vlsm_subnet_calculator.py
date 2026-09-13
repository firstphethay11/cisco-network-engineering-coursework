#!/usr/bin/env python3
"""
VLSM & CIDR Subnet Calculator
=============================
Part of Cisco Network Engineering Coursework.
Performs RFC 1878 / RFC 4632 Variable-Length Subnet Mask (VLSM) allocation,
CIDR address planning, wildcard mask calculations, and host capacity analysis.
"""

import math
import sys
from typing import List, Dict, Any

def ip_to_int(ip: str) -> int:
    octets = [int(x) for x in ip.split('.')]
    return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]

def int_to_ip(val: int) -> str:
    return f"{(val >> 24) & 0xFF}.{(val >> 16) & 0xFF}.{(val >> 8) & 0xFF}.{val & 0xFF}"

def cidr_to_netmask(prefix: int) -> str:
    mask_val = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
    return int_to_ip(mask_val)

def cidr_to_wildcard(prefix: int) -> str:
    wc_val = (~(0xFFFFFFFF << (32 - prefix))) & 0xFFFFFFFF
    return int_to_ip(wc_val)

def calculate_vlsm(base_network: str, base_prefix: int, requirements: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Allocates subnets using the Variable Length Subnet Mask (VLSM) algorithm.
    Sorts requests in descending order of needed hosts.
    """
    sorted_reqs = sorted(requirements, key=lambda r: r['hosts'], reverse=True)
    
    current_ip = ip_to_int(base_network)
    allocated = []

    for req in sorted_reqs:
        needed_hosts = req['hosts']
        total_ips = needed_hosts + 2
        host_bits = max(2, math.ceil(math.log2(total_ips)))
        prefix = 32 - host_bits
        block_size = 1 << host_bits
        
        # Align current_ip to block boundary
        if current_ip % block_size != 0:
            current_ip = ((current_ip // block_size) + 1) * block_size
            
        net_ip = current_ip
        broadcast_ip = net_ip + block_size - 1
        first_host = net_ip + 1
        last_host = broadcast_ip - 1
        usable_hosts = block_size - 2
        
        allocated.append({
            'name': req['name'],
            'requested_hosts': needed_hosts,
            'allocated_hosts': usable_hosts,
            'network': f"{int_to_ip(net_ip)}/{prefix}",
            'netmask': cidr_to_netmask(prefix),
            'wildcard': cidr_to_wildcard(prefix),
            'first_usable': int_to_ip(first_host),
            'last_usable': int_to_ip(last_host),
            'broadcast': int_to_ip(broadcast_ip),
            'prefix': prefix
        })
        
        current_ip += block_size
        
    return allocated

def print_vlsm_table(base_net: str, base_cidr: int, allocations: List[Dict[str, Any]]) -> None:
    print("\n" + "=" * 94)
    print(f"  CISCO CCNA VLSM SUBNET ALLOCATION TABLE — Base: {base_net}/{base_cidr}")
    print("=" * 94)
    header = f"{'Subnet / Segment':<25} | {'Req':<4} | {'Alloc':<5} | {'Network / CIDR':<18} | {'Usable Range':<31}"
    print(header)
    print("-" * 94)
    for a in allocations:
        usable = f"{a['first_usable']} - {a['last_usable']}"
        print(f"{a['name']:<25} | {a['requested_hosts']:<4} | {a['allocated_hosts']:<5} | {a['network']:<18} | {usable:<31}")
    print("=" * 94 + "\n")

def run_sample_vlsm() -> None:
    print("[*] Running Coursework Lab VLSM Allocation Model...")
    base_net = "192.168.0.0"
    base_cidr = 24
    sample_reqs = [
        {"name": "VLAN 20 (Faculty/Staff)", "hosts": 60},
        {"name": "VLAN 10 (Management)", "hosts": 28},
        {"name": "VLAN 30 (Student Lab)", "hosts": 14},
        {"name": "WAN Link (R1-R2 P2P)", "hosts": 2},
        {"name": "WAN Link (R2-R3 P2P)", "hosts": 2},
    ]
    results = calculate_vlsm(base_net, base_cidr, sample_reqs)
    print_vlsm_table(base_net, base_cidr, results)

if __name__ == "__main__":
    run_sample_vlsm()
