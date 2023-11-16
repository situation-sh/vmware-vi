# ChangesInfoEventArgument

The event argument contains changes.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modified** | **str** | Modified properties.  ***Since:*** vSphere API 6.5  | [optional] 
**added** | **str** | Added properties.  ***Since:*** vSphere API 6.5  | [optional] 
**deleted** | **str** | Deleted properties.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.changes_info_event_argument import ChangesInfoEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ChangesInfoEventArgument from a JSON string
changes_info_event_argument_instance = ChangesInfoEventArgument.from_json(json)
# print the JSON string representation of the object
print ChangesInfoEventArgument.to_json()

# convert the object into a dict
changes_info_event_argument_dict = changes_info_event_argument_instance.to_dict()
# create an instance of ChangesInfoEventArgument from a dict
changes_info_event_argument_form_dict = changes_info_event_argument.from_dict(changes_info_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


