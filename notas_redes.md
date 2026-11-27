# Notas de Redes

## Protocolo
- define como a comunicação vai ser efetuada
- comutação de circuito, comunicação direta e dedicada
- comutação de pacotes, mensagem divididas em pacotes se juntando no destino, permite escalar

## Gateway e IP
- Gateway, dispositivo que liga a rede local a uma rede como a internet. Cada computador é configurado com o IP do gateway, para onde envia os pacotes que têm destino fora da rede local. Esse IP é o mesmo para todas as máquinas da rede.
- IP, endereço Ip é um número usado para comunicação, identifica o computador em uma rede, pode ser distribuído automatico também. O protocolo IP, os dados são enviados por pacotes sem precisar nenhuma definição antes da comunicação
- endereçamento define como organizar os IPs até em sub-redes 
- encaminhamento é feito por roteadores que a salto a salto  vão escolhendo o caminho, usando protocolos para efetivar a comunicação

## DHCP e DNS
- DHCP, atribui o IP , mas também a máscara, o gateway e o servidor DNS, automaticamente aos dispositivos emprestado por um tempo DORA discover, offer, request e acknowledge
- DNS, traduz nomes de domínio em endereços de IP costuma usar a porta 53 e que as respostas ficam em cache por um tempo.

## TCP e UDP
- TCP protocolo de controle de transmissão, orientado a conexão, verifica se os dados transmitido estão sendo enviados em uma ordem correta, three way handshake cliente manda um pedido com um código, servidor responde, o cliente responde com um pacote de confirma o estabelecimento de conexão, assim ele reenvia o que se perdeu.
- UDP, não orientado a conexão, sem a garantia de entrega de pacotes, se o pacote se perder UDP não o reenvia, pode ser realizado pela aplicação, não confiável, velocidade mais rápida.

## Máscara da Rede
- Máscara da rede é em 32 bits divididos em 4 octetos de 8 bits, que se divide em parte da rede, todos dispositivos nessa mesma sub-rede compartilham o mesmo prefixo de rede, e a parte do dispositivo específica da máquina

- Notação /24 os 24 bits mais significativos são usados para rede os ultimos 8 são usados para os dispositivos

- IP público é roteável na internet e identifica a rede perante o mundo externo

- IP privado só tem significado em redes locais, há três faixas padrão definidas 10.0.0.0 – 10.255.255.255 mascára /8, 172.16.0.0 – 172.31.255.255 máscara /12 e 192.168.0.0 – 192.168.255.255 máscaras /16 o /24 é o tamanho de rede mais comum dentrro dele em casa

## Portas 
- Uma porta é um identificador de 16 bits que direciona os dados para um processo na máquina 

- Porta 22 (SSH): usada para acesso remoto seguro e tranferência segura de arquivos criptografando a sessão

- Porta 53 (DNS): Tradução de domínios em IPs, usa UDP nas consultas normais e TCP e alguns casos

- Porta 80 (HTTP): padrão para tráfego da web não criptografado

- Porta 443 (HTTPS): porta para tráfego da web criptografado protegendo a integridade dos dados entre o navegador e servidor 