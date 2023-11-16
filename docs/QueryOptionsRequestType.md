# QueryOptionsRequestType

The parameters of *OptionManager.QueryOptions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.query_options_request_type import QueryOptionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryOptionsRequestType from a JSON string
query_options_request_type_instance = QueryOptionsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryOptionsRequestType.to_json()

# convert the object into a dict
query_options_request_type_dict = query_options_request_type_instance.to_dict()
# create an instance of QueryOptionsRequestType from a dict
query_options_request_type_form_dict = query_options_request_type.from_dict(query_options_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


