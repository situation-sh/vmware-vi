# VMINotSupported

The virtual machine is configured to use a VMI ROM, which is not supported on the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vmi_not_supported import VMINotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of VMINotSupported from a JSON string
vmi_not_supported_instance = VMINotSupported.from_json(json)
# print the JSON string representation of the object
print VMINotSupported.to_json()

# convert the object into a dict
vmi_not_supported_dict = vmi_not_supported_instance.to_dict()
# create an instance of VMINotSupported from a dict
vmi_not_supported_form_dict = vmi_not_supported.from_dict(vmi_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


