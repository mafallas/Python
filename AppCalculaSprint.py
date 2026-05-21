import streamlit as st
from datetime import datetime, timedelta


def calcular_sprints(fecha_inicio, num_sprints=6, duracion_dias=15):
    sprints = []
    inicio_actual = fecha_inicio

    for i in range(1, num_sprints + 1):
        fin_sprint = inicio_actual + timedelta(days=duracion_dias - 1)
        sprints.append((i, inicio_actual, fin_sprint))

        inicio_actual = fin_sprint + timedelta(days=1)

    return sprints

# =============================
# INTERFAZ WEB
# =============================

st.title("📅 Sprint Release Planner")

fecha_inicio = st.date_input("Selecciona la fecha de inicio del Sprint")

if st.button("Calcular Release Plan"):

    sprints = calcular_sprints(fecha_inicio)

    st.subheader("📌 Resultado del Release Plan")

    for sprint_num, inicio, fin in sprints:
        st.write(f"✅ Sprint {sprint_num} | Start: {inicio} | End: {fin}")