from scapy.all import sniff, IP

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        payload_size = len(packet[IP].payload)
        return {"src_ip": src_ip, "dst_ip": dst_ip, "payload_size": payload_size}
    return None

def start_monitoring(interface="eth0"):
    sniff(iface=interface, prn=analyze_packet, filter="tcp", store=0)
