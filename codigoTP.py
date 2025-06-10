class ordenamiento_burbuja:
    @staticmethod
    def ordenar(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
class busqueda_binaria:
    @staticmethod
    def buscar_todos(arr, target):
        posiciones = []
        low = 0
        high = len(arr) - 1
        encontrado = False
        while low <= high and not encontrado:
            mid = (low + high) // 2
            if arr[mid] == target:
                i = mid
                while i >= 0 and arr[i] == target:
                    i -= 1
                i += 1
                while i < len(arr) and arr[i] == target:
                    posiciones.append(i)
                    i += 1
                encontrado = True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return posiciones
datos = [3, 19, 1, 2, 87, 3]
print ("Arreglo Original:", datos)
ordenamiento_burbuja.ordenar(datos)
print ("Arreglo Ordenado:", datos)
valor = int(input("Ingresa el valor que deseas buscar: "))
posiciones = busqueda_binaria.buscar_todos(datos, valor)
if posiciones:
    print("El valor: ", valor , " , encontrado en las posiciones:", posiciones)
else:
    print("No se encontró el valor solicitado.")
