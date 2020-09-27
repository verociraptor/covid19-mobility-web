# parse through csv to get only miami dade rows
# create functions to get diff rows related to diff mobilities
import plotly.express as px
import pandas as pd

places_list = ['retail_and_recreation_percent_change_from_baseline',
                'grocery_and_pharmacy_percent_change_from_baseline',
                'parks_percent_change_from_baseline','transit_stations_percent_change_from_baseline',
                'workplaces_percent_change_from_baseline', 'residential_percent_change_from_baseline']

mobility_dt = pd.read_csv("2020_US_Region_Mobility_Report.csv")

fig = px.scatter(mobility_dt[mobility_dt.sub_region_2 == "Miami-Dade County"],
        x='date', y=places_list,
        size='')
fig = px.bar(mobility_dt[mobility_dt.sub_region_2 == "Miami-Dade County"],
             color=places_list, x='date', barmode='group')

# Example code to visualize data in different graphs            
# # fig.show()
# # fig = px.scatter()   
# gap_df = px.data.gapminder()
# gap_df = gap_df.assign(gdp=gap_df['pop'] * gap_df['gdpPercap'])
# gap_df.info()
# gap_df.head()

# year_df = gap_df[gap_df.year == max(gap_df.year)]
# cont_df = year_df.groupby('continent').agg({'gdp': 'sum'})
# cont_df.reset_index(inplace=True)

# # # Pie chart
# # fig = px.pie(cont_df, values='gdp', names='continent')
# # fig.show()
# # # Bar chart
# # fig = px.bar(cont_df, color='continent', x='continent', y='gdp')
# # fig.show()
# # # Horizontal bar chart - stacked
# # fig = px.bar(cont_df, color='continent', x='gdp', orientation='h')
# # fig.show()
# # # Bubble chart
# # fig = px.scatter(cont_df.assign(dataType='GDP'), color='continent', x='continent', y='dataType', size='gdp', size_max=50)
# # fig.show()

# mul_yrs_df = gap_df[gap_df.year > 1985]
# mul_yr_cont_df = mul_yrs_df.groupby(['continent', 'year']).agg({'gdp': 'sum'})
# mul_yr_cont_df.reset_index(inplace=True)

# # #used for multi index data 
# # # Bar chart
# # mul_yr_cont_df = mul_yr_cont_df.assign(yrstr=mul_yr_cont_df.year.astype(str))
# # fig = px.bar(mul_yr_cont_df, color='continent', y='gdp', x='yrstr', barmode='group')
# # fig.show()
# # # Horizontal bar chart - stacked
# # fig = px.bar(mul_yr_cont_df, color='continent', x='gdp', orientation='h', y='yrstr')
# # fig.show()
# # # Bubble chart
# # fig = px.scatter(mul_yr_cont_df, y='continent', x='yrstr', color='continent', size='gdp', size_max=50)
# # fig.show()

# # used to lump data into own cats in vertial bar graph
# fig = px.bar(mul_yr_cont_df, color='continent', y='gdp', x='yrstr', barmode='group')
# fig.show()
# fig = px.bar(mul_yr_cont_df, color='yrstr', y='gdp', x='continent', barmode='group')
# fig.show()

# # fig = px.bar(mul_yr_cont_df, color='continent', facet_col='continent', x='gdp', orientation='h', facet_row='yrstr')
# # fig.update_yaxes(showticklabels=False)
# # fig.show()