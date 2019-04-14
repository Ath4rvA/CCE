from flask import Flask,render_template,request
from fetch_try import get_search_results
from algo import train,predict,load_data
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

@app.route("/searchQuery",methods=['POST'])
def search():
    data=request.form
    df=get_search_results(data['search_text'])
    df=df.fillna(0)
    x_tr,x_te,y_tr,y_te=load_data()
    train(x_tr,x_te,y_tr,y_te)
    df=predict(df)
#    import matplotlib.pyplot as plt
#    import pandas as pd
#    from pandas.plotting import table
#    ax = plt.subplot(111, frame_on=False) # no visible frame
#    ax.xaxis.set_visible(False)  # hide the x axis
#    ax.yaxis.set_visible(False)  # hide the y axis
#    table(ax, df)  # where df is your data frame
#    plt.savefig('mytable.png')
#    return render_template('show.html')
    return render_template('data_analysis.html', data= df.to_html())
#    return str(df)
if __name__=='__main__':
    app.run()