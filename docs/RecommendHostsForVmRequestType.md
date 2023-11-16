# RecommendHostsForVmRequestType

The parameters of *ClusterComputeResource.RecommendHostsForVm*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.recommend_hosts_for_vm_request_type import RecommendHostsForVmRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendHostsForVmRequestType from a JSON string
recommend_hosts_for_vm_request_type_instance = RecommendHostsForVmRequestType.from_json(json)
# print the JSON string representation of the object
print RecommendHostsForVmRequestType.to_json()

# convert the object into a dict
recommend_hosts_for_vm_request_type_dict = recommend_hosts_for_vm_request_type_instance.to_dict()
# create an instance of RecommendHostsForVmRequestType from a dict
recommend_hosts_for_vm_request_type_form_dict = recommend_hosts_for_vm_request_type.from_dict(recommend_hosts_for_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


