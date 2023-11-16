# NotSupportedHostInHACluster

A NotSupportedHostInHACluster fault occurs when the host does not support the necessary features to participate in the HA cluster.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The name of the host.  ***Since:*** vSphere API 5.0  | 
**build** | **str** | The product build number of the host.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.not_supported_host_in_ha_cluster import NotSupportedHostInHACluster

# TODO update the JSON string below
json = "{}"
# create an instance of NotSupportedHostInHACluster from a JSON string
not_supported_host_in_ha_cluster_instance = NotSupportedHostInHACluster.from_json(json)
# print the JSON string representation of the object
print NotSupportedHostInHACluster.to_json()

# convert the object into a dict
not_supported_host_in_ha_cluster_dict = not_supported_host_in_ha_cluster_instance.to_dict()
# create an instance of NotSupportedHostInHACluster from a dict
not_supported_host_in_ha_cluster_form_dict = not_supported_host_in_ha_cluster.from_dict(not_supported_host_in_ha_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


