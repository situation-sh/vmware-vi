# HostNewNetworkConnectInfo

Network information for a network that will be added to VirtualCenter when the host is added. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_new_network_connect_info import HostNewNetworkConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostNewNetworkConnectInfo from a JSON string
host_new_network_connect_info_instance = HostNewNetworkConnectInfo.from_json(json)
# print the JSON string representation of the object
print HostNewNetworkConnectInfo.to_json()

# convert the object into a dict
host_new_network_connect_info_dict = host_new_network_connect_info_instance.to_dict()
# create an instance of HostNewNetworkConnectInfo from a dict
host_new_network_connect_info_form_dict = host_new_network_connect_info.from_dict(host_new_network_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


