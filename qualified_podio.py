def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
  if tempo_chegada1 < tempo_chegada2 < tempo_chegada3:
    primeiro_colocado = tempo_chegada1
    segundo_colocado =  tempo_chegada2
    terceiro_colocado = tempo_chegada3
  elif tempo_chegada1 < tempo_chegada3 < tempo_chegada2:
    primeiro_colocado = tempo_chegada1
    segundo_colocado =  tempo_chegada3
    terceiro_colocado = tempo_chegada2
  elif tempo_chegada2 < tempo_chegada1 < tempo_chegada3:
    primeiro_colocado = tempo_chegada2
    segundo_colocado =  tempo_chegada1
    terceiro_colocado = tempo_chegada3
  elif tempo_chegada2 < tempo_chegada3 < tempo_chegada1:
    primeiro_colocado = tempo_chegada2
    segundo_colocado =  tempo_chegada3
    terceiro_colocado = tempo_chegada1
  elif tempo_chegada3 < tempo_chegada2 < tempo_chegada1:
    primeiro_colocado = tempo_chegada3
    segundo_colocado = tempo_chegada2
    terceiro_colocado = tempo_chegada1
  elif tempo_chegada3 < tempo_chegada1 < tempo_chegada2:
    primeiro_colocado = tempo_chegada3
    segundo_colocado = tempo_chegada1
    terceiro_colocado = tempo_chegada2
  podio = f"1 - {primeiro_colocado} minutos\n2 - {segundo_colocado} minutos\n3 - {terceiro_colocado} minutos\n"
  return podio

def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
  if tempo_chegada1 < tempo_chegada2 < tempo_chegada3:
    primeiro_colocado = tempo_chegada1
    segundo_colocado = tempo_chegada2
    terceiro_colocado = tempo_chegada3
    nome_primeiro = nome_corredor1
    nome_segundo = nome_corredor2
    nome_terceiro = nome_corredor3
  elif tempo_chegada1 < tempo_chegada3 < tempo_chegada2:
    primeiro_colocado = tempo_chegada1
    segundo_colocado = tempo_chegada3
    terceiro_colocado = tempo_chegada2
    nome_primeiro = nome_corredor1
    nome_segundo =  nome_corredor3
    nome_terceiro = nome_corredor2
  elif tempo_chegada2 < tempo_chegada1 < tempo_chegada3:
    primeiro_colocado = tempo_chegada2
    segundo_colocado = tempo_chegada1
    terceiro_colocado = tempo_chegada3
    nome_primeiro = nome_corredor2
    nome_segundo = nome_corredor1
    nome_terceiro = nome_corredor3
  elif tempo_chegada2 < tempo_chegada3 < tempo_chegada1:
    primeiro_colocado = tempo_chegada2
    segundo_colocado = tempo_chegada3
    terceiro_colocado = tempo_chegada1
    nome_primeiro = nome_corredor2
    nome_segundo = nome_corredor3
    nome_terceiro = nome_corredor1
  elif tempo_chegada3 < tempo_chegada2 < tempo_chegada1:
    primeiro_colocado = tempo_chegada3
    segundo_colocado = tempo_chegada2
    terceiro_colocado = tempo_chegada1
    nome_primeiro = nome_corredor3
    nome_segundo = nome_corredor2
    nome_terceiro = nome_corredor1
  elif tempo_chegada3 < tempo_chegada1 < tempo_chegada2:
    primeiro_colocado = tempo_chegada3
    segundo_colocado = tempo_chegada1
    terceiro_colocado = tempo_chegada2
    nome_primeiro = nome_corredor3
    nome_segundo = nome_corredor1
    nome_terceiro = nome_corredor2

  colocacao = f"1 - {nome_primeiro} - {primeiro_colocado} minutos\n2 - {nome_segundo} - {segundo_colocado} minutos\n3 - {nome_terceiro} - {terceiro_colocado} minutos\n"
  return colocacao
  
    
    
    
    
  

  
   

     
   
    
  
  
  
    
    
    
    

  


    
    
    
    

   