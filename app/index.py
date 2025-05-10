import PyPDF2
def break_password(pdf_path, rockyou_path):
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        with open(rockyou_path, "r", encoding="utf-8") as f:
            passwords = f.read().splitlines()

        for password in passwords:
            print(f"Tentando a senha: {password}")
            try:
                if reader.decrypt(password):
                    print(f"Senha encontrada: {password}")
                    return password
            except Exception:
                pass
        print("Nenhuma senha encontrada!")
        return None

pdf_protected = "./../assets/target_protected.pdf"
rockyou = "./../rockyou/password.txt"

break_password(pdf_protected, rockyou)
# Para testar python index.py
