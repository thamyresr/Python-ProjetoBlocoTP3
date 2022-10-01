import psutil
import socket
import cpuinfo

def menu():
    ativaMenu = True
    while ativaMenu:
        print('1 - Informação do Processador')
        print('2 - Informação da Memória')
        print('3 - Informação do Disco')
        print('4 - Informação do Rede')
        print('5 - Resumo das informações')
        print('0 - Sair')
        escolha = int(input('Escolha uma opção:'))
        if escolha < 0 or escolha > 5:
            print('Opção inválida!')
        else:
            if escolha == 1:
                informacaoProcessador()
            elif escolha == 2:
                informacaoMemoria()
            elif escolha == 3:
                informacaoDisco()
            elif escolha == 4:
                informacaoIP()
            elif escolha == 5:
                resumoInformacao()
            elif escolha == 0:
                ativaMenu = False

def informacaoProcessador():
    info_processador = cpuinfo.get_cpu_info()
    info_cpu = psutil.cpu_percent(interval=1)

    print('INFORMAÇÕES SOBRE PROCESSADOR')
    print('Modelo do processador:',info_processador['brand'])
    print('Arquitetura:', info_processador['arch'])
    print('Número de núcleos:', psutil.cpu_count())
    print('Palavra(bits):', info_processador['bits'])
    print('Frequência:', psutil.cpu_freq()[2], 'MHz')
    print('Porcentagem de uso - CPU:', info_cpu, '%\n')

def informacaoMemoria():
    info_memoria = psutil.virtual_memory()
    memoria_total = round(info_memoria.total/(1024*1024*1024), 2)
    memoria_disponivel = round(info_memoria.free/(1024*1024*1024), 2)
    memoria_uso = info_memoria.percent

    print('INFORMAÇÕES SOBRE A MEMÓRIA:')
    print('Memória Total:', memoria_total, 'GB')
    print('Memória Utilizada:', memoria_uso, '%')
    print('Memória Disponível:', memoria_disponivel, 'GB\n')

def informacaoDisco():
    info_disco = psutil.disk_usage(".")
    disco_total = round(info_disco.total/(1024*1024*1024), 2)
    disco_uso_porcentagem = info_disco.percent
    disco_disponivel = round(info_disco.free/(1024*1024*1024), 2)

    print('INFORMAÇÕES SOBRE O DISCO:')
    print('Disco Total:', disco_total, 'GB')
    print('Disco Utilizado:', disco_uso_porcentagem, '%')
    print('Disco Disponível:', disco_disponivel, 'GB\n')

def informacaoIP():
    info_hostname = socket.gethostname()
    info_rede = socket.gethostbyname(info_hostname)

    print('INFORMAÇÕES SOBRE O ENDEREÇO DE IP:')
    print('Endereço de IP:', info_rede)

def resumoInformacao():
    info_processador = cpuinfo.get_cpu_info()
    info_cpu = psutil.cpu_percent(interval=1)
    info_memoria = psutil.virtual_memory()
    memoria_total = round(info_memoria.total/(1024*1024*1024), 2)
    info_disco = psutil.disk_usage(".")
    disco_total = round(info_disco.total/(1024*1024*1024), 2)
    info_hostname = socket.gethostname()
    info_rede = socket.gethostbyname(info_hostname)

    print('Modelo do processador:',info_processador['brand'])
    print('Porcentagem de uso - CPU:', info_cpu, '%')
    print('Memória Total:', memoria_total, 'GB')
    print('Disco Total:', disco_total, 'GB')
    print('Endereço de IP:', info_rede, '\n')

menu()