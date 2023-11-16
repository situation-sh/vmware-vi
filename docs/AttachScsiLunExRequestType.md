# AttachScsiLunExRequestType

The parameters of *HostStorageSystem.AttachScsiLunEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_uuid** | **List[str]** | each element specifies UUID of LUN to be attached.  | 

## Example

```python
from vmware_vi.models.attach_scsi_lun_ex_request_type import AttachScsiLunExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AttachScsiLunExRequestType from a JSON string
attach_scsi_lun_ex_request_type_instance = AttachScsiLunExRequestType.from_json(json)
# print the JSON string representation of the object
print AttachScsiLunExRequestType.to_json()

# convert the object into a dict
attach_scsi_lun_ex_request_type_dict = attach_scsi_lun_ex_request_type_instance.to_dict()
# create an instance of AttachScsiLunExRequestType from a dict
attach_scsi_lun_ex_request_type_form_dict = attach_scsi_lun_ex_request_type.from_dict(attach_scsi_lun_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


