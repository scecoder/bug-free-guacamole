import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered")
st.title("Cash Flow Chart")
st.write("This is my process to pay bills.  I tried all sorts of other ways to save including setting up a budget, but I would inevitably find a way to cheat and justify every purchase, so in the end I did not save anything.  This is the first system that forces me to save.  I did not read about a similar system anywhere online or in person, so I cannot attribute this to anyone.")

html = """
<style>
.flowchart {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 18px;
    margin-top: 30px;
}

/* Rectangle style */
.box {
    width: 420px;   /*increased from 260px*/
    height: 180px; /* increased from 90px */
    border-radius: 10px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    text-align: left;
    font-size: 18px;
    font-weight: 600; /* default bold */
    color: white;
    font-family: Arial, sans-serif !important; 
}

/* Normal (unbolded) text inside boxes */
.normal {
    font-weight: 400;
}

/*panels to arial font*/
.panel {
    font-family: Arial, sans-serif;
}


/* 9 readable colors */
.box1 { background: #2c39da; }
.box2 { background: #007272; }
.box3 { background: #a06707; }
.box4 { background: #973b46; }
.box5 { background: #7B52AB; }
.box6 { background: #686868; }

/* Arrow styling */
.arrow {
    font-size: 128px;
    font-weight: bold;
    color: #555;
}
</style>

<div class="flowchart">

    <div class="box box1">
        Step 1 - Receive Take Home Pay<br>
        <span class="normal">I deposit the paycheck into two bank accounts: 10% of take home pay amount into a checking account and 90% into a high yield savings account.  This way I am keeping 90% of take home pay (ie paycheck minus tax) safe--from myself.</span>
    </div>
    <div class="arrow">⬇</div>

    <div class="box box2">
        Step 2 - Make Purchases<br>
        <span class="normal">Physical and online purchases are made using cash and card and are then recorded in a special database.</span>
    </div>
    <div class="arrow">⬇</div>

    <div class="box box3">
        Step 3 - Total Up Credit Card Purchases & Other Cash Needs<br>
        <span class="normal">Throughout the month, credit card transactions made in the past 30 days will eventually be due as the credit card bill becomes due, or as "the statement closes".  Also, money is deducted directly from the checking account for things like Internet access.  Finally, I need to have cash on hand for things like church and farmers' markets.</span>
    </div>
    <div class="arrow">⬇</div>

    <div class="box box4">
        Step 4 - Determine If Bills Can Be Paid<br>
        <span class="normal"> Here comes the tricky part of ensuring there is always money in the checking account since only 10 percent of take home pay goes into this account that pays all of the bills.  I look at the next 1-2 months to 1) review which credit card bills are coming due, 2) review the current balance of those cards online, 3) review scheduled direct payment amounts and what day they are scheduled for, and 4) cash needs.</span>
    </div>
    <div class="arrow">⬇</div>

    <div class="box box5">
        Step 5 -  Schedule Payments & Reduce Spend<br>
        <span class="normal"> Based on the previous step, I will see what credit cards I need to either a) forego spending (can't buy everything), or b) defer the purchase until the second next bill is issued so the bill for that purchase will be due in 2 months instead of 1.  Meanwhile, the "10% paychecks" that will arrive within those next 30 days may cover the deferred purchase.</span>
    </div>
    <div class="arrow">⬇</div>

    <div class="box box6">
        Step 6 - Decide Whether to Draw from Savings<br>
        <span class="normal">If I see that I will still need more funds, I will initiate transfer of the needed funds from the savings account with 90% take home pay.  It is a hard pill to swallow since it means I spent too much in a short time AND did not save prior to purchase.   I hope to at least have mimimized this transfer amount by reducing purchases.  The cycle continues next month.</span>
    </div>
</div>
"""

components.html(html, height=4800)
