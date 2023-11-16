# HostEnterMaintenanceResult

EnterMaintenanceResult is the result returned to the *HostSystem.QueryWhatIfEnterMaintenance* method.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_faults** | [**List[FaultsByVM]**](FaultsByVM.md) | VM specific faults that would prevent host from entering maintenance mode.  ***Since:*** vSphere API 6.7  | [optional] 
**host_faults** | [**List[FaultsByHost]**](FaultsByHost.md) | Host specific faults that would prevent host from entering maintenance mode.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.host_enter_maintenance_result import HostEnterMaintenanceResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostEnterMaintenanceResult from a JSON string
host_enter_maintenance_result_instance = HostEnterMaintenanceResult.from_json(json)
# print the JSON string representation of the object
print HostEnterMaintenanceResult.to_json()

# convert the object into a dict
host_enter_maintenance_result_dict = host_enter_maintenance_result_instance.to_dict()
# create an instance of HostEnterMaintenanceResult from a dict
host_enter_maintenance_result_form_dict = host_enter_maintenance_result.from_dict(host_enter_maintenance_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


