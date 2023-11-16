# NotSupported

Thrown if the method is not supported on the server.  Not all methods are supported on all servers (for example, an ESX Server host supports less functionality than a VirtualCenter server). A feature might also be disabled due to missing liceneses. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.not_supported import NotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of NotSupported from a JSON string
not_supported_instance = NotSupported.from_json(json)
# print the JSON string representation of the object
print NotSupported.to_json()

# convert the object into a dict
not_supported_dict = not_supported_instance.to_dict()
# create an instance of NotSupported from a dict
not_supported_form_dict = not_supported.from_dict(not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


