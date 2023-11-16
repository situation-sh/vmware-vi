# InvalidVmConfig

Thrown when virtual machine creation or configuration fails.  This is a base type for all virtual machine configuration errors. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Path of the property in configSpec that has an invalid value.  | [optional] 

## Example

```python
from vmware_vi.models.invalid_vm_config import InvalidVmConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidVmConfig from a JSON string
invalid_vm_config_instance = InvalidVmConfig.from_json(json)
# print the JSON string representation of the object
print InvalidVmConfig.to_json()

# convert the object into a dict
invalid_vm_config_dict = invalid_vm_config_instance.to_dict()
# create an instance of InvalidVmConfig from a dict
invalid_vm_config_form_dict = invalid_vm_config.from_dict(invalid_vm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


