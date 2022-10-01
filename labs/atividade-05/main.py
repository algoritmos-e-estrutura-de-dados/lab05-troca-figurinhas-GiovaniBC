def maximizar_troca_de_figurinhas(figurinhasMaria, figurinhasJoao):
    figM = 0
    figJ = 0

    figurinhasMaria = list(set(figurinhasMaria))
    figurinhasJoao = list(set(figurinhasJoao))


    for i in range(len(figurinhasMaria)):
        for j in range(len(figurinhasJoao)):
            if figurinhasMaria[i] == figurinhasJoao[j]:
                figM += 1


    for k in range(len(figurinhasJoao)):
        for l in range(len(figurinhasMaria)):
            if figurinhasJoao[k] == figurinhasMaria[l]:
                figJ += 1




    if (len(figurinhasMaria) - int(figM)) < (len(figurinhasJoao) - int(figJ)):
        return print(f"Máximo de figurinhas para troca {len(figurinhasMaria) - int(figM)}")
    else:
        return print(f"Máximo de figurinhas para troca {len(figurinhasJoao) - int(figJ)}")


if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)