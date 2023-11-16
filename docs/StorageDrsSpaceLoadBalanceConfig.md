# StorageDrsSpaceLoadBalanceConfig

Storage DRS configuration for space load balancing.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**space_threshold_mode** | **str** |  | [optional] 
**space_utilization_threshold** | **int** | Storage DRS makes storage migration recommendations if space utilization on one (or more) of the datastores is higher than the specified threshold.  The valid values are in the range of 50 (i.e., 50%) to 100 (i.e., 100%). If not specified, the default value is 80%.  ***Since:*** vSphere API 5.0  | [optional] 
**free_space_threshold_gb** | **int** | Storage DRS makes storage migration recommendations if free space on one (or more) of the datastores falls below the specified threshold.  The unit is in gigabytes and the minimum value is 1GB. The maximum value is limited by the capacity of the smallest datastore in a datastore cluster. If not specified, the default value is 50GB.  ***Since:*** vSphere API 6.0  | [optional] 
**min_space_utilization_difference** | **int** | Storage DRS considers making storage migration recommendations if the difference in space utilization between the source and destination datastores is higher than the specified threshold.  The valid values are in the range of 1 (i.e., 1%) to 50 (i.e., 50%). If not specified, the default value is 5%.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_space_load_balance_config import StorageDrsSpaceLoadBalanceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsSpaceLoadBalanceConfig from a JSON string
storage_drs_space_load_balance_config_instance = StorageDrsSpaceLoadBalanceConfig.from_json(json)
# print the JSON string representation of the object
print StorageDrsSpaceLoadBalanceConfig.to_json()

# convert the object into a dict
storage_drs_space_load_balance_config_dict = storage_drs_space_load_balance_config_instance.to_dict()
# create an instance of StorageDrsSpaceLoadBalanceConfig from a dict
storage_drs_space_load_balance_config_form_dict = storage_drs_space_load_balance_config.from_dict(storage_drs_space_load_balance_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


