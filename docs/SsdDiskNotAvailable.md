# SsdDiskNotAvailable

A SsdDiskNotAvailable fault indicating that the specified SSD disk is not available.  The disk either has been used or not a SSD disk.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **str** | The device path of the disk.  See also *HostScsiDisk.devicePath*.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.ssd_disk_not_available import SsdDiskNotAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of SsdDiskNotAvailable from a JSON string
ssd_disk_not_available_instance = SsdDiskNotAvailable.from_json(json)
# print the JSON string representation of the object
print SsdDiskNotAvailable.to_json()

# convert the object into a dict
ssd_disk_not_available_dict = ssd_disk_not_available_instance.to_dict()
# create an instance of SsdDiskNotAvailable from a dict
ssd_disk_not_available_form_dict = ssd_disk_not_available.from_dict(ssd_disk_not_available_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


