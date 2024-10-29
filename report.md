cat > /app/report.md << 'EOL'
# CENG 435 - Programming Assignment Phase 1
https://github.com/p2x0i/covertovert

## Group Information
- Group ID: 23
- Member:
  - Pinar Aksoy (2374338)

## Implementation Details

### Sender Implementation
- Created ICMP echo request packets with TTL=1
- Implemented using Scapy for packet creation
- Correct source IP (172.18.0.2) configuration

### Receiver Implementation
- Captured and filtered ICMP packets
- Verified TTL=1 packets
- Properly displayed packet details

### Verification Results
Tested with packet details:
- Source IP: 172.18.0.2
- Destination IP: 172.18.0.3
- TTL: 1
- ICMP Type: echo-request

### Documentation
- Generated complete Sphinx documentation
- Included proper code documentation
- Created HTML documentation with proper navigation
EOL