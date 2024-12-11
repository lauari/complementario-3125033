import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar el estilo y tema de los gráficos
sns.set_theme(style="darkgrid")

# Datos de uso de bases de datos más populares entre 2017 y 2023
database_trends = {
    'Año': [2017, 2018, 2019, 2020, 2021, 2022, 2023] * 6,
    'Base de datos': ['MySQL'] * 7 + ['PostgreSQL'] * 7 + ['MongoDB'] * 7 + 
                ['SQLite'] * 7 + ['OracleDB'] * 7 + ['Redis'] * 7,
    'Porcentaje': [
        # MySQL
        32.5, 33.0, 34.2, 35.7, 36.1, 36.5, 36.9,
        # PostgreSQL
        15.2, 17.8, 20.1, 23.3, 26.7, 28.9, 30.5,
        # MongoDB
        12.1, 14.2, 15.8, 17.6, 19.8, 21.3, 22.9,
        # SQLite
        18.5, 18.2, 17.7, 17.1, 16.8, 16.4, 16.0,
        # OracleDB
        10.3, 9.8, 9.4, 9.1, 8.9, 8.6, 8.2,
        # Redis
        6.4, 7.0, 7.8, 8.6, 9.4, 10.2, 11.1
    ]
}

# Crear un DataFrame con los datos
df_database_trends = pd.DataFrame(database_trends)

# Crear un gráfico de líneas con un tamaño más grande
plt.figure(figsize=(16, 9))  # Ajustar el tamaño de la figura (más grande)

sns.lineplot(data=df_database_trends, x='Año', y='Porcentaje', hue='Base de datos', marker='o', linewidth=2.5)

# Personalizar el gráfico
plt.title('Tendencias de uso de bases de datos (2017-2023)', fontsize=16, pad=20)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Base de datos', title_fontsize=12, fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')

## Añadir proyecciones para el año 2024
plt.axvline(x=2023, color='gray', linestyle='--', alpha=0.5)  # Línea vertical para marcar el año 2023
plt.text(2023.8, 20, 'Proyecciones 2024:', fontsize=10)  # Título de las proyecciones
plt.text(2023.8, 18, '• MySQL: Liderazgo estable en bases de datos relacionales', fontsize=9)
plt.text(2023.8, 16, '• PostgreSQL: Crecimiento continuo en aplicaciones modernas', fontsize=9)
plt.text(2023.8, 14, '• MongoDB: Demanda alta en bases de datos NoSQL', fontsize=9)
plt.text(2023.8, 12, '• Redis: Incremento por su uso en cachés y colas', fontsize=9)

# Ajustar el diseño para evitar cortes de texto
plt.tight_layout()

# Guardar el gráfico en un archivo
# plt.savefig('database_trends.png', bbox_inches='tight', dpi=300)
plt.show()

# Mostrar conclusiones en consola
print("\nConclusiones Principales:")
print("1. MySQL sigue siendo líder en bases de datos relacionales")
print("2. PostgreSQL muestra el crecimiento más rápido entre las bases de datos modernas")
print("3. MongoDB domina en el espacio NoSQL")
print("4. Redis está en aumento debido a su uso en sistemas distribuidos")

# Mostrar predicciones para 2024 en consola
print("\nPredicciones 2024:")
print("- MySQL: Seguirá siendo una opción sólida en aplicaciones tradicionales")
print("- PostgreSQL: Continuará creciendo gracias a su flexibilidad y rendimiento")
print("- MongoDB: La adopción de NoSQL impulsará su popularidad")
print("- Redis: Más aplicaciones lo integrarán para mejorar el rendimiento")
