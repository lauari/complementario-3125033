import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de lenguajes más populares en Git con porcentajes desorganizados
lenguajes_git = {
    'Lenguaje': ['Python'] * 7 + ['JavaScript'] * 7 + ['Java'] * 7 + ['C#'] * 7 +
                ['C++'] * 7 + ['Go'] * 7 + ['Ruby'] * 7 + ['PHP'] * 7 +
                ['Swift'] * 7 + ['Kotlin'] * 7,
    'Año': [2017, 2018, 2019, 2020, 2021, 2022, 2023] * 10,
    'Porcentaje': [
        20, 25, 30, 40, 45, 50, 55,  # Python
        30, 35, 40, 45, 50, 55, 60,  # JavaScript
        15, 18, 20, 25, 30, 35, 40,  # Java
        12, 15, 18, 22, 28, 34, 38,  # C#
        10, 12, 14, 18, 22, 28, 32,  # C++
        8, 10, 12, 15, 18, 22, 25,   # Go
        6, 7, 9, 12, 15, 18, 20,     # Ruby
        4, 5, 7, 9, 11, 13, 15,      # PHP
        18, 20, 22, 25, 30, 35, 40,  # Swift
        5, 6, 8, 10, 12, 14, 16      # Kotlin
    ]
}

# Crear DataFrame para los lenguajes más populares en Git
df_lenguajes_git = pd.DataFrame(lenguajes_git)

## Crear un gráfico de líneas con un tamaño más compacto
plt.figure(figsize=(10, 5))  # Reducir el tamaño de la figura

# Gráfico con líneas suaves y marcadores llamativos
sns.lineplot(data=df_lenguajes_git, x='Año', y='Porcentaje', hue='Lenguaje', 
             marker='o', linewidth=2, palette="Set2", markersize=6)

# Personalizar el gráfico
plt.title('Lenguajes más populares en Git (2017-2023)', fontsize=16, pad=15, color='darkblue', fontweight='bold')
plt.xlabel('Año', fontsize=12, color='darkgreen')
plt.ylabel('Popularidad (%)', fontsize=12, color='darkgreen')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Lenguajes', title_fontsize=10, fontsize=9, bbox_to_anchor=(1.05, 1), loc='upper left')

# Cambiar el fondo de la gráfica a un tono claro
plt.gcf().set_facecolor('mintcream')

# Ajustar el diseño para evitar cortes de texto
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Mostrar conclusiones en consola
print("\nLenguajes más populares en Git:")
print("1. Python sigue siendo muy popular debido a su versatilidad y uso en IA, ciencia de datos y desarrollo web.")
print("2. JavaScript es esencial para el desarrollo web y tiene un crecimiento constante.")
print("3. Java sigue siendo un lenguaje dominante en aplicaciones empresariales y móviles.")
print("4. C# es muy utilizado en el desarrollo de aplicaciones de escritorio y videojuegos.")
print("5. C++ es fundamental para el desarrollo de software de alto rendimiento y sistemas embebidos.")
print("6. Go se está volviendo popular para el desarrollo de aplicaciones escalables y microservicios.")
print("7. Ruby sigue siendo popular, especialmente en el desarrollo web con Rails.")
print("8. PHP sigue siendo utilizado en la creación de aplicaciones web, aunque ha perdido algo de popularidad.")
print("9. Swift se está consolidando en el desarrollo de aplicaciones para el ecosistema Apple.")
print("10. Kotlin está ganando popularidad como alternativa a Java en el desarrollo de aplicaciones Android.")

# Predicciones 2024
print("\nPredicciones 2024:")
print("- Python seguirá dominando en ciencia de datos, IA y desarrollo web.")
print("- JavaScript se mantendrá como el lenguaje más popular para el desarrollo web.")
print("- Java seguirá siendo esencial para aplicaciones grandes y de misión crítica.")
print("- C# continuará siendo utilizado en desarrollo de videojuegos con Unity y aplicaciones de Windows.")
print("- C++ seguirá siendo la opción preferida para sistemas de bajo nivel y de alto rendimiento.")
print("- Go se fortalecerá en la creación de aplicaciones distribuidas y de infraestructura.")
print("- Ruby tendrá una base de usuarios estable en desarrollo web con Ruby on Rails.")
print("- PHP se mantendrá como un lenguaje clave en el desarrollo de aplicaciones web dinámicas.")
print("- Swift seguirá siendo la elección preferida para el desarrollo de aplicaciones iOS.")
print("- Kotlin continuará ganando terreno como la principal opción para aplicaciones Android.")
