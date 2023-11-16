# DiskIsUSB

Fault used for disks which are ineligible for VSAN because they are USB disks.  See also *HostVsanSystem.QueryDisksForVsan*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.disk_is_usb import DiskIsUSB

# TODO update the JSON string below
json = "{}"
# create an instance of DiskIsUSB from a JSON string
disk_is_usb_instance = DiskIsUSB.from_json(json)
# print the JSON string representation of the object
print DiskIsUSB.to_json()

# convert the object into a dict
disk_is_usb_dict = disk_is_usb_instance.to_dict()
# create an instance of DiskIsUSB from a dict
disk_is_usb_form_dict = disk_is_usb.from_dict(disk_is_usb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


