# ScsiLunDescriptor

A structure that encapsulates an identifier and its properties for the ScsiLun object.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quality** | **str** | An indicator of the utility of the descriptor as an identifier that is stable, unique, and correlatable.  See also *ScsiLunDescriptorQuality_enum*.  ***Since:*** vSphere API 4.0  | 
**id** | **str** | The identifier represented as a string.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.scsi_lun_descriptor import ScsiLunDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ScsiLunDescriptor from a JSON string
scsi_lun_descriptor_instance = ScsiLunDescriptor.from_json(json)
# print the JSON string representation of the object
print ScsiLunDescriptor.to_json()

# convert the object into a dict
scsi_lun_descriptor_dict = scsi_lun_descriptor_instance.to_dict()
# create an instance of ScsiLunDescriptor from a dict
scsi_lun_descriptor_form_dict = scsi_lun_descriptor.from_dict(scsi_lun_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


