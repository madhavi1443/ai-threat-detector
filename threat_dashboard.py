import streamlit as st
import pandas as pd
import altair as alt
import os
import json

LOG_FILE = "prompt_injection_log.csv"

THREAT_LEVELS = {
    "Benign / Safe": "🟢 Low",
    "Prompt Injection": "🔴 High",
    "Command Injection": "🔴 High",
    "Social Engineering": "🟡 Medium",
    "Jailbreak / Role Play": "🟡 Medium"
}

st.set_page_config(page_title="AI Threat Dashboard", layout="wide")
st.title("🛡️ AI Threat Detection Dashboard")
st.markdown("Visualize past prompt injection test results")

# 🖌️ Fix text visibility in dark mode
st.markdown(
    """
    <style>
    table {
        color: white !important;
    }
    thead tr th {
        background-color: #111 !important;
        color: #fff !important;
    }
    tbody tr td {
        background-color: #222 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if not os.path.exists(LOG_FILE):
    st.warning("⚠️ No logs found yet. Please run some tests first.")
else:
    try:
        df = pd.read_csv(LOG_FILE, header=None)
        df.columns = ["Prompt", "Model Response", "Flagged", "Threat Type"]

        # Add threat level badges
        df["Threat Level"] = df["Threat Type"].map(THREAT_LEVELS)

        # 🔽 Download buttons (CSV + JSON)
        col1, col2 = st.columns(2)
        with col1:
            csv_bytes = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download CSV", data=csv_bytes, file_name="prompt_log.csv", mime="text/csv")
        with col2:
            json_bytes = json.dumps(df.to_dict(orient="records"), indent=2).encode("utf-8")
            st.download_button("⬇️ Download JSON", data=json_bytes, file_name="prompt_log.json", mime="application/json")

        # 📄 Raw log data with emojis
        with st.expander("📄 Raw Log Data", expanded=True):
            st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)

        # 📊 Threat Type Bar Chart
        threat_chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                x=alt.X("Threat Type:N", title="Threat Category"),
                y=alt.Y("count()", title="Number of Prompts"),
                color="Threat Type:N",
                tooltip=["Threat Type", "count()"]
            )
            .properties(title="Threat Type Distribution", height=300)
        )
        st.altair_chart(threat_chart, use_container_width=True)

        # 📊 Malicious Prompt Frequency
        flag_chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                x=alt.X("Flagged:N", title="Is Malicious?"),
                y=alt.Y("count()", title="Frequency"),
                color="Flagged:N",
                tooltip=["Flagged", "count()"]
            )
            .properties(title="Malicious Prompt Frequency", height=300)
        )
        st.altair_chart(flag_chart, use_container_width=True)

        # 🥧 Threat Level Pie Chart
        st.subheader("🥧 Threat Level Distribution")
        pie_df = df["Threat Level"].value_counts().reset_index()
        pie_df.columns = ["Threat Level", "Count"]
        pie_chart = (
            alt.Chart(pie_df)
            .mark_arc(innerRadius=40)
            .encode(
                theta=alt.Theta(field="Count", type="quantitative"),
                color=alt.Color(field="Threat Level", type="nominal"),
                tooltip=["Threat Level", "Count"]
            )
            .properties(height=300)
        )
        st.altair_chart(pie_chart, use_container_width=False)

    except pd.errors.ParserError as e:
        st.error(f"❌ CSV Parsing Error: {e}")
        st.info("Hint: Make sure your CSV has 4 fields per row.")
