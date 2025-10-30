# Snake Game 🐍

El clásico juego de la serpiente creado con Python Turtle, parte de la colección **Free Python Games**.

## 📋 Descripción

Este es el icónico juego Snake donde controlas una serpiente que crece cada vez que come. El objetivo es comer la mayor cantidad de comida posible sin chocar contra las paredes o contra tu propio cuerpo.

## 🎮 Cómo Jugar

1. **Usa las flechas del teclado** para controlar la dirección de la serpiente:
   - `→` Flecha Derecha: Mover a la derecha
   - `←` Flecha Izquierda: Mover a la izquierda
   - `↑` Flecha Arriba: Mover hacia arriba
   - `↓` Flecha Abajo: Mover hacia abajo

2. **Come los cuadrados verdes** para hacer crecer tu serpiente
3. **Evita chocar** contra las paredes o contra tu propio cuerpo
4. Cada vez que comes, la serpiente crece un segmento
5. Tu puntuación actual se imprime en la consola

## 🎯 Mecánicas del Juego

- **Serpiente (negra)**: Comienza con 1 segmento y crece al comer
- **Comida (verde)**: Aparece en posiciones aleatorias del tablero
- **Paredes invisibles**: Los límites del área de juego
- **Game Over**: Ocurre al chocar contra paredes o el propio cuerpo
- **Indicador de muerte (rojo)**: Muestra dónde ocurrió la colisión

## 🏆 Sistema de Puntuación

- La longitud de la serpiente se imprime en consola cada vez que comes
- Formato: `Snake: [número de segmentos]`
- Comienzas con 1 segmento
- Cada comida añade 1 segmento a tu serpiente

## Extra:
- En cada partida los colores de la serpiente y la comida son distintos (aleatorios)
- La comida se va moviendo un paso a la vez de forma aleatoria para complicar el juego

## 🔧 Requisitos

```bash
pip install freegames
```

## 🚀 Ejecución

```bash
python snake.py
```

O si tienes instalado `freegames`:

```bash
python -m freegames.snake
```

## 📦 Dependencias

- **Python 3.x**
- **turtle** (incluido en Python estándar)
- **freegames**: Librería que proporciona las funciones `square` y `vector`

## 🎲 Características Técnicas

- Ventana de juego: 420x420 píxeles
- Área de juego: -200 a 190 en ambos ejes
- Tamaño de cada segmento: 10x10 píxeles
- Velocidad de movimiento: 100ms por movimiento
- Tamaño de cuadrados dibujados: 9x9 píxeles (con espacio de 1 píxel)
- Grid de comida: Posiciones múltiplos de 10 (rango -150 a 150)

## 🎮 Detalles del Gameplay

### Movimiento
- La serpiente se mueve continuamente en la dirección actual
- Cambiar de dirección es instantáneo
- No puedes moverte en la dirección opuesta directamente

### Crecimiento
- Cuando la cabeza alcanza la comida exactamente (`head == food`)
- La serpiente mantiene todos sus segmentos y añade uno nuevo
- La comida reaparece en una posición aleatoria

### Colisión
- **Con paredes**: Si la cabeza sale del área (-200 a 190)
- **Consigo misma**: Si la cabeza toca cualquier parte del cuerpo
- Al colisionar, la cabeza se dibuja en rojo y el juego termina

## 📊 Estructura del Código

- **`change(x, y)`**: Cambia la dirección de movimiento de la serpiente
- **`inside(head)`**: Verifica si la cabeza está dentro de los límites
- **`move()`**: Mueve la serpiente y maneja toda la lógica del juego
- **Variables globales**:
  - `snake`: Lista de vectores que representan cada segmento
  - `food`: Vector con la posición de la comida
  - `aim`: Vector de dirección actual

## 💡 Estrategias de Juego

1. **Planifica tu ruta**: No te quedes atrapado en esquinas
2. **Usa el espacio**: Mantén espacio para maniobrar conforme creces
3. **Evita movimientos bruscos**: Piensa antes de cambiar de dirección
4. **Controla el centro**: Es más seguro que las orillas al principio

## 📝 Créditos

Este código pertenece a **Free Python Games**, una colección de juegos simples implementados en Python para fines educativos.

🔗 [Free Python Games - GitHub](https://github.com/grantjenks/free-python-games)

## 📄 Licencia

Este código es parte de Free Python Games. Consulta la licencia original del proyecto para más información.

---

**¡Intenta hacer la serpiente más larga posible! 🏆🐍**

