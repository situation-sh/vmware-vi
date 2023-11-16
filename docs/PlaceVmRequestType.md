# PlaceVmRequestType

The parameters of *ClusterComputeResource.PlaceVm*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_spec** | [**PlacementSpec**](PlacementSpec.md) |  | 

## Example

```python
from vmware_vi.models.place_vm_request_type import PlaceVmRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PlaceVmRequestType from a JSON string
place_vm_request_type_instance = PlaceVmRequestType.from_json(json)
# print the JSON string representation of the object
print PlaceVmRequestType.to_json()

# convert the object into a dict
place_vm_request_type_dict = place_vm_request_type_instance.to_dict()
# create an instance of PlaceVmRequestType from a dict
place_vm_request_type_form_dict = place_vm_request_type.from_dict(place_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


