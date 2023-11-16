# UpdateModuleOptionStringRequestType

The parameters of *HostKernelModuleSystem.UpdateModuleOptionString*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Module name.  | 
**options** | **str** | Option string to be passed to the kernel module at load time.  | 

## Example

```python
from vmware_vi.models.update_module_option_string_request_type import UpdateModuleOptionStringRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateModuleOptionStringRequestType from a JSON string
update_module_option_string_request_type_instance = UpdateModuleOptionStringRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateModuleOptionStringRequestType.to_json()

# convert the object into a dict
update_module_option_string_request_type_dict = update_module_option_string_request_type_instance.to_dict()
# create an instance of UpdateModuleOptionStringRequestType from a dict
update_module_option_string_request_type_form_dict = update_module_option_string_request_type.from_dict(update_module_option_string_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


