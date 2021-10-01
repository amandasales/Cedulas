print('----------BANCO-------------')
valor = int(input('Quanto você deseja sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
      if total >= ced:
            total -= ced
            totced = totced + 1
      else:
            print(f'{totced} cédulas de {ced} reais')
            if ced == 50:
                  ced = 20
            elif ced == 20:
                  ced = 10
            elif ced == 10:
                  ced = 1
            totced = 0
            if total == 0:
                break
print('Volte sempre!')
