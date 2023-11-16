# ArrayOfCannotAccessVmConfig

A boxed array of *CannotAccessVmConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CannotAccessVmConfig]**](CannotAccessVmConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cannot_access_vm_config import ArrayOfCannotAccessVmConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCannotAccessVmConfig from a JSON string
array_of_cannot_access_vm_config_instance = ArrayOfCannotAccessVmConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfCannotAccessVmConfig.to_json()

# convert the object into a dict
array_of_cannot_access_vm_config_dict = array_of_cannot_access_vm_config_instance.to_dict()
# create an instance of ArrayOfCannotAccessVmConfig from a dict
array_of_cannot_access_vm_config_form_dict = array_of_cannot_access_vm_config.from_dict(array_of_cannot_access_vm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


