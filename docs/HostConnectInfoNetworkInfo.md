# HostConnectInfoNetworkInfo

The base data object type for information about networks on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**NetworkSummary**](NetworkSummary.md) |  | 

## Example

```python
from vmware_vi.models.host_connect_info_network_info import HostConnectInfoNetworkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostConnectInfoNetworkInfo from a JSON string
host_connect_info_network_info_instance = HostConnectInfoNetworkInfo.from_json(json)
# print the JSON string representation of the object
print HostConnectInfoNetworkInfo.to_json()

# convert the object into a dict
host_connect_info_network_info_dict = host_connect_info_network_info_instance.to_dict()
# create an instance of HostConnectInfoNetworkInfo from a dict
host_connect_info_network_info_form_dict = host_connect_info_network_info.from_dict(host_connect_info_network_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


