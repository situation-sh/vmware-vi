# ArrayOfVirtualMachineFeatureRequirement

A boxed array of *VirtualMachineFeatureRequirement*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineFeatureRequirement]**](VirtualMachineFeatureRequirement.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_feature_requirement import ArrayOfVirtualMachineFeatureRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineFeatureRequirement from a JSON string
array_of_virtual_machine_feature_requirement_instance = ArrayOfVirtualMachineFeatureRequirement.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineFeatureRequirement.to_json()

# convert the object into a dict
array_of_virtual_machine_feature_requirement_dict = array_of_virtual_machine_feature_requirement_instance.to_dict()
# create an instance of ArrayOfVirtualMachineFeatureRequirement from a dict
array_of_virtual_machine_feature_requirement_form_dict = array_of_virtual_machine_feature_requirement.from_dict(array_of_virtual_machine_feature_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


