def interceptar(packet):
  try:
    if packet['IP']['src'] == '172.17.0.3':
      if packet['MDNS']['count.auth_rr'] == 0:
        print('Campo a cambiar "count.auth_rr": ')
        print(packet['MDNS']['count.auth_rr'])
        print('Nuevo campo "count.auth_rr": ')
        packet['MDNS']['count.auth_rr'] = 100
        print(packet['MDNS']['count.auth_rr'])
        return packet
  except:
    return packet
