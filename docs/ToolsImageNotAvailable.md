# ToolsImageNotAvailable

Thrown when tools install or upgrade fails because the required tools image is not available.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.tools_image_not_available import ToolsImageNotAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsImageNotAvailable from a JSON string
tools_image_not_available_instance = ToolsImageNotAvailable.from_json(json)
# print the JSON string representation of the object
print ToolsImageNotAvailable.to_json()

# convert the object into a dict
tools_image_not_available_dict = tools_image_not_available_instance.to_dict()
# create an instance of ToolsImageNotAvailable from a dict
tools_image_not_available_form_dict = tools_image_not_available.from_dict(tools_image_not_available_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


