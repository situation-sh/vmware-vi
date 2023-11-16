# ExitMaintenanceModeRequestType

The parameters of *HostSystem.ExitMaintenanceMode_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | Number of seconds to wait for the exit maintenance mode to succeed. If the timeout is less than or equal to zero, there is no timeout.  | 

## Example

```python
from vmware_vi.models.exit_maintenance_mode_request_type import ExitMaintenanceModeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ExitMaintenanceModeRequestType from a JSON string
exit_maintenance_mode_request_type_instance = ExitMaintenanceModeRequestType.from_json(json)
# print the JSON string representation of the object
print ExitMaintenanceModeRequestType.to_json()

# convert the object into a dict
exit_maintenance_mode_request_type_dict = exit_maintenance_mode_request_type_instance.to_dict()
# create an instance of ExitMaintenanceModeRequestType from a dict
exit_maintenance_mode_request_type_form_dict = exit_maintenance_mode_request_type.from_dict(exit_maintenance_mode_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


