# NoCompatibleHostWithAccessToDevice

This fault is used to report that a FT VM cannot be placed because there is no compatible host that can access all devices required to be connected when the VM powers on.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_compatible_host_with_access_to_device import NoCompatibleHostWithAccessToDevice

# TODO update the JSON string below
json = "{}"
# create an instance of NoCompatibleHostWithAccessToDevice from a JSON string
no_compatible_host_with_access_to_device_instance = NoCompatibleHostWithAccessToDevice.from_json(json)
# print the JSON string representation of the object
print NoCompatibleHostWithAccessToDevice.to_json()

# convert the object into a dict
no_compatible_host_with_access_to_device_dict = no_compatible_host_with_access_to_device_instance.to_dict()
# create an instance of NoCompatibleHostWithAccessToDevice from a dict
no_compatible_host_with_access_to_device_form_dict = no_compatible_host_with_access_to_device.from_dict(no_compatible_host_with_access_to_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


