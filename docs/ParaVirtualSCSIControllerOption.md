# ParaVirtualSCSIControllerOption

ParaVirtualSCSIControllerOption is the data object that contains the options for a a paravirtualized SCSI controller.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.para_virtual_scsi_controller_option import ParaVirtualSCSIControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of ParaVirtualSCSIControllerOption from a JSON string
para_virtual_scsi_controller_option_instance = ParaVirtualSCSIControllerOption.from_json(json)
# print the JSON string representation of the object
print ParaVirtualSCSIControllerOption.to_json()

# convert the object into a dict
para_virtual_scsi_controller_option_dict = para_virtual_scsi_controller_option_instance.to_dict()
# create an instance of ParaVirtualSCSIControllerOption from a dict
para_virtual_scsi_controller_option_form_dict = para_virtual_scsi_controller_option.from_dict(para_virtual_scsi_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


