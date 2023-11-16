# PostHealthUpdatesRequestType

The parameters of *HealthUpdateManager.PostHealthUpdates*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider id.  | 
**updates** | [**List[HealthUpdate]**](HealthUpdate.md) | The changes in health states.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.post_health_updates_request_type import PostHealthUpdatesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PostHealthUpdatesRequestType from a JSON string
post_health_updates_request_type_instance = PostHealthUpdatesRequestType.from_json(json)
# print the JSON string representation of the object
print PostHealthUpdatesRequestType.to_json()

# convert the object into a dict
post_health_updates_request_type_dict = post_health_updates_request_type_instance.to_dict()
# create an instance of PostHealthUpdatesRequestType from a dict
post_health_updates_request_type_form_dict = post_health_updates_request_type.from_dict(post_health_updates_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


