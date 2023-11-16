# ArrayOfVirtualMachineProfileDetails

A boxed array of *VirtualMachineProfileDetails*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineProfileDetails]**](VirtualMachineProfileDetails.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_profile_details import ArrayOfVirtualMachineProfileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineProfileDetails from a JSON string
array_of_virtual_machine_profile_details_instance = ArrayOfVirtualMachineProfileDetails.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineProfileDetails.to_json()

# convert the object into a dict
array_of_virtual_machine_profile_details_dict = array_of_virtual_machine_profile_details_instance.to_dict()
# create an instance of ArrayOfVirtualMachineProfileDetails from a dict
array_of_virtual_machine_profile_details_form_dict = array_of_virtual_machine_profile_details.from_dict(array_of_virtual_machine_profile_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


