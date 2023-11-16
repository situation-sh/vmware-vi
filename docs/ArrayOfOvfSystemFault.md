# ArrayOfOvfSystemFault

A boxed array of *OvfSystemFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfSystemFault]**](OvfSystemFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_system_fault import ArrayOfOvfSystemFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfSystemFault from a JSON string
array_of_ovf_system_fault_instance = ArrayOfOvfSystemFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfSystemFault.to_json()

# convert the object into a dict
array_of_ovf_system_fault_dict = array_of_ovf_system_fault_instance.to_dict()
# create an instance of ArrayOfOvfSystemFault from a dict
array_of_ovf_system_fault_form_dict = array_of_ovf_system_fault.from_dict(array_of_ovf_system_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


