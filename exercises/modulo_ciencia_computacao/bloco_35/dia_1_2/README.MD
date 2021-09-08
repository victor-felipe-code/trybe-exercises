# Exercício

### Exercício 1 : Defina uma regra de firewall utilizando o comando iptables -A , que bloqueie ( block ou REJECT/DROP ) toda a entrada ( in ou INPUT ) de pacotes utilizando o protocolo ICMP , impedindo assim que a máquina responda ao comando ping . Lembre-se, você pode executar o comando ping para validar se sua regra está funcionando corretamente: ping 127.0.0.1 (você pode adicionar o parâmetro -O para exibir os pings rejeitados também 😉).

    CRIANDO REGRA
    Bloqueando: iptables -A INPUT -j DROP

### Exercício 2 : Exclua a regra anterior utilizando o parâmetro -D .

    Excluindo regra:
        iptables -L --line-numbers
        sudo iptables -D INPUT <1>

### Exercício 3 : Agora vamos criar uma regra para bloquear o tráfego HTTPS. Para isso, iremos bloquear a saída de pacotes ( out ou OUTPUT ). Lembre-se, a porta padrão para esse protocolo é a 443 , para especificá-la utilize o parâmetro --sport . Ele utiliza também o protocolo tcp . Para testar sua regra, tente acessar um site pelo navegador que use o protocolo, como o Youtube, o Google ou o Facebook.

    iptables -A OUTPUT -p tcp --dport 443 -j DROP

### Exercício 4 : Bloqueie agora o tráfego de saída para HTTP. Lembre-se, também é utilizado o protocolo tcp e a porta 80 . Para testar sua regra, tente acessar um site pelo navegador que use HTTP .

    iptables -A INPUT -p tcp --dport 80 -j DROP

### Exercício 5 : Para finalizar, vamos limpar todas as regras. Para isso, utilize o comando --flush do iptables (Linux).

    iptables --flush

### Exercício 6 : Agora, vamos utilizar um tipo de proxy bem legal que pode ser bastante útil no nosso dia como pessoas desenvolvedoras: o NGROK . Com ele conseguimos criar um túnel para o nosso localhost .

    ### 1-Crie um servidor HTTP em sua máquina executando na porta 80 , pode ser um front-end ou um back-end criado em aulas anteriores.

Baixe o ngrok e extraia o arquivo baixado em uma pasta de sua preferência, conforme instruções no site oficial .
Conforme instruções do site, crie um túnel para a porta 80 de sua máquina.
Acesse o o link disponibilizado em seu navegador. Utilize ele para acessar de outros dispositivos, como seu smartphone ou outro computador 😎
