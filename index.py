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
def obter_e_closures(estado, afnde, lista_e_closure):
  for transicao in afnde["transicoes_entre_estados"]:
    if transicao["le"] == "ε" and estado == afnde["estado_inicial"]:
      lista_e_closure.append(estado)
      lista_e_closure.append(transicao["proximo_estado"])
      obter_e_closures(transicao["proximo_estado"], afnde, lista_e_closure)
    elif estado == transicao["estado"] and transicao["le"] == "ε"
      lista_e_closure.append(transicao["proximo_estado"])
      obter_e_closures()
    elif


def remove_transicoes_vazias(afnde):
  conjunto_de_estados = afnde["conjunto_de_estados"]
