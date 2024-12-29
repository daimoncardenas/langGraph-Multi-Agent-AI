from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

# Definir el estado inicial del grafo
class State(TypedDict):
    data: dict
    
# Crear el grafo
graph_builder = StateGraph(State)

# Definir los nodos

def analyzer_node(state: State):
    print("Analizando proyecto...")
    state['data'] = {"architecture": "detected"}  # Simula un análisis
    return {"data": state['data']}

def code_generator_node(state: State):
    print("Generando código...")
    state['data'].update({"code": "generated"})  # Simula la generación de código
    return {"data": state['data']}

def validator_node(state: State):
    print("Validando código...")
    state['data'].update({"result": "success"})  # Simula la validación
    return {"data": state['data']}

# Agregar nodos al grafo
graph_builder.add_node("Analyzer", analyzer_node)
graph_builder.add_node("CodeGenerator", code_generator_node)
graph_builder.add_node("Validator", validator_node)

# Definir transiciones
graph_builder.add_edge(START, "Analyzer")
graph_builder.add_edge("Analyzer", "CodeGenerator")
graph_builder.add_edge("CodeGenerator", "Validator")
graph_builder.add_edge("Validator", END)

# Compilar el grafo
graph = graph_builder.compile()

# Iniciar flujo
if __name__ == "__main__":
    initial_state = {"data": {}}
    result = graph.invoke(initial_state)
    print("Flujo completado:", result)
