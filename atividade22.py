# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.

# Inicializa a soma
soma = 0

while True:
    # Solicita um número ao usuário
    numero = float(input("Digite um número (ou 0 para sair): "))
    
    # Verifica se o número digitado é 0
    if numero == 0:
        break  # Sai do loop se o número for 0
    
    # Adiciona o número à soma
    soma += numero

# Exibe o resultado total
print(f"A soma total é: {soma}")


    

