# RemoveServiceConsoleVirtualNicRequestType

The parameters of *HostNetworkSystem.RemoveServiceConsoleVirtualNic*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** |  | 

## Example

```python
from vmware_vi.models.remove_service_console_virtual_nic_request_type import RemoveServiceConsoleVirtualNicRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveServiceConsoleVirtualNicRequestType from a JSON string
remove_service_console_virtual_nic_request_type_instance = RemoveServiceConsoleVirtualNicRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveServiceConsoleVirtualNicRequestType.to_json()

# convert the object into a dict
remove_service_console_virtual_nic_request_type_dict = remove_service_console_virtual_nic_request_type_instance.to_dict()
# create an instance of RemoveServiceConsoleVirtualNicRequestType from a dict
remove_service_console_virtual_nic_request_type_form_dict = remove_service_console_virtual_nic_request_type.from_dict(remove_service_console_virtual_nic_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


