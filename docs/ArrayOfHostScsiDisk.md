# ArrayOfHostScsiDisk

A boxed array of *HostScsiDisk*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostScsiDisk]**](HostScsiDisk.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_scsi_disk import ArrayOfHostScsiDisk

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostScsiDisk from a JSON string
array_of_host_scsi_disk_instance = ArrayOfHostScsiDisk.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostScsiDisk.to_json()

# convert the object into a dict
array_of_host_scsi_disk_dict = array_of_host_scsi_disk_instance.to_dict()
# create an instance of ArrayOfHostScsiDisk from a dict
array_of_host_scsi_disk_form_dict = array_of_host_scsi_disk.from_dict(array_of_host_scsi_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


