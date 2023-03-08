T1 = float(0)
T2 = float(1)
T3 = float(0)
print('-'*42)
print(''*3,'Consulta de Sequência de Fibonacci')
print('-'*42)
Valor = float(input("Digite o número: "))
while Valor > T3:
  T3 = T1 + T2
  T1 = T2
  T2 = T3
  if Valor==0 or Valor==1:
    print('O número faz parte da sequencia de fibonacci.')
  elif Valor == T3:
    print("O número faz parte da sequência de Fibonacci.")
  else:
    print('O número não faz parte da sequência de Fibonacci')
    break