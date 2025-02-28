📊 Dataset: Automobile Dataset
Este conjunto de datos, disponible en el repositorio de aprendizaje automático de la UCI, contiene información sobre diversas características de automóviles, incluyendo:

Marca y modelo: Identificador del fabricante y modelo del vehículo.
Especificaciones técnicas: Como el tipo de motor, número de cilindros, consumo de combustible, entre otros.
Características de precio y seguro: Incluyendo el precio del automóvil y costos asociados.
Tamaño del Dataset: Aproximadamente 200 registros y 26 columnas, lo que lo hace manejable para equipos con recursos limitados.

Nota: Este dataset contiene valores faltantes representados por el símbolo '?', posibles duplicados y datos desordenados, lo que lo hace ideal para practicar técnicas de limpieza y preprocesamiento de datos.

🔍 Preguntas Clave para el Análisis Empresarial
Para orientar tu análisis, aquí hay algunas preguntas que podrías abordar:

¿Cuál es la relación entre el precio del automóvil y sus especificaciones técnicas?

Objetivo: Identificar cómo características como el tipo de motor, número de cilindros y consumo de combustible afectan el precio del vehículo.

¿Qué marcas de automóviles tienen los costos de seguro más altos?

Objetivo: Evaluar si ciertas marcas están asociadas con primas de seguro más elevadas y analizar las posibles causas.
¿Existen patrones de consumo de combustible según el tipo de vehículo?

Objetivo: Clasificar los vehículos en categorías según su eficiencia de combustible y entender las características comunes en cada categoría.
¿Cómo afectan las especificaciones técnicas a la clasificación de seguridad del vehículo?

Objetivo: Determinar si ciertas configuraciones técnicas están correlacionadas con mejores o peores clasificaciones de seguridad.
🛠️ Pasos para el Análisis y Desarrollo de un Modelo de Machine Learning
Carga y Exploración de Datos:

Importa el dataset en tu entorno de análisis (por ejemplo, utilizando pandas en Python).
Explora la estructura de los datos y obtén una visión general de las columnas y tipos de datos.
Limpieza de Datos:

Identifica y maneja valores faltantes: Reemplaza los '?' por NaN y decide si imputar o eliminar registros con datos incompletos.
Detecta y elimina duplicados: Asegúrate de que cada registro sea único para evitar sesgos en el análisis.
Estandariza formatos: Asegúrate de que las fechas, precios y otras variables estén en el formato correcto.
Análisis Exploratorio de Datos (EDA):

Visualiza distribuciones de variables clave como precio, consumo de combustible, etc.
Analiza correlaciones entre variables para identificar relaciones significativas.
Ingeniería de Características:

Crea nuevas variables que puedan ser útiles para el modelo, como categorías de eficiencia de combustible, rangos de precios, etc.
Desarrollo de un Modelo de Machine Learning:

Objetivo del Modelo: Predecir el precio del automóvil basado en sus especificaciones técnicas.
Selección del Modelo: Modelos de regresión lineal, árboles de decisión o algoritmos de ensemble como Random Forest.
Entrenamiento y Evaluación: Divide los datos en conjuntos de entrenamiento y prueba, entrena el modelo y evalúa su desempeño utilizando métricas adecuadas como el RMSE o el MAE.
Implementación y Comunicación de Resultados:

Despliega el modelo en un entorno de producción si es aplicable.
Comunica los hallazgos a las partes interesadas mediante visualizaciones y reportes claros.




----------------DESPLIEGE DE ACTIVIDADES------------

**PRIMERA SOLICITUD**

¿Cuál es la relación entre el precio del automóvil y sus especificaciones técnicas?

Objetivo: Identificar cómo características como el tipo de motor, número de cilindros y consumo de combustible afectan el precio del vehículo.


🚀 Plan de trabajo para analizar el impacto de características en el precio del vehículo
1️⃣ Limpieza de datos (Data Cleaning)
Eliminar valores nulos o imputarlos si es necesario.
Convertir variables categóricas a numéricas (tipo de motor, número de cilindros, etc.).
Revisar outliers en el precio y otras variables clave.
Normalizar variables si tienen escalas muy diferentes.
2️⃣ Visualización de datos 📊 (para entender tendencias)
Histogramas para distribución de variables.
Boxplots para detectar outliers.
Scatter plots (ejemplo: engine size vs price, highway mpg vs price).
Matriz de correlación (heatmap) para identificar relaciones entre variables.
3️⃣ Análisis Exploratorio de Datos (EDA)
Revisar la correlación entre variables (para evitar multicolinealidad).
Ver si hay patrones claros en los datos (por ejemplo, si autos con más cilindros tienden a ser más caros).
Identificar características más relevantes para la predicción.
4️⃣ Dashboard en DAX (Power BI) con gráficas dinámicas 📈
Subir datos a un endpoint público para acceder desde Power BI.
Crear visualizaciones interactivas para responder preguntas del jefe.
Incluir más preguntas a medida que el análisis avance.
5️⃣ Creación del modelo de predicción
Calcular VIF para eliminar multicolinealidad.
Seleccionar variables más importantes.
Probar modelos de regresión (OLS, Ridge, Lasso).
Comparar métricas (R², RMSE, MAE).
Dejar el modelo listo para ser desplegado en la nube cuando se tenga acceso.