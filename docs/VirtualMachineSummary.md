# VirtualMachineSummary

The summary data object type encapsulates a typical set of virtual machine information that is useful for list views and summary pages.  VirtualCenter can retrieve this information very efficiently, even for large sets of virtual machines. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**runtime** | [**VirtualMachineRuntimeInfo**](VirtualMachineRuntimeInfo.md) |  | 
**guest** | [**VirtualMachineGuestSummary**](VirtualMachineGuestSummary.md) |  | [optional] 
**config** | [**VirtualMachineConfigSummary**](VirtualMachineConfigSummary.md) |  | 
**storage** | [**VirtualMachineStorageSummary**](VirtualMachineStorageSummary.md) |  | [optional] 
**quick_stats** | [**VirtualMachineQuickStats**](VirtualMachineQuickStats.md) |  | 
**overall_status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 
**custom_value** | [**List[CustomFieldValue]**](CustomFieldValue.md) | Custom field values.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_summary import VirtualMachineSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineSummary from a JSON string
virtual_machine_summary_instance = VirtualMachineSummary.from_json(json)
# print the JSON string representation of the object
print VirtualMachineSummary.to_json()

# convert the object into a dict
virtual_machine_summary_dict = virtual_machine_summary_instance.to_dict()
# create an instance of VirtualMachineSummary from a dict
virtual_machine_summary_form_dict = virtual_machine_summary.from_dict(virtual_machine_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


