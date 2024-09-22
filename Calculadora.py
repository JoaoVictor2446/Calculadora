operação=input("Coloque o sinal da sua operação")
numero=float(input("Coloque o seu primeiro número"))
numero2=float(input("Coloque o seu segundo número"))

if operação == "+":
  resultado=numero+numero2
  print(f"O seu resultado é {resultado:2f}.")
elif operação=="-":
   resultado=numero-numero2
   print(f"O seu resultado é {resultado:2f}.")
elif operação=="*" :
  resultado=numero*numero2
  print(f"O seu resultado é {resultado:2f}.")
elif operação=="/":
      if numero2 == 0 :
            print("Erro: Divisão por zero não é permitida.")
      else:
        resultado=numero/numero2  
      print(f"O seu resultado é {resultado:2f}.")
else:
 
 
 print("Por favor , coloque um sinal de operção válido.")
