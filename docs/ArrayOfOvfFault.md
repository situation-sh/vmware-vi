# ArrayOfOvfFault

A boxed array of *OvfFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfFault]**](OvfFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_fault import ArrayOfOvfFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfFault from a JSON string
array_of_ovf_fault_instance = ArrayOfOvfFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfFault.to_json()

# convert the object into a dict
array_of_ovf_fault_dict = array_of_ovf_fault_instance.to_dict()
# create an instance of ArrayOfOvfFault from a dict
array_of_ovf_fault_form_dict = array_of_ovf_fault.from_dict(array_of_ovf_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


