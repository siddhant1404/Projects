
import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()


#  we define the function make_dashboard. 


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


#Creating a dataframe that contains the GDP data and display the first five rows of the dataframe.</h3>

# Using the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the GDP data.




# csv='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv'
csv=links["GDP"]
df=pd.read_csv(csv)
print(df.head())




# Using the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the unemployment data.



csv1=links["unemployment"]
df_unemployment=pd.read_csv(csv1)
print(df_unemployment.head())


#Displaying a dataframe where unemployment was greater than 8.5%. Take a screen-shot.</h3>




df_unemp=df_unemployment[df_unemployment["unemployment"]>8.5]
print(df_unemp)


# Use the function make_dashboard to make a dashboard

# In this section, you will call the function  <code>make_dashboard</code> , to produce a dashboard. 
# Create a new dataframe with the column <code>'date'</code> called <code>x</code> from the dataframe that contains the GDP data.



x =pd.DataFrame(df_unemployment["date"])
print(x.head())


# Create a new dataframe with the column <code>'change-current' </code> called <code>gdp_change</code>  from the dataframe that contains the GDP data.
gdp_change =pd.DataFrame(df["change-current"])
# Create your dataframe with column change-current


# Create a new dataframe with the column <code>'unemployment' </code> called <code>unemployment</code>  from the dataframe that contains the  unemployment data.



unemployment =pd.DataFrame(df_unemployment["unemployment"]) # Create your dataframe with column unemployment




title =Siddhant_Analysing_US_Economy # Give your dashboard a string title


# Finally, the function <code>make_dashboard</code> will output an <code>.html</code> in your direictory, just like a <code>csv</code> file. The name of the file is <code>"index.html"</code> and it will be stored in the varable  <code>file_name</code>.



file_name = "index.html"


# Call the function make_dashboard , to produce a dashboard.
make_dashboard(x=pd.DataFrame(df_unemployment["date"]), gdp_change=pd.DataFrame(df["change-current"]), unemployment=pd.DataFrame(df_unemployment["unemployment"]) , title="Siddhant_Analysing_US_Economy", file_name="index.html")

