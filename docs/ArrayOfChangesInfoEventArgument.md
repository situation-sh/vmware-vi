# ArrayOfChangesInfoEventArgument

A boxed array of *ChangesInfoEventArgument*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ChangesInfoEventArgument]**](ChangesInfoEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.array_of_changes_info_event_argument import ArrayOfChangesInfoEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfChangesInfoEventArgument from a JSON string
array_of_changes_info_event_argument_instance = ArrayOfChangesInfoEventArgument.from_json(json)
# print the JSON string representation of the object
print ArrayOfChangesInfoEventArgument.to_json()

# convert the object into a dict
array_of_changes_info_event_argument_dict = array_of_changes_info_event_argument_instance.to_dict()
# create an instance of ArrayOfChangesInfoEventArgument from a dict
array_of_changes_info_event_argument_form_dict = array_of_changes_info_event_argument.from_dict(array_of_changes_info_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


