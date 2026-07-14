import streamlit as st

# 1. Page Configuration (Sets title and favicon in the browser tab)
st.set_page_config(
page_title="FitFocus App",
page_icon="💪",
layout="centered"
)

# 2. Sidebar UI
with st.sidebar:  
  st.header("⚙️ App Settings")
st.write("Welcome to FitFocus! Select a focus area to generate a custom routine.")
st.info("💡 **Tip:** Click on any recommended exercise card to see the full details.")

# 3. Main Header Section
st.title("💪 FitFocus Routine Generator")
st.write("Target specific symptoms or muscle groups with tailored, mobility-focused routines.")
st.write("---")

# 4. Mock Database
exercise_db = {
"Shoulder Tightness / Growth": [
{"name": "Face Pulls", "details": "3 sets of 15 reps. Keep your elbows high and focus on squeezing your rear delts and upper back."},
{"name": "Overhead Press", "details": "3 sets of 8 reps. Core tight, press straight up, and lock out at the top to build overall shoulder mass."},
{"name": "Dumbbell Lateral Raises", "details": "4 sets of 12 reps. Control the weight on the way down; targets the lateral head for shoulder width."},
{"name": "Doorway Stretch", "details": "Hold for 30 seconds. Place forearms on the doorframe and lean forward to relieve anterior shoulder tightness."}
],
"Lower Back Stiffness": [
{"name": "Cat-Cow Stretch", "details": "Move smoothly back and forth for 2 minutes. Improves spine mobility and relieves lower lumbar tension."},
{"name": "Bird-Dog", "details": "3 sets of 10 reps per side. Strengthens the core and lower back stabilizing muscles simultaneously."},
{"name": "Glute Bridges", "details": "3 sets of 15 reps. Drive through your heels. Activates glutes to naturally relieve pressure off the lower back."}
],
"Knee Discomfort": [
{"name": "Wall Sits", "details": "3 rounds of 30 seconds. Keeps the joint static while building quad strength directly around the kneecap."},
{"name": "Straight Leg Raises", "details": "3 sets of 10 reps. Lie flat and raise one leg at a time. Activates hip flexors and quads without knee strain."},
{"name": "Hamstring Curls", "details": "3 sets of 12 reps. Crucial for balancing out the strength ratios around the knee joint."}
]
}

# 5. UI Interactivity: Selection Dropdown
focus_areas = list(exercise_db.keys())

# Added an empty placeholder option so it doesn't automatically pick the first option on load
selected_area = st.selectbox(
"Choose a trouble spot or symptom to analyze:",
options=["-- Select an Option --"] + focus_areas
)

st.write("") # Just adds a bit of whitespace padding

# 6. Logic to Display UI Elements Dynamically based on Selection
if selected_area and selected_area != "-- Select an Option --":
  
# Visual success banner
  st.success(f"🎯 Displaying targeted exercises for: **{selected_area}**")
st.write("### Recommended Routines")

# Loop through the list and create clean, clickable drop-down elements for each exercise
for item in exercise_db[selected_area]:
with st.expander(f"🏋️‍♂️ {item['name']}"):
st.write(item['details'])

else:
# Friendly reminder UI state when nothing is selected yet
st.info("👋 Please select a symptom from the dropdown menu above to view exercises.")
