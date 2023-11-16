# ReconfigureAutostartRequestType

The parameters of *HostAutoStartManager.ReconfigureAutostart*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostAutoStartManagerConfig**](HostAutoStartManagerConfig.md) |  | 

## Example

```python
from vmware_vi.models.reconfigure_autostart_request_type import ReconfigureAutostartRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureAutostartRequestType from a JSON string
reconfigure_autostart_request_type_instance = ReconfigureAutostartRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureAutostartRequestType.to_json()

# convert the object into a dict
reconfigure_autostart_request_type_dict = reconfigure_autostart_request_type_instance.to_dict()
# create an instance of ReconfigureAutostartRequestType from a dict
reconfigure_autostart_request_type_form_dict = reconfigure_autostart_request_type.from_dict(reconfigure_autostart_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


