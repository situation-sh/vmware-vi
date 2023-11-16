# VirtualMachineRelocateTransformation

A boxed *VirtualMachineRelocateTransformation_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualMachineRelocateTransformationEnum**](VirtualMachineRelocateTransformationEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_relocate_transformation import VirtualMachineRelocateTransformation

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineRelocateTransformation from a JSON string
virtual_machine_relocate_transformation_instance = VirtualMachineRelocateTransformation.from_json(json)
# print the JSON string representation of the object
print VirtualMachineRelocateTransformation.to_json()

# convert the object into a dict
virtual_machine_relocate_transformation_dict = virtual_machine_relocate_transformation_instance.to_dict()
# create an instance of VirtualMachineRelocateTransformation from a dict
virtual_machine_relocate_transformation_form_dict = virtual_machine_relocate_transformation.from_dict(virtual_machine_relocate_transformation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


