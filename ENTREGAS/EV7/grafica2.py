import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos corregidos con el mismo número de elementos en cada lista
aplicaciones_programcion = {
    'Aplicación': ['Visual Studio Code'] * 7 + ['PyCharm'] * 7 + ['Eclipse'] * 7 + ['IntelliJ IDEA'] * 7 +
                  ['Xcode'] * 7 + ['Android Studio'] * 7 + ['Sublime Text'] * 7 + ['Atom'] * 7 +
                  ['NetBeans'] * 7 + ['Brackets'] * 7,
    'Año': [2017, 2018, 2019, 2020, 2021, 2022, 2023] * 10,
    'Porcentaje de Uso': [
        10, 15, 20, 25, 30, 35, 40,  # Visual Studio Code
        8, 10, 12, 13, 15, 18, 20,   # PyCharm
        12, 11, 10, 9, 8, 7, 6,     # Eclipse
        10, 12, 14, 16, 18, 20, 22, # IntelliJ IDEA
        8, 9, 10, 11, 12, 13, 14,   # Xcode
        15, 16, 18, 20, 22, 24, 25, # Android Studio
        6, 5, 5, 5, 5, 4, 4,        # Sublime Text
        5, 6, 7, 8, 9, 8, 7,        # Atom
        7, 7, 6, 6, 6, 5, 5,        # NetBeans
        4, 4, 3, 3, 3, 2, 2         # Brackets
    ]
}

# Crear un DataFrame con los datos
df_aplicaciones_programcion = pd.DataFrame(aplicaciones_programcion)

# Crear un gráfico de líneas
plt.figure(figsize=(14, 8))  # Ajustar el tamaño de la figura (más ancha)
sns.lineplot(data=df_aplicaciones_programcion, x='Año', y='Porcentaje de Uso', hue='Aplicación', marker='o', linewidth=2.5)

# Personalizar el gráfico
plt.title('Tendencias de uso de aplicaciones de programación (2017-2023)', fontsize=16, pad=20)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Aplicación', title_fontsize=12, fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')

# Añadir proyecciones para el año 2024
plt.axvline(x=2023, color='gray', linestyle='--', alpha=0.5)  # Línea vertical para marcar el año 2023
plt.text(2023.7, 22, 'Proyecciones 2024:', fontsize=10)  # Título de las proyecciones
plt.text(2023.7, 20, '• Visual Studio Code: Continuará siendo líder en editores', fontsize=9)
plt.text(2023.7, 18, '• PyCharm: Aumento moderado en la comunidad Python', fontsize=9)
plt.text(2023.7, 16, '• Eclipse: Reducción en el uso, aunque sigue siendo relevante', fontsize=9)
plt.text(2023.7, 14, '• IntelliJ IDEA: Crecimiento en entornos de Java y Kotlin', fontsize=9)
plt.text(2023.7, 12, '• Xcode: Firme en el desarrollo de apps para Apple', fontsize=9)
plt.text(2023.7, 10, '• Android Studio: Continuará fuerte en el desarrollo móvil Android', fontsize=9)

# Ajustar el diseño para evitar cortes de texto
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Mostrar conclusiones en consola
print("\nConclusiones Principales:")
print("1. Visual Studio Code sigue siendo el editor más popular")
print("2. PyCharm muestra crecimiento moderado debido a la popularidad de Python")
print("3. Eclipse ha disminuido, pero sigue siendo relevante para algunos desarrolladores")
print("4. IntelliJ IDEA sigue en crecimiento, especialmente para Java y Kotlin")
print("5. Xcode mantiene su dominio en el desarrollo para dispositivos Apple")
print("6. Android Studio sigue siendo la principal opción para el desarrollo móvil en Android")

# Mostrar predicciones para 2024 en consola
print("\nPredicciones 2024:")
print("- Visual Studio Code: Continuará siendo una opción líder entre los editores de código")
print("- PyCharm: Se incrementará su uso debido a la popularidad de Python")
print("- Eclipse: Su uso continuará disminuyendo, pero aún será usado por algunos desarrolladores")
print("- IntelliJ IDEA: Crecerá especialmente en entornos Java y Kotlin")
print("- Xcode: Seguirá siendo clave en el desarrollo de aplicaciones para Apple")
print("- Android Studio: Aumentará su adopción con nuevas características para el desarrollo móvil")
