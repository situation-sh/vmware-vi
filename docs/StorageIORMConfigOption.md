# StorageIORMConfigOption

Configuration setting ranges for *StorageIORMConfigSpec* object.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_option** | [**BoolOption**](BoolOption.md) |  | 
**congestion_threshold_option** | [**IntOption**](IntOption.md) |  | 
**stats_collection_enabled_option** | [**BoolOption**](BoolOption.md) |  | 
**reservation_enabled_option** | [**BoolOption**](BoolOption.md) |  | 

## Example

```python
from vmware_vi.models.storage_iorm_config_option import StorageIORMConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of StorageIORMConfigOption from a JSON string
storage_iorm_config_option_instance = StorageIORMConfigOption.from_json(json)
# print the JSON string representation of the object
print StorageIORMConfigOption.to_json()

# convert the object into a dict
storage_iorm_config_option_dict = storage_iorm_config_option_instance.to_dict()
# create an instance of StorageIORMConfigOption from a dict
storage_iorm_config_option_form_dict = storage_iorm_config_option.from_dict(storage_iorm_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


