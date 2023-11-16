# UpdateBootDeviceRequestType

The parameters of *HostBootDeviceSystem.UpdateBootDevice*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The *HostBootDevice.key* of the *HostBootDevice* from which the host will boot.  | 

## Example

```python
from vmware_vi.models.update_boot_device_request_type import UpdateBootDeviceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBootDeviceRequestType from a JSON string
update_boot_device_request_type_instance = UpdateBootDeviceRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateBootDeviceRequestType.to_json()

# convert the object into a dict
update_boot_device_request_type_dict = update_boot_device_request_type_instance.to_dict()
# create an instance of UpdateBootDeviceRequestType from a dict
update_boot_device_request_type_form_dict = update_boot_device_request_type.from_dict(update_boot_device_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


