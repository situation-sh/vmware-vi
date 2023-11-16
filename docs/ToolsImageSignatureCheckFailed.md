# ToolsImageSignatureCheckFailed

Thrown when tools install or upgrade fails because the signature check on the tools image failed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.tools_image_signature_check_failed import ToolsImageSignatureCheckFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsImageSignatureCheckFailed from a JSON string
tools_image_signature_check_failed_instance = ToolsImageSignatureCheckFailed.from_json(json)
# print the JSON string representation of the object
print ToolsImageSignatureCheckFailed.to_json()

# convert the object into a dict
tools_image_signature_check_failed_dict = tools_image_signature_check_failed_instance.to_dict()
# create an instance of ToolsImageSignatureCheckFailed from a dict
tools_image_signature_check_failed_form_dict = tools_image_signature_check_failed.from_dict(tools_image_signature_check_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


