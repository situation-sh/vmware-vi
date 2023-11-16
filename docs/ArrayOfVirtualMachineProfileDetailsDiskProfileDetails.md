# ArrayOfVirtualMachineProfileDetailsDiskProfileDetails

A boxed array of *VirtualMachineProfileDetailsDiskProfileDetails*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineProfileDetailsDiskProfileDetails]**](VirtualMachineProfileDetailsDiskProfileDetails.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_profile_details_disk_profile_details import ArrayOfVirtualMachineProfileDetailsDiskProfileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineProfileDetailsDiskProfileDetails from a JSON string
array_of_virtual_machine_profile_details_disk_profile_details_instance = ArrayOfVirtualMachineProfileDetailsDiskProfileDetails.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineProfileDetailsDiskProfileDetails.to_json()

# convert the object into a dict
array_of_virtual_machine_profile_details_disk_profile_details_dict = array_of_virtual_machine_profile_details_disk_profile_details_instance.to_dict()
# create an instance of ArrayOfVirtualMachineProfileDetailsDiskProfileDetails from a dict
array_of_virtual_machine_profile_details_disk_profile_details_form_dict = array_of_virtual_machine_profile_details_disk_profile_details.from_dict(array_of_virtual_machine_profile_details_disk_profile_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


