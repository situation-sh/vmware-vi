# ArrayOfVirtualDiskConfigSpec

A boxed array of *VirtualDiskConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDiskConfigSpec]**](VirtualDiskConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_disk_config_spec import ArrayOfVirtualDiskConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDiskConfigSpec from a JSON string
array_of_virtual_disk_config_spec_instance = ArrayOfVirtualDiskConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDiskConfigSpec.to_json()

# convert the object into a dict
array_of_virtual_disk_config_spec_dict = array_of_virtual_disk_config_spec_instance.to_dict()
# create an instance of ArrayOfVirtualDiskConfigSpec from a dict
array_of_virtual_disk_config_spec_form_dict = array_of_virtual_disk_config_spec.from_dict(array_of_virtual_disk_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


