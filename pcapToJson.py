import os
import argparse

def main(originalPcap, outputJson):
    # split pcap ( if pcap size is too large )
    spiltCmd = "tcpdump -r " + originalPcap + "-w tmp -C 20"
    # tcpdump -r 1G.pcap -w output_packet_capture -C 500
    os.system(spiltCmd)

    # convert pcap to json
    
    for splitPcap in 
    convertCmd = "sudo tshark -r " + originalPcap + " -T json >" + outputJson
    os.system(convertCmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pcap to Json')

    parser.add_argument('--r', metavar='test.pcap',required=True, help='Enter the pcap file name to convert json file')
    parser.add_argument('--w', metavar='output.json',required=True, help='Enter the json file name to receive the result')

    args = parser.parse_args()
    originalPcap = args.r
    outputJson = args.w

    main(originalPcap, outputJson)