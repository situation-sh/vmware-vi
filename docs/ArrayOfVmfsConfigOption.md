# ArrayOfVmfsConfigOption

A boxed array of *VmfsConfigOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmfsConfigOption]**](VmfsConfigOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmfs_config_option import ArrayOfVmfsConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmfsConfigOption from a JSON string
array_of_vmfs_config_option_instance = ArrayOfVmfsConfigOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmfsConfigOption.to_json()

# convert the object into a dict
array_of_vmfs_config_option_dict = array_of_vmfs_config_option_instance.to_dict()
# create an instance of ArrayOfVmfsConfigOption from a dict
array_of_vmfs_config_option_form_dict = array_of_vmfs_config_option.from_dict(array_of_vmfs_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


