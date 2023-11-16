# ArrayOfFaultToleranceMetaSpec

A boxed array of *FaultToleranceMetaSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FaultToleranceMetaSpec]**](FaultToleranceMetaSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_fault_tolerance_meta_spec import ArrayOfFaultToleranceMetaSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFaultToleranceMetaSpec from a JSON string
array_of_fault_tolerance_meta_spec_instance = ArrayOfFaultToleranceMetaSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfFaultToleranceMetaSpec.to_json()

# convert the object into a dict
array_of_fault_tolerance_meta_spec_dict = array_of_fault_tolerance_meta_spec_instance.to_dict()
# create an instance of ArrayOfFaultToleranceMetaSpec from a dict
array_of_fault_tolerance_meta_spec_form_dict = array_of_fault_tolerance_meta_spec.from_dict(array_of_fault_tolerance_meta_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


