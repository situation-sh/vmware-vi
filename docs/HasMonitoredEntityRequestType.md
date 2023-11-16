# HasMonitoredEntityRequestType

The parameters of *HealthUpdateManager.HasMonitoredEntity*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider id.  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.has_monitored_entity_request_type import HasMonitoredEntityRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HasMonitoredEntityRequestType from a JSON string
has_monitored_entity_request_type_instance = HasMonitoredEntityRequestType.from_json(json)
# print the JSON string representation of the object
print HasMonitoredEntityRequestType.to_json()

# convert the object into a dict
has_monitored_entity_request_type_dict = has_monitored_entity_request_type_instance.to_dict()
# create an instance of HasMonitoredEntityRequestType from a dict
has_monitored_entity_request_type_form_dict = has_monitored_entity_request_type.from_dict(has_monitored_entity_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


