while True:
    
    # Solicita ao usuário o CPF no formato xxx.xxx.xxx-xx
    cpf = str(input('Digite seu CPF: '))
    
    # Condição para validçaõ do CPF, se esta faltando os separadores
    if len(cpf) < 13 or cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        print('Formato de CPF inválido!')
        continue  # Se o CPF estiver com formato incorreto, repete a solicitação

    # Retira os espaços e os símbolos do cpf
    cpf_formatado = cpf.replace(".", "").replace("-", "")  
    
    # Condição para verificar se o cpf contém apenas números, se não for númerico
    # retorna  uma mensagem para o usuáriio
    if not cpf_formatado.isdigit():
        print('O CPF deve conter apenas números!')
        continue  # Se o CPF estiver com formato incorreto, repete a solicitação
    
    # Calculo do primeiro digíto 
    cont = 10
    soma_total = 0
    
    # Percorre até o ultimo número do cpf antes do " - "
    for item in cpf_formatado[:9]:  
        
        # Multiplica cada item com o contador em ordem decrescente
        soma = int(item) * cont 
        soma_total += soma  # Soma a multiplicação de cada item pelo contador
        cont -= 1  # Diminui o contador a cada iteração
    
    #  O resultado soma todos os valores percorridos  no cpf antes do hífen
    # E faz a divisão inteira pelo o número de itens percorridos
    resultado = (soma_total * 10) % 11
    
    # Condição para verificar se o primeiro digíto é 0
    primeiro_digito = 0 if resultado > 9 else resultado
    print(f'O primeiro digíto do seu cpf é {primeiro_digito}')
    
    # Calculo para verificar osegundo digíto
     
    cont2 = 11  # Contador para percorrer até o primeiro digíto do CPF
      
    soma_digito2 = 0
    
    # Laço para percorrer até o primeiro digíto
    for item in cpf_formatado[:10] + str(primeiro_digito):
        soma_digito2 += int(item) * cont2  # Soma a multiplicação de cada item pelo contador
        cont2 -= 1  # Diminui o contador a cada iteração
    
    #  O resultado soma todos os valores percorridos até o primeiro digíto
    # E faz a divisão inteira pelo o número de itens percorridos
    resultado_digito2 = (soma_digito2 * 10) % 11
    
    # Condição para verificar se o segundo digíto é 0 ou algum outro número 
    segundo_digito = 0 if resultado_digito2 > 9 else resultado_digito2
    
    print(f'O segundo digíto é {segundo_digito}')
    
    # Condição para verificar se os dois ultimos digítos coicidem, com os valores calculados
    if cpf_formatado[-2] == str(primeiro_digito) and cpf[-1] == str(segundo_digito):
        print('CPF válido')
    else:
        print('CPF inválido')
    break  # Interrompe o loop após verificar o CPF
   