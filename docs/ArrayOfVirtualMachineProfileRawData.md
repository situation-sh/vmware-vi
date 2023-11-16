# ArrayOfVirtualMachineProfileRawData

A boxed array of *VirtualMachineProfileRawData*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineProfileRawData]**](VirtualMachineProfileRawData.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_profile_raw_data import ArrayOfVirtualMachineProfileRawData

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineProfileRawData from a JSON string
array_of_virtual_machine_profile_raw_data_instance = ArrayOfVirtualMachineProfileRawData.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineProfileRawData.to_json()

# convert the object into a dict
array_of_virtual_machine_profile_raw_data_dict = array_of_virtual_machine_profile_raw_data_instance.to_dict()
# create an instance of ArrayOfVirtualMachineProfileRawData from a dict
array_of_virtual_machine_profile_raw_data_form_dict = array_of_virtual_machine_profile_raw_data.from_dict(array_of_virtual_machine_profile_raw_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


