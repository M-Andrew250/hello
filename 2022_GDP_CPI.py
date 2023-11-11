import pandas as pd
import streamlit as st
import plotly.express as px


# set_page_config
st.set_page_config(page_title="2022 GDP & CPI Dashboard", page_icon=":bar_chart:", layout="wide")



with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# reading the GDP file and their sheets

df1 = pd.read_excel("used_data.xlsx", sheet_name="Over_all_GDP", skiprows=3)
df2 = pd.read_excel("used_data.xlsx", sheet_name="GDP_by_kind_of_activity", skiprows=3)
df3 = pd.read_excel("used_data.xlsx", sheet_name="GDP_act_cat", skiprows=3)

df1["YEARS"] = pd.to_datetime(df1["YEARS"]).dt.year

#Sidebar controls

default_year = 2022
st.sidebar.image("NISR.png")
st.sidebar.markdown("####")
st.sidebar.header("CUSTOMIZE VISUALIZATION")
st.sidebar.header(":bar_chart: GDP")
st.sidebar.caption("Page1 visualizes 2022 Gross Domestic Product (GDP)")

selected_year = st.sidebar.selectbox("Select the Year", options=df1["YEARS"],
index=df1["YEARS"].eq(default_year).idxmax())

#predicted_years = st.sidebar.selectbox("Select Forecasted Year",
#options=forecasted_df[""])

Year_options = st.sidebar.multiselect("Year Options",help="Select the Years to adjust the GDP line chart",
options=df1["YEARS"], default=df1["YEARS"])

#forecasted_year_slider = st.sidebar.slider("Drag to Forecast the Trend",
#min_value=forecasted_df["YEARS"].min(), max_value=forecasted_df["YEARS"].max(), value=2024)

selected_cat = st.sidebar.selectbox("Activity Category",
options=df2["ACTIVITY_CATEGORY"].unique(), help = "Please select the category of which items fall and visualize its corresponding contributed GDP and its chart as well.")

filtered_cat = df3.query("ACTIVITY_CATEGORY == @selected_cat")

selected_act = st.sidebar.selectbox("Activity",
options=filtered_cat["ACTIVITY"].unique(), help = "Please select an item according to the above selected Category to view its contributed GDP and chart.")


#Filtering
filtered_year = df1.query("YEARS == @selected_year")
filtered_year2 = df2.query("YEARS == @selected_year")
filtered_year_options = df1.query("YEARS == @Year_options")
filtered_cat2 = df2.query("ACTIVITY_CATEGORY == @selected_cat & YEARS == @selected_year")
filtered_cat3 = df2.query("ACTIVITY_CATEGORY == @selected_cat & YEARS == @Year_options")
filtered_cat4 = df3.query("ACTIVITY_CATEGORY == @selected_cat & YEARS == @selected_year & ACTIVITY == @selected_act")
filtered_cat5 = df3.query("ACTIVITY_CATEGORY == @selected_cat & YEARS == @selected_year")
filtered_cat6 = df3.query("ACTIVITY_CATEGORY == @selected_cat & ACTIVITY == @selected_act")

#warnings

def dashboard():
    #main dashboard control
    st.title(":bar_chart: 2022 RWANDA GDP & CPI VISUALIZATION DASHBOARD")
    st.caption("2022 Gross Domestic Product (GDP) and Consumer Price Index (CPI) in Rwanda")
    st.markdown("####")
    st.header(":bar_chart: 2022 GDP Visualization")
    st.markdown("####")


    cor1, cor2 = st.columns(2, gap="large")

    with cor1:
        st.info(f"{selected_year} GDP in Billion Rwf ")
        st.metric(label= "GDP", value = f"{int(filtered_year['GDP']):,.0f}")

    with cor2:
        st.info(f"{selected_year} GDP growth rate")
        st.metric(label = "GDP growth rate", value = round(float(filtered_year["GROWTH RATE"]*100),2))

    st.markdown("""---""")

if filtered_year_options.empty:
    st.warning("Please select at least 2 years or more in the year options. No data available!")
    st.stop()

dashboard()
def charts():
    cor3, cor4 = st.columns(2, gap="large")
    with cor3:
        #st.subheader("GDP Graphical Presentation")
        GDP_chart = px.bar(filtered_year_options, x="YEARS", y="GDP", title="<b>GDP in Billion Rwf</b>",
        color_discrete_sequence=["#0083B8"],
        template="plotly_white")
        GDP_chart.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))

        st.plotly_chart(GDP_chart, use_container_width=True)
    with cor4:
        #st.subheader("GDP Growth Rate Presentation")
        GDP_rate_chart = px.line(filtered_year_options, x="YEARS", y="GROWTH RATE", title="<b>GDP Growth rate</b>",
        color_discrete_sequence=["#0083B8"],
        template="plotly_white")
        GDP_rate_chart.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))

        st.plotly_chart(GDP_rate_chart, use_container_width=True)
    st.markdown("""---""")

    cor5, cor6 = st.columns(2, gap="large")
    #filtered_cat2["GDP"] = pd.to_numeric(filtered_cat2["GDP"], errors="coerce").fillna(0).astype(int)

    with cor5:
        st.info(f"{selected_year} share on GDP in Billion Rwf by {selected_cat}")
        st.metric(label = "GDP", value = f"{int(filtered_cat2['GDP']):,.0f}")
    with cor6:
        st.info(f"{selected_year} GDP share in % by {selected_cat}")
        st.metric(label = "Rate", value = round(float(filtered_cat2["GROWTH RATE"]*100), 2))

    st.markdown("""---""")

    cor7, cor8 = st.columns(2, gap="large")
    with cor7:
        GDP_cat_chart = px.bar(filtered_year2, x="GDP", y="ACTIVITY_CATEGORY", title="<b>GDP BY CATEGORY OF ACTIVITY</b>",
        color_discrete_sequence=["#0083B8"],
        template="plotly_white", orientation = "h")
        GDP_cat_chart.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        st.plotly_chart(GDP_cat_chart)

    with cor8:
        GDP_cat_rate = px.line(filtered_cat3, x="YEARS", y="GDP", title=f"<b>{selected_cat} share in % </b>",
        color_discrete_sequence=["#0083B8"],
        template="plotly_white")
        GDP_cat_rate.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        st.plotly_chart(GDP_cat_rate)

    st.markdown("""---""")
    cor9, cor10 = st.columns(2, gap="large")

    with cor9:
        st.info(f"{selected_year} GDP by {selected_act} from {selected_cat} category in Billion Rwf")
        st.metric("GDP", f'{int(filtered_cat4["GDP"]):,.0f}')
    with cor10:
        st.info(f"{selected_year} GDP share in % by {selected_act} from {selected_cat} category")
        st.metric("Rate", round(float(filtered_cat4["GROWTH RATE"]*100), 2))
    st.markdown("""---""")

    cor11, cor12 = st.columns(2, gap="large")
    with cor11:
        GDP_cat_act_chart = px.bar(filtered_cat5, x="GDP", y="ACTIVITY", title=f"<b>GDP BY ACTIVITY in {selected_cat} in {selected_year}</b>",
        color_discrete_sequence=["#0083B8"], text="YEARS",
        template="plotly_white", orientation = "h")
        #GDP_cat_act_chart.update_traces(texttemplate='%{text}', textposition='outside')
        GDP_cat_chart.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))

        st.plotly_chart(GDP_cat_act_chart)

    with cor12:
        GDP_act_chart = px.scatter(filtered_cat6, x="YEARS", y="GDP", title=f"<b>{selected_act} GDP in different years </b>",
        color_discrete_sequence=["#0083B8"],
        template="plotly_white")
        GDP_act_chart.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        st.plotly_chart(GDP_act_chart)
charts()



#PART2: CPI Visualization


#Reading the  Rwanda_CPI sheet
Rwanda_CPI = pd.read_excel("used_data.xlsx",
sheet_name= "Rwanda_CPI",
skiprows=3, nrows= 167)

#converting and creating MonthYear column
Rwanda_CPI["Date"] = pd.to_datetime(Rwanda_CPI["Date"])
Rwanda_CPI['MonthYear'] = Rwanda_CPI['Date'].dt.strftime('%B %Y')

#reading the Urban_Rural sheet
Rural_Urban = pd.read_excel("used_data.xlsx",
sheet_name= "Urban_Rural", skiprows=3)

#converting and creating new MonthYear column
Rural_Urban["Date"] = pd.to_datetime(Rural_Urban["Date"])
Rural_Urban['MonthYear'] = Rural_Urban['Date'].dt.strftime('%B %Y')



#Reading the Rwanda_Basket_cat sheet
Basket_cat = pd.read_excel("used_data.xlsx", sheet_name="Rwanda_Basket_cat",
skiprows=3)

#Reading Rural_Urban Basket category
Rural_Urban_Basket = pd.read_excel("used_data.xlsx",sheet_name="Rural_Urban_Basket_Cat",
skiprows=3)



st.sidebar.markdown("""---""")
#sidebar controls
st.sidebar.header(":bar_chart: CPI")
st.sidebar.caption("Page 2 visualizes 2022 Consumer Price Index (CPI)")


#selectbox for date
default_monthyear = "November 2022"
selected_date = st.sidebar.selectbox("Select a date",
options= Rwanda_CPI["MonthYear"], index=Rwanda_CPI["MonthYear"].eq(default_monthyear).idxmax())

#selectbox for Region
selected_region = st.sidebar.selectbox("Select a region",
options= Rural_Urban["Region"].unique(), help = "Please select region (Rural or Urban) of which you would like to visualize.")

#date range date_input
From_date = st.sidebar.selectbox("Select 'From Date':", options= Rwanda_CPI["MonthYear"],
help = "Please select the start date of which you want to visualize")

To_date = st.sidebar.selectbox("Select 'To Date'", options=Rwanda_CPI["MonthYear"],
index = 165,
help="Please select the end date of which you want to visualize")

#selectbox for basket items
Basket = st.sidebar.selectbox("Select items from the Basket",
options= Basket_cat["Basket_Cat"].unique(), help = "select an item to visualize its CPI")



#Filter for Viewing Overall Rwanda_CPI based on the selected date
Filter_date1 = Rwanda_CPI.query("MonthYear == @selected_date")

if Filter_date1.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()

#Filter for Viewing Overall Rwanda_CPI based on the selected date and Region
Filter_region = Rural_Urban.query("MonthYear == @selected_date & Region == @selected_region")

if Filter_region.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()
#filter for Visualizing Rwanda CPI based on the selected date range
filtered_Rwanda_CPI = Rwanda_CPI[(Rwanda_CPI["Date"] >= pd.to_datetime(From_date)) & (Rwanda_CPI["Date"] <= pd.to_datetime(To_date))]

if filtered_Rwanda_CPI.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()

#filter for visualizing rural or urban cpi based chosen region and date range
filtered_rural_urban = Rural_Urban[
    (Rural_Urban["Date"] >= pd.to_datetime(From_date)) &
    (Rural_Urban["Date"] <= pd.to_datetime(To_date)) &
    (Rural_Urban["Region"] == selected_region)]

if filtered_rural_urban.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()

#Filter for visualising basket item CPI based on date and Region
filtered_Rwanda_CPI_Basket = Basket_cat[
(Basket_cat["Date"] >= pd.to_datetime(From_date)) &
(Basket_cat["Date"] <= pd.to_datetime(To_date)) &
(Basket_cat["Basket_Cat"] == Basket)]

if filtered_Rwanda_CPI_Basket.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()

#Filter for Visualizing basket item CPI based on selected region, item, and date range
filtered_Rural_Urban_Basket = Rural_Urban_Basket[
(Rural_Urban_Basket["Date"] >= pd.to_datetime(From_date)) &
(Rural_Urban_Basket["Date"] <= pd.to_datetime(To_date)) &
(Rural_Urban_Basket["Basket_Cat"] == Basket) &
(Rural_Urban_Basket["Region"] == selected_region)]


# Check if the dataframe is empty:
if Filter_date1.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.

#Dashboard title
st.header(":bar_chart: 2022 CPI Visualization")
st.markdown("####")

#Viewing the Overall CPI based on the selected date
Cor13, Cor14 = st.columns(2, gap = "large")

filtered_cpi = float(Filter_date1["CPI"])
with Cor13:
    st.info(f"Rwanda CPI on {selected_date}")
    st.metric(f"{selected_date} CPI", filtered_cpi)

with Cor14:
    st.info(f"{selected_region} CPI on {selected_date}")
    st.metric("CPI", round(float(Filter_region["CPI"]), 2))
st.markdown("""----""")

#line chart for rwanda cpi based on the selected date range


def CPI_charts():
    cor15, cor16 = st.columns(2, gap = "large")
    with cor15:
        Rwanda_CPI_linechart = px.line(filtered_Rwanda_CPI, x= "Date", y="CPI",
         title="Rwanda CPI Chart", color_discrete_sequence=["#0083B8"],
         template="plotly_white")
        Rwanda_CPI_linechart.update_layout(
             plot_bgcolor="rgba(0,0,0,0)",
             xaxis=(dict(showgrid=False)))

        #fig.show()
        st.plotly_chart(Rwanda_CPI_linechart)

    #line chart for Rural_Urban CPI
    with cor16:
        Rural_Urban_linechart = px.bar(filtered_rural_urban, x="Date", y="CPI",
        title = f"{selected_region} CPI Chart from {From_date} to {To_date}",
        color_discrete_sequence=["#0083B8"],
    template="plotly_white")

        #Rural_Urban_linechart.update_traces(texttemplate='%{text}', textposition='outside')
        Rural_Urban_linechart.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))

        # Center the chart on the page


        st.plotly_chart(Rural_Urban_linechart)


    cor17, cor18 = st.columns(2, gap = "large")
    #chart for Rwanda CPI based on selected basket item and date range
    with cor17:
        Basket_chart = px.line(filtered_Rwanda_CPI_Basket, x="Date", y="CPI", title = f"Overall_CPI by {Basket} Activity",
            color_discrete_sequence=["#0083B8"],
        template="plotly_white")

        #Basket_chart.update_traces(texttemplate='%{text}', textposition='outside')
        Basket_chart.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        st.plotly_chart(Basket_chart)

    #Chart for rural or urban basket item based on region,date range and selected item
    with cor18:
        rural_urban_basket_chart = px.bar(filtered_Rural_Urban_Basket, x="Date", y="CPI", title = f" {selected_region} CPI on {Basket} activiity",
            color_discrete_sequence=["#0083B8"], template="plotly_white")

        #rural_urban_basket_chart.update_traces(texttemplate='%{text}', textposition='outside')
        rural_urban_basket_chart.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        st.plotly_chart(rural_urban_basket_chart)
CPI_charts()
st.markdown("""---""")
st.markdown("####")

st.image("NISR.png")
st.write(f"Source: National Institute of Statistics (NISR)")



#hide CSS style
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
