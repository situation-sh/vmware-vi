# QueryDescriptionsRequestType

The parameters of *DiagnosticManager.QueryDescriptions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_descriptions_request_type import QueryDescriptionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDescriptionsRequestType from a JSON string
query_descriptions_request_type_instance = QueryDescriptionsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryDescriptionsRequestType.to_json()

# convert the object into a dict
query_descriptions_request_type_dict = query_descriptions_request_type_instance.to_dict()
# create an instance of QueryDescriptionsRequestType from a dict
query_descriptions_request_type_form_dict = query_descriptions_request_type.from_dict(query_descriptions_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


