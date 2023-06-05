print('Digite um nome')
s=input().lower()
palavras = s.split()
resultado=''
for palavra in palavras:
  match(palavra):
    case "da" | "de" |"do":
      resultado+=palavra
    case "das" | "dos" |"e":
      resultado+=palavra
    case _:
  
      resultado += palavra[0].upper()
      resultado += palavra[1:]
  resultado+=' '
print(resultado)
  