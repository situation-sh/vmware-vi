# QueryConfiguredModuleOptionStringRequestType

The parameters of *HostKernelModuleSystem.QueryConfiguredModuleOptionString*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Module name.  | 

## Example

```python
from vmware_vi.models.query_configured_module_option_string_request_type import QueryConfiguredModuleOptionStringRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryConfiguredModuleOptionStringRequestType from a JSON string
query_configured_module_option_string_request_type_instance = QueryConfiguredModuleOptionStringRequestType.from_json(json)
# print the JSON string representation of the object
print QueryConfiguredModuleOptionStringRequestType.to_json()

# convert the object into a dict
query_configured_module_option_string_request_type_dict = query_configured_module_option_string_request_type_instance.to_dict()
# create an instance of QueryConfiguredModuleOptionStringRequestType from a dict
query_configured_module_option_string_request_type_form_dict = query_configured_module_option_string_request_type.from_dict(query_configured_module_option_string_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


