# QueryFilterEntitiesRequestType

The parameters of *HealthUpdateManager.QueryFilterEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** | The filter id.  | 

## Example

```python
from vmware_vi.models.query_filter_entities_request_type import QueryFilterEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFilterEntitiesRequestType from a JSON string
query_filter_entities_request_type_instance = QueryFilterEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print QueryFilterEntitiesRequestType.to_json()

# convert the object into a dict
query_filter_entities_request_type_dict = query_filter_entities_request_type_instance.to_dict()
# create an instance of QueryFilterEntitiesRequestType from a dict
query_filter_entities_request_type_form_dict = query_filter_entities_request_type.from_dict(query_filter_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


