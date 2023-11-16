# RemoveMonitoredEntitiesRequestType

The parameters of *HealthUpdateManager.RemoveMonitoredEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider id.  | 
**entities** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The entities that are no longer monitored by this provider.  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.remove_monitored_entities_request_type import RemoveMonitoredEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveMonitoredEntitiesRequestType from a JSON string
remove_monitored_entities_request_type_instance = RemoveMonitoredEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveMonitoredEntitiesRequestType.to_json()

# convert the object into a dict
remove_monitored_entities_request_type_dict = remove_monitored_entities_request_type_instance.to_dict()
# create an instance of RemoveMonitoredEntitiesRequestType from a dict
remove_monitored_entities_request_type_form_dict = remove_monitored_entities_request_type.from_dict(remove_monitored_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


