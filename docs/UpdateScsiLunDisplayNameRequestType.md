# UpdateScsiLunDisplayNameRequestType

The parameters of *HostStorageSystem.UpdateScsiLunDisplayName*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_uuid** | **str** | The uuid of the ScsiLun to update.  | 
**display_name** | **str** | The new name to assign to the ScsiLun object.  | 

## Example

```python
from vmware_vi.models.update_scsi_lun_display_name_request_type import UpdateScsiLunDisplayNameRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScsiLunDisplayNameRequestType from a JSON string
update_scsi_lun_display_name_request_type_instance = UpdateScsiLunDisplayNameRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateScsiLunDisplayNameRequestType.to_json()

# convert the object into a dict
update_scsi_lun_display_name_request_type_dict = update_scsi_lun_display_name_request_type_instance.to_dict()
# create an instance of UpdateScsiLunDisplayNameRequestType from a dict
update_scsi_lun_display_name_request_type_form_dict = update_scsi_lun_display_name_request_type.from_dict(update_scsi_lun_display_name_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


