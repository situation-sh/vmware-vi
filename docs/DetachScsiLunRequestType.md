# DetachScsiLunRequestType

The parameters of *HostStorageSystem.DetachScsiLun*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_uuid** | **str** | The uuid of the ScsiLun device to detach.  | 

## Example

```python
from vmware_vi.models.detach_scsi_lun_request_type import DetachScsiLunRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DetachScsiLunRequestType from a JSON string
detach_scsi_lun_request_type_instance = DetachScsiLunRequestType.from_json(json)
# print the JSON string representation of the object
print DetachScsiLunRequestType.to_json()

# convert the object into a dict
detach_scsi_lun_request_type_dict = detach_scsi_lun_request_type_instance.to_dict()
# create an instance of DetachScsiLunRequestType from a dict
detach_scsi_lun_request_type_form_dict = detach_scsi_lun_request_type.from_dict(detach_scsi_lun_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


