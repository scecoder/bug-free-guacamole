import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 Interactive Monthly Food Budget")
st.write("This is my food budget.  I am sharing this because everyone needs to budget for food.  We all have different diets in the family, so most of this budget is for me personally.")
items = {
    "Meat": 50,
    "Sausage": 10,
    "Eggs": 10,
    "Fruit": 30,
    "Veggies": 30,
    "Cheese & Dairy": 10,
    "Bread": 5,
    "Drinks": 20,
    "Snacks": 20,
    "Sale": 25,
    "Recipes": 25,
    "Pantry": 10,
    "Restaurant": 125,
    "Office Lunch": 30,
}

# Split into two columns
col1, col2 = st.columns(2)

updated_values = {}
for i, (item, default) in enumerate(items.items()):
    # Alternate between columns for readability
    if i % 2 == 0:
        updated_values[item] = col1.number_input(
            f"{item} ($ per month)", min_value=0, value=default, step=1
        )
    else:
        updated_values[item] = col2.number_input(
            f"{item} ($ per month)", min_value=0, value=default, step=1
        )

# Build DataFrame
df = pd.DataFrame(list(updated_values.items()), columns=["Item", "Cost"])
total = df["Cost"].sum()
st.subheader(f"💰 Total Monthly Cost: ${total}")




# Define max y‑axis value (static)
y_max = 150  # adjust based on your expected highest cost

chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("Item", sort=None),
        y=alt.Y("Cost", scale=alt.Scale(domain=[0, y_max]))
    )
    .properties(width=600, height=400)
)

st.altair_chart(chart, use_container_width=True)



