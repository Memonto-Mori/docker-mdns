def interceptar(packet):
  try:
    if packet['IP']['src'] == '172.17.0.3':
      if packet['MDNS']['count.add_rr'] == 0:
        print('Campo a cambiar "count.add_rr": ')
        print(packet['MDNS']['count.add_rr'])
        print('Nuevo campo "count.add_rr": ')
        packet['MDNS']['count.add_rr'] = 7
        print(packet['MDNS']['count.answers'])
        return packet
  except:
    return packet
