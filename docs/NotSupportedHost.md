# NotSupportedHost

A NotSupportedHostFault occurs when the host is of a type that is not supported. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name** | **str** | The name of the unsupported product if available; for example, \&quot;VMware ESX Server\&quot;.  | [optional] 
**product_version** | **str** | The version of the unsupported product; for example, \&quot;1.5.2\&quot;  | [optional] 

## Example

```python
from vmware_vi.models.not_supported_host import NotSupportedHost

# TODO update the JSON string below
json = "{}"
# create an instance of NotSupportedHost from a JSON string
not_supported_host_instance = NotSupportedHost.from_json(json)
# print the JSON string representation of the object
print NotSupportedHost.to_json()

# convert the object into a dict
not_supported_host_dict = not_supported_host_instance.to_dict()
# create an instance of NotSupportedHost from a dict
not_supported_host_form_dict = not_supported_host.from_dict(not_supported_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


