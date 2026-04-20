Network-Analyzer-Pro 🌐
Part 1: The Monitoring Infrastructure
 The Network Security Trilogy
This is the foundational project in a three-part series exploring network security and performance:

Network-Analyzer-Pro (Current): Real-time traffic monitoring and packet inspection. https://github.com/swarnili/Network-Analyzer-Pro

VPN-Performance-Evaluator: Security modeling and encryption trade-offs. https://github.com/swarnili/VPN-Performance-Evaluator

NetProbe-V3: Advanced statistical analytics and automated insight engine. https://github.com/swarnili/NetProbe-V3 

 Project Overview
Network-Analyzer-Pro is a real-time network diagnostic tool designed to provide deep visibility into local and external traffic. It serves as the "Infrastructure Layer," capturing raw data packets and visualizing flow patterns to help administrators identify anomalies, monitor bandwidth usage, and troubleshoot connectivity issues.

 Key Features
Live Packet Capture: Real-time monitoring of TCP/UDP/ICMP traffic.

Traffic Visualization: Dynamic charts representing packet distribution and frequency.

Protocol Breakdown: Instant analysis of protocol types to identify network overhead.

Endpoint Detection: Tracks source and destination IPs to map network activity.

Scalable Foundation: Built with a modular backend to allow for the security and analytics layers added in Parts 2 and 3.

 Technical Stack
Backend: Python (Flask)

Traffic Handling: Scapy / Socket programming for packet sniffing.

Frontend: HTML5, CSS3 (Modern Dark UI), JavaScript (Chart.js).



The Network Security Trilogy: Infrastructure to Intelligence
This repository is part of a comprehensive three-module ecosystem designed to explore the lifecycle of network telemetry. The project series transitions from raw data acquisition to security modeling and concludes with automated analytical reporting.

Phase 1: Network-Analyzer-Pro — The Eyes: Focuses on the "Monitoring Layer." It utilizes Python-based packet sniffing to capture real-time TCP/UDP traffic, providing essential visibility into protocol distribution and network flow.

Phase 2: VPN-Performance-Evaluator — The Shield: Focuses on the "Security Layer." This module introduces encryption overhead and VPN tunneling simulations, modeling the mathematical trade-offs between data privacy (AES-256) and network throughput.

Phase 3: NetProbe-V3 — The Brain: Focuses on the "Intelligence Layer." It acts as the final analytical brain, using statistical variance to calculate stability scores and generating automated, multi-format (PDF/CSV) research insights from the data captured in the previous phases.

Together, these projects demonstrate a full-stack engineering journey through network infrastructure, cybersecurity trade-offs, and data-driven interpretation.