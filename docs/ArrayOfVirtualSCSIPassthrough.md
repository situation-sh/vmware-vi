# ArrayOfVirtualSCSIPassthrough

A boxed array of *VirtualSCSIPassthrough*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSCSIPassthrough]**](VirtualSCSIPassthrough.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_scsi_passthrough import ArrayOfVirtualSCSIPassthrough

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSCSIPassthrough from a JSON string
array_of_virtual_scsi_passthrough_instance = ArrayOfVirtualSCSIPassthrough.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSCSIPassthrough.to_json()

# convert the object into a dict
array_of_virtual_scsi_passthrough_dict = array_of_virtual_scsi_passthrough_instance.to_dict()
# create an instance of ArrayOfVirtualSCSIPassthrough from a dict
array_of_virtual_scsi_passthrough_form_dict = array_of_virtual_scsi_passthrough.from_dict(array_of_virtual_scsi_passthrough_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


