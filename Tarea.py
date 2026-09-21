# Ej. 1: Validador de notas con promedio
class Calificador:
    def __init__(self):
        self.notas_validas = []

    def validar_nota(self, nota):
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas_validas.append(nota)
        return self.notas_validas

    def promedio(self):
        if not self.notas_validas:
            return 0
        return sum(self.notas_validas) / len(self.notas_validas)

# Ej. 2: Contador de palabras únicas
class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.orden_palabras = []

    def agregar_palabra(self, palabra):
        if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.orden_palabras.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

# Ej. 3: Gestor de compras con totales
class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        return [nombre for nombre, precio in self.articulos.items() 
                if precio_min <= precio <= precio_max]

# Ej. 4: Inversor de secuencias
class InversorSecuencia:
    def __init__(self):
        pass

    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista)-1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultados = {}
        for lista in listas:
            # Las listas no son hasheables, se usa tuple como clave del diccionario
            resultados[tuple(lista)] = self.invertir_lista(lista)
        return resultados

# Ej. 5: Detector de números pares e impares
class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        for num in numeros:
            if self.es_par(num):
                self.pares.append(num)
            else:
                self.impares.append(num)
        return {'pares': self.pares, 'impares': self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))
    
# Ej. 6: Estadísticas de temperatura
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas) if self.temperaturas else None

    def maxima(self):
        return max(self.temperaturas) if self.temperaturas else None

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas) if self.temperaturas else 0

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

# Ej. 7: Mapeador de edades
class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        return [nombre for nombre, edad in self.personas.items() if edad >= edad_minima]

    def edad_promedio(self):
        if not self.personas:
            return 0
        return sum(self.personas.values()) / len(self.personas)

# Ej. 8: Asignador de equipos
class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        # key=lambda extrae el equipo con la lista más larga
        return max(self.equipos, key=lambda k: len(self.equipos[k]))

# Ej. 9: Validador de caracteres
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in 'aeiouáéíóú'

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
            
        conteos = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
        for char in texto:
            if char.isdigit():
                conteos['digitos'] += 1
            elif char.isalpha():
                if self.solo_vocales(char):
                    conteos['vocales'] += 1
                else:
                    conteos['consonantes'] += 1
        return conteos

# Ej. 10: Gestor de tareas con prioridad
class Tareas:
    def __init__(self):
        self.lista_tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        return [tarea for tarea in self.lista_tareas if tarea[1].lower() == 'alta']

    def eliminar_completada(self, descripcion):
        self.lista_tareas = [tarea for tarea in self.lista_tareas if tarea[0] != descripcion]

# Ej. 11: Contador de frecuencia
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        if not self.frecuencias:
            return None
        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)

# Ej. 12: Selector de rango con tuplas
class SelectorRango:
    def __init__(self):
        pass

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos_unicos = set()
        for r in rangos:
            elementos_unicos.update(self.crear_rango(r[0], r[1]))
        return list(elementos_unicos)

# Ej. 13: Combinador de listas
class CombinadorListas:
    def __init__(self):
        pass

    def intercalar(self, lista1, lista2):
        resultado = []
        longitud = max(len(lista1), len(lista2))
        for i in range(longitud):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas: return []
        resultado = listas[0]
        for lista in listas[1:]:
            resultado = self.intercalar(resultado, lista)
        return resultado

# Ej. 14: Mapeo de estudiantes a notas
class RegistroNotas:
    def __init__(self):
        self.registro = {}

    def registrar(self, estudiante, nota):
        self.registro[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        return [est for est, nota in self.registro.items() if nota >= nota_minima]

    def mejor_estudiante(self):
        if not self.registro:
            return None
        mejor_est = max(self.registro, key=self.registro.get)
        return (mejor_est, self.registro[mejor_est])

# Ej. 15: Divisores de un número
class DivisorFinder:
    def __init__(self):
        pass

    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        return sum(divisores) - numero == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultados = {}
        for num in numeros:
            resultados[num] = self.encontrar_divisores(num)
        return resultados

import math

# Ej. 16: Codificador/Decodificador
class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')
            return chr((ord(letra) - base + desplazamiento) % 26 + base)
        return letra

    def codificar_palabra(self, palabra, desplazamiento):
        codificada = ""
        for letra in palabra:
            codificada += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = codificada
        return codificada

# Ej. 17: Grupo de edades
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {'niño': [], 'adolescente': [], 'adulto': [], 'mayor': []}

    def clasificar_edad(self, edad):
        if edad < 12: return "niño"
        elif edad < 18: return "adolescente"
        elif edad < 65: return "adulto"
        else: return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {'niño': [], 'adolescente': [], 'adulto': [], 'mayor': []}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])
        return sum(edades) / len(edades) if edades else 0

# Ej. 18: Matriz de distancias
class CalculadorDistancia:
    def __init__(self):
        self.historial_distancias = []

    def distancia_euclidiana(self, p1, p2):
        dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        self.historial_distancias.append(dist)
        return dist

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos: return None
        mas_cercano = puntos[0]
        min_dist = self.distancia_euclidiana(referencia, mas_cercano)
        
        for p in puntos[1:]:
            dist = self.distancia_euclidiana(referencia, p)
            if dist < min_dist:
                min_dist = dist
                mas_cercano = p
                
        return mas_cercano

# Ej. 19: Inventario de productos
class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [prod for prod, cant in self.stock.items() if cant < minimo]

# Ej. 20: Analizador de patrones en textos
class AnalizadorPatrones:
    def __init__(self):
        pass

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        return [p for p in palabras if p.startswith(patron)]

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        grupos = {}
        for p in palabras:
            longitud = len(p)
            if longitud not in grupos:
                grupos[longitud] = []
            grupos[longitud].append(p)
        return grupos

    def palabras_unicas(self, texto):
        return set(texto.split())