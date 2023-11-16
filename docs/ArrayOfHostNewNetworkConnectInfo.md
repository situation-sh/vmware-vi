# ArrayOfHostNewNetworkConnectInfo

A boxed array of *HostNewNetworkConnectInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNewNetworkConnectInfo]**](HostNewNetworkConnectInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_new_network_connect_info import ArrayOfHostNewNetworkConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNewNetworkConnectInfo from a JSON string
array_of_host_new_network_connect_info_instance = ArrayOfHostNewNetworkConnectInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNewNetworkConnectInfo.to_json()

# convert the object into a dict
array_of_host_new_network_connect_info_dict = array_of_host_new_network_connect_info_instance.to_dict()
# create an instance of ArrayOfHostNewNetworkConnectInfo from a dict
array_of_host_new_network_connect_info_form_dict = array_of_host_new_network_connect_info.from_dict(array_of_host_new_network_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


