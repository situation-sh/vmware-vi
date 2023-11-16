# VirtualSATAControllerOption

The VirtualSATAControllerOption data object type contains the options for a virtual SATA controller defined by the *VirtualSATAController* data object type.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_sata_disks** | [**IntOption**](IntOption.md) |  | 
**num_sata_cdroms** | [**IntOption**](IntOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_sata_controller_option import VirtualSATAControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSATAControllerOption from a JSON string
virtual_sata_controller_option_instance = VirtualSATAControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualSATAControllerOption.to_json()

# convert the object into a dict
virtual_sata_controller_option_dict = virtual_sata_controller_option_instance.to_dict()
# create an instance of VirtualSATAControllerOption from a dict
virtual_sata_controller_option_form_dict = virtual_sata_controller_option.from_dict(virtual_sata_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


