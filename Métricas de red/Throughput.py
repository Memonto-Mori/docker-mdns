def metricaT(packet):
  import time as t 
  if (packet['UDP']{'dstport'] == 5353:
    try:
      time = int(t.time())
      try:
        packet.mapa[time] = packet.mapa[time] + (packet['IP']['len']*8) + 14
      except:
        packet.mapa[time] = (packet['IP']['len']*8) + 14
      print (packet.mapa)
    except:
      map = {}
      packet.global_var('mapa',map)
      packet.mapa[time] = (packet['IP']['len']*8)+14
      print (packet.mapa)
  return packet
