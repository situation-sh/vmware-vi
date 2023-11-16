# InsufficientStandbyMemoryResource

This fault is thrown by Distributed Power Management algorithm.  It indicates that there are insufficient memory resources on standby hosts (if any) to meet the requirements of a given operation.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **int** | The total amount of memory resource available (in bytes) on all the usable hosts in the cluster (including powered on and standby hosts).  ***Since:*** vSphere API 4.0  | 
**requested** | **int** | The additional amount of memory resource (other than that on the hosts included in \&quot;available\&quot;) needed (in bytes).  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.insufficient_standby_memory_resource import InsufficientStandbyMemoryResource

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientStandbyMemoryResource from a JSON string
insufficient_standby_memory_resource_instance = InsufficientStandbyMemoryResource.from_json(json)
# print the JSON string representation of the object
print InsufficientStandbyMemoryResource.to_json()

# convert the object into a dict
insufficient_standby_memory_resource_dict = insufficient_standby_memory_resource_instance.to_dict()
# create an instance of InsufficientStandbyMemoryResource from a dict
insufficient_standby_memory_resource_form_dict = insufficient_standby_memory_resource.from_dict(insufficient_standby_memory_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


