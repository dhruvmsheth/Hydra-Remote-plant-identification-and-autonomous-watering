%%writefile app.py


import streamlit as st
import plotly.graph_objects as go
from PIL import Image

PAGE_CONFIG = {"page_title":"Hydra-OpenVino_Tool","page_icon":":bar_chart:","layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)


  

def main():
    st.title("Hydra: OpenVino & AI based Remote plant monitoring & Feeding")
    st.subheader("Hydra is an Intel OpenVino based Apple Vegetation Monitoring and Watering system with Visual and Geospatial Analysis based on AIoT Technology")
if __name__ == '__main__':
    main()


fig = go.Figure(data=[go.Scatter(
        x=[2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2 ,2 ,2 ,2,
           4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
           6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
           8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
           10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
           12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
        y=[100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,
           100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,
           100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,
           100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,
           100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,
           100, 250, 345, 450, 560, 680, 790, 910, 1050, 1250, 1380, 1490, 1670, 1789,],
        mode='markers',
        marker=dict(
            color=[80, 80, 80, 80, 90, 80, 80 , 90, 85, 90, 95, 80, 70, 75,
                   80, 80, 80, 80, 90, 80, 80 , 90, 85, 90, 95, 80, 70, 75,
                   70, 75, 80, 90, 70, 75, 80 , 95, 90, 95, 85, 80, 75, 80,
                   80, 90, 80, 80, 90, 80, 80, 80, 85, 90, 95, 80, 70, 75,
                   80, 80, 80, 80, 90, 80, 80 , 90, 85, 90, 95, 80, 70, 75,
                   80, 80, 80, 80, 90, 80, 80 , 90, 85, 90, 95, 80, 70, 75,],
            size=[25, 25, 25, 25, 30, 25, 25, 30, 28, 30, 35, 25, 20, 23,
                  25, 25, 25, 25, 30, 25, 25, 30, 28, 30, 35, 25, 20, 23,
                  20, 23, 25, 30, 20, 23, 25, 35, 30, 35, 28, 25, 23, 25,
                  25, 30, 25, 25, 25, 25, 25, 30, 28, 30, 35, 25, 20, 23,
                  25, 25, 25, 25, 30, 25, 25, 30, 28, 30, 35, 25, 20, 23,
                  25, 25, 25, 25, 30, 25, 25, 30, 28, 30, 35, 25, 20, 23],
            showscale=True
            )
    )])

# 70 - 20, 
 # 75 - 23, 
  #80 - 25, 
  #85 - 28, 
  #90 - 30,
  #95 - 35

fig2 = go.Figure(
    data=[go.Bar(y=[78, 65, 68, 54, 104, 89.45, 1000, 845, 72, 71, 64, 24, 7])],
    layout_title_text="Average Temperature (dy)°C"
)



menu = ["Home","Average-Temp","Average-Humidity","Average-Moisture","Geospatial-analysis"]

choice = st.sidebar.selectbox('Menu',menu)
img = Image.open("/content/top-down-farm.jpg")

img2 = Image.open("/content/agri-farm.png")

img3 = Image.open("/content/keplergl.jpeg")

st.sidebar.subheader("Farm plot")
st.sidebar.image(img3, height=250, width=250)
st.sidebar.image(img, height=250, width=250)
st.sidebar.image(img2, height=250, width=250)
if choice == 'Average-Temp':
    
  st.plotly_chart(fig2)
if choice == 'Home':
        
  st.plotly_chart(fig)
