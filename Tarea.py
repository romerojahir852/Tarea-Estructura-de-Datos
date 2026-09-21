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

# Ej. 1: Registro de asistencia
class RegistroAsistencia:
    def __init__(self):
        self.asistencias = {}

    def registrar(self, alumno, presente):
        if alumno not in self.asistencias:
            self.asistencias[alumno] = []
        self.asistencias[alumno].append(presente)

    def porcentaje_asistencia(self, alumno):
        if alumno not in self.asistencias:
            return 0
        registros = self.asistencias[alumno]
        return (sum(registros) / len(registros)) * 100

    def alumnos_regulares(self, minimo_porcentaje):
        return [alumno for alumno in self.asistencias 
                if self.porcentaje_asistencia(alumno) >= minimo_porcentaje]

# Ej. 2: Conversor de unidades
class ConversorUnidades:
    def __init__(self):
        self.historial_conversiones = []

    def km_a_millas(self, km):
        resultado = km * 0.621371
        self.historial_conversiones.append(('km_a_millas', km, resultado))
        return resultado

    def celsius_a_fahrenheit(self, celsius):
        resultado = (celsius * 9/5) + 32
        self.historial_conversiones.append(('celsius_a_fahrenheit', celsius, resultado))
        return resultado

    def kg_a_libras(self, kg):
        resultado = kg * 2.20462
        self.historial_conversiones.append(('kg_a_libras', kg, resultado))
        return resultado

    def total_conversiones(self):
        return len(self.historial_conversiones)

# Ej. 3: Calculadora de propinas
class CalculadoraPropinas:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, monto):
        self.cuentas.append(monto)

    def calcular_propina(self, monto, porcentaje):
        return monto * (porcentaje / 100)

    def total_con_propinas(self, porcentaje):
        total = 0
        for cuenta in self.cuentas:
            total += cuenta + self.calcular_propina(cuenta, porcentaje)
        return total

    def cuenta_mas_alta(self):
        if not self.cuentas:
            return None
        return max(self.cuentas)

# Ej. 4: Organizador de contactos
class AgendaContactos:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def buscar_contacto(self, nombre):
        return self.contactos.get(nombre, "No encontrado")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            return True
        return False

    def contactos_por_letra(self, letra):
        return [nombre for nombre in self.contactos if nombre.startswith(letra.upper())]

# Ej. 5: Clasificador de números primos y compuestos
class ClasificadorPrimos:
    def __init__(self):
        self.primos = []
        self.compuestos = []

    def es_primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def clasificar(self, *numeros):
        for num in numeros:
            if self.es_primo(num):
                self.primos.append(num)
            else:
                self.compuestos.append(num)
        return {'primos': self.primos, 'compuestos': self.compuestos}

    def cantidad_primos(self):
        return len(self.primos)

# Ej. 6: Gestor de calificaciones por materia
class GestorMaterias:
    def __init__(self):
        self.materias = {}

    def agregar_materia(self, nombre_materia):
        if nombre_materia not in self.materias:
            self.materias[nombre_materia] = []

    def agregar_calificacion(self, materia, calificacion):
        if materia in self.materias:
            self.materias[materia].append(calificacion)

    def promedio_materia(self, materia):
        notas = self.materias.get(materia, [])
        if not notas:
            return 0
        return sum(notas) / len(notas)

    def materia_mejor_promedio(self):
        if not self.materias:
            return None
        return max(self.materias, key=lambda m: self.promedio_materia(m))

# Ej. 7: Verificador de palíndromos
class VerificadorPalindromo:
    def __init__(self):
        self.palindromos_encontrados = []

    def limpiar_texto(self, texto):
        limpio = ""
        for char in texto.lower():
            if char.isalnum():
                limpio += char
        return limpio

    def es_palindromo(self, texto):
        limpio = self.limpiar_texto(texto)
        resultado = limpio == limpio[::-1]
        if resultado:
            self.palindromos_encontrados.append(texto)
        return resultado

    def verificar_multiples(self, *textos):
        resultados = {}
        for texto in textos:
            resultados[texto] = self.es_palindromo(texto)
        return resultados

# Ej. 8: Control de gastos mensuales
class ControlGastos:
    def __init__(self):
        self.gastos = {}

    def registrar_gasto(self, categoria, monto):
        if categoria not in self.gastos:
            self.gastos[categoria] = []
        self.gastos[categoria].append(monto)

    def total_por_categoria(self, categoria):
        return sum(self.gastos.get(categoria, []))

    def gasto_total(self):
        total = 0
        for montos in self.gastos.values():
            total += sum(montos)
        return total

    def categoria_mayor_gasto(self):
        if not self.gastos:
            return None
        return max(self.gastos, key=lambda c: sum(self.gastos[c]))

# Ej. 9: Generador de tabla de multiplicar
class TablaMultiplicar:
    def __init__(self):
        self.tablas_generadas = {}

    def generar_tabla(self, numero, hasta=10):
        tabla = []
        for i in range(1, hasta + 1):
            tabla.append((numero, i, numero * i))
        self.tablas_generadas[numero] = tabla
        return tabla

    def buscar_resultado(self, numero, multiplicador):
        return numero * multiplicador

    def generar_multiples_tablas(self, *numeros):
        for num in numeros:
            self.generar_tabla(num)
        return self.tablas_generadas

# Ej. 10: Registro de libros con búsqueda
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor, anio):
        self.libros.append({'titulo': titulo, 'autor': autor, 'anio': anio})

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if libro['autor'] == autor]

    def libros_recientes(self, anio_minimo):
        return [libro for libro in self.libros if libro['anio'] >= anio_minimo]

    def libro_mas_antiguo(self):
        if not self.libros:
            return None
        return min(self.libros, key=lambda l: l['anio'])

# Ej. 11: Calculadora de estadísticas
class CalculadoraEstadisticas:
    def __init__(self):
        self.datos = []

    def agregar_datos(self, *valores):
        for v in valores:
            self.datos.append(v)

    def media(self):
        if not self.datos:
            return 0
        return sum(self.datos) / len(self.datos)

    def mediana(self):
        if not self.datos:
            return 0
        ordenados = sorted(self.datos)
        n = len(ordenados)
        if n % 2 == 0:
            return (ordenados[n//2 - 1] + ordenados[n//2]) / 2
        else:
            return ordenados[n//2]

    def rango(self):
        if not self.datos:
            return 0
        return max(self.datos) - min(self.datos)

# Ej. 12: Conversor de bases numéricas
class ConversorBases:
    def __init__(self):
        self.conversiones = []

    def decimal_a_binario(self, numero):
        resultado = bin(numero)[2:]
        self.conversiones.append(('decimal', 'binario', numero, resultado))
        return resultado

    def decimal_a_octal(self, numero):
        resultado = oct(numero)[2:]
        self.conversiones.append(('decimal', 'octal', numero, resultado))
        return resultado

    def decimal_a_hexadecimal(self, numero):
        resultado = hex(numero)[2:].upper()
        self.conversiones.append(('decimal', 'hexadecimal', numero, resultado))
        return resultado

    def convertir_multiples(self, *numeros):
        resultados = {}
        for num in numeros:
            resultados[num] = {
                'binario': self.decimal_a_binario(num),
                'octal': self.decimal_a_octal(num),
                'hexadecimal': self.decimal_a_hexadecimal(num)
            }
        return resultados

# Ej. 13: Simulador de dados
class SimuladorDados:
    def __init__(self):
        self.historial_tiradas = []

    def tirar_dado(self, caras=6):
        import random
        resultado = random.randint(1, caras)
        self.historial_tiradas.append(resultado)
        return resultado

    def tirar_multiples(self, cantidad, caras=6):
        tiradas = []
        for i in range(cantidad):
            tiradas.append(self.tirar_dado(caras))
        return tiradas

    def frecuencia_resultados(self):
        frecuencias = {}
        for tirada in self.historial_tiradas:
            if tirada in frecuencias:
                frecuencias[tirada] += 1
            else:
                frecuencias[tirada] = 1
        return frecuencias

    def promedio_tiradas(self):
        if not self.historial_tiradas:
            return 0
        return sum(self.historial_tiradas) / len(self.historial_tiradas)

# Ej. 14: Gestor de contraseñas
class ValidadorPassword:
    def __init__(self):
        self.passwords_validadas = []

    def tiene_mayuscula(self, password):
        for char in password:
            if char.isupper():
                return True
        return False

    def tiene_numero(self, password):
        for char in password:
            if char.isdigit():
                return True
        return False

    def validar_password(self, password):
        es_valida = (len(password) >= 8 and 
                     self.tiene_mayuscula(password) and 
                     self.tiene_numero(password))
        if es_valida:
            self.passwords_validadas.append(password)
        return es_valida

    def validar_multiples(self, *passwords):
        resultados = {}
        for p in passwords:
            resultados[p] = self.validar_password(p)
        return resultados

# Ej. 15: Calculadora de áreas
class CalculadoraAreas:
    def __init__(self):
        self.areas_calculadas = []

    def area_circulo(self, radio):
        import math
        area = math.pi * radio ** 2
        self.areas_calculadas.append(('circulo', area))
        return area

    def area_rectangulo(self, base, altura):
        area = base * altura
        self.areas_calculadas.append(('rectangulo', area))
        return area

    def area_triangulo(self, base, altura):
        area = (base * altura) / 2
        self.areas_calculadas.append(('triangulo', area))
        return area

    def area_total(self):
        total = 0
        for figura, area in self.areas_calculadas:
            total += area
        return total

# Ej. 16: Organizador de playlist
class PlaylistMusical:
    def __init__(self):
        self.canciones = []

    def agregar_cancion(self, titulo, artista, duracion):
        self.canciones.append({'titulo': titulo, 'artista': artista, 'duracion': duracion})

    def duracion_total(self):
        total = 0
        for cancion in self.canciones:
            total += cancion['duracion']
        return total

    def canciones_por_artista(self, artista):
        return [c for c in self.canciones if c['artista'] == artista]

    def cancion_mas_larga(self):
        if not self.canciones:
            return None
        return max(self.canciones, key=lambda c: c['duracion'])

# Ej. 17: Contador de vocales y consonantes por palabra
class AnalizadorPalabras:
    def __init__(self):
        self.analisis_realizados = {}

    def contar_vocales(self, palabra):
        contador = 0
        for letra in palabra.lower():
            if letra in 'aeiou':
                contador += 1
        return contador

    def contar_consonantes(self, palabra):
        contador = 0
        for letra in palabra.lower():
            if letra.isalpha() and letra not in 'aeiou':
                contador += 1
        return contador

    def analizar_palabra(self, palabra):
        resultado = {
            'vocales': self.contar_vocales(palabra),
            'consonantes': self.contar_consonantes(palabra),
            'longitud': len(palabra)
        }
        self.analisis_realizados[palabra] = resultado
        return resultado

    def palabra_mas_vocales(self):
        if not self.analisis_realizados:
            return None
        return max(self.analisis_realizados, 
                   key=lambda p: self.analisis_realizados[p]['vocales'])

# Ej. 18: Sistema de votación
class SistemaVotacion:
    def __init__(self):
        self.votos = {}
        self.votantes = set()

    def registrar_candidato(self, candidato):
        if candidato not in self.votos:
            self.votos[candidato] = 0

    def votar(self, votante, candidato):
        if votante in self.votantes:
            return False
        if candidato in self.votos:
            self.votos[candidato] += 1
            self.votantes.add(votante)
            return True
        return False

    def ganador(self):
        if not self.votos:
            return None
        return max(self.votos, key=self.votos.get)

    def total_votos(self):
        return sum(self.votos.values())

# Ej. 19: Historial de movimientos bancarios
class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.movimientos = []

    def depositar(self, monto):
        self.saldo += monto
        self.movimientos.append(('deposito', monto))

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            self.movimientos.append(('retiro', monto))
            return True
        return False

    def ultimos_movimientos(self, cantidad):
        return self.movimientos[-cantidad:]

    def total_depositos(self):
        total = 0
        for tipo, monto in self.movimientos:
            if tipo == 'deposito':
                total += monto
        return total

# Ej. 20: Comparador de conjuntos
class OperacionesConjuntos:
    def __init__(self):
        self.conjuntos = {}

    def crear_conjunto(self, nombre, *elementos):
        self.conjuntos[nombre] = set(elementos)

    def union(self, nombre1, nombre2):
        c1 = self.conjuntos.get(nombre1, set())
        c2 = self.conjuntos.get(nombre2, set())
        return c1 | c2

    def interseccion(self, nombre1, nombre2):
        c1 = self.conjuntos.get(nombre1, set())
        c2 = self.conjuntos.get(nombre2, set())
        return c1 & c2

    def diferencia(self, nombre1, nombre2):
        c1 = self.conjuntos.get(nombre1, set())
        c2 = self.conjuntos.get(nombre2, set())
        return c1 - c2

    def elementos_unicos_totales(self):
        todos = set()
        for conjunto in self.conjuntos.values():
            todos.update(conjunto)
        return todos
