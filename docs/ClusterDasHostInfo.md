# ClusterDasHostInfo

HA specific advanced information pertaining to the hosts in the cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cluster_das_host_info import ClusterDasHostInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasHostInfo from a JSON string
cluster_das_host_info_instance = ClusterDasHostInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDasHostInfo.to_json()

# convert the object into a dict
cluster_das_host_info_dict = cluster_das_host_info_instance.to_dict()
# create an instance of ClusterDasHostInfo from a dict
cluster_das_host_info_form_dict = cluster_das_host_info.from_dict(cluster_das_host_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


