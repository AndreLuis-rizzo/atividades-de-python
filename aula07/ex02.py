idade = int(input('Digite sua idade: '))
if idade >=18:
    print('Voce é maior de idade, vamos ao exames: ')
else:
    print('Voce nao possui idade para obter CNH. ')
exame_psicotecnico = input('Voce foi aprovado no exame psicotecinico? (s/n): ')
exame_legislacao = input('Voce foi aprovado no exame de legislacao? (s/n): ')
exame_direcao = input('Voce foi aprovado no exame de direcao? (s/n): ')
if exame_psicotecnico.lower() == 's' and exame_legislacao.lower() == 's'and exame_direcao.lower() == 's':
    print('Voce esta apto a obter sua CNH. ')
elif exame_psicotecnico.lower() == 'n'and exame_legislacao.lower() == 'n' and exame_direcao.lower() == 's':
    print('Voce nao aprovado em todos os testes. ')
elif exame_psicotecnico.lower() == 's'and exame_legislacao.lower() == 's' and exame_direcao.lower() == 'n':
    print('Voce nao foi aprovado em todos os testes. ')
elif exame_psicotecnico.lower() == 'n'and exame_legislacao.lower() == 's' and exame_direcao.lower() == 'n':
    print('Voce nao foi aprovado em todos os testes. ')
elif exame_psicotecnico.lower() == 's'and exame_legislacao.lower() == 'n' and exame_direcao.lower() == 's':
    print('Voce nao foi aprovado em todos os testes. ')
else:
    print('Voce nao esta apto para obter sua CNH. ') 