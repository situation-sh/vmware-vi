# AttachScsiLunRequestType

The parameters of *HostStorageSystem.AttachScsiLun*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_uuid** | **str** | The uuid of the ScsiLun to update.  | 

## Example

```python
from vmware_vi.models.attach_scsi_lun_request_type import AttachScsiLunRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AttachScsiLunRequestType from a JSON string
attach_scsi_lun_request_type_instance = AttachScsiLunRequestType.from_json(json)
# print the JSON string representation of the object
print AttachScsiLunRequestType.to_json()

# convert the object into a dict
attach_scsi_lun_request_type_dict = attach_scsi_lun_request_type_instance.to_dict()
# create an instance of AttachScsiLunRequestType from a dict
attach_scsi_lun_request_type_form_dict = attach_scsi_lun_request_type.from_dict(attach_scsi_lun_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


