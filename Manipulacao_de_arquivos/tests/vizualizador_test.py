import CRUD.leitor_de_dados as leitor
import Manipulacao_de_arquivos.manipulador_de_csv as csv
memotia_csv = csv.conversor_de_csv_em_lista('controle.csv')

print(leitor.ler_saldo_total(memotia_csv))