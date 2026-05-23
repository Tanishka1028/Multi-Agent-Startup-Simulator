import streamlit as st

from app.agents.ceo_agent import ceo_agent
from app.agents.finance_agent import finance_agent
from app.agents.marketing_agent import marketing_agent
from app.agents.swot_agent import swot_agent

from charts.revenue_chart import revenue_chart

st.set_page_config(
    page_title="Multi-Agent Startup Simulator",
    layout="wide"
)

st.title("Multi-Agent Startup Simulator")

st.write(
    "Generate AI-powered startup business plans"
)

st.sidebar.title("Navigation")

idea = st.text_area(
    "Enter your startup idea"
)

if st.button("Generate Startup Plan"):

    if idea == "":

        st.warning(
            "Please enter a startup idea"
        )

    else:

        with st.spinner(
            "AI Agents Working..."
        ):

            ceo_output = ceo_agent(idea)

            finance_output = finance_agent(idea)

            marketing_output = marketing_agent(idea)

            swot_output = swot_agent(idea)

        st.header("CEO Agent")
        st.write(ceo_output)

        st.header("Finance Agent")
        st.write(finance_output)

        st.header("Marketing Agent")
        st.write(marketing_output)

        st.header("SWOT Analysis")
        st.write(swot_output)

        st.header("Revenue Forecast")

        fig = revenue_chart()

        st.plotly_chart(fig)