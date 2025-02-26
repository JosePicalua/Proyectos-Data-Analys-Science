El Automobile Dataset no es un dataset de clasificación, sino de regresión, ya que la variable objetivo (price) es un valor numérico continuo. En un problema de machine learning supervisado, este dataset puede usarse para predecir el precio de un automóvil en función de sus características.


📌 Definición de las columnas del Automobile Dataset
Columna	            Descripción	                                                Tipo de dato
symboling	        Clasificación de riesgo del seguro del automóvil (-3 a 3)	int
normalized-losses	Promedio de pérdidas normalizadas por aseguradoras 
                    (tiene valores ? que representan datos          faltantes)	                                                float
make	            Marca del automóvil (Ej: alfa-romero, audi, bmw)	        string
fuel-type	        Tipo de combustible (gas o diesel)	                        string
aspiration	        Tipo de inducción de aire (std = normal, 
                    turbo = turboalimentado)	                                string
num-of-doors	    Número de puertas (two, four)	                            string
body-style	        Tipo de carrocería (convertible, sedan, hatchback, etc.)	string
drive-wheels	    Tipo de tracción (fwd, rwd, 4wd)	                        string
engine-location	    Ubicación del motor (front o rear)	                        string
wheel-base	        Distancia entre los ejes en pulgadas	                    float
length	            Largo del vehículo en pulgadas	                            float
width	            Ancho del vehículo en pulgadas	                            float
height	            Altura del vehículo en pulgadas	                            float
curb-weight	        Peso del vehículo vacío en libras	                        int
engine-type	        Tipo de motor (dohc, ohcv, ohc, etc.)	                    string
num-of-cylinders	Número de cilindros del motor (four, six, eight, etc.)	    string
engine-size	        Cilindrada del motor en cm³	                                int
fuel-system	        Sistema de combustible (mpfi, 2bbl, idi, etc.)	            string
bore	            Diámetro del cilindro en pulgadas	                        float
stroke	            Longitud de la carrera del pistón en pulgadas	            float
compression-ratio	Relación de compresión del motor	                        float
horsepower	        Potencia del motor en HP (caballos de fuerza)	            int
peak-rpm	        Máximas revoluciones por minuto del motor	                int
city-mpg	        Consumo de combustible en ciudad (millas por galón)	        int
highway-mpg	        Consumo de combustible en carretera (millas por galón)	    int
price	            Precio del automóvil en dólares 
                    (variable objetivo para regresión)	                        int



📌 Definiciones de Columnas del Automobile Dataset
symboling (int) → Clasificación de riesgo del seguro

Rango de -3 a 3. Un número mayor indica mayor riesgo.
normalized-losses (float) → Pérdidas normalizadas por aseguradora

Valor numérico que representa el promedio de pérdidas por modelo de automóvil. Puede contener valores faltantes (?).
make (str) → Marca del automóvil

Ejemplo: Toyota, BMW, Honda, etc.
fuel-type (str) → Tipo de combustible

gas (gasolina) o diesel.
aspiration (str) → Tipo de inducción del motor

std (natural) o turbo (turboalimentado).
num-of-doors (str) → Número de puertas

Puede ser two (2) o four (4), con valores faltantes posibles.
body-style (str) → Tipo de carrocería

Ejemplo: sedan, hatchback, wagon, convertible, hardtop.
drive-wheels (str) → Tipo de tracción

fwd (tracción delantera), rwd (tracción trasera), 4wd (tracción en las cuatro ruedas).
engine-location (str) → Ubicación del motor

front (frontal) o rear (trasero).
wheel-base (float) → Distancia entre ejes (pulgadas)

Afecta estabilidad y espacio interior.
length (float) → Largo del automóvil (pulgadas)
Longitud total del vehículo.
width (float) → Ancho del automóvil (pulgadas)
Influye en la estabilidad y espacio interior.
height (float) → Altura del automóvil (pulgadas)
Afecta aerodinámica y comodidad.
curb-weight (float) → Peso en vacío (libras)
Peso del vehículo sin pasajeros ni carga.
engine-type (str) → Tipo de motor
Ejemplo: dohc (doble árbol de levas), ohc (árbol de levas en cabeza), l (motor en línea), rotor (motor rotativo).
num-of-cylinders (str) → Número de cilindros del motor
Puede ser two, three, four, five, six, eight, twelve.
engine-size (float) → Tamaño del motor (cc)
Relacionado con la potencia y consumo de combustible.
fuel-system (str) → Sistema de inyección de combustible
Ejemplo: mpfi (inyección multipunto), 2bbl (carburador de doble barril).
bore (float) → Diámetro del cilindro (pulgadas)
Afecta la potencia del motor.
stroke (float) → Carrera del pistón (pulgadas)
Influye en la eficiencia y consumo de combustible.
compression-ratio (float) → Relación de compresión del motor
Cuanto mayor sea, mejor la eficiencia, pero puede requerir combustible premium.
horsepower (float) → Potencia del motor (HP - caballos de fuerza)
Indica el rendimiento del motor. Puede contener valores faltantes (?).
peak-rpm (float) → Revoluciones máximas del motor (RPM)
Indica el punto máximo de potencia del motor.
city-mpg (float) → Consumo de combustible en ciudad (millas por galón - MPG)
Cuanto mayor, más eficiente es el vehículo en áreas urbanas.
highway-mpg (float) → Consumo de combustible en carretera (MPG)
Medida de eficiencia en viajes largos.
price (float) → Precio del automóvil en dólares
Valor objetivo si se quiere predecir el costo del vehículo. Puede contener valores faltantes (?).