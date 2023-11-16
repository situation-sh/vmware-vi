# ArrayOfVirtualMachineDvxClassInfo

A boxed array of *VirtualMachineDvxClassInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineDvxClassInfo]**](VirtualMachineDvxClassInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_dvx_class_info import ArrayOfVirtualMachineDvxClassInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineDvxClassInfo from a JSON string
array_of_virtual_machine_dvx_class_info_instance = ArrayOfVirtualMachineDvxClassInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineDvxClassInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_dvx_class_info_dict = array_of_virtual_machine_dvx_class_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineDvxClassInfo from a dict
array_of_virtual_machine_dvx_class_info_form_dict = array_of_virtual_machine_dvx_class_info.from_dict(array_of_virtual_machine_dvx_class_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


