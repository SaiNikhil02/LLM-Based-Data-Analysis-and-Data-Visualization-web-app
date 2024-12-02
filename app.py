import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
import requests
import plotly.express as px
import openai
from openai import OpenAI
import io
#from pycaret.regression import setup, compare_models, pull, save_model, load_model
import os

api_key = st.secrets["OPENAI"]["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=api_key)
# device = torch.device('mps') if torch.backends.mps.is_available() else torch.device("cpu")
# model_name = "GPT-2"  # Replace with a larger model like "EleutherAI/gpt-neo-1.3B"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name).to(device)


with st.sidebar:
    
    selected = option_menu('Data Analysis  & Visualization',
                          
                          ['Home',
                           'Data Analysis',
                           'Data Visualization',
                           
                           ],
                          icons=['house','activity','bar-chart'],
                          default_index=0)

#--------------------------------------------------------------->>Home<<---------------------------------------------------------------------
selected_option = None

if selected == 'Home':
    st.markdown("<h1 style='color: #FF5733';><em>Welcome to LLM Based Data Analysis and Visualization WebApp!</em></h1>", unsafe_allow_html=True)
    st.image('home.jpg')
    st.markdown("<h2 style='color: #FF5733';><em>Overview :</em></h2>", unsafe_allow_html=True)
    st.write('Visuverse - A data analysis and visualization web application is a software platform that allows users to explore, analyze, and present data in a visual format. The primary goal of this web application is to simplify the process of interpreting complex datasets and gaining valuable insights from them.')
    st.markdown("<h2 style='color: #FF5733';><em>We are Extracting insights and patterns from raw data through :</em></h2>", unsafe_allow_html=True)
    options = ['Data Analysis', 'Data Visualization']
    selected_option = st.radio('', options)

    if selected_option == 'Data Analysis':
        st.markdown("<h2 style='color: #FF5733';><em>Data Analysis :</em></h2>", unsafe_allow_html=True)
        st.write('Data analysis involves examining, cleaning, transforming, and interpreting data to uncover meaningful information, patterns, and trends. It aims to answer specific questions, validate hypotheses, or make informed decisions based on data.')
        st.image('dataanalysisprocess.png')
        st.write('Key steps in data analysis include :')
        st.markdown("<h6 style='color:  #FF7F50;'><em>1 - Data Cleaning : </em></h6>", unsafe_allow_html=True)
        list_items = ['Removing errors, inconsistencies, and duplicates from the dataset to ensure data quality and accuracy.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)

        st.markdown("<h6 style='color:  #FF7F50;'><em>2 - Data Exploration : </em></h6>", unsafe_allow_html=True)
        list_items = ['Analyzing the datasets basic statistics and distributions to understand the datas characteristics.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)

        st.markdown("<h6 style='color:  #FF7F50;'><em>3 - Data Transformation : </em></h6>", unsafe_allow_html=True)
        list_items = ['Converting data into a suitable format or aggregating it to perform further analysis.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)

        st.markdown("<h6 style='color:  #FF7F50;'><em>4 - Statistical Analysis : </em></h6>", unsafe_allow_html=True)
        list_items = [' Applying statistical techniques to draw conclusions and make predictions from the data.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)

        st.markdown("<h6 style='color:  #FF7F50;'><em>5 -  Data Mining : </em></h6>", unsafe_allow_html=True)
        list_items = ['Discovering patterns, associations, and correlations in large datasets using algorithms.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)


    else : 
        st.markdown("<h2 style='color: #FF5733';><em>Data Visualization :</em></h2>", unsafe_allow_html=True)
        st.write('Data visualization is the graphical representation of data to communicate information clearly and effectively. It helps users comprehend complex data and identify trends, outliers, and relationships. Visualizations aid in storytelling, presenting findings, and making data-driven decisions.')
        st.image('dataviz.jpg')
        st.write('Common types of data visualizations include :')
        st.markdown("<h6 style='color:  #FF7F50;'><em>1 -  Charts : </em></h6>", unsafe_allow_html=True)
        list_items = ['Bar charts, line charts, scatter plots, pie charts, and area charts are used to show trends, comparisons, and proportions.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)

        st.markdown("<h6 style='color:  #FF7F50;'><em>2 - Maps : </em></h6>", unsafe_allow_html=True)
        list_items = ['Choropleth maps and heatmaps display geographic data and spatial distributions.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)

        st.markdown("<h6 style='color:  #FF7F50;'><em>3 - Dashboards : </em></h6>", unsafe_allow_html=True)
        list_items = ['Interactive displays that consolidate multiple visualizations and provide a comprehensive view of data.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)

        st.markdown("<h6 style='color:  #FF7F50;'><em>4 - Infographics : </em></h6>", unsafe_allow_html=True)
        list_items = ['Combining visuals and text to convey information in a visually engaging manner.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)

        st.markdown("<h6 style='color:  #FF7F50;'><em>5 - Treemaps and Sunbursts : </em></h6>", unsafe_allow_html=True)
        list_items = ['Hierarchical data structures visualized as nested rectangles or circles.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)

        st.markdown("<h6 style='color:  #FF7F50;'><em>6 - Word Clouds : </em></h6>", unsafe_allow_html=True)
        list_items = ['Representing text data, where the size of words corresponds to their frequency.']
                # Create an unordered list using HTML tags
        unordered_list = "<ul>" + "".join([f"<li>{item}</li>" for item in list_items]) + "</ul>"
                # Display the unordered list using st.markdown()
        st.markdown(unordered_list, unsafe_allow_html=True)

        st.markdown("<h4 style='color:  #FF7F50;'><em>Note : </em></h6>", unsafe_allow_html=True)
        st.write('Effective data visualization relies on thoughtful design choices, such as choosing the appropriate visualization type, using color effectively, providing clear labels and titles, and ensuring the visual does not mislead or distort the data. There are various data visualization tools available, ranging from simple spreadsheet software to advanced programming libraries, which allow users to create engaging and impactful visual representations of their data.')



elif selected == 'Data Analysis' : 
    st.markdown("<h2 style='color:  #FF5733;'><em>Data Analysis : </em></h6>", unsafe_allow_html=True)
    #st.markdown("<h4 style='color:  #FF7F50;'><em>Select How You want to load your Dataset : </em></h4>", unsafe_allow_html=True)
    def load_data(file):

        file_extension = file.name.split(".")[-1]
        if file_extension == "csv":
            data = pd.read_csv(file)
        elif file_extension in ["xls", "xlsx"]:
            data = pd.read_excel(file)
        else:
            st.warning("Unsupported file format. Please upload a CSV or Excel file.")
            return None
        return data
    
    #file_option = st.radio("Data Source", options=["Upload Local File"])
    file = None
    data = None

    #if file_option == "Upload Local File":
    file = st.file_uploader("Upload your DataSet in CSV or EXCEL format", type=["csv", "excel"])

    

    if file is not None:
        data = load_data(file)

    if data is not None:
        st.markdown("<h4 style='color:  #FF7F50;'><em>Preview of Loaded Dataset : </em></h4>", unsafe_allow_html=True)
        #st.dataframe(data.head())

    def group_data(data, aggregation):
        def select_group_column(df):
            group_columns = st.sidebar.multiselect("Select columns for Analysis", df.columns, key="group_cols")
            return group_columns

    def select_columns(df):
        st.write("### Select Columns")
        all_columns = df.columns.tolist()
        options_key = "_".join(all_columns)
        selected_columns = st.multiselect("Select columns", options=all_columns)
    
        if selected_columns:
            sub_df = df[selected_columns]
            st.write("### Sub DataFrame")
            st.write(sub_df.head())
        else:
            st.warning("Please select at least one column.")

    def analyze_data(data):
    
        show_file_header(data)
        st.markdown("<h2 style='color:  #FF5733;'><em>Select Columns for Analysis : </em></h2>", unsafe_allow_html=True)
        all_columns = data.columns.tolist()
        options_key = "_".join(all_columns)
        selected_columns = st.multiselect("Select columns", options=all_columns)
    
        if selected_columns:
            sub_df = data[selected_columns]
            st.markdown("<h4 style='color:  #FF7F50;'><em>Sub DataFrame : </em></h4>", unsafe_allow_html=True)
            st.table(sub_df.head())

            def show_data_shape(data):
                st.markdown("<h4 style='color:  #FF7F50;'><em>Number of Rows : </em></h4>", unsafe_allow_html=True)
                st.write(data.shape[0])
                st.markdown("<h4 style='color:  #FF7F50;'><em>Number of Columns : </em></h4>", unsafe_allow_html=True)
                st.write(data.shape[1])
            show_data_shape(sub_df)

            st.markdown("<h4 style='color:  #FF7F50;'><em>Description of Your DataSet : </em></h4>", unsafe_allow_html=True)
            st.table(sub_df.describe())


            show_columns_info(sub_df)
            show_missing_and_unique_values(sub_df)
            show_standard_deviation(sub_df)
            sorted_data = sort_data(sub_df)
            show_sorted_data(sorted_data)
            def groupby_function(data_frame, group_by_column, aggregation_column, aggregation_function):
                grouped_data = data_frame.groupby(group_by_column)[aggregation_column].apply(aggregation_function)
                return grouped_data
            
            st.markdown("<h2 style='color: #FF5733;'><em>GroupBy Function</em></h2>", unsafe_allow_html=True)
            group_by_column = st.selectbox("Select column to group by:", data.columns)
            aggregation_column = st.selectbox("Select column for aggregation:", data.columns)
            aggregation_function = st.selectbox("Select aggregation function:", ['sum', 'mean', 'max', 'min'])

            if st.button("Apply GroupBy"):
                grouped_data = groupby_function(data, group_by_column, aggregation_column, aggregation_function)
                st.markdown("<h4 style='color: #FF5733;'><em>Grouped Data</em></h2>", unsafe_allow_html=True)
                st.write(grouped_data)
    
          


        else:
            st.warning("Please select at least one column.")


    def show_file_header(data):
        st.write("File Header")
        st.table(data.head())

    def sort_data(data):
    # Sort the data by a selected column
        st.markdown("<h4 style='color:  #FF7F50;'><em>Sorting : </em></h4>", unsafe_allow_html=True)
        sort_column = st.selectbox("Select a column to sort by", data.columns)
        sorted_df = data.sort_values(by=sort_column)
        return sorted_df


    def show_sorted_data(sorted_df):
        st.markdown("<h4 style='color:  #FF7F50;'><em>Sorted Data : </em></h4>", unsafe_allow_html=True)
        #with st.expander("Click to view all data"):
        st.write(sorted_df)  # Display the entire DataFrame

        # Create a downloadable Excel file
        #output = io.BytesIO()
            #writer = pd.ExcelWriter(output, engine='xlsxwriter')
            #sorted_df.to_excel(writer, index=False, sheet_name='Sorted Data')
           # writer.save()
        #excel_data = output.getvalue()

        #st.download_button("Download Excel", data=excel_data, file_name="sorted_data.xlsx")
    def show_columns_info(data):
        
        st.markdown("<h4 style='color:  #FF7F50;'><em>Column Names And their DataTypes : </em></h4>", unsafe_allow_html=True)
        column_info_df = pd.DataFrame({
        'Column Names': data.columns,
        'Data Types': data.dtypes
        })
        st.table(column_info_df)

    
    

    def show_missing_and_unique_values(data):
        st.markdown("<h4 style='color:  #FF7F50;'><em>Missing and Unique Values in Sub DataFrame : </em></h4>", unsafe_allow_html=True)
        missing_values = data.isnull().sum()
        unique_values = data.nunique()
    
    # Create a DataFrame to combine the missing and unique values
        info_df = pd.DataFrame({
            'Column Names': data.columns,
            'Missing Values': missing_values,
            'Unique Values': unique_values
        })
        info_df = info_df.rename(columns={
            'Column Names': 'Column Name',
            'Missing Values': 'Missing Values Count',
            'Unique Values': 'Unique Values Count'
        })
        st.table(info_df)


    def show_standard_deviation(data):
        st.markdown("<h4 style='color:  #FF7F50;'><em>Standard Deviation : </em></h4>", unsafe_allow_html=True)
        std_deviation = data.std(numeric_only=True)
    
    # Create a DataFrame to show the standard deviation
        std_dev_df = pd.DataFrame({
            'Column Names': std_deviation.index,
            'Standard Deviation': std_deviation.values
        })
    
    # Rename the columns in the std_dev_df DataFrame
        std_dev_df = std_dev_df.rename(columns={
            'Column Names': 'Column Name',
            'Standard Deviation': 'Standard Deviation'
        })
    
        st.table(std_dev_df)

    if data is not None:
        analyze_data(data)
        
        #sorted_data = sort_data(data)
        #show_sorted_data(sorted_data)


elif selected == 'Data Visualization':
    def load_data(file):
        file_extension = file.name.split(".")[-1]
        if file_extension == "csv":
            data = pd.read_csv(file)
        elif file_extension in ["xls", "xlsx"]:
            data = pd.read_excel(file)
        else:
            st.warning("Unsupported file format. Please upload a CSV or Excel file.")
            return None
        return data

# Function to plot bar chart
    def plot_bar_chart(data, x_column, y_column):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=data, x=x_column, y=y_column, ax=ax)
        ax.set_title(f"Bar Chart: {y_column} vs {x_column}")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)

# Function to plot line chart
    def plot_line_chart(data, x_column, y_column):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=data, x=x_column, y=y_column, ax=ax)
        ax.set_title(f"Line Chart: {y_column} vs {x_column}")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)

# Function to plot scatter plot
    def plot_scatter_plot(data, x_column, y_column):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=data, x=x_column, y=y_column, ax=ax)
        ax.set_title(f"Scatter Plot: {y_column} vs {x_column}")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        st.pyplot(fig)  
    def plot_box(data, x_column, y_column):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=data, x=x_column, y=y_column, ax=ax)
        ax.set_title(f"Box Plot: {y_column} vs {x_column}")
        st.pyplot(fig)

# Violin Plot Function
    def plot_violin(data, x_column, y_column):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.violinplot(data=data, x=x_column, y=y_column, ax=ax)
        ax.set_title(f"Violin Plot: {y_column} vs {x_column}")
        st.pyplot(fig)

# Contour Plot Function
    def plot_contour(data, x_column, y_column):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.kdeplot(data=data, x=x_column, y=y_column, ax=ax, fill=True, cmap="viridis")
        ax.set_title(f"Contour Plot: {y_column} vs {x_column}")
        st.pyplot(fig) 
    def convert_date_columns(data):
        for col in data.columns:
            try:
                data[col] = pd.to_datetime(data[col])
            except (ValueError, TypeError):
                pass
        return data 
    def clean_data(data):
        """
        Converts numeric-like object/string columns into numeric columns.
        """
        for column in data.select_dtypes(include=['object', 'string']).columns:
            try:
                temp = pd.to_numeric(data[column], errors='coerce')
                if temp.notna().sum() / len(temp) > 0.8:  # 80% or more numeric
                    data[column] = temp
                    st.info(f"Column '{column}' has been converted to numeric.")
            except Exception as e:
                st.warning(f"Could not process column '{column}' for numeric conversion. Error: {e}")
        return data
    def main():
        st.markdown("<h1 style='color: #FF5733;'><em>Data Visualization :</em></h1>", unsafe_allow_html=True)

        # File upload
        file = st.file_uploader("Upload your dataset (CSV or Excel format):", type=["csv", "xls", "xlsx"])
        data = None

        if file is not None:
            data = load_data(file)
            

        if data is not None:
            st.markdown("<h2 style='color: #FF5733;'><em>Data Preview</em></h2>", unsafe_allow_html=True)
            st.write(data.head())

            # Data visualization
            st.markdown("<h1 style='color: #FF5733;'><em>Data Visualization</em></h1>", unsafe_allow_html=True)

            chart_type = st.selectbox("Select Chart Type", ["", "Bar Chart", "Line Chart", "Scatter Plot", "Histogram", "Pie Chart"])
            if not chart_type:
                st.warning("Please select a chart type to proceed.")
                return

            x_column = None
            y_column = None

            # Column selection based on chart type
            if chart_type in ["Bar Chart", "Line Chart", "Scatter Plot"]:
                x_column = st.selectbox("Select X Column",[""] + list(data.columns), index=0) 
                if x_column == "":
                    st.warning('Please select a valid X column.')
                    return 
                if chart_type != "Pie Chart":
                    y_column = st.selectbox("Select Y Column", [""]+ list(data.select_dtypes(include=['int', 'float']).columns)) 
                    if y_column == "":
                        st.warning('Please select a valid Y column.')
                        return 

                # Ensure valid column selection
                if x_column == y_column:
                    st.warning("X and Y columns must be different.")
                    return

            elif chart_type == "Histogram":
                x_column = st.selectbox("Select Column for Histogram", [""]+ list(data.columns)) 
                if x_column == "":
                    st.warning("Please select a valid column for the histogram.")
                    return

            elif chart_type == "Pie Chart":
                x_column = st.selectbox("Select Column for Pie Chart", [""]+ list(data.columns)) 
                if x_column == "":
                    st.warning("Please select a valid column for the pie chart.")
                    return

            # Generate the plot
            fig = None
            try:
                if chart_type == "Bar Chart":
                    fig = px.bar(data, x=x_column, y=y_column, title=f"Bar Chart: {y_column} vs {x_column}")
                elif chart_type == "Line Chart":
                    fig = px.line(data, x=x_column, y=y_column, title=f"Line Chart: {y_column} vs {x_column}")
                elif chart_type == "Scatter Plot":
                    fig = px.scatter(data, x=x_column, y=y_column, title=f"Scatter Plot: {y_column} vs {x_column}")
                elif chart_type == "Histogram":
                    fig = px.histogram(data, x=x_column, title=f"Histogram: {x_column}")
                elif chart_type == "Pie Chart":
                    fig = px.pie(data, names=x_column, title=f"Pie Chart: {x_column}")

                if fig:
                    st.plotly_chart(fig)

            except Exception as e:
                st.error(f"Error generating the plot: {e}")

            # Interpretation with GPT
            if st.button("Get Interpretation"):
                try:
                    # Prepare data for GPT
                    if y_column:
                        selected_data = data[[x_column, y_column]].to_csv(index=False)
                    else:
                        selected_data = data[[x_column]].to_csv(index=False)

                    prompt = f"""
                    Analyze the {chart_type} using the following dataset:
                    {selected_data}

                    Columns:
                    - X-axis: {x_column}
                    """
                    if y_column:
                        prompt += f"- Y-axis: {y_column}\n"

                    prompt += "Provide insights, patterns, or trends observed in the chart."

                    # GPT API call
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a data Visualization expert in interpreting plots and drawing conclusions from the data & plot."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    interpretation = response.choices[0].message.content.strip()
                    st.markdown("### Chart Interpretation")
                    st.write(interpretation)

                except Exception as e:
                    st.error(f"Error generating interpretation: {e}")
        
   
    if __name__ == "__main__":
        main()


   



    