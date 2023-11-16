# ArrayOfHostFaultToleranceManagerComponentHealthInfo

A boxed array of *HostFaultToleranceManagerComponentHealthInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFaultToleranceManagerComponentHealthInfo]**](HostFaultToleranceManagerComponentHealthInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_fault_tolerance_manager_component_health_info import ArrayOfHostFaultToleranceManagerComponentHealthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFaultToleranceManagerComponentHealthInfo from a JSON string
array_of_host_fault_tolerance_manager_component_health_info_instance = ArrayOfHostFaultToleranceManagerComponentHealthInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFaultToleranceManagerComponentHealthInfo.to_json()

# convert the object into a dict
array_of_host_fault_tolerance_manager_component_health_info_dict = array_of_host_fault_tolerance_manager_component_health_info_instance.to_dict()
# create an instance of ArrayOfHostFaultToleranceManagerComponentHealthInfo from a dict
array_of_host_fault_tolerance_manager_component_health_info_form_dict = array_of_host_fault_tolerance_manager_component_health_info.from_dict(array_of_host_fault_tolerance_manager_component_health_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


