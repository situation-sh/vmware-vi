# ExtensionResourceInfo

This data object encapsulates the message resources for all locales.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | 
**module** | **str** | Module for a resource type and other message or fault resources.  Examples: \&quot;task\&quot; for task, \&quot;event\&quot; for event and \&quot;auth\&quot; for \&quot;privilege\&quot;.  ***Since:*** VI API 2.5  | 
**data** | [**List[KeyValue]**](KeyValue.md) |  | 

## Example

```python
from vmware_vi.models.extension_resource_info import ExtensionResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionResourceInfo from a JSON string
extension_resource_info_instance = ExtensionResourceInfo.from_json(json)
# print the JSON string representation of the object
print ExtensionResourceInfo.to_json()

# convert the object into a dict
extension_resource_info_dict = extension_resource_info_instance.to_dict()
# create an instance of ExtensionResourceInfo from a dict
extension_resource_info_form_dict = extension_resource_info.from_dict(extension_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


