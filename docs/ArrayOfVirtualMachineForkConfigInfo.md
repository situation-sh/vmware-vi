# ArrayOfVirtualMachineForkConfigInfo

A boxed array of *VirtualMachineForkConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineForkConfigInfo]**](VirtualMachineForkConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_fork_config_info import ArrayOfVirtualMachineForkConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineForkConfigInfo from a JSON string
array_of_virtual_machine_fork_config_info_instance = ArrayOfVirtualMachineForkConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineForkConfigInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_fork_config_info_dict = array_of_virtual_machine_fork_config_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineForkConfigInfo from a dict
array_of_virtual_machine_fork_config_info_form_dict = array_of_virtual_machine_fork_config_info.from_dict(array_of_virtual_machine_fork_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


