# ToolsImageCopyFailed

Thrown when the tools image couldn't be copied to the guest operating system: disk out of space, file access error, etc.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.tools_image_copy_failed import ToolsImageCopyFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsImageCopyFailed from a JSON string
tools_image_copy_failed_instance = ToolsImageCopyFailed.from_json(json)
# print the JSON string representation of the object
print ToolsImageCopyFailed.to_json()

# convert the object into a dict
tools_image_copy_failed_dict = tools_image_copy_failed_instance.to_dict()
# create an instance of ToolsImageCopyFailed from a dict
tools_image_copy_failed_form_dict = tools_image_copy_failed.from_dict(tools_image_copy_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


