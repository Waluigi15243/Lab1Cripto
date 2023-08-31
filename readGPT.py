from scapy.all import *
import string

def cesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    packets = rdpcap('capturaGPT.pcapng')
    filtered_packets = [packet for packet in packets if ICMP in packet and packet[IP].dst == '8.8.8.8']
    
    data_bytes = b""
    for packet in filtered_packets:
        data_bytes += packet[Raw].load[-1:]

    data_string = data_bytes.decode('utf-8')
    print("Datos extraídos:", data_string)

    variations = []
    for shift in range(1, 26):
        shifted_data = cesar_cipher(data_string, shift)
        variations.append(shifted_data)

    print("\nVariaciones usando el cifrado Cesar:")
    for idx, var in enumerate(variations):
        print(f"Shift {idx + 1}: {var}")

if __name__ == "__main__":
    main()
