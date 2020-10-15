Def interceptar (packet):
  try:
    if pakcet['IP']['src] == '172.17.0.2': #Dirección IP del cliente
                    if packet['MDNS']['count.queries'] == 1: #Campo Question del msj MDNS
                            print ('Campo a modificar "count.queries": ')
                            print (packet['MDNS']['count.queries'])
                            print ('Nuevo campo "count.queries":')
                            packet['MDNS']['count.queries'] = 10
                            print (packet['MDNS']['count.queries']) 
                            return packet
  except:
                    return packet
