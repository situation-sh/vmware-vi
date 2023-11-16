# ArrayOfExtendedFault

A boxed array of *ExtendedFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExtendedFault]**](ExtendedFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_extended_fault import ArrayOfExtendedFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtendedFault from a JSON string
array_of_extended_fault_instance = ArrayOfExtendedFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtendedFault.to_json()

# convert the object into a dict
array_of_extended_fault_dict = array_of_extended_fault_instance.to_dict()
# create an instance of ArrayOfExtendedFault from a dict
array_of_extended_fault_form_dict = array_of_extended_fault.from_dict(array_of_extended_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


