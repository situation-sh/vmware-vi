# MarkAsSsdRequestType

The parameters of *HostStorageSystem.MarkAsSsd_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scsi_disk_uuid** | **str** | The SCSI disk UUID.  | 

## Example

```python
from vmware_vi.models.mark_as_ssd_request_type import MarkAsSsdRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAsSsdRequestType from a JSON string
mark_as_ssd_request_type_instance = MarkAsSsdRequestType.from_json(json)
# print the JSON string representation of the object
print MarkAsSsdRequestType.to_json()

# convert the object into a dict
mark_as_ssd_request_type_dict = mark_as_ssd_request_type_instance.to_dict()
# create an instance of MarkAsSsdRequestType from a dict
mark_as_ssd_request_type_form_dict = mark_as_ssd_request_type.from_dict(mark_as_ssd_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


