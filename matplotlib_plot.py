import matplotlib.pyplot as mp

x=[10,2,3]
mp.plot(x)
mp.show()

x=[10,2,3]
mp.plot(x)
mp.xlabel("height")
mp.ylabel("width")
mp.title("Area")
mp.show()

x=[10,2,3]
y=[1,2,3]
mp.plot(x,y)
mp.xlabel("height")
mp.ylabel("width")
mp.title("Area")
mp.show()

x=[10,2,3]
y=[1,2,3]
mp.plot(x,y,marker="*",linestyle="-",label="tv")
mp.xlabel("height")
mp.ylabel("width")
mp.title("Area")
mp.legend()
mp.show()

x=[10,2,3]
y=[1,2,3]
mp.plot(x,y,marker="*",linestyle="--",label="samsung")
mp.xlabel("height")
mp.ylabel("width")
mp.title("TV Ratio")
mp.legend()
mp.show()

x=[10,2,3]
y=[1,2,3]
mp.plot(x,y,marker="s",linestyle="--",label="samsung")
mp.xlabel("height")
mp.ylabel("width")
mp.title("TV Ratio")
mp.legend()
mp.show()

x=[10,2,3]
y=[1,2,3]
mp.plot(x,y,marker="p",linestyle="--",label="samsung")
mp.xlabel("height")
mp.ylabel("width")
mp.title("TV Ratio")
mp.legend()
mp.show()

x=[10,2,3]
y=[1,2,3]
mp.plot(x,y,marker="*",linestyle=":",label="samsung")
mp.xlabel("height")
mp.ylabel("width")
mp.title("TV Ratio")
mp.legend()
mp.show()


x=[10,2,3]
y=[1,2,3]
mp.plot(x,marker="p",linestyle=":",label=["samsung","onida"])
mp.plot(y,marker="*",linestyle="-",label="sony")
mp.xlabel("height")
mp.ylabel("width")
mp.title("TV Ratio")
mp.legend()
mp.show()


x=[10,2,3]
y=[1,2,3]
mp.plot(x,marker="p",linestyle=":",color="R",label=["samsung","onida"])
mp.plot(y,marker="*",linestyle="-",color="G",label="sony")
mp.xlabel("height")
mp.ylabel("width")
mp.title("TV Budget Ratio")
mp.legend()
mp.show()


x=[10,2,3]
y=[1,2,3]
mp.plot(x,marker="p",linestyle=":",color="R",label=["samsung","onida"],markersize=10)
mp.plot(y,marker="*",linestyle="-",color="G",label="sony",markersize=5)
mp.xlabel("height")
mp.ylabel("width")
mp.title("TV Budget Ratio")
mp.legend()
mp.show()


x=[10,2,3]
y=[1,2,3]
mp.plot(x,marker="p",linestyle=":",color="R",label=["samsung","onida"],markersize=15,linewidth=4)
mp.plot(y,marker="*",linestyle="-",color="G",label="sony",markersize=15,linewidth=5)
mp.xlabel("height")
mp.ylabel("width")
mp.title("TV Budget Ratio")
mp.legend()
mp.grid()
mp.show()
































































