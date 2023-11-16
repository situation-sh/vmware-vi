# ClusterProactiveDrsConfigInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag indicating whether or not the service is enabled.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.cluster_proactive_drs_config_info import ClusterProactiveDrsConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProactiveDrsConfigInfo from a JSON string
cluster_proactive_drs_config_info_instance = ClusterProactiveDrsConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterProactiveDrsConfigInfo.to_json()

# convert the object into a dict
cluster_proactive_drs_config_info_dict = cluster_proactive_drs_config_info_instance.to_dict()
# create an instance of ClusterProactiveDrsConfigInfo from a dict
cluster_proactive_drs_config_info_form_dict = cluster_proactive_drs_config_info.from_dict(cluster_proactive_drs_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


