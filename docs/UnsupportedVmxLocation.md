# UnsupportedVmxLocation

ESX 3 Server products requires the .vmx file to be stored on NAS or VMFS3 storage.  If attempting to power on a virtual machine with the .vmx file stored on the service console, this fault will be thrown. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.unsupported_vmx_location import UnsupportedVmxLocation

# TODO update the JSON string below
json = "{}"
# create an instance of UnsupportedVmxLocation from a JSON string
unsupported_vmx_location_instance = UnsupportedVmxLocation.from_json(json)
# print the JSON string representation of the object
print UnsupportedVmxLocation.to_json()

# convert the object into a dict
unsupported_vmx_location_dict = unsupported_vmx_location_instance.to_dict()
# create an instance of UnsupportedVmxLocation from a dict
unsupported_vmx_location_form_dict = unsupported_vmx_location.from_dict(unsupported_vmx_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


