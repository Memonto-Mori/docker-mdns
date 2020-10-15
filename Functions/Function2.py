def interceptar(packet):
  try:
    if packet['IP']['src'] == '172.17.0.2':
      if packet['MDNS']['count.answers'] == 0:
        print('Campo a modificar "count.answers": ')
        print(packet['MDNS']['count.answers'])
        print('Nuevo campo "count.answers": ')
        packet['MDNS']['count.answers'] = 100
        print(packet['MDNS']['count.answers'])
        return packet
  except:
    return packet
