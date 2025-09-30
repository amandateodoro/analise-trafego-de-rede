1. Captura de tráfego:
   sudo timeout 60 tcpdump -i <interface> -nn -ttt ip > trafego.txt

2. Executar análise:
   python3 analise_trafego.py

3. Arquivos:
   - trafego.txt : saída do tcpdump
   - relatorio.csv : relatório com análise
   - analise_trafego.py : script Python

4. Colunas do CSV:
   - IP: endereço IP de origem
   - Total_Eventos: número de pacotes do IP
   - Detectado_PortScan: "Sim" se tentou mais de 10 portas em 60s, senão "Não"

5. Limitações:
   - Pouco tráfego pode não mostrar nada
   - Pode marcar serviços legítimos como port scan
   - Só funciona para IPv4 no formato do tcpdump
