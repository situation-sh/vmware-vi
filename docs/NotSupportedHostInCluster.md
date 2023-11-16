# NotSupportedHostInCluster

A NotSupportedHostInCluster fault occurs when the host does not support the necessary features to participate in the cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.not_supported_host_in_cluster import NotSupportedHostInCluster

# TODO update the JSON string below
json = "{}"
# create an instance of NotSupportedHostInCluster from a JSON string
not_supported_host_in_cluster_instance = NotSupportedHostInCluster.from_json(json)
# print the JSON string representation of the object
print NotSupportedHostInCluster.to_json()

# convert the object into a dict
not_supported_host_in_cluster_dict = not_supported_host_in_cluster_instance.to_dict()
# create an instance of NotSupportedHostInCluster from a dict
not_supported_host_in_cluster_form_dict = not_supported_host_in_cluster.from_dict(not_supported_host_in_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


