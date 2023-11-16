# StorageIORMConfigSpec

Configuration settings used for creating or reconfiguring storage I/O resource management.  All fields are defined as optional. If a field is unset, the property is not changed.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag indicating whether or not the service is enabled.  ***Since:*** vSphere API 4.1  | [optional] 
**congestion_threshold_mode** | **str** | Mode of congestion threshold specification For more information, see *StorageIORMThresholdMode_enum*  ***Since:*** vSphere API 5.1  | [optional] 
**congestion_threshold** | **int** | The latency beyond which the storage array is considered congested.  For more information, see *StorageIORMInfo.congestionThreshold*  ***Since:*** vSphere API 4.1  | [optional] 
**percent_of_peak_throughput** | **int** | The percentage of peak throughput to be used for setting threshold latency of a datastore.  Valid values are between 50 to 100.  For more information, see *StorageIORMInfo.congestionThreshold*  ***Since:*** vSphere API 5.1  | [optional] 
**stats_collection_enabled** | **bool** | Flag indicating whether the service is enabled in stats collection mode.  ***Since:*** vSphere API 5.0  | [optional] 
**reservation_enabled** | **bool** | Flag indicating whether IO reservations support is enabled.  ***Since:*** vSphere API 6.0  | [optional] 
**stats_aggregation_disabled** | **bool** | Flag indicating whether stats aggregation is disabled.  ***Since:*** vSphere API 5.0  | [optional] 
**reservable_iops_threshold** | **int** | Storage DRS makes storage migration recommendations if total IOPs reservation for all VMs running on the datastore is higher than specified threshold value.  This value (if present) overrides  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_iorm_config_spec import StorageIORMConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of StorageIORMConfigSpec from a JSON string
storage_iorm_config_spec_instance = StorageIORMConfigSpec.from_json(json)
# print the JSON string representation of the object
print StorageIORMConfigSpec.to_json()

# convert the object into a dict
storage_iorm_config_spec_dict = storage_iorm_config_spec_instance.to_dict()
# create an instance of StorageIORMConfigSpec from a dict
storage_iorm_config_spec_form_dict = storage_iorm_config_spec.from_dict(storage_iorm_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


