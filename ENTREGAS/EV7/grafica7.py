import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de tendencias en la industria del software con porcentajes desorganizados
tendencias_industria_software = {
    'Tendencia': ['Inteligencia Artificial'] * 7 + ['Ciberseguridad'] * 7 + ['Cloud Computing'] * 7 + ['Desarrollo Ágil'] * 7 +
                 ['Big Data'] * 7 + ['Automatización'] * 7 + ['Blockchain'] * 7 + ['Internet de las Cosas'] * 7 +
                 ['Realidad Virtual'] * 7 + ['5G'] * 7,
    'Año': [2017, 2018, 2019, 2020, 2021, 2022, 2023] * 10,
    'Porcentaje': [
        20, 25, 30, 40, 50, 60, 70,  # Inteligencia Artificial
        15, 20, 25, 30, 35, 40, 50,  # Ciberseguridad
        30, 35, 40, 45, 50, 55, 65,  # Cloud Computing
        40, 45, 50, 55, 60, 65, 70,  # Desarrollo Ágil
        25, 30, 35, 40, 45, 50, 60,  # Big Data
        10, 15, 20, 30, 40, 50, 60,  # Automatización
        5, 10, 15, 20, 25, 30, 40,   # Blockchain
        8, 12, 15, 18, 25, 30, 35,   # Internet de las Cosas
        2, 5, 10, 15, 20, 25, 30,    # Realidad Virtual
        0, 5, 10, 15, 25, 35, 50     # 5G
    ]
}

# Crear DataFrame para las tendencias del software
df_tendencias_industria_software = pd.DataFrame(tendencias_industria_software)

## Crear un gráfico de líneas con un tamaño más compacto
plt.figure(figsize=(10, 5))  # Reducir el tamaño de la figura

# Gráfico con líneas suaves y marcadores llamativos
sns.lineplot(data=df_tendencias_industria_software, x='Año', y='Porcentaje', hue='Tendencia', 
             marker='o', linewidth=2, palette="coolwarm", markersize=6)

# Personalizar el gráfico
plt.title('Tendencias de la industria del software (2017-2023)', fontsize=16, pad=15, color='darkblue', fontweight='bold')
plt.xlabel('Año', fontsize=12, color='darkgreen')
plt.ylabel('Popularidad (%)', fontsize=12, color='darkgreen')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Tendencias', title_fontsize=10, fontsize=9, bbox_to_anchor=(1.05, 1), loc='upper left')

# Cambiar el fondo de la gráfica a un tono claro
plt.gcf().set_facecolor('mintcream')

# Ajustar el diseño para evitar cortes de texto
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Mostrar conclusiones en consola
print("\nTendencias de la industria del software más populares:")
print("1. Inteligencia Artificial ha mostrado un crecimiento exponencial y seguirá dominando la industria.")
print("2. Ciberseguridad está en auge debido al aumento de amenazas digitales.")
print("3. Cloud Computing sigue siendo esencial para la infraestructura tecnológica.")
print("4. Desarrollo Ágil se mantiene como el estándar en gestión de proyectos de software.")
print("5. Big Data impulsa la toma de decisiones basadas en datos.")
print("6. Automatización está creciendo rápidamente en la industria para reducir costos y aumentar eficiencia.")
print("7. Blockchain se está adoptando más allá de las criptomonedas.")
print("8. Internet de las Cosas conecta más dispositivos cada año.")
print("9. Realidad Virtual ha comenzado a crecer con aplicaciones en entretenimiento y educación.")
print("10. 5G está transformando las capacidades de conectividad y velocidad en todo el mundo.")

# Predicciones 2024
print("\nPredicciones 2024:")
print("- Inteligencia Artificial seguirá liderando, especialmente con avances en IA generativa.")
print("- Ciberseguridad verá inversiones masivas debido a la sofisticación de los ataques.")
print("- Cloud Computing continuará creciendo con enfoques en nubes híbridas.")
print("- Desarrollo Ágil se combinará más con prácticas DevOps.")
print("- Big Data se centrará en análisis en tiempo real y mayor integración con IA.")
print("- Automatización avanzará hacia la hiperautomatización.")
print("- Blockchain ampliará su uso en la gestión de identidades y contratos inteligentes.")
print("- Internet de las Cosas integrará más inteligencia en dispositivos conectados.")
print("- Realidad Virtual se utilizará más en formación profesional y simulaciones.")
print("- 5G habilitará nuevas aplicaciones en ciudades inteligentes y vehículos autónomos.")
