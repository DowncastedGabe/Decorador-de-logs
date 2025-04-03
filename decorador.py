from datetime import datetime
from functools import wraps

def log_transacao(funcao):
    """
    Decorador que registra data/hora e tipo de transação.
    
    Args:
        funcao: Função de transação a ser decorada (depósito, saque, etc.)
    
    Returns:
        Função decorada com registro de log
    """
    @wraps(funcao)
    def envelope(*args, **kwargs):
        # Executa a função original e captura o retorno
        resultado = funcao(*args, **kwargs)
        
        # Registra a transação
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{data_hora}] Transação: {funcao.__name__}")
        
        return resultado
    
    return envelope

@log_transacao
def depositar(valor, conta):
    # Lógica de depósito
    pass

@log_transacao
def sacar(valor, conta):
    # Lógica de saque
    pass

@log_transacao
def criar_conta(cliente):
    # Lógica de criação de conta
    pass
