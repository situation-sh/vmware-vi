# RestartServiceConsoleVirtualNicRequestType

The parameters of *HostNetworkSystem.RestartServiceConsoleVirtualNic*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** |  | 

## Example

```python
from vmware_vi.models.restart_service_console_virtual_nic_request_type import RestartServiceConsoleVirtualNicRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RestartServiceConsoleVirtualNicRequestType from a JSON string
restart_service_console_virtual_nic_request_type_instance = RestartServiceConsoleVirtualNicRequestType.from_json(json)
# print the JSON string representation of the object
print RestartServiceConsoleVirtualNicRequestType.to_json()

# convert the object into a dict
restart_service_console_virtual_nic_request_type_dict = restart_service_console_virtual_nic_request_type_instance.to_dict()
# create an instance of RestartServiceConsoleVirtualNicRequestType from a dict
restart_service_console_virtual_nic_request_type_form_dict = restart_service_console_virtual_nic_request_type.from_dict(restart_service_console_virtual_nic_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


