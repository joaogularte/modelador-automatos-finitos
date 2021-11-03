"""
Exemplo de entrada:

{
  "conjunto_de_estados": ["q0", "q1"],
  "alfabeto": ["a", "b"],
  "estado_inicial": "q0",
  "estados_finais": ["q1"],
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
  }]
}


{
  "q0": ["q0", "q1"],
  "q1": ["q1"]
}


"""

nested transicoes em vazio

def remove_transicoes_vazias(afnde):
