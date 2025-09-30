import re
import csv
from collections import defaultdict

INPUT_FILE = "trafego.txt"
OUTPUT_FILE = "relatorio.csv"

# Regex para pegar timestamp, IP origem, porta origem, IP destino e porta destino
LINE_RE = re.compile(
    r'^\s*([0-9]+\.[0-9]+)\s+'       # timestamp
    r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\.([0-9]+)\s+>\s+'  # srcIP.srcPort
    r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\.([0-9]+)'         # dstIP.dstPort
)

def parse_line(line):
    m = LINE_RE.search(line)
    if not m:
        return None
    ts = float(m.group(1))
    src_ip = m.group(2)
    dst_port = int(m.group(5))
    return ts, src_ip, dst_port

def main():
    eventos = defaultdict(list)   # {IP: [(tempo, porta), ...]}
    total = defaultdict(int)

    with open(INPUT_FILE) as f:
        for line in f:
            parsed = parse_line(line)
            if not parsed:
                continue
            ts, ip, port = parsed
            eventos[ip].append((ts, port))
            total[ip] += 1

    rows = []
    for ip, lista in eventos.items():
        lista.sort()
        detectado = "Não"
        for i in range(len(lista)):
            inicio = lista[i][0]
            portas = {lista[i][1]}
            for j in range(i+1, len(lista)):
                if lista[j][0] - inicio <= 60:
                    portas.add(lista[j][1])
                else:
                    break
            if len(portas) > 10:
                detectado = "Sim"
                break
        rows.append((ip, total[ip], detectado))

    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP", "Total_Eventos", "Detectado_PortScan"])
        for r in rows:
            writer.writerow(r)

    print("Relatório gerado em", OUTPUT_FILE)

if __name__ == "__main__":
    main()
