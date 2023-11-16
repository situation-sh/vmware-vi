# ArrayOfOvfCpuCompatibility

A boxed array of *OvfCpuCompatibility*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfCpuCompatibility]**](OvfCpuCompatibility.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_cpu_compatibility import ArrayOfOvfCpuCompatibility

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfCpuCompatibility from a JSON string
array_of_ovf_cpu_compatibility_instance = ArrayOfOvfCpuCompatibility.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfCpuCompatibility.to_json()

# convert the object into a dict
array_of_ovf_cpu_compatibility_dict = array_of_ovf_cpu_compatibility_instance.to_dict()
# create an instance of ArrayOfOvfCpuCompatibility from a dict
array_of_ovf_cpu_compatibility_form_dict = array_of_ovf_cpu_compatibility.from_dict(array_of_ovf_cpu_compatibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


