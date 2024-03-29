# PlacementAction

Describes a placement action of a single virtual machine.  One or more of such actions can be included in a placement recommendation, and such recommendations can be generated by the *ClusterComputeResource.PlaceVm* method.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**target_host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**relocate_spec** | [**VirtualMachineRelocateSpec**](VirtualMachineRelocateSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.placement_action import PlacementAction

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementAction from a JSON string
placement_action_instance = PlacementAction.from_json(json)
# print the JSON string representation of the object
print PlacementAction.to_json()

# convert the object into a dict
placement_action_dict = placement_action_instance.to_dict()
# create an instance of PlacementAction from a dict
placement_action_form_dict = placement_action.from_dict(placement_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


