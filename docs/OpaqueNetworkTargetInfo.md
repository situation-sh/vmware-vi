# OpaqueNetworkTargetInfo

This class describes an opaque network that a device backing can attached to.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**OpaqueNetworkSummary**](OpaqueNetworkSummary.md) |  | 
**network_reservation_supported** | **bool** | Indicates whether network bandwidth reservation is supported on the opaque network  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.opaque_network_target_info import OpaqueNetworkTargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueNetworkTargetInfo from a JSON string
opaque_network_target_info_instance = OpaqueNetworkTargetInfo.from_json(json)
# print the JSON string representation of the object
print OpaqueNetworkTargetInfo.to_json()

# convert the object into a dict
opaque_network_target_info_dict = opaque_network_target_info_instance.to_dict()
# create an instance of OpaqueNetworkTargetInfo from a dict
opaque_network_target_info_form_dict = opaque_network_target_info.from_dict(opaque_network_target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


