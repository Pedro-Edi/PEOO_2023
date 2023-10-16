import enum
import datetime
class Boleto:
  def __init__(self,cod,emissao,venc,valorBoleto):
    self.__cod=cod
    self.__emissao=datetime.datetime.strptime(emissao,"%d/%m/%Y")
    self.__venc=datetime.datetime.strptime(venc,"%d/%m/%Y")
    self.__valorBoleto=valorBoleto
    self.__valorPago=0
    self.__datapago=datetime.datetime.today()   
  def valorBoleto(self):
    return self.__valorBoleto
    
  def Pagar(self,valorPago):
      self.__valorPago+=valorPago
    
  def situacao(self):
    if self.__valorPago==0:
      return f'{Pagamento(1).name} - Data: {self.__datapago.strftime("%d/%m/%Y %H:%m")}'
    if self.__valorPago<self.valorBoleto():
      return f'{Pagamento(2).name} - Data: {self.__datapago.strftime("%d/%m/%Y %H:%m")}'
    if self.__valorPago==self.valorBoleto():
      return f'{Pagamento(2).name} - Data: {self.__datapago.strftime("%d/%m/%Y %H:%m")}'
    if self.__valorPago==self.valorBoleto():
      return f'{Pagamento(2).name} - Data: {self.__datapago.strftime("%d/%m/%Y %H:%m")}'
      
  def __str__(self):
    return f'O codigo do boleto:{self.__cod}\nData de Emissão: {self.__emissao.strftime("%d/%m/%Y")}\nVencimento: {self.__venc.strftime("%d/%m/%Y")}\nValor Boleto: {self.__valorBoleto}'


class Pagamento(enum.Enum): 
    Emaberto=1
    PagoParcial=2
    Pago=3
class UI:
  def main():
    cod=int(input('Qual o cod: '))
    emissao=input('Data de emissão(dia/mes/ano): ')
    vencimento=input('Data de vencimento(dia/mes/ano): ')
    valorBoleto=float(input('Qual o valor do Boleto: '))
    
    B=Boleto(cod,emissao,vencimento,valorBoleto)
    
    print(B)
    op=int(input('1-Pagar Boleto,2-Situação,0-fim '))
    
    while True:
      if op==1:
        valorPago=float(input('Qual o valor do Pagamento: '))
        
        B.Pagar(valorPago)
      if op==2:
        
        print(B.situacao())
        
      if op==0:
        break
      op=int(input('1-Pagar Boleto,2-Situação,0-fim '))

UI.main()
        