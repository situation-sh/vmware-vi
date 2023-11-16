# ArrayOfScsiLunDurableName

A boxed array of *ScsiLunDurableName*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ScsiLunDurableName]**](ScsiLunDurableName.md) |  | 

## Example

```python
from vmware_vi.models.array_of_scsi_lun_durable_name import ArrayOfScsiLunDurableName

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfScsiLunDurableName from a JSON string
array_of_scsi_lun_durable_name_instance = ArrayOfScsiLunDurableName.from_json(json)
# print the JSON string representation of the object
print ArrayOfScsiLunDurableName.to_json()

# convert the object into a dict
array_of_scsi_lun_durable_name_dict = array_of_scsi_lun_durable_name_instance.to_dict()
# create an instance of ArrayOfScsiLunDurableName from a dict
array_of_scsi_lun_durable_name_form_dict = array_of_scsi_lun_durable_name.from_dict(array_of_scsi_lun_durable_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


