# DetachScsiLunExRequestType

The parameters of *HostStorageSystem.DetachScsiLunEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_uuid** | **List[str]** | each element specifies UUID of LUN to be detached.  | 

## Example

```python
from vmware_vi.models.detach_scsi_lun_ex_request_type import DetachScsiLunExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DetachScsiLunExRequestType from a JSON string
detach_scsi_lun_ex_request_type_instance = DetachScsiLunExRequestType.from_json(json)
# print the JSON string representation of the object
print DetachScsiLunExRequestType.to_json()

# convert the object into a dict
detach_scsi_lun_ex_request_type_dict = detach_scsi_lun_ex_request_type_instance.to_dict()
# create an instance of DetachScsiLunExRequestType from a dict
detach_scsi_lun_ex_request_type_form_dict = detach_scsi_lun_ex_request_type.from_dict(detach_scsi_lun_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


