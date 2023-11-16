# QueryConfigOptionRequestType

The parameters of *EnvironmentBrowser.QueryConfigOption*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key found in the VirtualMachineConfigOptionDescriptor, obtained by invoking the *EnvironmentBrowser.QueryConfigOptionDescriptor* operation.  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_config_option_request_type import QueryConfigOptionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryConfigOptionRequestType from a JSON string
query_config_option_request_type_instance = QueryConfigOptionRequestType.from_json(json)
# print the JSON string representation of the object
print QueryConfigOptionRequestType.to_json()

# convert the object into a dict
query_config_option_request_type_dict = query_config_option_request_type_instance.to_dict()
# create an instance of QueryConfigOptionRequestType from a dict
query_config_option_request_type_form_dict = query_config_option_request_type.from_dict(query_config_option_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


