import hash_table

ht = hash_table.HashTableChaining(11)
ht.insert(hash_table.Aluno("Maria", 20, 12345))
ht.insert(hash_table.Aluno("João", 22, 67890))
ht.insert(hash_table.Aluno("Ana", 19, 54321))
ht.insert(hash_table.Aluno("Carlos", 21, 54321))

ht.display()

print("\nRemoving RGM 67890:")
aluno_removido = ht.remove(67890)
if aluno_removido:
    print("Aluno removido com sucesso.")
else:
    print("Aluno não encontrado para remoção.")

ht.display()

print("\nSearching for RGM 67890:")
aluno = ht.search(67890)
if aluno:
    print(f"Aluno encontrado: {aluno}")
else:
    print("Aluno não encontrado.")