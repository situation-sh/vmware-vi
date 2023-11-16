# EnterMaintenanceModeRequestType

The parameters of *HostSystem.EnterMaintenanceMode_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | The task completes when the host successfully enters maintenance mode or the timeout expires, and in the latter case the task contains a Timeout fault. If the timeout is less than or equal to zero, there is no timeout. The timeout is specified in seconds.  | 
**evacuate_powered_off_vms** | **bool** | This is a parameter only supported by VirtualCenter. If set to true, for a DRS disabled cluster, the task will not succeed unless all powered-off virtual machines have been manually reregistered; for a DRS enabled cluster, VirtualCenter will automatically reregister powered-off virtual machines and a powered-off virtual machine may remain at the host only for two reasons: (a) no compatible host found for reregistration, (b) DRS is disabled for the virtual machine. If set to false, powered-off virtual machines do not need to be moved.  | [optional] 
**maintenance_spec** | [**HostMaintenanceSpec**](HostMaintenanceSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.enter_maintenance_mode_request_type import EnterMaintenanceModeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EnterMaintenanceModeRequestType from a JSON string
enter_maintenance_mode_request_type_instance = EnterMaintenanceModeRequestType.from_json(json)
# print the JSON string representation of the object
print EnterMaintenanceModeRequestType.to_json()

# convert the object into a dict
enter_maintenance_mode_request_type_dict = enter_maintenance_mode_request_type_instance.to_dict()
# create an instance of EnterMaintenanceModeRequestType from a dict
enter_maintenance_mode_request_type_form_dict = enter_maintenance_mode_request_type.from_dict(enter_maintenance_mode_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


