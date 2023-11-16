# StorageDrsIoLoadBalanceConfig

Storage DRS configuration for I/O load balancing.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservable_percent_threshold** | **int** | Storage DRS makes storage migration recommendations if total IOPs reservation of all VMs running on a datastore is higher than the specified threshold.  Storage DRS recommends migration out of all such datastores, if more than one datastore exceed their reserved IOPs threshold.  The actual Iops used to determine threshold are computed from Storage DRS estimation of IOPs capacity of a datastore. The absolute value may change over time, according to storage response to workloads.  The valid values are in the range of 30 (i.e., 30%) to 100 (i.e., 100%). If not specified, the default value is 60%.  ***Since:*** vSphere API 6.0  | [optional] 
**reservable_iops_threshold** | **int** | Storage DRS makes storage migration recommendations if total IOPs reservation of all VMs running on a datastore is higher than the specified threshold.  Storage DRS recommends migration out of all such datastores, if more than one datastore exceed their reserved IOPs threshold.  This is an advanced option, and should only be used if Storage DRS estimated IOPs capacity is incorrect for datastores. The value should be based on conservative estimate of storage performance, and ideally should be set to about 50-60% of worse case peak performance of backing LUN.  ***Since:*** vSphere API 6.0  | [optional] 
**reservable_threshold_mode** | **str** | Determines which reservation threshold specification to use.  See *StorageDrsPodConfigInfoBehavior_enum*. If unspecified, the mode is assumed automatic by default. Storage DRS uses percentage value in that case. If mode is specified, but corresponding reservationThreshold value is absent, option specific defaults are used.  ***Since:*** vSphere API 6.0  | [optional] 
**io_latency_threshold** | **int** | Storage DRS makes storage migration recommendations if I/O latency on one (or more) of the datastores is higher than the specified threshold.  Unit: millisecond. The valid values are in the range of 5 to 100. If not specified, the default value is 15.  ***Since:*** vSphere API 5.0  | [optional] 
**io_load_imbalance_threshold** | **int** | Storage DRS makes storage migration recommendations if I/O load imbalance level is higher than the specified threshold.  Unit: a number. The valid values are in the range of 1 to 100. If not specified, the default value is 5.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_io_load_balance_config import StorageDrsIoLoadBalanceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsIoLoadBalanceConfig from a JSON string
storage_drs_io_load_balance_config_instance = StorageDrsIoLoadBalanceConfig.from_json(json)
# print the JSON string representation of the object
print StorageDrsIoLoadBalanceConfig.to_json()

# convert the object into a dict
storage_drs_io_load_balance_config_dict = storage_drs_io_load_balance_config_instance.to_dict()
# create an instance of StorageDrsIoLoadBalanceConfig from a dict
storage_drs_io_load_balance_config_form_dict = storage_drs_io_load_balance_config.from_dict(storage_drs_io_load_balance_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


