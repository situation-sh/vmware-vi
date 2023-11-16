# AddMonitoredEntitiesRequestType

The parameters of *HealthUpdateManager.AddMonitoredEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider id.  | 
**entities** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The entities that are newly monitored by this provider.  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.add_monitored_entities_request_type import AddMonitoredEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddMonitoredEntitiesRequestType from a JSON string
add_monitored_entities_request_type_instance = AddMonitoredEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print AddMonitoredEntitiesRequestType.to_json()

# convert the object into a dict
add_monitored_entities_request_type_dict = add_monitored_entities_request_type_instance.to_dict()
# create an instance of AddMonitoredEntitiesRequestType from a dict
add_monitored_entities_request_type_form_dict = add_monitored_entities_request_type.from_dict(add_monitored_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


