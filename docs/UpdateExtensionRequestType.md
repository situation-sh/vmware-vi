# UpdateExtensionRequestType

The parameters of *ExtensionManager.UpdateExtension*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension** | [**Extension**](Extension.md) |  | 

## Example

```python
from vmware_vi.models.update_extension_request_type import UpdateExtensionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExtensionRequestType from a JSON string
update_extension_request_type_instance = UpdateExtensionRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateExtensionRequestType.to_json()

# convert the object into a dict
update_extension_request_type_dict = update_extension_request_type_instance.to_dict()
# create an instance of UpdateExtensionRequestType from a dict
update_extension_request_type_form_dict = update_extension_request_type.from_dict(update_extension_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


