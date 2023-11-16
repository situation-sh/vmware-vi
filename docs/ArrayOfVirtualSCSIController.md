# ArrayOfVirtualSCSIController

A boxed array of *VirtualSCSIController*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSCSIController]**](VirtualSCSIController.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_scsi_controller import ArrayOfVirtualSCSIController

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSCSIController from a JSON string
array_of_virtual_scsi_controller_instance = ArrayOfVirtualSCSIController.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSCSIController.to_json()

# convert the object into a dict
array_of_virtual_scsi_controller_dict = array_of_virtual_scsi_controller_instance.to_dict()
# create an instance of ArrayOfVirtualSCSIController from a dict
array_of_virtual_scsi_controller_form_dict = array_of_virtual_scsi_controller.from_dict(array_of_virtual_scsi_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


