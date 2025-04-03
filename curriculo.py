# Gerador de Currículo Simples

# Solicita as informações do usuário
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")
objetivo = input("Digite seu objetivo profissional: ")

# Pede informações de experiência profissional
experiencia = input("Descreva sua experiência profissional: ")

# Monta o currículo formatado
curriculo = f"""
=============================
        CURRÍCULO
=============================
Nome: {nome}
E-mail: {email}
Telefone: {telefone}
Endereço: {endereco}

Objetivo Profissional:
{objetivo}

Experiência Profissional:
{experiencia}
"""

# Salva o currículo em um arquivo de texto
with open("curriculo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(curriculo)

print("\nCurrículo gerado com sucesso! O arquivo 'curriculo.txt' foi criado.")
