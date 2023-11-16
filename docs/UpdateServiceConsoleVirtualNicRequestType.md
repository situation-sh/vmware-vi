# UpdateServiceConsoleVirtualNicRequestType

The parameters of *HostNetworkSystem.UpdateServiceConsoleVirtualNic*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** |  | 
**nic** | [**HostVirtualNicSpec**](HostVirtualNicSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_service_console_virtual_nic_request_type import UpdateServiceConsoleVirtualNicRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServiceConsoleVirtualNicRequestType from a JSON string
update_service_console_virtual_nic_request_type_instance = UpdateServiceConsoleVirtualNicRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateServiceConsoleVirtualNicRequestType.to_json()

# convert the object into a dict
update_service_console_virtual_nic_request_type_dict = update_service_console_virtual_nic_request_type_instance.to_dict()
# create an instance of UpdateServiceConsoleVirtualNicRequestType from a dict
update_service_console_virtual_nic_request_type_form_dict = update_service_console_virtual_nic_request_type.from_dict(update_service_console_virtual_nic_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


