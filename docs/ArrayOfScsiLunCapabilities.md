# ArrayOfScsiLunCapabilities

A boxed array of *ScsiLunCapabilities*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ScsiLunCapabilities]**](ScsiLunCapabilities.md) |  | 

## Example

```python
from vmware_vi.models.array_of_scsi_lun_capabilities import ArrayOfScsiLunCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfScsiLunCapabilities from a JSON string
array_of_scsi_lun_capabilities_instance = ArrayOfScsiLunCapabilities.from_json(json)
# print the JSON string representation of the object
print ArrayOfScsiLunCapabilities.to_json()

# convert the object into a dict
array_of_scsi_lun_capabilities_dict = array_of_scsi_lun_capabilities_instance.to_dict()
# create an instance of ArrayOfScsiLunCapabilities from a dict
array_of_scsi_lun_capabilities_form_dict = array_of_scsi_lun_capabilities.from_dict(array_of_scsi_lun_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


