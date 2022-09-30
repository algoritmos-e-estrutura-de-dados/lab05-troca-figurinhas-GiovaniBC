def maximizar_troca_de_figurinhas(figurinhaMaria, figurinhaJoao, A, B):

    indm = 0
    indj = 0 
    i = 0
    j = 0
    m = 0
    n = 0

    for i in range(int(A)):
      for j in range(int(B)):
        if figurinhaMaria[i] == figurinhaJoao[j]:
          indm += 1
   

 
    for m in range(int(B)):
      for n in range(int(A)):
        if figurinhaJoao[m] == figurinhaMaria[n]:
          indj += 1
   
    if (int(A) - int(indm)) < (int(B) - int(indj)):
        return print(f"O máximo de figurinhas para troca é:{int(A) - int(indm)}")
    else:
        return print(f"O máximo de figurinhas para troca é:{int(B) - int(indj)}")
 
  

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao, A, B)