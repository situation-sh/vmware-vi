# ArrayOfFaultToleranceConfigSpec

A boxed array of *FaultToleranceConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FaultToleranceConfigSpec]**](FaultToleranceConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_fault_tolerance_config_spec import ArrayOfFaultToleranceConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFaultToleranceConfigSpec from a JSON string
array_of_fault_tolerance_config_spec_instance = ArrayOfFaultToleranceConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfFaultToleranceConfigSpec.to_json()

# convert the object into a dict
array_of_fault_tolerance_config_spec_dict = array_of_fault_tolerance_config_spec_instance.to_dict()
# create an instance of ArrayOfFaultToleranceConfigSpec from a dict
array_of_fault_tolerance_config_spec_form_dict = array_of_fault_tolerance_config_spec.from_dict(array_of_fault_tolerance_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


