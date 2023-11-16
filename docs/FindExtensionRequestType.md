# FindExtensionRequestType

The parameters of *ExtensionManager.FindExtension*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | Key to search for.  | 

## Example

```python
from vmware_vi.models.find_extension_request_type import FindExtensionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindExtensionRequestType from a JSON string
find_extension_request_type_instance = FindExtensionRequestType.from_json(json)
# print the JSON string representation of the object
print FindExtensionRequestType.to_json()

# convert the object into a dict
find_extension_request_type_dict = find_extension_request_type_instance.to_dict()
# create an instance of FindExtensionRequestType from a dict
find_extension_request_type_form_dict = find_extension_request_type.from_dict(find_extension_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


