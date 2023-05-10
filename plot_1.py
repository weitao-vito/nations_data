#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage,AnnotationBbox
from matplotlib.font_manager import FontProperties
import flagpy as fp
# Set the font family to 'SimHei'
CN_font = FontProperties(fname="C:/Windows/Fonts/simsun.ttc")

countries = ["Switzerland", "Singapore", "Luxembourg", "The United States", "Iceland",
             "Qatar","Denmark","Australia","Norway","Canada","Germany","Sweden","The United Kingdom","France",
             "Japan","South Korea","Italy","South Africa","China","Mexico","Russia","India",
             "Turkey","Brazil","Argentina","Indonesia","Nigeria"]

countries_CN = ["瑞士", "新加坡", "卢森堡", "美国", "冰岛",
             "卡塔尔","丹麦","澳大利亚","挪威","加拿大","德国","瑞典","英国","法国",
             "日本","韩国","意大利","南非","中国","墨西哥","俄罗斯","印度",
             "土耳其","巴西","阿根廷","印尼","尼日利亚"]

valuesA = [6144, 4923, 4918, 4232, 4100,3884,3551,3449,3321,3049,3031,2932,2760,2505,2452,2296,1719,1208,
           1060,719,648,568,487,416,415,341,160]

countries.reverse()
valuesA.reverse()
countries_CN.reverse()


for country in countries:
        flag_image = fp.get_flag_img(country)
        flag_image.save("flags/"+ country+ ".png")
      
        
def get_flag(name):
    path = "flags/{}.png".format(name.title())
    im = plt.imread(path)
    return im

def offset_image(coord, name, ax):
    img = get_flag(name)
    im = OffsetImage(img, zoom=0.1)
    im.image.axes = ax

    ab = AnnotationBbox(im, (5, coord),  xybox=(-12., 0.), frameon=False,
                        xycoords='data',  boxcoords="offset points", pad=0)

    ax.add_artist(ab)
    
# Define a list of colors for the bars
 
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_facecolor('lightyellow')
fig.patch.set_facecolor('lightyellow')
'''
ax.bar(valuesA, range(len(countries)), width=1)
ax.set_yticks(range(len(countries)))
ax.set_yticklabels(countries)
ax.tick_params(axis='y', which='major', pad=26)
'''
# Change this line to use ax.barh() instead of ax.bar()
bars=ax.barh(range(len(countries)), valuesA, height=0.5, align="center",color='royalblue',edgecolor='black')
# Set y-axis ticks to numbers (1 to the total number of countries)
ax.set_yticks(range(len(countries)))
ax.set_yticklabels(countries_CN, fontproperties=CN_font,color='black')
ax.tick_params(axis='y', which='major', pad=26)
ax.set_title("各国家的平均税后月收入($)", fontproperties=CN_font, fontsize=12, color='black')

plt.grid()
for bar in bars:
    width = bar.get_width()
    ax.text(width + 50, bar.get_y() + bar.get_height() / 2, str(width), ha='left', va='center',color='black')


for i, c in enumerate(countries):
    offset_image(i, c, ax)


plt.show()
