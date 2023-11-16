# HostBootDevice

The *HostBootDevice* data object represents a boot device on the host system.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The identifier for the boot device.  ***Since:*** VI API 2.5  | 
**description** | **str** | The description of the boot device.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.host_boot_device import HostBootDevice

# TODO update the JSON string below
json = "{}"
# create an instance of HostBootDevice from a JSON string
host_boot_device_instance = HostBootDevice.from_json(json)
# print the JSON string representation of the object
print HostBootDevice.to_json()

# convert the object into a dict
host_boot_device_dict = host_boot_device_instance.to_dict()
# create an instance of HostBootDevice from a dict
host_boot_device_form_dict = host_boot_device.from_dict(host_boot_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


