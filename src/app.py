import streamlit as st

from datetime import datetime, timedelta


st.title("🕒 Arbeitszeitrechner")

start_time = st.time_input("Startzeit", value=datetime.strptime("08:00", "%H:%M").time(), step=60)

work_hours = st.number_input("Arbeitsstunden", min_value=0, max_value=12, value=7)

work_minutes = st.number_input("Arbeitsminuten", min_value=0, max_value=59, value=36)

break_minutes = st.number_input("Pausenminuten", min_value=0, max_value=120, value=45)

if st.button("Berechne Feierabend"):

    start_dt = datetime.combine(datetime.today(), start_time)

    end_dt = start_dt + timedelta(hours=work_hours, minutes=work_minutes + break_minutes)

    st.success(f"Feierabend ist um: {end_dt.strftime('%H:%M')}")