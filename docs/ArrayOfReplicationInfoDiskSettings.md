# ArrayOfReplicationInfoDiskSettings

A boxed array of *ReplicationInfoDiskSettings*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ReplicationInfoDiskSettings]**](ReplicationInfoDiskSettings.md) |  | 

## Example

```python
from vmware_vi.models.array_of_replication_info_disk_settings import ArrayOfReplicationInfoDiskSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfReplicationInfoDiskSettings from a JSON string
array_of_replication_info_disk_settings_instance = ArrayOfReplicationInfoDiskSettings.from_json(json)
# print the JSON string representation of the object
print ArrayOfReplicationInfoDiskSettings.to_json()

# convert the object into a dict
array_of_replication_info_disk_settings_dict = array_of_replication_info_disk_settings_instance.to_dict()
# create an instance of ArrayOfReplicationInfoDiskSettings from a dict
array_of_replication_info_disk_settings_form_dict = array_of_replication_info_disk_settings.from_dict(array_of_replication_info_disk_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


