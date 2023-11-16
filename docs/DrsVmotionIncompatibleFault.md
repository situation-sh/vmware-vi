# DrsVmotionIncompatibleFault

This fault is thrown when DRS tries to migrate a virtual machine to a host, but finds that the host is incompatible with the given virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.drs_vmotion_incompatible_fault import DrsVmotionIncompatibleFault

# TODO update the JSON string below
json = "{}"
# create an instance of DrsVmotionIncompatibleFault from a JSON string
drs_vmotion_incompatible_fault_instance = DrsVmotionIncompatibleFault.from_json(json)
# print the JSON string representation of the object
print DrsVmotionIncompatibleFault.to_json()

# convert the object into a dict
drs_vmotion_incompatible_fault_dict = drs_vmotion_incompatible_fault_instance.to_dict()
# create an instance of DrsVmotionIncompatibleFault from a dict
drs_vmotion_incompatible_fault_form_dict = drs_vmotion_incompatible_fault.from_dict(drs_vmotion_incompatible_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


