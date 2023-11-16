# StorageIORMInfo

Configuration of storage I/O resource management.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag indicating whether or not the service is enabled.  ***Since:*** vSphere API 4.1  | 
**congestion_threshold_mode** | **str** | Mode of congestion threshold specification For more information, see *StorageIORMThresholdMode_enum*  ***Since:*** vSphere API 5.1  | 
**congestion_threshold** | **int** | The latency beyond which the storage array is considered congested.  If storage I/O resource management is enabled on a datastore, the algorithm tries to maintain the latency to be below or close to this value. The unit is millisecond. The range of this value is between 5 to 100 milliseconds.  ***Since:*** vSphere API 4.1  | 
**percent_of_peak_throughput** | **int** | The percentage of peak throughput to be used for setting congestion threshold of a datastore.  Valid values are between 50 to 100. Default value is 90%  For more information, see *StorageIORMInfo.congestionThreshold*  ***Since:*** vSphere API 5.1  | [optional] 
**stats_collection_enabled** | **bool** | Deprecated as of vSphere API 6.5, use *StorageIORMInfo.enabled* instead.  Flag indicating whether service is running in stats collection mode.  ***Since:*** vSphere API 5.0  | 
**reservation_enabled** | **bool** | Flag indicating whether IO reservations support is enabled.  ***Since:*** vSphere API 6.0  | 
**stats_aggregation_disabled** | **bool** | Flag indicating whether stats aggregation is disabled.  ***Since:*** vSphere API 5.0  | [optional] 
**reservable_iops_threshold** | **int** | Storage DRS makes storage migration recommendations if total IOPs reservation for all VMs running on the datastore is higher than specified threshold value.  This value (if present) overrides  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_iorm_info import StorageIORMInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StorageIORMInfo from a JSON string
storage_iorm_info_instance = StorageIORMInfo.from_json(json)
# print the JSON string representation of the object
print StorageIORMInfo.to_json()

# convert the object into a dict
storage_iorm_info_dict = storage_iorm_info_instance.to_dict()
# create an instance of StorageIORMInfo from a dict
storage_iorm_info_form_dict = storage_iorm_info.from_dict(storage_iorm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


