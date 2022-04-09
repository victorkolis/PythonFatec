from hashlib import sha256

usuario_padrao = "14514307be9ef4287877636f9a3397b7bb9dddfded42ee0449e8c83ac2f2a78a"
senha_padrao = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"

usuario_digitado = input("Digite seu usuário: ").encode("ascii")
senha_digitada = input("Digite sua senha: ").encode("ascii")
usuario_digitado = sha256(usuario_digitado).hexdigest()
senha_digitada = sha256(senha_digitada).hexdigest()

if senha_digitada == senha_padrao and usuario_digitado == usuario_padrao:
    print("Bem vindo ao curso Fatec")
else:
    print("Ou senha ou usuário incorreto")
