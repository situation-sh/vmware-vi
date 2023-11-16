# CannotAccessVmConfig

One or more of the virtual machine's configuration files are not accessible. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.cannot_access_vm_config import CannotAccessVmConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CannotAccessVmConfig from a JSON string
cannot_access_vm_config_instance = CannotAccessVmConfig.from_json(json)
# print the JSON string representation of the object
print CannotAccessVmConfig.to_json()

# convert the object into a dict
cannot_access_vm_config_dict = cannot_access_vm_config_instance.to_dict()
# create an instance of CannotAccessVmConfig from a dict
cannot_access_vm_config_form_dict = cannot_access_vm_config.from_dict(cannot_access_vm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


