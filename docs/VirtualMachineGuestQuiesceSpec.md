# VirtualMachineGuestQuiesceSpec

This data object type encapsulates configuration settings when creating a virtual machine quiesced snapshot.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | The property to indicate maximum time in minutes for snapshot operation to be performed on the virtual machine.  The timeout can not be less than 5 minutes or more than 240 minutes.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_guest_quiesce_spec import VirtualMachineGuestQuiesceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineGuestQuiesceSpec from a JSON string
virtual_machine_guest_quiesce_spec_instance = VirtualMachineGuestQuiesceSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineGuestQuiesceSpec.to_json()

# convert the object into a dict
virtual_machine_guest_quiesce_spec_dict = virtual_machine_guest_quiesce_spec_instance.to_dict()
# create an instance of VirtualMachineGuestQuiesceSpec from a dict
virtual_machine_guest_quiesce_spec_form_dict = virtual_machine_guest_quiesce_spec.from_dict(virtual_machine_guest_quiesce_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


