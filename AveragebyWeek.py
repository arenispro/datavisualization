import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data= pandas.read_csv('reviews.csv',parse_dates=['Timestamp'])

data['Week']= data['Timestamp'].dt.strftime('%Y-%U')
weekAverage = data.groupby(['Week']).mean()

chartDef="""{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Week'
    },
    subtitle: {
        text: 'From 2018 to 2021'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating Average'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: []
    }]
}
""" 

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Review", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    hc = jp.HighCharts(a=wp, options = chartDef)
    
    hc.options.titles.text ="Average Rating by Week"

    hc.options.xAxis.categories = list(weekAverage.index)
    hc.options.series[0].data = list(weekAverage['Rating'])

    return wp

jp.justpy(app)

