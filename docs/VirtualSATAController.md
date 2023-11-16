# VirtualSATAController

The VirtualSATAController data object type represents a SATA controller in a virtual machine.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_sata_controller import VirtualSATAController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSATAController from a JSON string
virtual_sata_controller_instance = VirtualSATAController.from_json(json)
# print the JSON string representation of the object
print VirtualSATAController.to_json()

# convert the object into a dict
virtual_sata_controller_dict = virtual_sata_controller_instance.to_dict()
# create an instance of VirtualSATAController from a dict
virtual_sata_controller_form_dict = virtual_sata_controller.from_dict(virtual_sata_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


