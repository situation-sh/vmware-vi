# OpaqueNetworkCapability

The data object representing the capabilities supported by the Opaque Network.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_reservation_supported** | **bool** | Indicates whether network I/O control is supported for a network adapter that connects to the opaque network.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.opaque_network_capability import OpaqueNetworkCapability

# TODO update the JSON string below
json = "{}"
# create an instance of OpaqueNetworkCapability from a JSON string
opaque_network_capability_instance = OpaqueNetworkCapability.from_json(json)
# print the JSON string representation of the object
print OpaqueNetworkCapability.to_json()

# convert the object into a dict
opaque_network_capability_dict = opaque_network_capability_instance.to_dict()
# create an instance of OpaqueNetworkCapability from a dict
opaque_network_capability_form_dict = opaque_network_capability.from_dict(opaque_network_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


