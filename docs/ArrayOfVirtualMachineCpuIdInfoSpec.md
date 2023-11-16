# ArrayOfVirtualMachineCpuIdInfoSpec

A boxed array of *VirtualMachineCpuIdInfoSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineCpuIdInfoSpec]**](VirtualMachineCpuIdInfoSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_cpu_id_info_spec import ArrayOfVirtualMachineCpuIdInfoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineCpuIdInfoSpec from a JSON string
array_of_virtual_machine_cpu_id_info_spec_instance = ArrayOfVirtualMachineCpuIdInfoSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineCpuIdInfoSpec.to_json()

# convert the object into a dict
array_of_virtual_machine_cpu_id_info_spec_dict = array_of_virtual_machine_cpu_id_info_spec_instance.to_dict()
# create an instance of ArrayOfVirtualMachineCpuIdInfoSpec from a dict
array_of_virtual_machine_cpu_id_info_spec_form_dict = array_of_virtual_machine_cpu_id_info_spec.from_dict(array_of_virtual_machine_cpu_id_info_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


