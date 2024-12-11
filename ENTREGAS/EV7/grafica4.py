import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos corregidos con el mismo número de elementos en cada lista (ahora con frameworks)
frameworks_usados = {
    'Framework': ['React'] * 7 + ['Angular'] * 7 + ['Django'] * 7 + ['Spring'] * 7 +
                 ['Vue.js'] * 7 + ['Flask'] * 7 + ['Ruby on Rails'] * 7 + ['Laravel'] * 7 +
                 ['ASP.NET'] * 7 + ['Express'] * 7,
    'Año': [2017, 2018, 2019, 2020, 2021, 2022, 2023] * 10,
    'Porcentaje de Uso': [
        20, 25, 30, 35, 40, 45, 50,  # React
        18, 20, 22, 23, 25, 26, 27,   # Angular
        8, 9, 10, 12, 14, 16, 18,     # Django
        10, 12, 14, 16, 17, 18, 19,   # Spring
        10, 12, 14, 16, 18, 20, 22,   # Vue.js
        5, 6, 7, 8, 9, 10, 12,        # Flask
        7, 8, 9, 10, 11, 12, 13,      # Ruby on Rails
        6, 7, 8, 9, 10, 11, 12,       # Laravel
        4, 5, 6, 7, 8, 9, 10,         # ASP.NET
        5, 6, 7, 8, 9, 9, 9           # Express
    ]
}

# Crear un DataFrame con los datos
df_frameworks_usados = pd.DataFrame(frameworks_usados)

# Crear un gráfico de líneas con un estilo llamativo
plt.figure(figsize=(12, 6))  # Ajustar el tamaño de la figura

# Gráfico con líneas suaves y marcadores llamativos
sns.lineplot(data=df_frameworks_usados, x='Año', y='Porcentaje de Uso', hue='Framework', 
             marker='o', linewidth=3, palette="Set2", markersize=8)

# Personalizar el gráfico
plt.title('Tendencias de uso de frameworks de desarrollo (2017-2023)', fontsize=18, pad=20, color='purple', fontweight='bold')
plt.xlabel('Año', fontsize=14, color='darkred')
plt.ylabel('Porcentaje (%)', fontsize=14, color='darkred')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Framework', title_fontsize=12, fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')

# Cambiar el fondo de la gráfica a color claro
plt.gcf().set_facecolor('beige')

# Ajustar el diseño para evitar cortes de texto
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Mostrar conclusiones en consola
print("\nConclusiones Principales:")
print("1. React sigue siendo el framework más popular para desarrollo front-end")
print("2. Angular continúa siendo una opción popular, especialmente en empresas grandes")
print("3. Django mantiene su presencia fuerte en el desarrollo web backend con Python")
print("4. Spring sigue siendo la opción principal en entornos Java para aplicaciones empresariales")
print("5. Vue.js gana popularidad por su simplicidad y enfoque progresivo")
print("6. Flask continúa siendo la opción preferida para aplicaciones ligeras y microservicios")
print("7. Ruby on Rails sigue siendo muy utilizado en startups y para prototipos rápidos")
print("8. Laravel sigue siendo una opción clave en PHP para el desarrollo web")
print("9. ASP.NET sigue siendo muy popular en soluciones empresariales")
print("10. Express sigue siendo el framework más utilizado en el ecosistema Node.js")

# Mostrar predicciones para 2024 en consola
print("\nPredicciones 2024:")
print("- React: Continuará dominando el mercado de frameworks front-end")
print("- Angular: Aumento moderado, especialmente en empresas grandes")
print("- Django: Su uso se mantendrá estable, especialmente en el backend con Python")
print("- Spring: Continuará creciendo en el ecosistema Java")
print("- Vue.js: Seguirá ganando terreno en el desarrollo web")
print("- Flask: Su adopción aumentará, especialmente en proyectos de microservicios")
print("- Ruby on Rails: Se mantendrá relevante en startups y desarrollo rápido")
print("- Laravel: Aumentará su uso, especialmente en aplicaciones PHP web")
print("- ASP.NET: Permanecerá fuerte en el desarrollo de aplicaciones empresariales")
print("- Express: Mantendrá su popularidad en el ecosistema Node.js")
