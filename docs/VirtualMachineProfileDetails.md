# VirtualMachineProfileDetails

The *VirtualMachineProfileDetails* data object type provides details of the policy associated with a virtual machine and it's virtual disks.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | Storage profile associated with Virtual Machine&#39;s home directory.  ***Since:*** vSphere API 6.7  | [optional] 
**disk_profile_details** | [**List[VirtualMachineProfileDetailsDiskProfileDetails]**](VirtualMachineProfileDetailsDiskProfileDetails.md) | An optional list that allows specifying details of the policy associated with virutual disks.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_profile_details import VirtualMachineProfileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineProfileDetails from a JSON string
virtual_machine_profile_details_instance = VirtualMachineProfileDetails.from_json(json)
# print the JSON string representation of the object
print VirtualMachineProfileDetails.to_json()

# convert the object into a dict
virtual_machine_profile_details_dict = virtual_machine_profile_details_instance.to_dict()
# create an instance of VirtualMachineProfileDetails from a dict
virtual_machine_profile_details_form_dict = virtual_machine_profile_details.from_dict(virtual_machine_profile_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


