import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered")
st.title("📁 Stuff to Pay for Earlier Than Later")
st.write("Forget all the fun stuff, these are all the boring things that are better off paid for earlier than later.  However the fun stuff, such as Disneyland tickets, do increase in price and often.")
st.write(" If there is a lack of motivation to consider any of these for future financial well-being, keep in mind 2 things: 1) most people are not able to remember any purchase that they are still excited about, and 2) even people paying for experiences, such as world travellers, cannot relive those memories for long aside from a conversations with others who also went where they did.")

html = """
<style>
.card {
    padding: 18px;
    margin-bottom: 12px;
    border-radius: 10px;
    cursor: pointer;
    font-size: 22px;
    font-weight: 600;
    color: white;
    display: flex;
    align-items: center;
    gap: 12px;
    
}

.tab {
    margin-left: 20px;   /* indent */
    text-indent: 20px;   /* optional: indent first line */
}



/* Soft readable colors */
.insurance { background: #4A90E2; }     /* Blue */
.credit    { background: #7B52AB; }     /* Purple */
.retire    { background: #8B008B; }     /* Magenta */
.interest  { background: #F5A623; }     /* Orange */

.panel {
    display: none;
    padding: 14px;
    background: #ffffff;
    border-left: 4px solid #4CAF50;
    margin-bottom: 18px;
    border-radius: 0 0 10px 10px;
    font-size: 16px;
    line-height: 1.4;
}
</style>

<div class="card credit" onclick="togglePanel('p2')">💳 Get a Credit Card AEAP (As Early As Possible)</div>
<div id="p2" class="panel">
    <div>
    • Like auto insurance rates being lower the earlier you get your driver's licence, <b> the earlier you get a credit card </b> (not a debit/ATM card; not a prepaid card; not a reloadable prepaid card), the more easily you can obtain credit cards with better benefits, cheaper home loans, etc.<br></p>
    • One way get a credit card is to show that you get paid very well <b> W-2 regular salary wages </b>, not 1099 gig "Uber" money).  You'll need to show paystubs.<br></p>
    • As a student, the easiest way is to become an <b> Authorized User.</b>  Ask someone with a credit card to put you on as an Authorized User but not to give you the card at all and do not use that card if given.  A credit record will be established.  You need to give them your <b> SSN </b> (social security number), so make sure it is someone you trust. 💳
    </div>
</div>


<div class="card insurance" onclick="togglePanel('p1')">🧬 Buy Term Life Insurance AEAP </div>
<div id="p1" class="panel">
    <div>
    • Recall the Biblical incident of the widow's only son passing away and people including Jesus taking pity on this widow because that son was the her only means to an income (Luke 7:11-16).  Jesus brought him back to life; however, had he had a life insurance policy, the policy would have paid money to his mom, ensuring her financial survival. <b> Life insurance, specifically term life insurance, is much cheaper before you turn 30</b>, when it's around $20 per month; when you're over 30, you pay around twice as much.  <b> Term life insurance</b> gives your family a <b>payout if you die between within a certain time </b> (specified in the policy).  Whole life pays out when you die no matter when that is, so it's more expensive. <br></p>
    
    • For an additional $10 per month, you can add a <b> Return of Premium rider </b> (a special insurance feature that costs more), meaning if you live past the term of the policy, you get your monthly payments back on a rising scale (the later in the term the more you get back). <br></p>
	
	• Term life prices are higher if the payout, or money received at death, is more.  How much of a payout do you need? </b> Just pay for as much as you can tolerate.  It depends on a dizzying array of factors, but my rule of thumb is to get enough to keep the family in the house for one year until they can transition on their own income.  If you outlive the term of the insurance policy, you'll have enough money saved for your family to survive (so no need for Whole Life insurance), and with the Return of Premium rider, you will get your monthly payments returned to you 🧬 </p> 
    </div>
</div>


<div class="card retire" onclick="togglePanel('p3')">🏦 Max Your Contribution to 401k AEAP</div>
<div id="p3" class="panel">
    <div>
    • From the mouths of two independent successful retirees, I have been advised to contribute the maximum to retirement accounts, specifically the 401k, which has a maximum contribution of $24,500 in 2026 and increases about $1k every year. <br></p> 
    
    • There are many different types retirement accounts with different max contribution amounts: IRA, Roth IRA, 410k, 403b, etc.  You can set up your own IRA and Roth IRA.  401k and 403b accounts are only offered by companies to their employees.  Aim to contribute the corresponding maximum, or at least the maximum you can tolerate. <br></p>
    
	• In addition to the max contribution, consider the <b> Roth IRA and Roth 401k </b> accounts because they allow you to take money out without penalties.  Roth IRAs are offered by many banks and many have sign-up bonuses.  Roth 401k accounts are offered by companies to their employees and are administered by a third party company.  If that third party company doesn't make it too much of a headache to take out money, why not contribute the maximum amount and take out the money as needed?  <br> </p>
	</div>
</div>

<div class="card interest" onclick="togglePanel('p4')">📈 Higher, Faster, Earlier (An Ode to Interest) </div>
<div id="p4" class="panel">
    <div><p><b>"Interest" = "Yield" = "Rate" = a % of your money is added to your money monthly or daily</b> at a financial institution because you have it in a bank or shady crypto website and not under the mattress.  (There is also loan-related interest which you pay, such as credit card loans, not discussed here.) </p>
	<p>  If I want high interest on money sitting around even at the bank, it usually means I need to have it locked up without easy access to it, or vice versa, I can have easy access but very low interest.  Unless I have a lot of money, which renders moot the original problem anyway</p>	
	
	<br> <b> WANT: HIGH RATE + HIGH ACCESS </b></br>
    <br><b> HAVE: HIGH RATE + LOW ACCESS </b> (Certificates of Deposits or Some High Yield Savings Accounts/HYSAs) </br>
	<br><b> HAVE: LOW RATE + HIGH ACCESS </b> (Checking Accounts) </br>
	<br><b> HAVE: HIGH RATE + HIGH ACCESS but with $100k Minimum Deposit </b></br>
	<p><b>3 OPTIONS</b></p>
	<p><b> OPTION 1 (easiest): Open a High Yield Savings Account (HYSA) in combination with a Checking Account at the same bank </b></p>
	<p> Since I can transfer between accounts instantly or in one business day at most, I can easily receive high interest and still have easy access to cash.  If bank does not offer one of the highest interest rates around at the time (like foreign exchange rates, interest rates change every day, so this must be monitored),go to Option 2 </p>
	
	<p><b> OPTION 2: Open an HYSA in combination with a Brokerage (Investment) Account </b></p>
	<p> Major banks offer investment accounts.  Some major banks have great savings rates at the brokerage portion of the bank, eg e*Trade by Morgan Stanley.  Use the trading account as a checking account by requesting a debit card for the trading account.  Check out-of-network ATM fees (search "fee schedule" on website) and if refunds are offered.  No need to trade in the trading account.  Unless you have only $1 in the account... </p>
	
	<p><b> OPTION 3: Use a Brokerage (Investment) Account as both a Checking and Savings Account </b></p>
	<p> If a bank  does not offer high interest, or offers high interest with high minimum deposit, use the trading account as both savings and checking at once.  <b>1) Set up an investment account </b> (FYI the questionnaires for setup are a headache, get someone to guide you to answer "correctly"), <b> 2) Order a debit card </b> and check out-of-network ATMs fees as described in Option 2, <b> 3) Buy a mutual fund </b> that never changes in price because it invests in treasury bills (eg: SWVXX by Schwab or SPRXX Fidelity or equivalent) and receive corresponding monthly dividend (this is the "interest") + reinvest dividends, <b> 4) Convert back to low-interest cash </b> by selling the mutual fund, which will take <b> one trading day </b> (Note: trading days are usually business days and most but not all federal holidays).
    <p><b>OPTION 3 TAX NOTE: </b>If you don't have a lot of income, your income tax will be 15% or less of that income which includes regular interest.  On these dividends the income tax is 15% max but 0% if your total income is low enough. </p>
	
    <p class="tab"><b>Example:</b></p>
    <p class="tab"> $100 total funds
	<p class="tab"> $75 in HYSA (Option 1 & 2) or mutal fund (Option 3)
    <p class="tab"> $25 in cash, no interest received in all 3 options
    <p class="tab"> $50 cash needed </p>
    <p class="tab"> Options 1 & 2: Transfer $50 into Checking (Option 1) or Investment Account (Option 2).  (Note: Withdraw $50 instead of $25 because cash should not be used up completely.)  Use debit card to withdraw cash or make any digital payments using debit card number</p>
    <p class="tab"> Option 3: Put in a sell order by dollar amount of $50 (these funds always cost $1/share).  Wait one trading day (Try to use the bank's own mutual funds; when using mutal funds issued by other banks, there may be further delays). Then use debit card as in Options 1 & 2.</p>
    

	<p><b>BONUS OPTION: Since all of the above is one giant headache, I can put all (or most) of my eggs in one basket and let the interest work</b>.  Earning interest is exponential and not linear: The more money that is in an account, the faster the interest will grow.  If you have $10 spread over 10 accounts, over a period of time (think of the the exponential function) you will not earn as much interest as when you put all $10 into a single account. Some people prefer creating different accounts for different purposes, but be aware of how this impacts your interest income, so try not to create too many accounts. </p>
    </div>
</div>

<script>
function togglePanel(id) {
    var panel = document.getElementById(id);
    panel.style.display = (panel.style.display === "block") ? "none" : "block";
}
</script>
"""

components.html(html, height=3333)
