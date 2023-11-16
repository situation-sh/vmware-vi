# RegisterExtensionRequestType

The parameters of *ExtensionManager.RegisterExtension*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension** | [**Extension**](Extension.md) |  | 

## Example

```python
from vmware_vi.models.register_extension_request_type import RegisterExtensionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterExtensionRequestType from a JSON string
register_extension_request_type_instance = RegisterExtensionRequestType.from_json(json)
# print the JSON string representation of the object
print RegisterExtensionRequestType.to_json()

# convert the object into a dict
register_extension_request_type_dict = register_extension_request_type_instance.to_dict()
# create an instance of RegisterExtensionRequestType from a dict
register_extension_request_type_form_dict = register_extension_request_type.from_dict(register_extension_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


