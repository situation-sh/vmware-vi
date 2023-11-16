# QueryConfigOptionExRequestType

The parameters of *EnvironmentBrowser.QueryConfigOptionEx*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**EnvironmentBrowserConfigOptionQuerySpec**](EnvironmentBrowserConfigOptionQuerySpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_config_option_ex_request_type import QueryConfigOptionExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryConfigOptionExRequestType from a JSON string
query_config_option_ex_request_type_instance = QueryConfigOptionExRequestType.from_json(json)
# print the JSON string representation of the object
print QueryConfigOptionExRequestType.to_json()

# convert the object into a dict
query_config_option_ex_request_type_dict = query_config_option_ex_request_type_instance.to_dict()
# create an instance of QueryConfigOptionExRequestType from a dict
query_config_option_ex_request_type_form_dict = query_config_option_ex_request_type.from_dict(query_config_option_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


