import argparse
from scapy.all import IP, ICMP, send

def enviar_icmp_stealth(cadena):
    count = 0
    for char in cadena:
        count = count + 1
        paquete = IP(dst="8.8.8.8") / ICMP() / char
        send(paquete, verbose=0)
        print("Sent 1 packet.")
    print(count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enviar caracteres en modo stealth usando ICMP.")
    parser.add_argument("cadena", type=str, help="Cadena a enviar en modo stealth.")
    args = parser.parse_args()

    enviar_icmp_stealth(args.cadena)
