import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos sobre el estado de la seguridad en código abierto
seguridad_codigo_abierto = {
    'Aspecto': ['Proyectos Vulnerables'] * 7 + ['Vulnerabilidades Promedio'] * 7,
    'Año': [2017, 2018, 2019, 2020, 2021, 2022, 2023] * 2,
    'Porcentaje': [
       10, 15, 50, 70, 90, 95, 98,  # Proyectos Vulnerables
        1.0, 2.5, 5.0, 7.5, 10.0, 15.0, 20.0  # Vulnerabilidades Promedio
    ]
}

# Crear DataFrame para el estado de la seguridad en código abierto
df_seguridad_codigo_abierto = pd.DataFrame(seguridad_codigo_abierto)

# Crear un gráfico de líneas
plt.figure(figsize=(10, 5))

# Gráfico con líneas y marcadores
sns.lineplot(data=df_seguridad_codigo_abierto, x='Año', y='Porcentaje', hue='Aspecto',
             marker='o', linewidth=2, palette="viridis", markersize=6)

# Personalizar el gráfico
plt.title('Estado de la seguridad en código abierto (2017-2023)', fontsize=16, pad=15, color='darkblue', fontweight='bold')
plt.xlabel('Año', fontsize=12, color='darkgreen')
plt.ylabel('Porcentaje (%)', fontsize=12, color='darkgreen')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Aspecto', title_fontsize=10, fontsize=9, bbox_to_anchor=(1.05, 1), loc='upper left')

# Cambiar el fondo de la gráfica a un tono claro
plt.gcf().set_facecolor('mintcream')

# Ajustar el diseño para evitar cortes de texto
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Conclusiones en consola
print("\nEstado de la seguridad en código abierto:")
print("1. El porcentaje de proyectos vulnerables ha ido en aumento desde 2017.")
print("2. Las vulnerabilidades promedio por proyecto también han incrementado.")
print("3. Es crucial implementar prácticas de seguridad para mitigar estos riesgos.")
print("4. Las auditorías de código y el uso de herramientas de escaneo son clave.")

# Predicciones 2024
print("\nPredicciones 2024:")
print("- Los proyectos vulnerables podrían superar el 50% si no se toman medidas preventivas.")
print("- Las vulnerabilidades promedio continuarán creciendo debido a la complejidad del software.")
print("- Se espera una adopción más amplia de herramientas automatizadas de detección de vulnerabilidades.")
print("- Las comunidades de código abierto aumentarán su enfoque en mejorar la seguridad desde las primeras etapas del desarrollo.")
