import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de herramientas de testing con porcentajes desorganizados
herramientas_pruebas = {
    'Herramientas Pruebas': ['Jest'] * 7 + ['Mocha'] * 7 + ['Selenium'] * 7 + ['JUnit'] * 7 +
                 ['Cypress'] * 7 + ['Karma'] * 7 + ['Jasmine'] * 7 + ['TestNG'] * 7 +
                 ['Puppeteer'] * 7 + ['Chai'] * 7,
    'Año': [2017, 2018, 2019, 2020, 2021, 2022, 2023] * 10,
    'Porcentaje': [
        25, 10, 22, 30, 35, 5, 40,  # Jest
        16, 20, 10, 14, 18, 22, 12,   # Mocha
        12, 5, 8, 10, 14, 16, 6,      # Selenium
        40, 30, 25, 35, 50, 45, 55,   # JUnit
        28, 12, 20, 22, 18, 25, 15,   # Cypress
        13, 9, 11, 8, 12, 14, 10,     # Karma
        9, 10, 7, 12, 8, 11, 13,      # Jasmine
        7, 8, 12, 6, 9, 10, 11,       # TestNG
        7, 4, 8, 5, 10, 9, 6,         # Puppeteer
        16, 5, 14, 12, 9, 10, 18    # Chai
    ]
}

# Crear DataFrame para las herramientas de testing
df_herramientas_pruebas = pd.DataFrame(herramientas_pruebas)

# Crear un gráfico de líneas con un estilo llamativo
plt.figure(figsize=(12, 6))  # Ajustar el tamaño de la figura

# Gráfico con líneas suaves y marcadores llamativos
sns.lineplot(data=df_herramientas_pruebas, x='Año', y='Porcentaje', hue='Herramientas Pruebas', 
             marker='o', linewidth=3, palette="Set2", markersize=8)

# Personalizar el gráfico
plt.title('Tendencias de uso de herramientas de testing (2017-2023)', fontsize=18, pad=20, color='purple', fontweight='bold')
plt.xlabel('Año', fontsize=14, color='darkred')
plt.ylabel('Porcentaje (%)', fontsize=14, color='darkred')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Herramientas Pruebas / Testing Tool', title_fontsize=12, fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')

# Cambiar el fondo de la gráfica a color claro
plt.gcf().set_facecolor('beige')

# Ajustar el diseño para evitar cortes de texto
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Mostrar conclusiones en consola
print("\nHerramientas de testing más populares:")
print("1. Jest es la herramienta de testing más utilizada en el ecosistema JavaScript")
print("2. Mocha es muy popular en pruebas unitarias en Node.js")
print("3. Selenium es una de las herramientas más usadas para pruebas end-to-end en aplicaciones web")
print("4. JUnit sigue siendo la principal herramienta de testing en el mundo Java")
print("5. Cypress ha ganado popularidad rápidamente por su facilidad de uso")
print("6. Karma se sigue utilizando para pruebas unitarias y de integración")
print("7. Jasmine es ampliamente usado para testing en aplicaciones Angular")
print("8. TestNG sigue siendo popular en entornos de testing en Java")
print("9. Puppeteer se utiliza ampliamente para pruebas automatizadas en Chrome")
print("10. Chai es muy conocido en combinación con Mocha para aserciones en pruebas")

# Predicciones 2024
print("\nPredicciones 2024:")
print("- Jest: Seguirá siendo la opción predilecta para pruebas en JavaScript")
print("- Mocha: Continuará siendo utilizado por su flexibilidad en pruebas unitarias")
print("- Selenium: Seguirá siendo popular para pruebas end-to-end")
print("- JUnit: Permanecerá como estándar en pruebas unitarias en Java")
print("- Cypress: Su adopción seguirá aumentando debido a su facilidad de uso")
print("- Karma: Continuará siendo utilizado para testing en Angular")
print("- Jasmine: Será utilizado mayormente en proyectos Angular")
print("- TestNG: Mantendrá su uso en entornos Java")
print("- Puppeteer: Seguirá creciendo en popularidad para pruebas automatizadas en Chrome")
print("- Chai: Continuará siendo la librería de aserciones preferida en pruebas con Mocha")
