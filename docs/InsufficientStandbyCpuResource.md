# InsufficientStandbyCpuResource

This fault is thrown when Distributed Power Management cannot perform a given opeartion because there is insufficient CPU resource on standby hosts (if any) to meet the requirements of the operation.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **int** | The total amount of CPU resource available (in MHz) on all the usable hosts in the cluster (including powered on and standby hosts).  ***Since:*** vSphere API 4.0  | 
**requested** | **int** | The additional amount of CPU resource (other than that on the hosts included in \&quot;available\&quot;) needed (in MHz).  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.insufficient_standby_cpu_resource import InsufficientStandbyCpuResource

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientStandbyCpuResource from a JSON string
insufficient_standby_cpu_resource_instance = InsufficientStandbyCpuResource.from_json(json)
# print the JSON string representation of the object
print InsufficientStandbyCpuResource.to_json()

# convert the object into a dict
insufficient_standby_cpu_resource_dict = insufficient_standby_cpu_resource_instance.to_dict()
# create an instance of InsufficientStandbyCpuResource from a dict
insufficient_standby_cpu_resource_form_dict = insufficient_standby_cpu_resource.from_dict(insufficient_standby_cpu_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


