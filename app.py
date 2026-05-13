import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(
    page_title="Robot Fleet Monitoring Simulator",
    layout="wide"
)

st.title("🤖 Robot Fleet Monitoring Simulator")

st.markdown(
    "Simulated operational monitoring system for robotics workflows."
)

# Simulated robot statuses
statuses = [
    "Active",
    "Charging",
    "Idle",
    "Error"
]

# Simulated incidents
incidents = [
    "No Incident",
    "Obstacle Detected",
    "Battery Overheating",
    "Sensor Failure",
    "Navigation Delay"
]

# Generate robot fleet
robots = []

for i in range(1, 6):

    battery = random.randint(15, 100)

    status = random.choice(statuses)

    incident = random.choice(incidents)

    robots.append({
        "Robot": f"RoboUnit-{i}",
        "Battery (%)": battery,
        "Status": status,
        "Current Task": random.choice([
            "Warehouse Delivery",
            "Inspection",
            "Material Transport",
            "Charging",
            "Idle"
        ]),
        "Incident": incident
    })

# Convert to DataFrame
df = pd.DataFrame(robots)

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Robots",
    len(df)
)

col2.metric(
    "Active Robots",
    len(df[df["Status"] == "Active"])
)

col3.metric(
    "Incidents",
    len(df[df["Incident"] != "No Incident"])
)

st.divider()

# Fleet Table
st.subheader("📡 Fleet Status")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# Alerts
st.subheader("⚠ Live Incident Alerts")

alerts = df[df["Incident"] != "No Incident"]

if len(alerts) > 0:

    for _, row in alerts.iterrows():

        st.warning(
            f"{row['Robot']} → {row['Incident']}"
        )

else:
    st.success("No active incidents.")

st.divider()

# Operational Logs
st.subheader("📋 Operational Logs")

for _, row in df.iterrows():

    st.write(
        f"{row['Robot']} | "
        f"Status: {row['Status']} | "
        f"Battery: {row['Battery (%)']}% | "
        f"Task: {row['Current Task']}"
    )

# Refresh button
st.divider()

if st.button("🔄 Refresh Simulation"):
    st.rerun()