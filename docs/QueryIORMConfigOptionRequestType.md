# QueryIORMConfigOptionRequestType

The parameters of *StorageResourceManager.QueryIORMConfigOption*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_iorm_config_option_request_type import QueryIORMConfigOptionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryIORMConfigOptionRequestType from a JSON string
query_iorm_config_option_request_type_instance = QueryIORMConfigOptionRequestType.from_json(json)
# print the JSON string representation of the object
print QueryIORMConfigOptionRequestType.to_json()

# convert the object into a dict
query_iorm_config_option_request_type_dict = query_iorm_config_option_request_type_instance.to_dict()
# create an instance of QueryIORMConfigOptionRequestType from a dict
query_iorm_config_option_request_type_form_dict = query_iorm_config_option_request_type.from_dict(query_iorm_config_option_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


