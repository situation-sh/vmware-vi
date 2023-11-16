# InvalidDeviceSpec

An InvalidDeviceSpec exception is thrown if a virtual machine creation or configuration fails because a device specification contains an invalid value. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_index** | **int** | Index of the device in the configuration specification that has the invalid value.  | 

## Example

```python
from vmware_vi.models.invalid_device_spec import InvalidDeviceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDeviceSpec from a JSON string
invalid_device_spec_instance = InvalidDeviceSpec.from_json(json)
# print the JSON string representation of the object
print InvalidDeviceSpec.to_json()

# convert the object into a dict
invalid_device_spec_dict = invalid_device_spec_instance.to_dict()
# create an instance of InvalidDeviceSpec from a dict
invalid_device_spec_form_dict = invalid_device_spec.from_dict(invalid_device_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


