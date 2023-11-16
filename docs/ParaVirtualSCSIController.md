# ParaVirtualSCSIController

ParaVirtualSCSIController is the data object that represents a paravirtualized SCSI controller.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.para_virtual_scsi_controller import ParaVirtualSCSIController

# TODO update the JSON string below
json = "{}"
# create an instance of ParaVirtualSCSIController from a JSON string
para_virtual_scsi_controller_instance = ParaVirtualSCSIController.from_json(json)
# print the JSON string representation of the object
print ParaVirtualSCSIController.to_json()

# convert the object into a dict
para_virtual_scsi_controller_dict = para_virtual_scsi_controller_instance.to_dict()
# create an instance of ParaVirtualSCSIController from a dict
para_virtual_scsi_controller_form_dict = para_virtual_scsi_controller.from_dict(para_virtual_scsi_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


