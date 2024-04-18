# AES - RSA (Implementação)
### Alunos: Thiago Bittencourt Santana, Gael Huk Kukla, Gabriel Martins Delfes
![criptografia](https://github.com/oThiagoBittencourt/AES-RSA/assets/106789198/ae680ae5-541b-4232-b51c-7772d24bf0a1)


Projeto acadêmico que visa desenvolver a implementação dos sistemas de criptografia `AES (chave simétrica)` e `RSA (chave assimétrica)`

---

### Index:
<!--ts-->
   * [DETALHES](#detalhes)
   * [RSA](#execução-rsa)
   * [PESQUISA](#pesquisa)
<!--te-->

---

### Detalhes:

#### AES
AES (Advanced Encryption Standard): É um algoritmo de criptografia simétrica amplamente utilizado para proteger dados. AES opera em blocos de dados e suporta chaves de 128, 192 e 256 bits. É conhecido por sua eficiência e segurança, sendo adotado em diversas aplicações, desde comunicações seguras até criptografia de arquivos.

#### RSA
RSA (Rivest-Shamir-Adleman): É um algoritmo de criptografia assimétrica amplamente usado para criptografia de chaves públicas. RSA é baseado na dificuldade de fatorar números inteiros grandes, o que é fundamental para a segurança do sistema. É frequentemente utilizado para estabelecer chaves de sessão seguras em protocolos de comunicação e para assinaturas digitais.

---

### Execução RSA:
> **Para iniciar o RSA:**
> 
> 1º Abra dois terminais
> 
> 2º No primeiro terminal, execute o arquivo destinatario.py
> 
> 3º Após isso vá até o segundo terminal e execute o arquivo remetente.py
> 
> 4º Ao voltar para o primeiro terminal, teremos a mensagem descriptada.

---

### Pesquisa:

#### AES:

**Pontos fortes:**
- Eficiência: Rápido e eficiente para criptografar grandes volumes de dados.
- Segurança: Considerado seguro quando usado corretamente, especialmente com chaves longas.
- Simplicidade: Implementação e uso mais simples devido à natureza simétrica.

**Pontos fracos:**
- Necessidade de compartilhamento de chaves de forma segura.
- Gerenciamento de chaves pode ser complexo em larga escala.

#### RSA:

**Pontos fortes:**
- Criptografia de chave pública: Permite comunicação segura entre partes sem compartilhar uma chave secreta.
- Assinaturas digitais: Oferece autenticidade e integridade dos dados.
- Base matemática sólida: Segurança baseada na dificuldade computacional de fatorar números primos grandes.

**Pontos fracos:**
- Desempenho mais lento, especialmente para chaves longas.
- Necessidade de chaves mais longas para oferecer o mesmo nível de segurança que a encriptação simétrica.
- Complexidade e exigência de mais recursos computacionais.

---

#### Conclusão
Para comunicação direta com chave compartilhada, AES é melhor devido à eficiência e simplicidade. Para redes públicas ou onde autenticação é crítica, RSA é preferível por sua criptografia de chave pública e assinaturas digitais. Em muitos sistemas, ambos são usados para aproveitar seus pontos fortes.

---
