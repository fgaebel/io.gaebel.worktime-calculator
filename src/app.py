import streamlit as st

from datetime import datetime, timedelta


st.title("🕒 Work-Life Calculator")

start_time = st.time_input("You started at", value=datetime.strptime("08:00", "%H:%M").time(), step=60)

work_hours = st.number_input("Working Hours", min_value=0, max_value=12, value=7)

work_minutes = st.number_input("Working Minutes", min_value=0, max_value=59, value=36)

break_minutes = st.number_input("Break", min_value=0, max_value=120, value=45)

if st.button("Calculate Clock-Out"):

    start_dt = datetime.combine(datetime.today(), start_time)

    end_dt = start_dt + timedelta(hours=work_hours, minutes=work_minutes + break_minutes)

    st.success(f"Life starts at {end_dt.strftime('%H:%M')}")