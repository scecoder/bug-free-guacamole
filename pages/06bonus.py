import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered")
st.title("🚦 Soul Survival")
st.write("Money is only good for the good that it does.  And you can't keep it forever.")
st.write("Click on each light for brief guidelines to avoid hell")

html = """
<style>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 25px;
    margin-top: 30px;
}

/* Circle styling */
.circle {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 0 18px rgba(0,0,0,0.25);

    /* Text inside circle */
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    font-weight: 700;
    color: white;
    text-align: center;

    transition: box-shadow 0.3s ease;
}

/* Glow colors */
.red:hover {
    box-shadow: 0 0 25px 8px rgba(208, 2, 27, 0.8);
}
.yellow:hover {
    box-shadow: 0 0 25px 8px rgba(248, 231, 28, 0.8);
}
.green:hover {
    box-shadow: 0 0 25px 8px rgba(80, 200, 120, 0.8);
}

/* Traffic light colors */
.red    { background: #D0021B; }
.yellow { background: #F8E71C; color: #333; }
.green  { background: #50C878; }

/* Slide-out panel */
.panel { 
    display: none; 
    width: 90%; /* wider */ 
    min-height: 140px; /* taller */ 
    background: rgba(128,128,128,0.7); 
    padding: 28px; /* more breathing room */ 
    border-radius: 12px; 
    font-size: 20px; /* larger text */ 
    line-height: 1.5; 
    position: relative; 
    margin-top: -10px; 
}

/* Outline colors matching circles */
.outline-red    { border: 4px solid #D0021B; }
.outline-yellow { border: 4px solid #F8E71C; }
.outline-green  { border: 4px solid #50C878; }


/*colored checkmarks*/
.check-red {
    color: #D0021B;      /* red */
    font-weight: 900;
}

.check-yellow {
    color: #F8E71C;      /* yellow */
    font-weight: 900;
}

.check-green {
    color: #50C878;      /* green */
    font-weight: 900;
}

/* Close button */
.close-btn {
    position: absolute;
    top: 8px;
    right: 12px;
    background: white;
    border: 2px solid #444;
    border-radius: 6px;
    padding: 2px 8px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 600;
}

/* REMOVE BULLETS COMPLETELY */
ul {
    list-style: none;
    padding-left: 0;
    margin-left: 0;
}

/* Spacing for list items */
ul li {
    margin: 8px 0;
}

</style>

<div class="container">

    <!-- RED -->
    <div class="circle red" onclick="togglePanel('p1')">Attend Mass</div>
    <div id="p1" class="panel outline-red">
        <div class="close-btn" onclick="closePanel('p1')">Close</div>
        <ul> 
            <li><span class="check-red">✔</span> Required to attend mass on <b> Easter, Christmas, Sundays</b></li> 
            <li><span class="check-red">✔</span> Also required on <b> All Saints Day & Immaculate Conception</b></li> 
            <li><span class="check-red">✔</span> NOT Required to attend on Ash Wednesday.  No mass is celebrated on Good Friday.</li> 
            <li><span class="check-red">✔</span><b>masstimes.org</b> (has an app) and other websites and apps shows times for mass.  Confirm with parish website.</li> 
        </ul>      
    </div>

    <!-- YELLOW -->
    <div class="circle yellow" onclick="togglePanel('p2')">Go to Confession</div>
    <div id="p2" class="panel outline-yellow">
        <div class="close-btn" onclick="closePanel('p2')">Close</div>
        <ul> 
            <li><span class="check-yellow">✔</span> For Mortal sins (sins meriting hell) refer to the the <b> 10 Commandments</b></li>
            <li><span class="check-yellow">✔</span> For Venial sins, refer to the 2 greatest commandments love God and love neighbor as self</li>
            <li><span class="check-yellow">✔</span> Compare self with <i> A Year with the Saints </i> by Anonymous (about 400 pages long; has 12 chapters for each month on a specific virtue) </li>
            <li><span class="check-yellow">✔</span> Compare actions with <i> Spiritual Combat</i> by Lorenzo Scupoli - available in iPieta app for free or go online</li>
            <li><span class="check-yellow">✔</span> <b> Examination of Conscience </b> in iPieta or Laudate apps </li>
            <li><span class="check-yellow">✔</span> After confession, sins are forgiven but punishment remains.  Take advantage of <b>Divine Mercy Novena & Divine Mercy Sunday</b> (Good Friday to 2nd Sunday of Easter), when both sins and punishment are expunged</li>
        </ul>
    </div>

    <!-- GREEN -->
    <div class="circle green" onclick="togglePanel('p3')">Daily Prayer</div>
    <div id="p3" class="panel outline-green">
        <div class="close-btn" onclick="closePanel('p3')">Close</div>
        <ul> 
            <li><span class="check-green">✔</span> Pray the <b>20 Mysteries of the Rosary </b>, use Youtube or iPieta/Laudate apps</li> 
            <li><span class="check-green">✔</span> <b> Prayer of Spiritual Communion </b> when cannot attend mass; can say every day but not as replacement for required mass</li> 
            <li><span class="check-green">✔</span> Prayer to <b> Guardian Angel </b> useful for being stuck on something at school or work, driving/travelling</li>
            <li><span class="check-green">✔</span> Prayer for <b> Holy Souls in Purgatory</b> by St. Gertrude for the dead</li>
            <li><span class="check-green">✔</span> When nothing holy comes to mind during prayer, visualize <i> Jesus on the Cross!</i></li>
        </ul>
    </div>

</div>

<script>
function togglePanel(id) {
    var panel = document.getElementById(id);
    panel.style.display = (panel.style.display === "block") ? "none" : "block";
}

function closePanel(id) {
    document.getElementById(id).style.display = "none";
}
</script>
"""

components.html(html, height=2400)
