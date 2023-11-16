# DeleteScsiLunStateRequestType

The parameters of *HostStorageSystem.DeleteScsiLunState*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_canonical_name** | **str** | The &#39;canonicalName&#39; of the ScsiLun whose state needs to be deleted.  | 

## Example

```python
from vmware_vi.models.delete_scsi_lun_state_request_type import DeleteScsiLunStateRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteScsiLunStateRequestType from a JSON string
delete_scsi_lun_state_request_type_instance = DeleteScsiLunStateRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteScsiLunStateRequestType.to_json()

# convert the object into a dict
delete_scsi_lun_state_request_type_dict = delete_scsi_lun_state_request_type_instance.to_dict()
# create an instance of DeleteScsiLunStateRequestType from a dict
delete_scsi_lun_state_request_type_form_dict = delete_scsi_lun_state_request_type.from_dict(delete_scsi_lun_state_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


