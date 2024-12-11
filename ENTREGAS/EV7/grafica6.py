import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de metodologías de desarrollo con porcentajes desorganizados
metodologias_desarrollo = {
    'Metodología': ['Scrum'] * 7 + ['Kanban'] * 7 + ['XP'] * 7 + ['Waterfall'] * 7 +
                    ['Lean'] * 7 + ['Agile'] * 7 + ['DevOps'] * 7 + ['SAFe'] * 7 +
                    ['FDD'] * 7 + ['Crystal'] * 7,
    'Año': [2017, 2018, 2019, 2020, 2021, 2022, 2023] * 10,
    'Porcentaje': [
        40, 20, 30, 50, 45, 25, 60,  # Scrum
        25, 30, 15, 35, 40, 10, 50,  # Kanban
        18, 15, 20, 10, 25, 12, 30,  # XP
        50, 40, 35, 30, 25, 20, 15,  # Waterfall
        10, 15, 18, 12, 20, 25, 22,  # Lean
        60, 50, 45, 55, 65, 40, 70,  # Agile
        30, 35, 40, 50, 55, 60, 65,  # DevOps
        5, 10, 15, 12, 18, 20, 25,   # SAFe
        8, 12, 10, 5, 7, 6, 9,       # FDD
        6, 8, 5, 7, 10, 12, 9        # Crystal
    ]
}

# Crear DataFrame para las metodologías de desarrollo
df_metodologias_desarrollo = pd.DataFrame(metodologias_desarrollo)

# Pivotar la tabla para gráfico de barras apiladas
df_pivot = df_metodologias_desarrollo.pivot(index='Año', columns='Metodología', values='Porcentaje')

# Crear un gráfico de barras apiladas
plt.figure(figsize=(12, 6))  # Ajustar el tamaño de la figura
df_pivot.plot(kind='bar', stacked=True, colormap='Paired', alpha=0.85, figsize=(12, 6))

# Personalizar el gráfico
plt.title('Tendencias de uso de metodologías de desarrollo (2017-2023)', fontsize=18, pad=20, color='teal', fontweight='bold')
plt.xlabel('Año', fontsize=14, color='darkblue')
plt.ylabel('Porcentaje (%)', fontsize=14, color='darkblue')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(title='Metodologías', title_fontsize=12, fontsize=10, loc='upper left', bbox_to_anchor=(1.05, 1))

# Cambiar el fondo de la gráfica a color neutro
plt.gcf().set_facecolor('whitesmoke')

# Ajustar el diseño para evitar cortes de texto
plt.tight_layout()

# Mostrar el gráfico
plt.show()


# Mostrar conclusiones en consola
print("\nMetodologías de desarrollo más populares:")
print("1. Scrum sigue siendo la metodología más utilizada en equipos ágiles")
print("2. Kanban mantiene su popularidad en equipos con flujos continuos de trabajo")
print("3. XP (Extreme Programming) se utiliza especialmente en proyectos con iteraciones cortas")
print("4. Waterfall ha disminuido significativamente, pero sigue siendo usado en proyectos tradicionales")
print("5. Lean está ganando popularidad en proyectos enfocados en minimizar desperdicios")
print("6. Agile como marco general sigue siendo dominante en el desarrollo de software")
print("7. DevOps ha tenido un crecimiento constante por la integración entre desarrollo y operaciones")
print("8. SAFe se utiliza principalmente en empresas grandes para escalamiento ágil")
print("9. FDD es menos común, pero sigue siendo aplicado en proyectos pequeños y específicos")
print("10. Crystal, aunque poco popular, mantiene su nicho en proyectos pequeños")

# Predicciones 2024
print("\nPredicciones 2024:")
print("- Scrum: Continuará siendo la metodología ágil más adoptada")
print("- Kanban: Aumentará en adopción gracias a su flexibilidad")
print("- XP: Seguirá siendo relevante en proyectos con necesidades extremas de calidad")
print("- Waterfall: Su uso seguirá disminuyendo en favor de metodologías ágiles")