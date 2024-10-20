import streamlit as st
import csv
import datetime
import pandas as pd

# Función para registrar la percepción de esfuerzo
def registrar_rpe(rpe_value):
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
    dia_semana = datetime.datetime.now().strftime("%A")
    
    # Guardar los datos en un archivo CSV
    with open('percepcion_esfuerzo.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([fecha_actual, dia_semana, rpe_value])
    
    st.success(f"Percepción de esfuerzo de {rpe_value} registrada para el día {dia_semana} ({fecha_actual}).")

# Función para ver el historial
def ver_historial():
    try:
        # Leer el archivo CSV en un DataFrame de Pandas
        data = pd.read_csv('percepcion_esfuerzo.csv', names=['Fecha', 'Día', 'RPE'])
        st.write("Historial de Percepción de Esfuerzo:")
        st.dataframe(data)
    except FileNotFoundError:
        st.warning("No hay datos registrados aún.")

# Interfaz principal de la app
def main():
    st.title("Registro de Percepción de Esfuerzo (RPE)")
    
    # Seleccionar el modo de operación
    menu = ["Registrar RPE", "Ver historial"]
    choice = st.sidebar.selectbox("Menú", menu)
    
    if choice == "Registrar RPE":
        st.subheader("Registrar percepción de esfuerzo diaria")
        # Slider para la percepción de esfuerzo (0-10)
        rpe_value = st.slider("Selecciona tu percepción de esfuerzo (0-10)", 0, 10, 5)
        
        # Botón para registrar la percepción
        if st.button("Registrar"):
            registrar_rpe(rpe_value)
    
    elif choice == "Ver historial":
        st.subheader("Ver historial de RPE")
        ver_historial()

if __name__ == '__main__':
    main()
