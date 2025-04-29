import pandas as pd
import numpy as np
import os
from os.path import dirname
from math import pi
from bokeh.plotting import figure
from bokeh.models import (ColumnDataSource, Range1d, FactorRange, HoverTool)

#######################################CONSTANTS#################################################################################
## classes
gender_cats = ['Female','Male']
age_cats = [ 'Over 50','Up to 50']

## colors
gender_colors = ['orange','gainsboro']
age_colors = ['green','gainsboro']

## pie charts
r = 1.1
rad_width = 0.4
lw_gender = 9
font_size_subfig_titles = "1em"
font_size_pie_annot = "1.2em"
width = 600
pie_height = 200
pie_width = 200
## 
split_fact = 40
gap_angle = pi/split_fact
gap_angle = 0
#############################################METHODS############################################################
def gender_split_by_age(df, gender_cats, age_cats):
    """
    {'Gender':['Female','Female','Male','Male'],
     'Age':['Over 50','Up to 50','Over 50','Up to 50'],
     'freq':[25,25,24,26]}
    """
    split_data = {'Gender':[],'Age':[],'freq':[]}
    for gen_cat in gender_cats:
        gen_data = df[df['Gender']==gen_cat]
        for sec_attr_cat in age_cats:
            split_data['Gender'].append(gen_cat)
            split_data['Age'].append(sec_attr_cat)
            split_data['freq'].append((len(gen_data[gen_data['Age']==sec_attr_cat])/len(df))*100 )
    return pd.DataFrame(split_data)

def get_percentages(df, attribute, cats):
    """"
    Return list of percentages for each category of attribute
    """
    values = []
    for cat in cats:
        values.append(df[df[attribute]==cat]['freq'].sum())
    return values

def pie_data(cats, values, colors):

    angles = [-2*pi*(pct/100) for pct in values]
    
    source = dict(
        start  = [0]+np.cumsum(angles[:-1]).tolist(),
        end    = np.cumsum(angles).tolist(),
        colors = colors,
        categories = cats,
        percentages = [str(round(pct,1))+"%" for pct in values],
    )

    return source

def pie_data_gender_split_by_age(df, age_cats, gender_values, age_values, gender_colors, age_colors):
    age_ratios = []
    age_labels = []
    ag_angles = []

    ## FEMALE
    fem_data = df[df['Gender']=='Female']
    for age_cat in age_cats:
        age_labels.append('Female '+age_cat)
        age_ratios.append(fem_data[fem_data['Age']==age_cat]['freq'].tolist()[0])
    total_fem_rads = -1*((2*pi)-(2*gap_angle))*(gender_values[0]/100)
    ag_angles.append((total_fem_rads*age_ratios[0]) / (age_ratios[0]+age_ratios[1]))
    ag_angles.append((total_fem_rads*age_ratios[1]) / (age_ratios[0]+age_ratios[1]))

    ## MALE
    male_data = df[df['Gender']=='Male']
    for age_cat in age_cats[::-1]:
        age_labels.append('Male '+age_cat)
        age_ratios.append(male_data[male_data['Age']==age_cat]['freq'].tolist()[0])
    total_mal_rads = -1*((2*pi)-(2*gap_angle))*(gender_values[1]/100)
    ag_angles.append((total_mal_rads*age_ratios[2]) / (age_ratios[2]+age_ratios[3]))
    ag_angles.append((total_mal_rads*age_ratios[3]) / (age_ratios[2]+age_ratios[3]))

    start = np.cumsum(ag_angles[:-1]).tolist()
    end = np.cumsum(ag_angles).tolist()
    ag_source = dict(
        start  = [0]+[start[0]]+[start[1]-gap_angle]+[start[2]-gap_angle],
        end    = [end[0]]+[end[1]]+[end[2]-gap_angle]+[end[3]-gap_angle],
        colors = age_colors+age_colors[::-1],
        categories = age_labels,
        percentages = [str(round(pct,1))+"%" for pct in age_ratios],
    )

    ## GENDER ANNOTATIONS
    val1 = None
    # if gender_values[0] - round(gender_values[0]):
    #     val1 = str(round(gender_values[0],1)) 
    # else:
    #     val1 = str(int(gender_values[0]))
    val1 = str(int(round(gender_values[0])))
    gender_annot_source = dict(
        x  = [0.],
        y = [0.],
        text = ["""Female """+val1+"%"],
        color = [gender_colors[0]],
    )

    ## AGE ANNOTATIONS
    # val2 = None
    # if age_values[0] - round(age_values[0]):
    #     val2 = str(round(age_values[0],1)) 
    # else:
    #     val2 = str(int(age_values[0]))
    val2 = str(int(round(age_values[0])))
    age_annot_source = dict(
        x  = [0.],
        y = [0.],
        text = ["""Over 50's """+val2+"%"],
        color = [age_colors[0]],
    )

    return ag_source, gender_annot_source, age_annot_source

def draw_pie_chart_nested(source1, source2, annot_source1, annot_source2):
    """
    attribute: List with at least two Strings in ["Gender","Age"]
    source: Dict to be turned in ColumnDataSource
    """
    ## FIGURE
    plot = figure(x_range=Range1d(start=-1.1, end=1.1), 
                  y_range=Range1d(start=-1.1, end=1.1), 
                #   title = attributes[0]+" - "+ attributes[1]+" Breakdown",
                 tools="hover",
                 toolbar_location = None,
                  min_height = pie_height,
                  min_width = pie_width,
              #     width = 300,
                 sizing_mode="scale_both",
                  outline_line_width =0
                 )
    plot.title.align = "center"
    plot.title.text_font_size = font_size_subfig_titles
    plot.axis.visible = False
    plot.grid.visible = False

    ## outer circle
    aw1 = plot.annular_wedge(x = 0, y = 0, 
                     inner_radius = r-rad_width, 
                     outer_radius = r,
                     start_angle = "start", 
                     end_angle = "end",
                    #  legend_group='categories',
                    #  line_color = "white", 
                    #  line_width = lw_gender, 
                    line_width = 0,
                     direction = 'clock',
                     fill_color = "colors",
                     source = ColumnDataSource(source1)
                    )

    ## inner circle
    aw2 = plot.annular_wedge(x = 0, y = 0, 
                         inner_radius = r-rad_width-0.15, 
                         outer_radius = r-rad_width - 0.05,
                         start_angle = "start", 
                         end_angle = "end", 
                         #  legend_group='categories',
                        #  line_color = "white",
                         line_width = 0, 
                         direction = 'clock',
                         fill_color = "colors",                        
                         source = ColumnDataSource(source2)
                        )
    hover = plot.select(dict(type=HoverTool))
    hover.tooltips = """<strong>@categories</strong>:<br>@percentages"""
    hover.renderers = [aw1,aw2]

    # plot.legend.items[0].Label = False
    # plot.legend.items[0].visible = False
    # plot.legend.items[1].visible = False
    # plot.legend.items[3].visible = False
    # plot.legend.items[4].visible = False
    # plot.legend.items[5].visible = False

#     legend = Legend(items=[
#     LegendItem(label="Female", renderers=[aw1], index=0),
#     LegendItem(label="Over 50's", renderers=[aw2], index=1),
# ])
#     plot.add_layout(legend)
#     plot.legend.location = 'center'

    # ANNOTATIONS
    plot.text(x = 'x', 
              y = 'y', 
              text = 'text',
              x_offset = 7.5, 
              y_offset = -5, 
              anchor = "center",
              color = 'color',
              text_align = 'center',
              text_font_size = font_size_pie_annot,
              text_font_style = 'bold',
              source = ColumnDataSource(annot_source1)
             )
    
    plot.text(x = 'x', 
              y = 'y', 
              text = 'text',
              x_offset = 0, 
              y_offset = 20, 
              anchor = "center",
              color = 'color',
              text_align = 'center',
              text_font_size = font_size_pie_annot,
              text_font_style = 'bold',
              source = ColumnDataSource(annot_source2)
             )

    ## WHITE LINES
    # plot.line([r-rad_width-0.11,r-rad_width], [0.,0.], color='white', line_width=lw_gender)
    
    # x_in_top = (r-rad_width-0.11) * np.cos(source2['start'][2])
    # y_in_top = (r-rad_width-0.11) * np.sin(source2['start'][2])
    # x_out_top = (r-rad_width)*np.cos(source2['start'][2])
    # y_out_top = (r-rad_width)*np.sin(source2['start'][2])
    # plot.line([x_in_top,x_out_top], [y_in_top,y_out_top], color='white', line_width=lw_gender)

    plot.line([r-rad_width-0.16,r], [0.,0.], color='white', line_width=lw_gender)
    
    x_in_top = (r-rad_width-0.16) * np.cos(source2['start'][2])
    y_in_top = (r-rad_width-0.16) * np.sin(source2['start'][2])
    x_out_top = (r+0.05)*np.cos(source2['start'][2])
    y_out_top = (r+0.05)*np.sin(source2['start'][2])
    plot.line([x_in_top,x_out_top], [y_in_top,y_out_top], color='white', line_width=lw_gender)

    return plot

def draw_bar_charts_performance(source, colors):
    """
    attribute: String in ["Gender","Age"]
    source, annot_source: Dict to be turned in ColumnDataSource
    """
    ## FIGURE
    plot = figure(#x_range = Range1d(start=0., end=100),
                y_range = FactorRange(*source['results']),
                  # title = attribute+" Breakdown",
                  tools = "hover",
                  toolbar_location = None,
                  height = 150,
                  min_width = 200,
                  sizing_mode="scale_width",
                  outline_line_width = 0
                 )
    plot.title.align = "center"
    plot.title.text_font_size = font_size_subfig_titles
    plot.grid.visible = False
    plot.xaxis.visible = False
    # plot.xaxis.axis_label = 'Percentage %'
    # plot.xaxis.major_tick_line_color = None
    plot.yaxis.major_tick_line_color = None
    # plot.xaxis.minor_tick_line_color = None
    # plot.xaxis.major_label_text_font_size = '0pt'
    # plot.xaxis.axis_line_color = None
    plot.yaxis.axis_line_color = None

    plot.hbar_stack(list(source.keys())[1:], 
                    y = 'results', 
                    height = 0.88, 
                    color = colors,
                    source = ColumnDataSource(data = source),
                    # legend_label=[f"{year} exports" for year in years]
                   )
    hover = plot.select(dict(type=HoverTool))
    hover.tooltips = "<strong>$name</strong>:<br>@$name{0.0}%"
    plot.x_range.start = 0
    plot.x_range.end = 100
    return plot

###################################################DATA LOADING#########################################################################
# #### GENERATE RANDOM DATA
# N = 200

# ## F low, Over 50's low
# gender_data = np.random.choice(len(gender_cats), size=N, p=[0.3,0.7])
# age_data = np.random.choice(len(age_cats), size=N, p=[0.2,0.8])
# df = pd.DataFrame({'Gender':[gender_cats[i] for i in gender_data.tolist()],
#                    'Age':[age_cats[i] for i in age_data.tolist()]
#                    })

# ## split data
# ## FILM 1
# df_gen_split_film1 = gender_split_by_age(df, gender_cats, age_cats)

# ## FILM 2
# gen_split_data_film2 = {'Gender':['Female','Female','Male','Male'],
#                         'Age':['Over 50','Up to 50','Over 50','Up to 50'],
#                         'freq':[50,20,20,10]}
# df_gen_split_film2 = pd.DataFrame(gen_split_data_film2)

# ## FILM 3
# gen_split_data_film3 = {'Gender':['Female','Female','Male','Male'],
#                         'Age':['Over 50','Up to 50','Over 50','Up to 50'],
#                         'freq':[25,25,24,26]}
# df_gen_split_film3 = pd.DataFrame(gen_split_data_film3)

#### LOAD DATA FROM CSV
DATA_PATH = os.path.join(dirname(dirname(__file__)), "data")

df_summary = None
dfs_gen_split = []
film_names = []
for root,dirs,files in os.walk(DATA_PATH):
    for file in files:
       if file.endswith(".csv"):
           if file == "summary.csv":
               df_summary = pd.read_csv(os.path.join(DATA_PATH, file))
           else:
               df = pd.read_csv(os.path.join(DATA_PATH, file))[['dominant_gender','age_group']]
               df.rename(columns={'dominant_gender': 'Gender', 'age_group': 'Age'}, inplace=True)
               dfs_gen_split.append(gender_split_by_age(df, gender_cats, age_cats))
               film_names.append(file.removesuffix("_demography.csv").replace("_", "") )

confidence_scores=[]
for f in film_names:
    confidence_scores = confidence_scores+ df_summary['avg_conf_gender_'+f].to_list()+df_summary['avg_conf_age_'+f].to_list()
confidence_perc = [round(i*100,0) for i in confidence_scores]


###########################################DATA RETRIEVAL#############################################################
gender_perf = dict(
    results = ["AI-identified Female","Actual Female"],
    Female = [round(df_summary['perc_fem_val_pred'].to_list()[0],1),round(df_summary['perc_fem_val'].to_list()[0],1)],
    Male = [round(df_summary['perc_mal_val_pred'].to_list()[0],1),round(df_summary['perc_mal_val'].to_list()[0],1)]
)

age_perf = {
    "results": ["AI-identified Over 50's","Actual Over 50's"],
    "Over 50": [round(df_summary['perc_o50_val_pred'].to_list()[0],1),round(df_summary['perc_o50_val'].to_list()[0],1)],
    "Up to 50": [round(df_summary['perc_ut50_val_pred'].to_list()[0],1),round(df_summary['perc_ut50_val'].to_list()[0],1)],    
}


## 
gender_sources = []
age_sources = []
gender_annot_sources = []
age_annot_sources = []
for df_gen_split in dfs_gen_split:
    gender_vals = get_percentages(df_gen_split, 'Gender', gender_cats)
    gender_source = pie_data(gender_cats, gender_vals, gender_colors)
    gender_sources.append(gender_source)
    age_vals = get_percentages(df_gen_split, 'Age', age_cats)
    ##
    age_source, gender_annot_source, age_annot_source = pie_data_gender_split_by_age(df_gen_split, age_cats, gender_vals, age_vals,  gender_colors, age_colors)
    age_sources.append(age_source)
    gender_annot_sources.append(gender_annot_source)
    age_annot_sources.append(age_annot_source)

###########################################VISUALIZATION#############################################################
## PIE CHARTS
plot_pie_charts = []
for i,gender_source in enumerate(gender_sources):
    plot_pie_charts.append(draw_pie_chart_nested(gender_source, age_sources[i], gender_annot_sources[i], age_annot_sources[i]))

## BIAS BAR GRAPHS
bar_gender = draw_bar_charts_performance(gender_perf, gender_colors)
bar_age = draw_bar_charts_performance(age_perf, age_colors)

def get_onscreentime_graphs():
    # return [plot_gender_nest_film1, plot_gender_nest_film2, plot_gender_nest_film3, bar_gender, bar_age, confidence_perc]
    # return [plot_gender_nest_film1, plot_gender_nest_film2, bar_gender, bar_age, confidence_perc[0:4]]
    return plot_pie_charts+[bar_gender, bar_age, confidence_perc]
