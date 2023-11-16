# ArrayOfScsiLun

A boxed array of *ScsiLun*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ScsiLun]**](ScsiLun.md) |  | 

## Example

```python
from vmware_vi.models.array_of_scsi_lun import ArrayOfScsiLun

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfScsiLun from a JSON string
array_of_scsi_lun_instance = ArrayOfScsiLun.from_json(json)
# print the JSON string representation of the object
print ArrayOfScsiLun.to_json()

# convert the object into a dict
array_of_scsi_lun_dict = array_of_scsi_lun_instance.to_dict()
# create an instance of ArrayOfScsiLun from a dict
array_of_scsi_lun_form_dict = array_of_scsi_lun.from_dict(array_of_scsi_lun_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


