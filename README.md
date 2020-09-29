# docker-mdns
Proyecto para ejecutar una aplicación asociada a un servico MDNS que establece una comunicación entre Cliente/Servidor 

# Uso
Crea el contenedor por medio del siguiente comando:
```
docker build .
```
No obstante, si se desea etiquetar la imagen:

```
docker build -t <NAME ETIQUETA> .
```
Ejecute el contenedor con el CONTAINER ID:
```
docker run -it <CONTAINER ID>
```
Perfecto, la consola de elixir ya esta en marcha! 

para hacer uso del cliente/servidor MDNS, 
visite https://github.com/rosetta-home/mdns

# Análisis del tráfico capturado entre host
En el siguiente vinculo https://youtu.be/YrY_72C9yTk, se aprecia una explicación referente a ciertos comportamientos que tuvo la comunicación MDNS entre los host establecidos en la red de la interface de docker.
