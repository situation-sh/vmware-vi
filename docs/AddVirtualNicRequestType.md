# AddVirtualNicRequestType

The parameters of *HostNetworkSystem.AddVirtualNic*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portgroup** | **str** | Note: Must be the empty string in case nic.distributedVirtualPort is set.  | 
**nic** | [**HostVirtualNicSpec**](HostVirtualNicSpec.md) |  | 

## Example

```python
from vmware_vi.models.add_virtual_nic_request_type import AddVirtualNicRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddVirtualNicRequestType from a JSON string
add_virtual_nic_request_type_instance = AddVirtualNicRequestType.from_json(json)
# print the JSON string representation of the object
print AddVirtualNicRequestType.to_json()

# convert the object into a dict
add_virtual_nic_request_type_dict = add_virtual_nic_request_type_instance.to_dict()
# create an instance of AddVirtualNicRequestType from a dict
add_virtual_nic_request_type_form_dict = add_virtual_nic_request_type.from_dict(add_virtual_nic_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


