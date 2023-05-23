import CRUD.deletador_de_dados as crud
import Manipulacao_de_arquivos.criação_de_arquivo as ca

arq = ca.criararquivo()
saldo = crud.ler_saldo_total(arq)

print(saldo)

