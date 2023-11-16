# VsanPolicyCost

PolicyCost -- Structure to describe the cost of satisfying a policy.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_data_size** | **int** | Change (in bytes) of size of data stored on the datastore.  This is the max of reserved and used capacity.  ***Since:*** vSphere API 5.5  | [optional] 
**current_data_size** | **int** | Size (in bytes) of data currently stored on the datastore.  This is the max of reserved and used capacity.  ***Since:*** vSphere API 5.5  | [optional] 
**temp_data_size** | **int** | Size (in bytes) for temporary data that will be needed on disk if new policy is applied.  ***Since:*** vSphere API 5.5  | [optional] 
**copy_data_size** | **int** | Size (in bytes) of data we need to write to VSAN Datastore if new policy is applied.  ***Since:*** vSphere API 5.5  | [optional] 
**change_flash_read_cache_size** | **int** | Change (in bytes) of flash space reserved for read cache if new policy is applied.  ***Since:*** vSphere API 5.5  | [optional] 
**current_flash_read_cache_size** | **int** | Size (in bytes) of flash space currently reserved for read cache.  ***Since:*** vSphere API 5.5  | [optional] 
**current_disk_space_to_address_space_ratio** | **float** | Current ratio of physical disk space of an object to the logical VSAN address space.  For eg. an object of size 1GB with two copies of the data has two 1GB replicas and so this ratio is 2.  ***Since:*** vSphere API 6.0  | [optional] 
**disk_space_to_address_space_ratio** | **float** | Ratio of physical disk space of an object to the logical VSAN address space after new policy is applied.  For eg. an object of size 1GB with two copies of the data has two 1GB replicas and so this ratio is 2.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.vsan_policy_cost import VsanPolicyCost

# TODO update the JSON string below
json = "{}"
# create an instance of VsanPolicyCost from a JSON string
vsan_policy_cost_instance = VsanPolicyCost.from_json(json)
# print the JSON string representation of the object
print VsanPolicyCost.to_json()

# convert the object into a dict
vsan_policy_cost_dict = vsan_policy_cost_instance.to_dict()
# create an instance of VsanPolicyCost from a dict
vsan_policy_cost_form_dict = vsan_policy_cost.from_dict(vsan_policy_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


