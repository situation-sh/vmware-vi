# QueryMonitoredEntitiesRequestType

The parameters of *HealthUpdateManager.QueryMonitoredEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider id.  | 

## Example

```python
from vmware_vi.models.query_monitored_entities_request_type import QueryMonitoredEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMonitoredEntitiesRequestType from a JSON string
query_monitored_entities_request_type_instance = QueryMonitoredEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print QueryMonitoredEntitiesRequestType.to_json()

# convert the object into a dict
query_monitored_entities_request_type_dict = query_monitored_entities_request_type_instance.to_dict()
# create an instance of QueryMonitoredEntitiesRequestType from a dict
query_monitored_entities_request_type_form_dict = query_monitored_entities_request_type.from_dict(query_monitored_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


