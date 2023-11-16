# MarkAsNonSsdRequestType

The parameters of *HostStorageSystem.MarkAsNonSsd_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scsi_disk_uuid** | **str** | The SCSI disk UUID.  | 

## Example

```python
from vmware_vi.models.mark_as_non_ssd_request_type import MarkAsNonSsdRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAsNonSsdRequestType from a JSON string
mark_as_non_ssd_request_type_instance = MarkAsNonSsdRequestType.from_json(json)
# print the JSON string representation of the object
print MarkAsNonSsdRequestType.to_json()

# convert the object into a dict
mark_as_non_ssd_request_type_dict = mark_as_non_ssd_request_type_instance.to_dict()
# create an instance of MarkAsNonSsdRequestType from a dict
mark_as_non_ssd_request_type_form_dict = mark_as_non_ssd_request_type.from_dict(mark_as_non_ssd_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


