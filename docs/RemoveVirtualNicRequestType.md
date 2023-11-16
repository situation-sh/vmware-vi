# RemoveVirtualNicRequestType

The parameters of *HostNetworkSystem.RemoveVirtualNic*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** |  | 

## Example

```python
from vmware_vi.models.remove_virtual_nic_request_type import RemoveVirtualNicRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveVirtualNicRequestType from a JSON string
remove_virtual_nic_request_type_instance = RemoveVirtualNicRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveVirtualNicRequestType.to_json()

# convert the object into a dict
remove_virtual_nic_request_type_dict = remove_virtual_nic_request_type_instance.to_dict()
# create an instance of RemoveVirtualNicRequestType from a dict
remove_virtual_nic_request_type_form_dict = remove_virtual_nic_request_type.from_dict(remove_virtual_nic_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


