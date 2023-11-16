# ProfileEventArgument

The event argument is a Profile object  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**name** | **str** |  | 

## Example

```python
from vmware_vi.models.profile_event_argument import ProfileEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileEventArgument from a JSON string
profile_event_argument_instance = ProfileEventArgument.from_json(json)
# print the JSON string representation of the object
print ProfileEventArgument.to_json()

# convert the object into a dict
profile_event_argument_dict = profile_event_argument_instance.to_dict()
# create an instance of ProfileEventArgument from a dict
profile_event_argument_form_dict = profile_event_argument.from_dict(profile_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


