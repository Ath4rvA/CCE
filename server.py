from flask import Flask,render_template,request
from fetch_try import get_search_results
from algo import train,predict,load_data
import pandas as pd
import mysql_backend_connector
app=Flask(__name__,static_url_path="/static")
yt_df=""
#nltk.download()

connector=mysql_backend_connector.MysqlBackendConnector("login","root","Atharva123")

@app.route("/login",methods=["POST"])
def login():
    if connector.login(request.form['username'],request.form['password']):
        return render_template("index.html")
    else:
        return "<h1>Error! Please check your credentials.</h1>"

@app.route("/signup",methods=["GET","POST"])
def signup():
    data=request.form
    connector.signup(data['email'],data['password'])
    return render_template("login.html")

@app.route("/signup_page")
def signup_page():
    return render_template("signup.html")


@app.route("/login_page")
def login_page():
    return render_template("login.html")

@app.route('/')
def index():
    return render_template('index_.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/FAQ')
def FAQ():
    return render_template('FAQ.html')

@app.route('/team')
def team():
    return render_template('team.html')


@app.route("/searchQuery",methods=['POST'])
def search():
    data=request.form
    print("Search text:",data['search_text'])
    df=get_search_results(data['search_text'])
    df=df.fillna(0)
    global yt_df
    yt_df=df
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
@app.route("/youtube")
def yt_results():
    global yt_df
    return render_template('table.html', data= yt_df.to_html(escape=False))
if __name__=='__main__':
    app.run()