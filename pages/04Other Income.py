import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Flashcards Demo", layout="centered")
st.title("🃏 Job Benefits to Compare")
st.write("While your paycheck and commute to the office will be the number one and two considerations, here is a list of company benefits I receive, listed here for you to compare against another company's list of benefits.  These benefits can boost your total compensation (your total pay) by twice as much or even more.  Some companies tout their benefits, but they are actually not great; for example they say they offer health insurance, but if you need to pay $50 to visit the doctor, will you see the doctor unless you are really ill?")


# Define your flashcards (front → back)
flashcards = [
    ("Health", "I am charged $300/month to be able to pay $30 to see the doc"),
    ("Dental", "I am charged $20/month to be able to get 3 teeth cleanings per year"),
    ("Vision", "No paycheck deduction.  I am charged $20 for a periodic eye exam and free frames"),
    ("401k Match", "I can contribute to pretax or taxed IRA and have it 6% of my contributions matched by the company"),
    ("Donation Match", "My donation to any 501c3 organization such as church will be matched"),
    ("Other Cash Compensation", "I have up to about 5k reimbursed per year in tuition and $400 in health-related activities"),
    ("HCRA-Health Care Reimbursement Account", "I can set aside $ for items such as medicine free of income tax and sometimes sales tax too"),
    ("DCRA-Daycare Reimbursement Account", "same as HCRA but for kids' daycare"),
    ("ESPP-Employee Stock Purchase Plan", "I can buy company stock at a discount"),
]

# Build full HTML for a single render
cards = ""
for i, (front, back) in enumerate(flashcards):
    cards += f"""
      <div class="flip-card" onclick="flipCard({i})">
        <div class="flip-card-inner" id="card-{i}">
          <div class="flip-card-front">{front}</div>
          <div class="flip-card-back">{back}</div>
        </div>
      </div>
    """

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  .grid-container {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    justify-items: center;
    margin-top: 10px;
  }}
  .flip-card {{
    background-color: transparent;
    width: 180px;
    height: 120px;
    perspective: 1000px;
    cursor: pointer;
  }}
  .flip-card-inner {{
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.6s;
    transform-style: preserve-3d;
  }}
  .flipped {{
    transform: rotateY(180deg);
  }}
  .flip-card-front, .flip-card-back {{
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 600;
    border: 2px solid #333;
    border-radius: 10px;
    box-sizing: border-box;
    padding: 8px;
  }}
  .flip-card-front {{
    background-color: #4C72B0;
    color: white;
  }}
  .flip-card-back {{
    background-color: #E5ECF6;
    color: #111;
    transform: rotateY(180deg);
  }}
</style>
</head>
<body>
  <div class="grid-container">
    {cards}
  </div>
  <script>
    function flipCard(i) {{
      const el = document.getElementById('card-' + i);
      el.classList.toggle('flipped');
    }}
  </script>
</body>
</html>
"""

# Render once via HTML component
components.html(html, height=520, scrolling=False)
