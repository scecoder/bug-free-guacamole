import streamlit as st
import pandas as pd
import altair as alt

st.title("Credit Cards")
st.write("Minimum Payment: The amount you pay without incurring a penalty fee")
st.write("Interest Charges: Charges as a result of not paying your entire credit card bill")
st.write("You can be stuck with both a penalty and interest charges.  If bill is paid in full every month, there is no need to worry about mimimum payments or interest charges")
st.write("Card offers for Balance Transfers and Cash Advances are ignored.  These are unnecessary, expensive services")
st.write("My cards offer an autopay option that auto-deducts the full bill amount.  I do not use this because I need to review my bill every month; however, I do schedule a recurring payment for the average amount of my credit card bill in case I forget about a bill.")

st.write("Here are my credit cards for comparison.  I have a credit card from Citibank, a credit card from Barclays, and 2 credit cards from US Bank.  So I need to keep track of 4 different due dates to successfully pay the bill for each credit card.")


import streamlit as st
import pandas as pd
import altair as alt

# Your data
data = {
    "Card": ["Barclays", "Citi", "USBANK1", "USBANK2"],
    "Cashback Rewards (%)": [2, 1.99, 5, 5],
    "Minimum Payment ($)": [29, 41, 41, 41],
    "Interest for Underpayment (APR %)": [19, 18, 17, 19],
    "Days to Pay without Penalty": [17, 20, 26, 28]
}

df = pd.DataFrame(data)

# Ensure numeric types
numeric_cols = ["Cashback Rewards (%)", "Minimum Payment ($)", "Interest for Underpayment (APR %)", "Days to Pay without Penalty"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

# Radio to select metric (must match column names exactly)
metric = st.radio(
    "Select a metric to visualize:",
    numeric_cols,
    index=0
)

# Altair chart (explicit quantitative type)
chart = alt.Chart(df).mark_bar(size=40).encode(
    x=alt.X("Card:N", sort=None, title="Card"),
    y=alt.Y(f"{metric}:Q", title=metric),
    color=alt.Color("Card:N", legend=None),
    tooltip=[
        alt.Tooltip("Card:N"),
        alt.Tooltip(f"{metric}:Q", format=".2f")
    ]
).properties(
    width=600,
    height=350,
    title=f"{metric} by Card"
)

st.altair_chart(chart, use_container_width=True)