# ArrayOfHostEnterMaintenanceResult

A boxed array of *HostEnterMaintenanceResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostEnterMaintenanceResult]**](HostEnterMaintenanceResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_enter_maintenance_result import ArrayOfHostEnterMaintenanceResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostEnterMaintenanceResult from a JSON string
array_of_host_enter_maintenance_result_instance = ArrayOfHostEnterMaintenanceResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostEnterMaintenanceResult.to_json()

# convert the object into a dict
array_of_host_enter_maintenance_result_dict = array_of_host_enter_maintenance_result_instance.to_dict()
# create an instance of ArrayOfHostEnterMaintenanceResult from a dict
array_of_host_enter_maintenance_result_form_dict = array_of_host_enter_maintenance_result.from_dict(array_of_host_enter_maintenance_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


