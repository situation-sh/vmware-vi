# ArrayOfVirtualMachinePrecisionClockInfo

A boxed array of *VirtualMachinePrecisionClockInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachinePrecisionClockInfo]**](VirtualMachinePrecisionClockInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_precision_clock_info import ArrayOfVirtualMachinePrecisionClockInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachinePrecisionClockInfo from a JSON string
array_of_virtual_machine_precision_clock_info_instance = ArrayOfVirtualMachinePrecisionClockInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachinePrecisionClockInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_precision_clock_info_dict = array_of_virtual_machine_precision_clock_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachinePrecisionClockInfo from a dict
array_of_virtual_machine_precision_clock_info_form_dict = array_of_virtual_machine_precision_clock_info.from_dict(array_of_virtual_machine_precision_clock_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


