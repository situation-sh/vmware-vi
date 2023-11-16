# ReleaseIpAllocationRequestType

The parameters of *IpPoolManager.ReleaseIpAllocation*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dc** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**pool_id** | **int** | The unique ID of the pool  | 
**allocation_id** | **str** | The unique ID for this allocation  | 

## Example

```python
from vmware_vi.models.release_ip_allocation_request_type import ReleaseIpAllocationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseIpAllocationRequestType from a JSON string
release_ip_allocation_request_type_instance = ReleaseIpAllocationRequestType.from_json(json)
# print the JSON string representation of the object
print ReleaseIpAllocationRequestType.to_json()

# convert the object into a dict
release_ip_allocation_request_type_dict = release_ip_allocation_request_type_instance.to_dict()
# create an instance of ReleaseIpAllocationRequestType from a dict
release_ip_allocation_request_type_form_dict = release_ip_allocation_request_type.from_dict(release_ip_allocation_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


