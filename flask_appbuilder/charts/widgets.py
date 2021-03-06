from flask.ext.appbuilder.widgets import RenderTemplateWidget


class ChartWidget(RenderTemplateWidget):
    template = 'appbuilder/general/widgets/chart.html'


class MultipleChartWidget(RenderTemplateWidget):
    template = 'appbuilder/general/widgets/multiple_chart.html'
