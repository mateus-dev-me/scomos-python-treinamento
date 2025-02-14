from typing import List, Optional

def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Executa a busca binária em uma lista ordenada.
    
    :param arr: Lista de inteiros ordenada.
    :param target: Elemento a ser encontrado.
    :return: Índice do elemento se encontrado, senão None.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None

if __name__ == "__main__":
    # Exemplo de uso
    numbers = [1, 3, 5, 7, 9, 11, 13, 15]
    target_value = 7
    result = binary_search(numbers, target_value)
    
    if result is not None:
        print(f"Elemento {target_value} encontrado no índice {result}.")
    else:
        print(f"Elemento {target_value} não encontrado na lista.")

