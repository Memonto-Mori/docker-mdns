Def interceptar(packet):
  if packet['IP']['src'] == '172.17.0.2':
    packet['MDNS']['id'] = '0x69'
    print ("Interceptando tráfico MDNS, modificación cabecera MDNS id")
    return packet
