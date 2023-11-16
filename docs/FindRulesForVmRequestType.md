# FindRulesForVmRequestType

The parameters of *ClusterComputeResource.FindRulesForVm*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.find_rules_for_vm_request_type import FindRulesForVmRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindRulesForVmRequestType from a JSON string
find_rules_for_vm_request_type_instance = FindRulesForVmRequestType.from_json(json)
# print the JSON string representation of the object
print FindRulesForVmRequestType.to_json()

# convert the object into a dict
find_rules_for_vm_request_type_dict = find_rules_for_vm_request_type_instance.to_dict()
# create an instance of FindRulesForVmRequestType from a dict
find_rules_for_vm_request_type_form_dict = find_rules_for_vm_request_type.from_dict(find_rules_for_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


