# ArrayOfGenericDrsFault

A boxed array of *GenericDrsFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GenericDrsFault]**](GenericDrsFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_generic_drs_fault import ArrayOfGenericDrsFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGenericDrsFault from a JSON string
array_of_generic_drs_fault_instance = ArrayOfGenericDrsFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfGenericDrsFault.to_json()

# convert the object into a dict
array_of_generic_drs_fault_dict = array_of_generic_drs_fault_instance.to_dict()
# create an instance of ArrayOfGenericDrsFault from a dict
array_of_generic_drs_fault_form_dict = array_of_generic_drs_fault.from_dict(array_of_generic_drs_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


