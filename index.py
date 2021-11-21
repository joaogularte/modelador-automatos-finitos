"""
Exemplo de entrada:

{
  "conjunto_de_estados": ["q0", "q1", "q2", "q3"],
  "alfabeto": ["a", "b", "c", "d"],
  "estado_inicial": "q0",
  "estados_finais": ["q3"],
  "transicoes_entre_estados": [{
    "estado": "q0",
    "le": "a",
    "proximo_estado": ["q0"]
  },
  {
    "estado": "q0",
    "le": "ε",
    "proximo_estado": ["q1"]
  },
  {
    "estado": "q1",
    "le": "b",
    "proximo_estado": ["q1"]
  },
  {
    "estado": "q1",
    "le": "ε",
    "proximo_estado": ["q2"]
  },
  {
    "estado": "q2",
    "le": "c",
    "proximo_estado": ["q2"]
  },
  {
    "estado": "q2",
    "le": "ε",
    "proximo_estado": ["q3"]
  },
  {
    "estado": "q3",
    "le": "d",
    "proximo_estado": ["q3"]
  }]
}


{
  "q0": ["q0", "q1"],
  "q1": ["q1"]
}


"""

def remover_transicoes_vazias(afnde):
  return obter_e_closures_por_estado(afnde)

def obter_e_closures_por_estado(afnde):
  e_closures_por_estados =  {}
  conjunto_de_estados = afnde["conjunto_de_estados"]
  for estado in conjunto_de_estados:
    e_closures = obter_e_closures(estado, afnde, [])
    e_closures_por_estados[estado] = e_closures
    break

  return e_closures_por_estados

def obter_e_closures(estado, afnde, lista_e_closure):
  for transicao in afnde["transicoes_entre_estados"]:

    if estado in afnde["estados_finais"] and transicao["estado"] == transicao["proximo_estado"]:
      print("primeiro if")
      lista_e_closure.append(estado)
    elif not transicao["le"] == "ε" and transicao["estado"] == transicao["proximo_estado"]:
      print("segundo if")

      break
    elif transicao["le"] == "ε" and estado == transicao["estado"] and estado == afnde["estado_inicial"]:
      print("terceiro if")

      lista_e_closure.append(estado)
      lista_e_closure = obter_e_closures(transicao["proximo_estado"], afnde, lista_e_closure)
    elif transicao["le"] == "ε" and estado == transicao["estado"]:
      print("quarto if")

      lista_e_closure.append(estado)
      lista_e_closure = obter_e_closures(transicao["proximo_estado"], afnde, lista_e_closure)
    elif transicao["le"] == "ε" and estado == transicao["estado"] and transicao["proximo_estado"] in afnde["estados_finais"]:
      print("quinto if")

      lista_e_closure.append(estado)
      lista_e_closure.append(transicao["proximo_estado"])

  return lista_e_closure


afnde = {
  "conjunto_de_estados": ["q0", "q1", "q2", "q3"],
  "alfabeto": ["a", "b", "c", "d"],
  "estado_inicial": "q0",
  "estados_finais": ["q3"],
  "transicoes_entre_estados": [{
    "estado": "q0",
    "le": "a",
    "proximo_estado": ["q0"]
  },
  {
    "estado": "q0",
    "le": "ε",
    "proximo_estado": ["q1"]
  },
  {
    "estado": "q1",
    "le": "b",
    "proximo_estado": ["q1"]
  },
  {
    "estado": "q1",
    "le": "ε",
    "proximo_estado": ["q2"]
  },
  {
    "estado": "q2",
    "le": "c",
    "proximo_estado": ["q2"]
  },
  {
    "estado": "q2",
    "le": "ε",
    "proximo_estado": ["q3"]
  },
  {
    "estado": "q3",
    "le": "d",
    "proximo_estado": ["q3"]
  }]
}

print(remover_transicoes_vazias(afnde))
