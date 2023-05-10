#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage,AnnotationBbox
from matplotlib.font_manager import FontProperties
import flagpy as fp
# Set the font family to 'SimHei'
CN_font = FontProperties(fname="C:/Windows/Fonts/simsun.ttc")

countries = ["Finland", "Denmark", "Japan", "Austria", "Sweden",
             "Belgium","Israel","Portugal","Spain","Australia","China","France","Germany","South Africa",
            "South Korea","the United Kingdom","Italy","India","Ireland","Switzerland","Turkey",
             "Norway","The United States","Indonesia","Mexico","Pakistan","Canada","Brazil","Egypt",
             "Nigeria","Ukraine","Russia","Romania","Qatar","Saudi Arabia"]

countries_CN = ["芬兰", "丹麦", "日本", "奥地利", "瑞典",
                 "比利时","以色列","葡萄牙","西班牙","澳大利亚","中国","法国","德国","南非",
                 "韩国","英国","意大利","印度","爱尔兰","瑞士","土耳其","挪威",
                 "美国","印尼","墨西哥","巴基斯坦","加拿大","巴西","埃及","尼日利亚",
                 "乌克兰","俄罗斯","罗马尼亚","卡塔尔","沙特阿拉伯"]

valuesA = [56.95, 56, 55.97, 55, 52.3,50,50,48,47,45,45,45,45,45,45,45,43,
           42.74,40,40,40,38.2,37,35,35,35,33,27.5,25,24,18,13,10,0,0]

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

    ab = AnnotationBbox(im, (5, coord),  xybox=(-50., 0.), frameon=False,
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
ax.set_title("各国家平均个人所得税(%)", fontproperties=CN_font, fontsize=12, color='black')

plt.grid()
for bar in bars:
    width = bar.get_width()
    ax.text(width +1 , bar.get_y() + bar.get_height() / 2, str(width), ha='left', va='center',color='black')


for i, c in enumerate(countries):
    offset_image(i, c, ax)


plt.show()
