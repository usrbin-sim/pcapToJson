import os
import argparse

def convertJson(pcapChunk):
    convertCmd = "sudo tshark -r ./splitPcap/" + pcapChunk + " -T json >./splitJson/" + pcapChunk +".json"
    os.system(convertCmd)

def main(originalPcap, outputJson):
    # split pcap ( if pcap size is too large )
    spiltCmd = "tcpdump -r " + originalPcap + " -w ./splitPcap/tmp -C 100"
    os.system(spiltCmd)
    print("[+] Success to split pcap")

    path = "./splitPcap/"
    fileList = os.listdir(path)
    p = Pool()
    p.map(convertJson, fileList)

    #os.system("sudo tshark -r ./originalPcap/1G.pcap -T ek >./1G.json")
    os.system("rm ./splitPcap/*")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pcap to Json')

    parser.add_argument('--r', metavar='test.pcap',required=True, help='Enter the pcap file name to convert json file')
    parser.add_argument('--w', metavar='output.json',required=True, help='Enter the json file name to receive the result')

    args = parser.parse_args()
    originalPcap = args.r
    outputJson = args.w

    main(originalPcap, outputJson)