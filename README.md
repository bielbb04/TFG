# Simulacions del Model QIF i Processos Estocàstics

Aquest repositori conté una sèrie de Jupyter Notebooks i scripts en Python dedicats a la simulació computacional i l'anàlisi del model neuronal **Quadratic Integrate-and-Fire (QIF)** sota diferents règims de soroll estocàstic, així com fonaments teòrics de processos estocàstics elementals.

## 📂 Contingut del Repositori

A continuació es detalla la funció de cadascun dels arxius inclosos:

### 1. `Simulació QIF.ipynb`
Aquest quadern es centra en la part determinista del model QIF. 
* Traça el retrat de fase del sistema, visualitzant la dinàmica de la variable d'estat $V$ en funció del corrent aplicat ($I_{app}$).
* Identifica i dibuixa gràficament els punts d'equilibri del sistema: l'atractor (estable) i el repulsor (inestable)[cite: 3].

### 2. `QIF amb renou gaussià.ipynb`
Simulació estocàstica del model QIF perturbat per **soroll blanc gaussià**[cite: 2].
* Implementa la integració numèrica utilitzant el mètode d'Euler-Maruyama[cite: 2].
* Inclou algorismes per estimar paràmetres estadístics a partir de les trajectòries simulades, com el corrent aplicat ($I_{app}$) i l'amplitud del soroll ($\sigma$)[cite: 2].

### 3. `QIF amb OU process.ipynb`
Estén l'anàlisi del model QIF modelant el soroll sinàptic o d'entrada mitjançant un **Procés d'Ornstein-Uhlenbeck (OU)** (soroll de color)[cite: 1].
* Simula la dinàmica acoblada de la neurona QIF i el procés de reversió a la mitjana[cite: 1].
* Implementa mètodes estadístics per inferir els paràmetres subjacents del procés de soroll ($\theta$, $\sigma$) comparant els valors reals amb els estimats i calculant els errors absoluts[cite: 1].

### 4. `brownian simulation.py`
Un script pur de Python dissenyat per generar i visualitzar simulacions fonamentals de **Moviment Brownià** (Procés de Wiener)[cite: 4].
* Calcula trajectòries a través de la suma acumulativa d'increments amb distribució normal[cite: 4].
* Genera gràfics personalitzables amb múltiples realitzacions del procés estocàstic sobre un horitzó temporal finit[cite: 4].
