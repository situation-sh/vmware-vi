# ArrayOfExtensionEventTypeInfo

A boxed array of *ExtensionEventTypeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExtensionEventTypeInfo]**](ExtensionEventTypeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_extension_event_type_info import ArrayOfExtensionEventTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtensionEventTypeInfo from a JSON string
array_of_extension_event_type_info_instance = ArrayOfExtensionEventTypeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtensionEventTypeInfo.to_json()

# convert the object into a dict
array_of_extension_event_type_info_dict = array_of_extension_event_type_info_instance.to_dict()
# create an instance of ArrayOfExtensionEventTypeInfo from a dict
array_of_extension_event_type_info_form_dict = array_of_extension_event_type_info.from_dict(array_of_extension_event_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


