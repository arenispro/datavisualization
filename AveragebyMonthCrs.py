import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
 
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month']= data['Timestamp'].dt.strftime('%Y-%m')
monthAverageCrs = data.groupby(['Month','Course Name'])['Rating'].mean().unstack()

chartDef ="""{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating by Month and Course 2018-2021'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 160,
        y: 100,
        floating: false,
        borderWidth: 2,
        
    },
    xAxis: {
        title: {
            text: 'Date'
        }
       
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ''
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}

"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Review", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")

    hc = jp.HighCharts(a=wp, options=chartDef)
    hc.options.xAxis.categories = list(monthAverageCrs.index)

    hcData = [{"name":v1, "data":[v2 for v2 in monthAverageCrs[v1]]} for v1 in monthAverageCrs.columns]
    hc.options.series = hcData

    return wp

jp.justpy(app)