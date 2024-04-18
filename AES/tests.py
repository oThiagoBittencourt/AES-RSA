from aes import encrypt, decrypt

chave = 'chave secreta'
mensagem = 'Chove. Que fiz eu da vida? Fiz o que ela fez de mim... De pensada, mal vivida... Triste de quem e assim!'

criptografado = encrypt(chave, mensagem, 100000)
descriptografado = decrypt(chave, criptografado, 100000)

print(criptografado)
print(descriptografado)