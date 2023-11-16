# ArrayOfParaVirtualSCSIControllerOption

A boxed array of *ParaVirtualSCSIControllerOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ParaVirtualSCSIControllerOption]**](ParaVirtualSCSIControllerOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_para_virtual_scsi_controller_option import ArrayOfParaVirtualSCSIControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfParaVirtualSCSIControllerOption from a JSON string
array_of_para_virtual_scsi_controller_option_instance = ArrayOfParaVirtualSCSIControllerOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfParaVirtualSCSIControllerOption.to_json()

# convert the object into a dict
array_of_para_virtual_scsi_controller_option_dict = array_of_para_virtual_scsi_controller_option_instance.to_dict()
# create an instance of ArrayOfParaVirtualSCSIControllerOption from a dict
array_of_para_virtual_scsi_controller_option_form_dict = array_of_para_virtual_scsi_controller_option.from_dict(array_of_para_virtual_scsi_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


