# ArrayOfInvalidVmConfig

A boxed array of *InvalidVmConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidVmConfig]**](InvalidVmConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_vm_config import ArrayOfInvalidVmConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidVmConfig from a JSON string
array_of_invalid_vm_config_instance = ArrayOfInvalidVmConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidVmConfig.to_json()

# convert the object into a dict
array_of_invalid_vm_config_dict = array_of_invalid_vm_config_instance.to_dict()
# create an instance of ArrayOfInvalidVmConfig from a dict
array_of_invalid_vm_config_form_dict = array_of_invalid_vm_config.from_dict(array_of_invalid_vm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


