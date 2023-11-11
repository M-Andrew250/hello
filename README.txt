Project name: 2022 Rwanda GDP and CPI Visualization Dashboard
description: The project visualizes the 2022 Rwanda Gross Domestic Product (GDP) and Consumer Price Index (CPI).

INSTALLATION
pip install pandas
pip install streamlit
pip install plotly.express

PARTS OF THE DASHBOARD
part1: 2022 GDP Visualization
part2: 2022 CPI Visualization

USAGE:
CONTROL PANEL:
The dashboard have the control panel on the left side that the user can use to customize visualization
the control panel too falls into two parts which are "GDP" and "CPI". the GDP part control panel is used
to customize GDP Visualization only.  and the CPI part control widgets is used to customize CPI Visualization only.
By default, in both parts of the control panel the default year of GDP Visualization is 2022 and default date of CPI visualtion is November 2022.

On GDP part visualization, you may customize it using "YEAR, YEAR OPTIONS, Activity category 
and Activity" the year options, by default all the years are selected so that the chart is automatically adjusted according to the selected years. 
the Activity select box is made according to the above selected Activity category. 
therefore the GDP Visualization automatically changes accordingly.

On CPI part Visualization, the controls are Date, Region, "From date", "To date" and item from the basket. 
when the date is selected the CPI both Rwanda and regional (rural or urban)  reveals respectively. by default the default date is November 2022. 
The Region control contains Rural and Urban and from there you may choose to visualize rural or urban.
To control charts visualization, you will need to choose the From date and To date of which you want to reveal. 
and charts will automatically adjust accordingly.
lastly, you will need to choose an item from the basket of which you would like to view its chart.

BODY
2022 GDP Visualition
This part presents numerical and graphical 2022 Rwandan Gross Domestic Product, growth rate, Category of Activity and Activity. the respective GDP presented is in BILLION Rwandan francs and the respective GDP growth is percentage. further more there are also their respective charts. and all are customizable from the control panel.

2022 CPI Visualization
This part presents 2022 Rwanda CPI Visualization according the control panel. this means you view the CPI according to chosen Date, From date, To date, lastly Item from the basket. therefore the metrics and graphs adjusts respective to the control pannel

Lastly, the css style code hides the streamlit headers and footers


Note:All data used are in excel file and were obtained from the National Institute of Statistics of Rwanda under its authorisation.










