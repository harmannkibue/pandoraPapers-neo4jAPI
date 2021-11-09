from django.conf.urls import re_path
from fetch_api.views import GetNodesData, GetDataSource, GetJurisdictions, GetCountries, GetNodeData, GetNodesCount

urlpatterns = [
    re_path(r'^count[/]?$', GetNodesCount.as_view(), name='get_nodes_count'),
    re_path(r'^nodes[/]?$', GetNodesData.as_view(), name='get_nodes_data'),
    re_path(r'^node[/]?$', GetNodeData.as_view(), name='get_node_data'),
    re_path(r'^countries[/]?$', GetCountries.as_view(), name='get_countries'),
    re_path(r'^jurisdictions[/]?$', GetJurisdictions.as_view(), name='get_jurisdictions'),
    re_path(r'^datasource[/]?$', GetDataSource.as_view(), name='get_data_source'),
]