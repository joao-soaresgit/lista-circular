import time

class Processo:
    def __init__(self, nome, prioridade, taxaCompleto, taxaPorCiclo, tempoProcessamento):
        self.nome = nome
        self.prioridade = prioridade
        self.taxaCompleto = taxaCompleto
        self.taxaPorCiclo = taxaPorCiclo
        self.tempoProcessamento = tempoProcessamento
        self.prox = None

class ListaCircular:
    def __init__(self):
        self.primeiro = None

    def insere(self, nome, prioridade, taxaCompleto, taxaPorCiclo, tempoProcessamento):
        novo_no = Processo(nome, prioridade, taxaCompleto, taxaPorCiclo, tempoProcessamento)

        if self.primeiro is None:
            self.primeiro = novo_no
            novo_no.prox = self.primeiro  
        else:
            atual = self.primeiro
            while atual.prox != self.primeiro and atual.prioridade < prioridade:
                atual = atual.prox
            
            # Inserir o novo processo em ordem de prioridade
            novo_no.prox = atual.prox
            atual.prox = novo_no

    def remover(self, nome):
        if self.primeiro is None:
            print("A lista está vazia!")
            return

        atual = self.primeiro
        anterior = None
        while True:
            if atual.nome == nome:
                if anterior is None: 
                    if atual.prox == self.primeiro:  # Se for o único processo
                        self.primeiro = None
                    else:
                        # Encontrar o último para atualizar o ponteiro
                        temp = self.primeiro
                        while temp.prox != self.primeiro:
                            temp = temp.prox
                        self.primeiro = atual.prox
                        temp.prox = self.primeiro
                else:
                    anterior.prox = atual.prox
                return
            anterior = atual
            atual = atual.prox
            if atual == self.primeiro:
                break
        print(f"Processo '{nome}' não encontrado na lista.")

    def imprimir(self):
        atual = self.primeiro
        while atual is not None:
            print(f"{atual.nome} entrou no processador")
            time.sleep(atual.tempoProcessamento)  

            # Atualiza a taxa de completamento
            atual.taxaCompleto += atual.taxaPorCiclo
            if atual.taxaCompleto >= 100:
                atual.taxaCompleto = 100  # Não pode ultrapassar 100%

            print(f"{atual.nome} saiu do processador com taxa de {atual.taxaCompleto}%")

            # Se o processo estiver completo, removê-lo da lista
            if atual.taxaCompleto == 100:

                print(f"{atual.nome} foi finalizado")
                self.remover(atual.nome)

            # Avança para o próximo processo
            atual = atual.prox
            if self.primeiro is None:
                break


lista = ListaCircular()


lista.insere("Proc1", 1, 0, 5, 1)
lista.insere("Proc2", 2, 0, 10, 1)
lista.insere("proc3", 3, 0, 20, 1)
lista.insere("proc4", 4, 0, 25, 1)
lista.insere("proc5", 5, 0, 50, 1)


lista.imprimir()
