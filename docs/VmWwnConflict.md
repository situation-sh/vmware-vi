# VmWwnConflict

Thrown if a user attempts to assign a WWN that is currently being used by other virtual machine or host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**name** | **str** | The name of the virtual machine/host that is using the same WWN.  ***Since:*** VI API 2.5  | [optional] 
**wwn** | **int** | The WWN that is in conflict.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.vm_wwn_conflict import VmWwnConflict

# TODO update the JSON string below
json = "{}"
# create an instance of VmWwnConflict from a JSON string
vm_wwn_conflict_instance = VmWwnConflict.from_json(json)
# print the JSON string representation of the object
print VmWwnConflict.to_json()

# convert the object into a dict
vm_wwn_conflict_dict = vm_wwn_conflict_instance.to_dict()
# create an instance of VmWwnConflict from a dict
vm_wwn_conflict_form_dict = vm_wwn_conflict.from_dict(vm_wwn_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


