import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data= pandas.read_csv('reviews.csv',parse_dates=['Timestamp'])

share = data.groupby(['Course Name'])['Rating'].count()

chartDef ="""{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Course Rating Shares 2018-2021'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            
        }]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Review", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    hc = jp.HighCharts(a=wp, options=chartDef)

    hcData = [{"name":v1, "y":v2} for v1, v2 in zip(share.index, share)]
    hc.options.series[0].data = hcData

    return wp

jp.justpy(app)

