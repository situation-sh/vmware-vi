# ReconnectHostRequestType

The parameters of *HostSystem.ReconnectHost_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cnx_spec** | [**HostConnectSpec**](HostConnectSpec.md) |  | [optional] 
**reconnect_spec** | [**HostSystemReconnectSpec**](HostSystemReconnectSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.reconnect_host_request_type import ReconnectHostRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconnectHostRequestType from a JSON string
reconnect_host_request_type_instance = ReconnectHostRequestType.from_json(json)
# print the JSON string representation of the object
print ReconnectHostRequestType.to_json()

# convert the object into a dict
reconnect_host_request_type_dict = reconnect_host_request_type_instance.to_dict()
# create an instance of ReconnectHostRequestType from a dict
reconnect_host_request_type_form_dict = reconnect_host_request_type.from_dict(reconnect_host_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


