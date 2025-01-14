#render_template（HTMLを表示させるための関数）をインポート
from flask import Flask, request, render_template
import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64
from comparison_gsvs import app
from datetime import datetime

app = Flask(__name__)

#「/」へアクセスがあった場合に、関数の内容を実行
@app.route('/')
def index():
    return render_template('index.html')

#「/chart」へアクセスがあった場合に、関数の内容を実行
@app.route('/chart', methods=['POST'])
def chart():
    ticker1 = request.form.get('ticker1')
    ticker2 = request.form.get('ticker2')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    #株価データを取得
    stock_data1 = yf.download(ticker1, start=start_date, end=end_date, actions=True)
    stock_data2 = yf.download(ticker2, start=start_date, end=end_date, actions=True)
    
    #キャピタルゲインを計算
    start_price1 = stock_data1['Close'].iloc[0]
    end_price1 = stock_data1['Close'].iloc[-1]
    capital_gain1 = end_price1 - start_price1

    start_price2 = stock_data2['Close'].iloc[0]
    end_price2 = stock_data2['Close'].iloc[-1]
    capital_gain2 = end_price2 - start_price2

    #配当金総額の算出に必要な年数を計算
    start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
    passed_years = (end_date_dt - start_date_dt).days / 364  # 1年を364日として計算

    #年間配当金の予測（仮に配当金が存在する場合のみ計算）
    if 'Dividends' in stock_data1.columns:
        annual_dividend1 = stock_data1['Dividends'].sum()  # 全期間の配当金の合計を年ベースとみなす
        total_dividend1 = annual_dividend1 * passed_years
    else:
        total_dividend1 = 0

    if 'Dividends' in stock_data2.columns:
        annual_dividend2 = stock_data2['Dividends'].sum()
        total_dividend2 = annual_dividend2 * passed_years
    else:
        total_dividend2 = 0

    #キャピタルゲインと配当金額の合計を計算
    total1 = capital_gain1 + total_dividend1
    total2 = capital_gain2 + total_dividend2

    #グラフを描画
    plt.figure(figsize=(12, 8))
    plt.plot(stock_data1['Close'], label=f'{ticker1} Close Price', color='blue')
    plt.plot(stock_data2['Close'], label=f'{ticker2} Close Price', color='orange')
    plt.title(f'Stock Prices Comparison : {ticker1} to {ticker2}')
    plt.xlabel('Date')
    plt.ylabel('price(USD)')
    plt.legend()
    plt.grid()

    #グラフを画像として保存
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    chart_url = base64.b64encode(buf.getvalue()).decode('utf8')
    buf.close()
    
    #templateに変数を渡してHTMLを表示
    return render_template('chart.html', ticker1=ticker1, ticker2=ticker2,
                            start_date=start_date, end_date=end_date, 
                            capital_gain1=capital_gain1, capital_gain2=capital_gain2, 
                            total_dividend1=total_dividend1, total_dividend2=total_dividend2,
                            total1=total1, total2=total2,
                            chart_url=chart_url)


#デバッグモードで実行
if __name__ == '__main__':
    app.main(debug=True)