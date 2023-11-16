# ExtensionTaskTypeInfo

This data object type describes task types defined by the extension.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | The ID of the task type.  Should follow java package naming conventions for uniqueness.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.extension_task_type_info import ExtensionTaskTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionTaskTypeInfo from a JSON string
extension_task_type_info_instance = ExtensionTaskTypeInfo.from_json(json)
# print the JSON string representation of the object
print ExtensionTaskTypeInfo.to_json()

# convert the object into a dict
extension_task_type_info_dict = extension_task_type_info_instance.to_dict()
# create an instance of ExtensionTaskTypeInfo from a dict
extension_task_type_info_form_dict = extension_task_type_info.from_dict(extension_task_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


