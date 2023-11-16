# InsufficientCpuResourcesFault

CPU resources admission control failed 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unreserved** | **int** | The CPU available in the resource pool requested in MHz.  | 
**requested** | **int** | The CPU resource amount requested in the failed operation in MHz.  | 

## Example

```python
from vmware_vi.models.insufficient_cpu_resources_fault import InsufficientCpuResourcesFault

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientCpuResourcesFault from a JSON string
insufficient_cpu_resources_fault_instance = InsufficientCpuResourcesFault.from_json(json)
# print the JSON string representation of the object
print InsufficientCpuResourcesFault.to_json()

# convert the object into a dict
insufficient_cpu_resources_fault_dict = insufficient_cpu_resources_fault_instance.to_dict()
# create an instance of InsufficientCpuResourcesFault from a dict
insufficient_cpu_resources_fault_form_dict = insufficient_cpu_resources_fault.from_dict(insufficient_cpu_resources_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


