import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from hash_table import Aluno, HashTableChaining
import main

M = 11


def chaves_da_lista(tabela, indice):
    chaves = []
    atual = tabela.tabela[indice]
    while atual is not None:
        chaves.append(atual.aluno.rgm)
        atual = atual.prox
    return chaves


class TesteFuncaoHash(unittest.TestCase):
    def setUp(self):
        self.ht = HashTableChaining(M)

    def test_hash_e_chave_mod_11(self):
        for chave, esperado in [(0, 0), (5, 5), (10, 10), (11, 0), (12, 1),
                                (22, 0), (12345, 3), (67890, 9), (54321, 3)]:
            self.assertEqual(self.ht.hash_function(chave), esperado, f"h({chave})")

    def test_tabela_inicia_vazia_com_11_posicoes(self):
        self.assertEqual(len(self.ht.tabela), 11)
        self.assertTrue(all(p is None for p in self.ht.tabela))


class TesteInsercaoEColisoes(unittest.TestCase):
    def setUp(self):
        self.ht = HashTableChaining(M)

    def test_insercao_simples(self):
        self.assertTrue(self.ht.insert(Aluno("Maria", 20, 12345)))
        self.assertEqual(chaves_da_lista(self.ht, 3), [12345])

    def test_colisoes_ficam_no_mesmo_endereco(self):
        # 1, 12, 23 e 34 => todos com h = 1
        for chave in (1, 12, 23, 34):
            self.assertTrue(self.ht.insert(Aluno(f"A{chave}", 20, chave)))
        self.assertEqual(chaves_da_lista(self.ht, 1), [34, 23, 12, 1])
        # Nenhum outro endereço foi ocupado
        for i in range(M):
            if i != 1:
                self.assertIsNone(self.ht.tabela[i])

    def test_todos_os_alunos_com_colisao_sao_encontrados(self):
        for chave in (2, 13, 24, 35, 46):  # h = 2
            self.ht.insert(Aluno(f"A{chave}", 20, chave))
        for chave in (2, 13, 24, 35, 46):
            aluno = self.ht.search(chave)
            self.assertIsNotNone(aluno)
            self.assertEqual(aluno.nome, f"A{chave}")

    def test_colisao_real_dos_dados_do_projeto(self):
        # 12345 e 54321 têm h = 3
        self.ht.insert(Aluno("Maria", 20, 12345))
        self.ht.insert(Aluno("Ana", 19, 54321))
        self.assertEqual(chaves_da_lista(self.ht, 3), [54321, 12345])

    def test_uma_chave_em_cada_endereco(self):
        for i in range(M):
            self.ht.insert(Aluno(f"A{i}", 20, i))
        for i in range(M):
            self.assertEqual(chaves_da_lista(self.ht, i), [i])


class TesteMatriculaDuplicada(unittest.TestCase):
    def setUp(self):
        self.ht = HashTableChaining(M)

    def test_duplicada_e_recusada(self):
        self.assertTrue(self.ht.insert(Aluno("Ana", 19, 54321)))
        self.assertFalse(self.ht.insert(Aluno("Carlos", 21, 54321)))
        self.assertEqual(chaves_da_lista(self.ht, 3), [54321])
        self.assertEqual(self.ht.search(54321).nome, "Ana")  # dados originais mantidos

    def test_duplicada_no_fim_de_lista_com_colisao(self):
        for chave in (1, 12, 23):
            self.ht.insert(Aluno(f"A{chave}", 20, chave))
        # 1 está no fim da lista 23 -> 12 -> 1
        self.assertFalse(self.ht.insert(Aluno("Outro", 30, 1)))
        self.assertEqual(chaves_da_lista(self.ht, 1), [23, 12, 1])

    def test_pode_reinserir_depois_de_remover(self):
        self.ht.insert(Aluno("Ana", 19, 54321))
        self.ht.remove(54321)
        self.assertTrue(self.ht.insert(Aluno("Carlos", 21, 54321)))
        self.assertEqual(self.ht.search(54321).nome, "Carlos")


class TesteRemocaoEmCadaPosicao(unittest.TestCase):
    def setUp(self):
        self.ht = HashTableChaining(M)
        for chave in (1, 12, 23):  # lista do endereço 1: 23 -> 12 -> 1
            self.ht.insert(Aluno(f"A{chave}", 20, chave))

    def test_remover_inicio_da_lista(self):
        self.assertTrue(self.ht.remove(23))
        self.assertEqual(chaves_da_lista(self.ht, 1), [12, 1])
        self.assertIsNone(self.ht.search(23))

    def test_remover_meio_da_lista(self):
        self.assertTrue(self.ht.remove(12))
        self.assertEqual(chaves_da_lista(self.ht, 1), [23, 1])
        self.assertIsNone(self.ht.search(12))

    def test_remover_fim_da_lista(self):
        self.assertTrue(self.ht.remove(1))
        self.assertEqual(chaves_da_lista(self.ht, 1), [23, 12])
        self.assertIsNone(self.ht.search(1))

    def test_remover_todos_esvazia_endereco(self):
        for chave in (12, 1, 23):
            self.assertTrue(self.ht.remove(chave))
        self.assertIsNone(self.ht.tabela[1])

    def test_remover_unico_elemento(self):
        ht = HashTableChaining(M)
        ht.insert(Aluno("Solo", 20, 5))
        self.assertTrue(ht.remove(5))
        self.assertIsNone(ht.tabela[5])

    def test_remover_em_cada_endereco_da_tabela(self):
        ht = HashTableChaining(M)
        for i in range(M):
            ht.insert(Aluno(f"A{i}", 20, i + M))  # chaves 11..21 -> endereços 0..10
        for i in range(M):
            self.assertTrue(ht.remove(i + M), f"endereço {i}")
            self.assertIsNone(ht.tabela[i])
        self.assertTrue(all(p is None for p in ht.tabela))

    def test_remover_inexistente_nao_altera_tabela(self):
        self.assertFalse(self.ht.remove(34))  # mesmo endereço (1), mas não existe
        self.assertFalse(self.ht.remove(7))   # endereço vazio
        self.assertEqual(chaves_da_lista(self.ht, 1), [23, 12, 1])

    def test_remover_duas_vezes(self):
        self.assertTrue(self.ht.remove(12))
        self.assertFalse(self.ht.remove(12))


class TesteBuscaInexistente(unittest.TestCase):
    def setUp(self):
        self.ht = HashTableChaining(M)

    def test_busca_em_tabela_vazia(self):
        self.assertIsNone(self.ht.search(12345))

    def test_busca_em_endereco_vazio(self):
        self.ht.insert(Aluno("Maria", 20, 12345))  # endereço 3
        self.assertIsNone(self.ht.search(4))        # endereço 4, vazio

    def test_busca_em_endereco_ocupado_sem_a_chave(self):
        for chave in (1, 12, 23):
            self.ht.insert(Aluno(f"A{chave}", 20, chave))
        self.assertIsNone(self.ht.search(34))  # h(34) = 1, percorre a lista toda

    def test_busca_depois_de_remover(self):
        self.ht.insert(Aluno("João", 22, 67890))
        self.ht.remove(67890)
        self.assertIsNone(self.ht.search(67890))


class TesteValidacaoMatricula(unittest.TestCase):
    def test_inteiros_validos(self):
        for texto, esperado in [("123", 123), ("  42  ", 42), ("0", 0), ("+7", 7)]:
            self.assertEqual(main.validar_inteiro(texto, minimo=0), (esperado, None))

    def test_entradas_invalidas(self):
        for texto in ["", "   ", "abc", "12.5", "1e3", "12a", "12 34", "--1", "½", "٣"]:
            valor, erro = main.validar_inteiro(texto, minimo=0)
            self.assertIsNone(valor, repr(texto))
            self.assertIsNotNone(erro, repr(texto))

    def test_matricula_negativa_recusada(self):
        valor, erro = main.validar_inteiro("-5", minimo=0)
        self.assertIsNone(valor)
        self.assertIn("maior ou igual a 0", erro)

    def test_limite_maximo(self):
        self.assertIsNone(main.validar_inteiro("200", minimo=1, maximo=150)[0])
        self.assertEqual(main.validar_inteiro("150", minimo=1, maximo=150)[0], 150)


def executar_menu(entradas):
    """Roda o menu com as entradas dadas e retorna tudo o que foi impresso."""
    saida = io.StringIO()
    with patch("builtins.input", side_effect=entradas), redirect_stdout(saida):
        main.main()
    return saida.getvalue()


class TesteMenu(unittest.TestCase):
    def test_encerrar(self):
        self.assertIn("Encerrando o sistema", executar_menu(["0"]))

    def test_opcao_invalida_pede_de_novo(self):
        saida = executar_menu(["9", "x", "0"])
        self.assertEqual(saida.count("Entrada inválida"), 2)

    def test_fluxo_completo(self):
        saida = executar_menu([
            "1", "12345", "Maria", "20",       # inserir
            "1", "54321", "Ana", "19",         # inserir (colide com 12345)
            "1", "54321",                      # duplicada: recusa sem pedir nome
            "2", "54321",                      # buscar existente
            "2", "99999",                      # buscar inexistente
            "4",                               # exibir
            "3", "12345",                      # remover
            "3", "12345",                      # remover de novo (inexistente)
            "0",
        ])
        self.assertIn("h(12345) = 12345 mod 11 = 3", saida)
        self.assertIn("Aluno inserido com sucesso no endereço 3", saida)
        self.assertIn("já existe um aluno com a matrícula 54321", saida)
        self.assertIn("Encontrado no endereço 3: Aluno: Ana", saida)
        self.assertIn("matrícula 99999 não encontrado", saida)
        self.assertIn("Index 3: [Aluno: Ana, Idade: 19, RGM: 54321] -> "
                      "[Aluno: Maria, Idade: 20, RGM: 12345] -> None", saida)
        self.assertIn("removido do endereço 3", saida)
        self.assertIn("Nada foi removido", saida)

    def test_matricula_invalida_no_inserir(self):
        saida = executar_menu(["1", "abc", "-3", "12.5", "7", "Rita", "dez", "0", "21", "2", "7", "0"])
        self.assertEqual(saida.count("Entrada inválida"), 5)  # 3 matrículas + 2 idades
        self.assertIn("Encontrado no endereço 7: Aluno: Rita, Idade: 21", saida)

    def test_nome_vazio_recusado(self):
        saida = executar_menu(["1", "5", "   ", "Leo", "30", "0"])
        self.assertIn("o nome não pode ser vazio", saida)
        self.assertIn("Aluno inserido com sucesso no endereço 5", saida)


if __name__ == "__main__":
    unittest.main(verbosity=2)
