# ArrayOfFaultToleranceVMConfigSpec

A boxed array of *FaultToleranceVMConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FaultToleranceVMConfigSpec]**](FaultToleranceVMConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_fault_tolerance_vm_config_spec import ArrayOfFaultToleranceVMConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFaultToleranceVMConfigSpec from a JSON string
array_of_fault_tolerance_vm_config_spec_instance = ArrayOfFaultToleranceVMConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfFaultToleranceVMConfigSpec.to_json()

# convert the object into a dict
array_of_fault_tolerance_vm_config_spec_dict = array_of_fault_tolerance_vm_config_spec_instance.to_dict()
# create an instance of ArrayOfFaultToleranceVMConfigSpec from a dict
array_of_fault_tolerance_vm_config_spec_form_dict = array_of_fault_tolerance_vm_config_spec.from_dict(array_of_fault_tolerance_vm_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


