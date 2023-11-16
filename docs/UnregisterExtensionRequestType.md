# UnregisterExtensionRequestType

The parameters of *ExtensionManager.UnregisterExtension*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | Unique name of extension to unregister.  | 

## Example

```python
from vmware_vi.models.unregister_extension_request_type import UnregisterExtensionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterExtensionRequestType from a JSON string
unregister_extension_request_type_instance = UnregisterExtensionRequestType.from_json(json)
# print the JSON string representation of the object
print UnregisterExtensionRequestType.to_json()

# convert the object into a dict
unregister_extension_request_type_dict = unregister_extension_request_type_instance.to_dict()
# create an instance of UnregisterExtensionRequestType from a dict
unregister_extension_request_type_form_dict = unregister_extension_request_type.from_dict(unregister_extension_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


