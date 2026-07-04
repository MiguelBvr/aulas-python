tarefas = []
adc_ou_sair = 0


print('1. Adcionar string\n2.Sair')

adc_ou_sair = int(input(''))

while adc_ou_sair == 1:

    recebe_tarefa = input('Digite uma tarefa para adcionar à lista ')
    print('-' * 25)

    tarefas.append(recebe_tarefa)
    
    print('1. Adcionar string\n2.Sair')
    adc_ou_sair = int(input(''))

if adc_ou_sair == 2:
    print(f'Foram adcionados {len(tarefas)} tarefas à lista')
    
    tarefas.sort()
    print(tarefas)
    



