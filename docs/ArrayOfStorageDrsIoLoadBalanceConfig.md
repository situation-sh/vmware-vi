# ArrayOfStorageDrsIoLoadBalanceConfig

A boxed array of *StorageDrsIoLoadBalanceConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageDrsIoLoadBalanceConfig]**](StorageDrsIoLoadBalanceConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_drs_io_load_balance_config import ArrayOfStorageDrsIoLoadBalanceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageDrsIoLoadBalanceConfig from a JSON string
array_of_storage_drs_io_load_balance_config_instance = ArrayOfStorageDrsIoLoadBalanceConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageDrsIoLoadBalanceConfig.to_json()

# convert the object into a dict
array_of_storage_drs_io_load_balance_config_dict = array_of_storage_drs_io_load_balance_config_instance.to_dict()
# create an instance of ArrayOfStorageDrsIoLoadBalanceConfig from a dict
array_of_storage_drs_io_load_balance_config_form_dict = array_of_storage_drs_io_load_balance_config.from_dict(array_of_storage_drs_io_load_balance_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


