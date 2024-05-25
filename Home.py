import streamlit as st

st.header("From Piggy Banks to Pin Codes")
st.title("An Analysis on AAC’s Customers and their Spending Behaviors")
st.caption('Presented By: Group 2 | Hungry Sleepers')

st.subheader("Goals and Objectives")
st.image("images/3.jpg")
st.subheader("About the dataset")
st.image("images/4.jpg")
st.subheader("Scope and Limitations")
st.image("images/5.jpg")
st.header("Methodology")
st.image("images/6.jpg")
st.subheader("Overview of customer demographics.")
st.image("images/7.jpg")
st.subheader("Pre-profiling")
st.image("images/8.jpg")

st.subheader("Cluster #0: DIGITAL DYNAMOS")
st.write("Top tier based on rfm, on average has the same spending for both digital and physical.")
st.image("images/12.jpg")

st.subheader("Cluster #3: CYBER SAVVY SHOPPERS")
st.write("Next tier of overall spending has higher digital average than digital dynamos.")
st.image("images/16.jpg")

st.subheader("Cluster #5: FESTIVE SPENDERS")
st.write("Occasional spenders who has the affinity to spend during holidays and summer.")
st.image("images/20.jpg")

st.subheader("Cluster #4: EPIC COMEBACK CONNOISSEURS")
st.write("Infrequent spenders but when they come back, they are very high average spenders.")
st.image("images/24.jpg")

st.subheader("Post-profiling")
st.image("images/25.jpg")

st.image("images/26.jpg")

st.subheader("Summary")
st.markdown("- For the entire dataset, Six (6) clusters were determined. Two (2) of which were considered disengaged while the remaining Four (4) were subjected to further profiling.")
st.markdown(" - Digital Dynamo consisted of heavy frequent spenders with around same average spending for digital and physical")
st.markdown(" - Festive Spenders were considered as ‘Festive Spenders’ since their average spendings peaked during the holidays")
st.markdown(" - Epic Comeback Connoisseurs were made up infrequent, but heavy spenders")
st.markdown("- Campaigns were designed for each customer cluster based on their spending behaviors to encourage increased digital transactions.")
