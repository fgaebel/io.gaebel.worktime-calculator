import streamlit as st

from datetime import datetime, timedelta


st.title("🕒 Your personal End of Business")

start_time = st.time_input("You startet at", value=datetime.strptime("08:00", "%H:%M").time(), step=60)

work_hours = st.number_input("Workhours today", min_value=0, max_value=12, value=7)

work_minutes = st.number_input("Workminutes today", min_value=0, max_value=59, value=36)

break_minutes = st.number_input("Your pause today", min_value=0, max_value=120, value=45)

if st.button("Calculate EOB"):

    start_dt = datetime.combine(datetime.today(), start_time)

    end_dt = start_dt + timedelta(hours=work_hours, minutes=work_minutes + break_minutes)

    st.success(f"Your EOB: {end_dt.strftime('%H:%M')}")