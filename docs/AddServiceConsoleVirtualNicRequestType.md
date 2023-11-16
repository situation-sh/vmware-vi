# AddServiceConsoleVirtualNicRequestType

The parameters of *HostNetworkSystem.AddServiceConsoleVirtualNic*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portgroup** | **str** |  | 
**nic** | [**HostVirtualNicSpec**](HostVirtualNicSpec.md) |  | 

## Example

```python
from vmware_vi.models.add_service_console_virtual_nic_request_type import AddServiceConsoleVirtualNicRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddServiceConsoleVirtualNicRequestType from a JSON string
add_service_console_virtual_nic_request_type_instance = AddServiceConsoleVirtualNicRequestType.from_json(json)
# print the JSON string representation of the object
print AddServiceConsoleVirtualNicRequestType.to_json()

# convert the object into a dict
add_service_console_virtual_nic_request_type_dict = add_service_console_virtual_nic_request_type_instance.to_dict()
# create an instance of AddServiceConsoleVirtualNicRequestType from a dict
add_service_console_virtual_nic_request_type_form_dict = add_service_console_virtual_nic_request_type.from_dict(add_service_console_virtual_nic_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


