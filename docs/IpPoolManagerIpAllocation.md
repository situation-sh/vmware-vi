# IpPoolManagerIpAllocation

Describes an IP allocation.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP address  ***Since:*** vSphere API 5.1  | 
**allocation_id** | **str** | The allocation ID  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.ip_pool_manager_ip_allocation import IpPoolManagerIpAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of IpPoolManagerIpAllocation from a JSON string
ip_pool_manager_ip_allocation_instance = IpPoolManagerIpAllocation.from_json(json)
# print the JSON string representation of the object
print IpPoolManagerIpAllocation.to_json()

# convert the object into a dict
ip_pool_manager_ip_allocation_dict = ip_pool_manager_ip_allocation_instance.to_dict()
# create an instance of IpPoolManagerIpAllocation from a dict
ip_pool_manager_ip_allocation_form_dict = ip_pool_manager_ip_allocation.from_dict(ip_pool_manager_ip_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


