from flask import Flask,render_template,request
from fetch_try import get_search_results
from algo import train,predict,load_data
import pandas as pd
app=Flask(__name__,static_url_path="/static")

#nltk.download()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/searchQuery",methods=['POST'])
def search():
    data=request.form
    print("Search text:",data['search_text'])
    df=get_search_results(data['search_text'])
    df=df.fillna(0)
    x_tr,x_te,y_tr,y_te=load_data()
    train(x_tr,x_te,y_tr,y_te)
    df=predict(df)
    print(df)
#    import matplotlib.pyplot as plt
#    import pandas as pd
#    from pandas.plotting import table
#    ax = plt.subplot(111, frame_on=False) # no visible frame
#    ax.xaxis.set_visible(False)  # hide the x axis
#    ax.yaxis.set_visible(False)  # hide the y axis
#    table(ax, df)  # where df is your data frame
#    plt.savefig('mytable.png')
#    return render_template('show.html')
    #new_df= df.sort_values(by=['score'], ascending= False)
    new_df=df
    new_df.set_index('score',inplace=True)
    new_df=new_df.sort_values(by=['score'],ascending=False)
    for i in range(len(new_df)):
        new_df.iloc[i,0]='<a href="{0}" target="_blank">{0}</a>'.format(new_df.iloc[i,0])
    new_df= new_df.loc[:,['Link','Title','View Count','Likes','Dislikes','Sentiment']]
    print(new_df)
    pd.set_option('display.max_colwidth',-1)
    #new_df= new_df.reset_index()
    return render_template('table.html', data= new_df.to_html(escape=False))
#    return str(df)
if __name__=='__main__':
    app.run()