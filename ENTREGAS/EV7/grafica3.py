import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de uso estimado de comunidades de desarrolladores entre 2023 y 2028
comunidades_desarrolladoras = {
    'Año': [2023, 2024, 2025, 2026, 2027, 2028] * 5,
    'Comunidad': ['Stack Overflow'] * 6 + ['GitHub'] * 6 + ['Dev.to'] * 6 + ['Reddit'] * 6 + ['GitLab'] * 6,
    'Porcentaje de Participación': [
        # Stack Overflow (esperado crecimiento moderado)
        75, 78, 80, 82, 84, 86,
        # GitHub (esperado crecimiento continuo)
        68, 70, 73, 76, 80, 83,
        # Dev.to (expansión creciente)
        20, 25, 30, 35, 40, 45,
        # Reddit (crecimiento constante de subreddits de programación)
        35, 40, 42, 44, 46, 48,
        # GitLab (expansión entre desarrolladores de código abierto)
        30, 35, 38, 42, 45, 47
    ]
}

# Crear un DataFrame con los datos
df_comunidades_desarrolladoras = pd.DataFrame(comunidades_desarrolladoras)

# Crear un gráfico de líneas con un tamaño más pequeño
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura (más pequeño)

sns.lineplot(data=df_comunidades_desarrolladoras, x='Año', y='Porcentaje de Participación', hue='Comunidad', marker='o', linewidth=2.5)

# Personalizar el gráfico
plt.title('Proyección de crecimiento de comunidades de desarrolladores (2023-2028)', fontsize=16, pad=20)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Porcentaje de Participación (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Comunidad', title_fontsize=12, fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')

# Ajustar el diseño para evitar cortes de texto
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Mostrar conclusiones en consola
print("\nConclusiones Principales:")
print("1. Stack Overflow continuará siendo la comunidad más grande de desarrolladores.")
print("2. GitHub verá un crecimiento continuo debido a su rol clave en proyectos open-source.")
print("3. Dev.to tendrá un aumento importante por su enfoque inclusivo y educativo.")
print("4. Reddit seguirá siendo popular por sus subreddits de desarrollo y discusión técnica.")
print("5. GitLab ganará terreno debido a su integración de herramientas DevOps y CI/CD.")

# Mostrar predicciones para 2023-2028 en consola
print("\nPredicciones 2023-2028:")
print("- Stack Overflow: Continuará siendo la comunidad líder de preguntas y respuestas.")
print("- GitHub: Aumentará en participación, con más proyectos open-source.")
print("- Dev.to: Expansión por su enfoque amigable para desarrolladores novatos.")
print("- Reddit: Crecimiento en la participación de comunidades técnicas.")
print("- GitLab: Aumento de la base de usuarios debido a su completo sistema de integración y entrega continua (CI/CD).")
